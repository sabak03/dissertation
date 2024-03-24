from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import librosa
import numpy as np
from keras.models import load_model
from werkzeug.utils import secure_filename
from pydub import AudioSegment
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
CORS(app)  
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


model = load_model('khaaModel.h5')

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/upload-audio', methods=['POST'])
def uploadAudio():
    if 'audio' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    audioFile = request.files['audio']
    if audioFile.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if audioFile and isAllowedFile(audioFile.filename):
        secureFilename = secure_filename(audioFile.filename)
        filePath = os.path.join(UPLOAD_FOLDER, secureFilename)
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
    original_audio = AudioSegment.from_file(filePath)
    converted_path = filePath.replace(".wav", "_converted.wav")
    original_audio.export(converted_path, format="wav")
    features = extractFeatures(converted_path)
    prediction = model.predict(features)
    isCorrect = prediction >= 0.5
    result = 'Correct' if isCorrect else 'Incorrect'
    # Remove the converted file after processing
    if os.path.exists(converted_path):
        os.remove(converted_path)
    return jsonify({'pronunciation': result})

if __name__ == '__main__':
    app.run(debug=True)
