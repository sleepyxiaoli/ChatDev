'''
InputFrame class to handle user input and button.
'''
from tkinter import Frame, Entry, Button
class InputFrame(Frame):
    def __init__(self, master, show_message_callback):
        super().__init__(master)
        self.show_message_callback = show_message_callback
        self.create_widgets()
    def create_widgets(self):
        self.entry = Entry(self)
        self.entry.pack(padx=10, pady=10)
        self.button = Button(self, text="Show Message", command=self.on_button_click)
        self.button.pack(padx=10, pady=10)
    def on_button_click(self):
        text = self.entry.get()
        if text:  # Check if the entry is not empty
            self.show_message_callback(text)
        else:
            self.show_message_callback("Please enter a message.")  # Prompt for input if empty