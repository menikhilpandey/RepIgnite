import Viewer
import NewReport
from Tkinter import *


class OpeningFrame:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.ViewRepButton = Button(frame, text="View Existing Reports", width=20, command=Viewer.viewall)
        self.CreateRepButton = Button(frame, text="Create New Report", width=20, command=NewReport.create)
        self.ExitButton = Button(frame, text="Exit", width=10, command=frame.quit)

        self.ViewRepButton.grid(row=1, columnspan=2)
        self.CreateRepButton.grid(row=3, columnspan=2)
        self.ExitButton.grid(row=5, columnspan=2)

        # Blank Label for increasing quality of UX in frame
        self.blank_lbl1 = Label(frame).grid(row=0)
        self.blank_lbl1 = Label(frame).grid(row=2)
        self.blank_lbl1 = Label(frame).grid(row=4)

masterObj = Tk(screenName='HomeScreen', className='repIgnite')

WelcomeLabel = Label(masterObj, width=30, text="Welcome to RepIgnite 1.0")
WelcomeLabel.pack(side=TOP)
FrameInit = OpeningFrame(masterObj)

masterObj.mainloop()
