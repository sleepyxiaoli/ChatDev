'''
MessageBox utility class to show message boxes.
'''
from tkinter import messagebox
class MessageBox:
    @staticmethod
    def show(text):
        messagebox.showinfo("Message", text)