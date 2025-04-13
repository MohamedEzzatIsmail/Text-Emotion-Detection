# 🧠 Emotion Detection from Text (Desktop App)

A simple desktop application built with Python that detects emotions from text using a machine learning model trained on real tweets.

<img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="python-version" />
<img src="https://img.shields.io/badge/License-MIT-green" alt="license" />

---

## 📌 Features

- Detects emotions such as **happiness**, **sadness**, **anger**, **love**, **worry**, and more.
- Easy-to-use GUI made with Tkinter.
- Trained on a dataset of 40,000 labeled tweets.
- Fast and lightweight — no internet required after setup.

---

## 📁 Dataset

The app uses the `tweet_emotions.csv` dataset, which contains 40,000 tweets labeled with 13 emotions including:

- anger, boredom, empty, enthusiasm, fun, happiness, hate, love, neutral, relief, sadness, surprise, worry

---

## 💻 Installation

1. **Clone the repository**

pip install -r requirements.txt
You can manually install required packages if there's no requirements.txt:

pip install pandas scikit-learn joblib nltk
Train the model

python model.py
Run the GUI 
python app.py

## 🚀 Usage
Launch the desktop app.

Enter any sentence or paragraph.

Click "Detect Emotion".

The app will display the predicted emotion instantly.

## 🧪 Sample Inputs
Try some of these:

"I’m so happy right now!"

"I miss my old friends."

"I hate being ignored."

"What a surprise party!"

## 📦 File Structure

emotion-detector-gui/
│
├── tweet_emotions.csv          # Dataset
├── train_emotion_model.py      # Model training script
├── emotion_model.pkl           # Saved model after training
├── emotion_gui_app.py          # GUI app script
├── requirements.txt            # Dependencies (optional)
└── README.md                   # Documentation

## 📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

## ✨ Credits
Dataset: Tweet Emotion Dataset

GUI: Built with Tkinter

Model: Scikit-learn + Logistic Regression

