'''
Main application file to run the GUI.
'''
from tkinter import Tk
from input_frame import InputFrame
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Just Test Application")
        self.input_frame = InputFrame(self.root, self.show_message)
        self.input_frame.pack()
    def show_message(self, text):
        from message_box import MessageBox
        MessageBox.show(text)
if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()