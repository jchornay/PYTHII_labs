#Jonathan Chornay
#CMSY 257 Spring 2023 Class
#Professor Charles Edwards
#
#Lab 2 Problem 4

import tkinter
import tkinter.messagebox

def main():

    GUI("My First Gooey")

class GUI:

    def __init__(self, title):

        IPADX = 10
        IPADY = 10
        PADX = 10
        PADY = 10

        #calls tkinter main method, assigning the main window to a python variable
        self.main_window = tkinter.Tk()

        #MODIFIES main window object
        self.main_window.title(title)

        #creates frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #creates button, chooses frame or window to place it in, chooses text, chooses callback method
        self.button1 = tkinter.Button(self.bottom_frame, text='This is the button', command=self.error_message)
        self.button2 = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        #creates labels
        self.label1 = tkinter.Label(self.top_frame, text='Do not click the button')

        #packs labels, labels appear IN ORDER packed
        #packing is where padding may take place
        self.label1.pack(ipady=IPADY, ipadx=IPADX)
        self.button1.pack(side='left',ipady=IPADY, ipadx=IPADX, padx=PADX, pady=PADY)
        self.button2.pack(side='right',ipady=IPADY, ipadx=IPADX, padx=PADX, pady=PADY)

        #packs frames, frames appear in ORDER packed
        self.top_frame.pack()
        self.bottom_frame.pack()

        #enter tkinter main loop
        tkinter.mainloop()

    #callback method
    def error_message(self):
        tkinter.messagebox.showinfo('OH GOD', 'YOU CLICKED THE BUTTON >:(')


if __name__ == '__main__':
    main()