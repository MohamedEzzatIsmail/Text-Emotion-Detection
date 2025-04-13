# emotion_gui_app.py
import tkinter as tk
from tkinter import messagebox
import joblib

# Load the saved model
model = joblib.load("emotion_model.pkl")

def detect_emotion():
    text = input_text.get("1.0", tk.END).strip()
    if text:
        prediction = model.predict([text])[0]
        result_label.config(text=f"Detected Emotion: {prediction}")
    else:
        messagebox.showwarning("Input Error", "Please enter some text.")

# GUI Setup
root = tk.Tk()
root.title("Emotion Detection from Text")
root.geometry("450x300")
root.configure(bg="#e6f2ff")

title_label = tk.Label(root, text="Emotion Detector", font=("Helvetica", 18, "bold"), bg="#e6f2ff")
title_label.pack(pady=10)

input_text = tk.Text(root, height=6, width=50, font=("Helvetica", 12))
input_text.pack(pady=10)

detect_button = tk.Button(root, text="Detect Emotion", command=detect_emotion, font=("Helvetica", 12), bg="#4caf50", fg="white")
detect_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#e6f2ff", fg="blue")
result_label.pack(pady=10)

root.mainloop()
