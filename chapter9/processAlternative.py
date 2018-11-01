from tkinter import *


class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOK = Button(window, text="OK", fg="red", command=self.processOK)
        btCancel = Button(window, text="Cancel", bg="yellow", command=self.processCancel)
        btOK.pack()
        btCancel.pack()

        window.mainloop()

    @staticmethod
    def processOK():
        print("OK button is clicked")

    @staticmethod
    def processCancel():
        print("Cancel button is clicked")


ProcessButtonEvent()
