# AI-Powered Arabic Pronunciation Feedback Tool (BSc Dissertation 2024)

A deep learning-based prototype designed to provide instant feedback on Arabic pronunciation, with a focus on Tajweed accuracy.
This project explores how AI can be used to support language learning by analysing user speech and providing real-time corrective feedback.

---

## Project Overview

This project explores how deep learning techniques can be can be used to develop an AI-powered tool for providing instantaneous feedback on pronunciation.  
The system analyses user-recorded audio and compares it against trained models to determine pronunciation accuracy and provide feedback, to support effective learning.

---

## Objectives

- Develop a deep learning model to analyse Arabic pronunciation  
- Extract meaningful audio features using MFCC  
- Train CNN-based models for phonetic classification  
- Provide real-time feedback on pronunciation accuracy  
- Build an accessible and user-friendly interface  

---

## Technologies Used

- **Python**
- **TensorFlow / Keras**
- **Librosa (audio processing)**
- **CNN (Convolutional Neural Networks)**
- **MFCC (Mel Frequency Cepstral Coefficients)**
- **Flask (backend API)**
- **HTML / CSS / JavaScript (frontend)**
- **Heroku (deployment)**

---

## System Architecture

User → Microphone Input → Flask API → Audio Processing (MFCC) → CNN Model → Prediction → Feedback → UI

The system follows a client-server architecture:
- **Frontend** → captures user audio  
- **Backend (Flask)** → processes and analyses data  
- **Deep Learning Model** → predicts pronunciation accuracy  
- **Feedback System** → returns real-time results  

---

## Key Concepts Demonstrated

- Deep learning for audio classification  
- Feature extraction using MFCC  
- CNN-based speech analysis  
- Real-time feedback systems  
- AI in language learning  
- End-to-end system design (frontend + backend + model)  

---

## Why This Project Stands Out

- Combines **AI, linguistics, and education** into one system  
- Addresses a real-world problem affecting learners globally  
- Supports individuals who lack access to qualified teachers  
- Provides a private, non-judgemental learning environment 
- Demonstrates both technical depth and real-world impact
- Demonstrates advanced application of deep learning concepts typically explored at postgraduate level  

- Addresses a real-world issue affecting learners of all ages, where incorrect pronunciation can impact confidence, accuracy, and overall learning experience  
- Bridges the gap between traditional teaching methods and modern AI-driven solutions

---

## Real-World Impact

This tool is designed to:

- Improve accessibility to Arabic pronunciation learning  
- Support diverse learners (non-native speakers, reverts, beginners)  
- Enhance Quranic recitation accuracy  
- Provide inclusive and scalable learning support  

The project highlights how AI can be used for **cultural, educational, and community benefit**, not just technical innovation.

---

## How It Works

1. User records pronunciation  
2. Audio is sent to backend (Flask API)  
3. Audio is processed into MFCC features  
4. CNN model predicts correctness  
5. System returns:
   - Correct  
   - Incorrect + feedback  

---

## Model Approach

- Audio converted into MFCC features  
- CNN model trained on labelled pronunciation data  
- Models stored as `.h5` files  
- Predictions made on unseen audio inputs  

---

## Limitations

- Prototype currently supports a limited number of Arabic letters  
- Model accuracy depends on dataset size and diversity  
- Limited handling of accent variation  

---

## Future Improvements

- Expand to full Arabic alphabet  
- Increase dataset diversity (accents, dialects)  
- Improve feedback detail (not just correct/incorrect)  
- Add user progress tracking  
- Deploy scalable cloud-based version  
- Integrate more advanced deep learning models (e.g. CRNN, transformers)  

---

## Research Contribution

This project contributes to:

- AI-driven language learning tools  
- Speech recognition in Arabic phonetics  
- Accessible education technology  
- Integration of deep learning into cultural/religious education  

---

## Repository

https://github.com/sabak03/ai-pronunciation-feedback-tool/tree/master
> Note: Project files are located in the `master` branch of this repository.

