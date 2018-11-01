from tkinter import *


class WidgetsDemo:
    def __init__(self):
        window = Tk()
        window.title('widgets demo')

        frame1 = Frame(window)
        frame1.pack()

        # IntVar for CheckButton
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text="Bold",
                              variable=self.v1,
                              command=self.processCheckButton)
        # IntVar for RadioButton
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text="Red", bg="red",
                            variable=self.v2, value=1,
                            command=self.processRadioButton)
        rbYellow = Radiobutton(frame1, text="Yellow", bg="yellow",
                               variable=self.v2, value=2,
                               command=self.processRadioButton)
        cbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="Enter your name: ")
        
        # StringVar for Inout box
        self.name = StringVar()
        entryName = Entry(frame2, textvariable=self.name)
        btGetName = Button(frame2, text="Get Name", command=self.processButton)
        message = Message(frame2, text="It's me a mario")
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)
        message.grid(row=1, column=4)

        # Add Text
        text = Text(window)
        text.pack()
        text.insert(END, "Tip\nThe best way to learn it is to use it")
        text.insert(END, "use the crap out of it")
        text.insert(END, "to create some shieet")

        window.mainloop()

    def processCheckButton(self):
        print("check button is " + ("checked" if self.v1.get() == 1 else "unchecked"))

    def processRadioButton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected ")

    def processButton(self):
        print("Your name is " + self.name.get())


WidgetsDemo()
