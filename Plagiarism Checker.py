import tkinter as tk
from tkinter import messagebox
from difflib import SequenceMatcher


def plagiarism_checker():
    text1 = input1.get("1.0", tk.END).strip()
    text2 = input2.get("1.0", tk.END).strip()
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    similarity_percentage = similarity_ratio * 100
    messagebox.showinfo("Result", f"Similarity: {similarity_percentage:.2f}%")


root = tk.Tk()
root.title("Plagiarism Checker")
root.geometry("700x500")
root.configure(bg="grey")

title_label = tk.Label(root, text="Plagiarism Checker", font="arial 20 bold", fg="white", bg="blue")
title_label.pack()

input1_label = tk.Label(root, text="Original Text: ", font="arial 10 bold", fg="black", bg="yellow")
input1_label.pack()

input1 = tk.Text(root, wrap=tk.WORD, width=70, height=10, fg="white", bg="black")
input1.pack()

input2_label = tk.Label(root, text="Reference Text: ", font="arial 10 bold", fg="black", bg="yellow")
input2_label.pack()

input2 = tk.Text(root, wrap=tk.WORD, width=70, height=10, fg="white", bg="black")
input2.pack()

check_button = tk.Button(root, text="Check Plagiarism", font="arial 15 bold", fg="black", bg="red", command=plagiarism_checker)
check_button.pack()

root.mainloop()
