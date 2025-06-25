import pyttsx3
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2

voice = pyttsx3.init()


text = "Subcribe "
window = tk.Tk()
window.title("Voice_Project")
window.geometry("400x400")

def On_button_clicked():
    voice.say(text)
    voice.runAndWait()



button = tk.Button(window, text="Start", command=On_button_clicked)
button.pack()

if __name__ == '__main__':
    window.mainloop()