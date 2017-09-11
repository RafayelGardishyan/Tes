from tkinter import *

class ConfigurationWindow:


    def get_info(self):

        data = self.inputEntry1.get()
        data2 = self.inputEntry2.get()
        with open('Configuration/data/time.txt', 'w+') as f:
            f.write(data)
        with open('Configuration/data/name.txt', 'w+') as f:
            f.write(data2)
        with open('Configuration/data/configured.txt', 'w+') as f:
            f.write('true')

    def __init__(self):
        self.root = Tk()
        self.title = Label(self.root, text='Raf Assistant Configuration', font="'Verdana', 20")
        self.mainFrame = Frame(self.root, bd=5)
        self.inputLabel1 = Label(self.mainFrame, text='Alarm Time (0 - 24):')
        self.inputEntry1 = Entry(self.mainFrame)
        self.inputLabel2 = Label(self.mainFrame, text='Your name:')
        self.inputEntry2 = Entry(self.mainFrame)
        self.submitButton = Button(self.mainFrame, text='Submit', command=self.get_info)

        self.title.grid(column=0, row=0, padx=5, pady=5)
        self.mainFrame.grid(column=0, row=1, padx=5, pady=5)
        self.inputLabel1.grid(column=0, row=0, padx=5, pady=5)
        self.inputEntry1.grid(column=1, row=0, padx=5, pady=5)
        self.inputLabel2.grid(column=0, row=1, padx=5, pady=5)
        self.inputEntry2.grid(column=1, row=1, padx=5, pady=5)
        self.submitButton.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
        self.root.mainloop()



