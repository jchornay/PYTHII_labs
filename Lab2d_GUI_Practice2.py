#Jonathan Chornay
#CMSY 257 Spring 2023 Class
#Professor Charles Edwards
#
#Lab 2 Problem 4
import random
import tkinter
import tkinter.messagebox

def main():

    Lb_to_Kg("My Second Gooey")

class Lb_to_Kg:

    def __init__(self, title):

        IPADX = 5
        IPADY = 5
        PADX = 10
        PADY = 10

        #calls tkinter main method, assigning the main window to a python variable
        self.main_window = tkinter.Tk()

        #MODIFIES main window object
        self.main_window.title(title)

        #creates frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #creates button, chooses frame or window to place it in, chooses text, chooses callback method
        self.convertbutton = tkinter.Button(self.middle_frame, text='Convert', command=self.convert)
        self.quitbutton = tkinter.Button(self.middle_frame, text='Quit', command=self.main_window.destroy)


        #creates labels
        self.label1 = tkinter.Label(self.top_frame, text='Enter weight in Kg: ')

        self.entry1 = tkinter.Entry(self.top_frame, width=10)

        self.label2 = tkinter.Label(self.bottom_frame, text='')

        #packs labels, labels appear IN ORDER packed
        #packing is where padding may take place
        self.label1.pack(side='left', ipady=IPADY, ipadx=IPADX)
        self.entry1.pack(side='left', ipady=IPADY, ipadx=IPADX)

        self.convertbutton.pack(side='left', ipady=IPADY, ipadx=IPADX, padx=PADX, pady=PADY)
        self.quitbutton.pack(side='right', ipady=IPADY, ipadx=IPADX, padx=PADX, pady=PADY)

        self.label2.pack()

        #packs frames, frames appear in ORDER packed
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        #enter tkinter main loop
        tkinter.mainloop()

    #callback method
    def convert(self):

        kilograms = float(self.entry1.get())
        pounds = kilograms*2.2

        roll = random.randint(1,10)
        print(roll)

        if roll == 1:
            self.label2.configure(text=f"{kilograms:,.2f}kg equals 74 million billion lb")
        else:
            self.label2.configure(text=f"{kilograms:,.2f}kg equals {pounds:,.2f}lb")


if __name__ == '__main__':
    main()