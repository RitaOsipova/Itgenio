##########################################################
##########################################################
##########################################################

from tkinter import *

# window settings
window = Tk()
window.geometry('400x300')
window.title('')
window.resizable(False, False)

# widgets

passwordbox = LabelFrame()
passwordbox.pack(padx=80, pady=80)

label1 = Label(passwordbox, text='Enter password:')
label1.pack(padx=20)
inputbox = Entry(passwordbox, background='black', fg='white', justify=CENTER, relief=RAISED, width=20, state=NORMAL)
inputbox.pack(padx=20)
label2 = Label(passwordbox, text='Your password:')
label2.pack(padx=20)
outputbox = Entry(passwordbox, justify=CENTER, relief=RAISED, width=20,)
outputbox.pack(padx=20)

showbutton = Button(passwordbox, text='Show')
showbutton.pack(side=BOTTOM)

password = inputbox.get()

outputbox.insert(0, password)













# label1 = Label( text='''Lorem ipsum dolor sit amet, consectetur \n 
# adipiscing elit. Pellentesque ultricies lobortis mi \n
# sit amet pellentesque.,''', justify=CENTER, relief=RAISED, bg='#722c85', fg='white', width=50, height=5)
# label1.pack(pady=30)


# frame1 = LabelFrame(bg='#722c85')
# frame1.pack(padx=80, pady=30)


# button10 = Button(frame1, text='start', highlightbackground='#ff0000', fg='white', width=10)
# button10.pack(padx=10, pady=10, side=LEFT)

# button11 = Button(frame1, text='exit', highlightbackground='#029e45', fg='white', width=10)
# button11.pack(padx=10, pady=10, side=LEFT)

# frame1 = LabelFrame(text='Pack', width=300, height=100)
# frame1.place(x=10, y=400)
# frame2 = LabelFrame(text='Gird', width=300, height=100)
# frame2.place(x=10, y=130)
# frame3 = LabelFrame(text='Place', width=300, height=100)
# frame3.place(relx=0.15, y=10, relwidth=0.7)

# button12 = Button(frame1, text='Button12', highlightbackground='black', fg='white', width=10)
# button12.pack(padx=10, pady=10, side=LEFT)


# button20 = Button(frame2, text='Button20', highlightbackground='black', fg='white', width=30)
# button20.grid(row=0, padx=10, pady=10, columnspan=2)

# button21 = Button(frame2, text='Button21', highlightbackground='black', fg='white', width=10)
# button21.grid(row=1, padx=10, pady=10)

# button22 = Button(frame2, text='Button22', highlightbackground='black', fg='white', width=10, height=10)
# button22.grid(row=1, column=1, padx=10, pady=10, rowspan=3)

# button23 = Button(frame2, text='Button23', highlightbackground='black', fg='white', width=10)
# button23.grid(row=2, padx=10, pady=10)
 
# # button24 = Button(frame2, text='Button24', highlightbackground='black', fg='white', width=10)
# # button24.grid(row=2, column=1, padx=10, pady=10)

# button25 = Button(frame2, text='Button25', highlightbackground='black', fg='white', width=10)
# button25.grid(row=3, padx=10, pady=10)

# button30 = Button(frame3, text='Button22', highlightbackground='black', fg='white', width=10)
# button30.place(x=85, y=15)

# button31 = Button(frame3, text='Button23', highlightbackground='black', fg='white', width=10)
# button31.place(x=185, y=15)


# end of program 
window.mainloop()
