from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import os
import librosa
import numpy as np
from keras.models import load_model
from werkzeug.utils import secure_filename
from tempfile import gettempdir  

app = Flask(__name__)
CORS(app)  

model = load_model('khaaModel.h5')

@app.route('/upload-audio', methods=['POST'])
def uploadAudio():
    if 'audio' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    audioFile = request.files['audio']
    if audioFile.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if audioFile and isAllowedFile(audioFile.filename):
        secureFilename = secure_filename(audioFile.filename)
        filePath = os.path.join(gettempdir(), secureFilename) 
        audioFile.save(filePath)
        return processAudioFile(filePath)

    return jsonify({'message': 'Invalid file'}), 400

def isAllowedFile(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'wav'}

def extractFeatures(filePath):
    audio, sampleRate = librosa.load(filePath, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio, sr=sampleRate, n_mfcc=40)
    mfccsProcessed = np.mean(mfccs.T, axis=0)
    return mfccsProcessed.reshape(1, -1)

def processAudioFile(filePath):
    features = extractFeatures(filePath)
    prediction = model.predict(features)
    isCorrect = prediction >= 0.5
    result = 'Correct' if isCorrect else 'Incorrect'
    
    os.remove(filePath)
    
    return jsonify({'pronunciation': result})

if __name__ == '__main__':
    app.run(debug=True)  
