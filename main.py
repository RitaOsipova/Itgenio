##########################################################
##########################################################
##########################################################

from tkinter import *

# window settings
window = Tk()
window.geometry('400x500')
window.title('Widget position')

# widgets
frame1 = LabelFrame(text='Pack', width=300, height=100)
frame1.pack(padx=30, pady=10)
frame2 = LabelFrame(text='Gird', width=300, height=100)
frame2.pack(padx=30, pady=10)
frame3 = LabelFrame(text='Place', width=300, height=100)
frame3.pack(padx=30, pady=10)
button10 = Button(frame1, text='Button10', highlightbackground='black', fg='white', width=10)
button10.pack(padx=10, pady=10, side=LEFT)
button11 = Button(frame1, text='Button11', highlightbackground='black', fg='white', width=10)
button11.pack(padx=10, pady=10, side=LEFT)
button12 = Button(frame1, text='Button12', highlightbackground='black', fg='white', width=10)
button12.pack(padx=10, pady=10, side=LEFT)

# end of program 
window.mainloop()

