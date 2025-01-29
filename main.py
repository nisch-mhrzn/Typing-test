import time
import random
import tkinter as tk
from tkinter import messagebox

def calculate_errors(original_text, user_input):
    original_words = original_text.split()
    user_words = user_input.split()
    
    errors = sum(1 for i in range(min(len(original_words), len(user_words))) if original_words[i] != user_words[i])
    errors += abs(len(original_words) - len(user_words))  # Account for missing or extra words
    
    return errors

def calculate_speed(start_time, end_time, user_input):
    elapsed_time = end_time - start_time
    words_per_minute = (len(user_input.split()) / elapsed_time) * 60
    return round(words_per_minute, 2)

def start_typing():
    global start_time, test_text
    test_text = random.choice(test_texts)
    text_label.config(text=test_text)
    user_input.delete("1.0", tk.END)
    user_input.focus()
    start_time = time.time()

def check_results(event=None):  # Allow calling via button or Enter key
    end_time = time.time()
    user_text = user_input.get("1.0", tk.END).strip()
    
    speed = calculate_speed(start_time, end_time, user_text)
    errors = calculate_errors(test_text, user_text)
    
    messagebox.showinfo("Results", f"Typing Speed: {speed} WPM\nErrors: {errors}")

def close_app():
    root.quit()

test_texts = [
    "Python is a powerful programming language.",
    "Practice makes perfect, so keep typing fast!",
    "Speed and accuracy are key in typing tests.",
    "He will get his money's worth in the long run.",
    "Success is not the key to happiness; happiness is the key to success."
]

test_text = ""
start_time = 0

# GUI Setup
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=20)

title_label = tk.Label(frame, text="Typing Speed Test", font=("Arial", 18, "bold"))
title_label.pack()

text_label = tk.Label(frame, text="Click 'Start' to begin", wraplength=500, font=("Arial", 14))
text_label.pack(pady=10)

user_input = tk.Text(frame, height=5, width=60, font=("Arial", 12))
user_input.pack(pady=10)
user_input.bind("<Return>", check_results)  # Bind Enter key to check results

start_button = tk.Button(frame, text="Start", command=start_typing, font=("Arial", 12))
start_button.pack(side=tk.LEFT, padx=10)

check_button = tk.Button(frame, text="Check Results", command=check_results, font=("Arial", 12))
check_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(frame, text="Exit", command=close_app, font=("Arial", 12))
exit_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
