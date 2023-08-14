import tkinter as tk
from tkinter import filedialog
from processing import *
import os
import sys

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def browse_file():
    filename = filedialog.askopenfilename()
    file_path.set(filename)

def process_button():
    global file_path
    eeg_file = file_path.get()
    processed_eeg, time_range, sfreq_value = process_eeg(eeg_file)
    sfreq.delete('1.0', tk.END)  # очистить текущий текст
    sfreq.insert(tk.END, str(sfreq_value))  # добавить новое значение частоты дискретизации

def create_window():
    window = tk.Tk()
    window.title("FreqApp")
    # Размер окна
    window.geometry('700x500')

    # Загружаем иконку оттуда
    icon_path = resource_path('icon.ico')
    window.wm_iconbitmap(icon_path)

    global file_path
    file_path = tk.StringVar()

    label = tk.Label(window, text="File path: ")
    label.grid(row=0, column=0)

    entry = tk.Entry(window, textvariable=file_path)
    entry.grid(row=0, column=1)

    browse_button = tk.Button(window, text="Browse", command=browse_file)
    browse_button.grid(row=0, column=2)

    # Создаём рамку с подписью
    frame = tk.LabelFrame(window, text='EEG processing', padx=5, pady=5)
    frame.grid(row=1, column=0, columnspan=3, padx=5, pady=30)  # Используем .grid()

    results_button = tk.Button(frame, text="Process eeg", command=process_button)
    results_button.pack()  # Упаковываем кнопку в рамку с помощью pack

    global sfreq
    sfreq = tk.Text(window, height=10)  # это текстовое поле, а не значение частоты дискретизации
    sfreq.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    return window

# Edited here

