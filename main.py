##########################################################
##########################################################
##########################################################

from tkinter import *

# window settings
window = Tk()
window.geometry('570x300')
window.title('Color picer')
window.resizable(False, False)

# widgets
def color_generate(value):
    red = red_scale.get() 
    green = green_scale.get()
    blue = blue_scale.get()
    color = f'#{red:02x}{green:02x}{blue:02x}'
    i_red = 255 - red
    i_green = 255 - green
    i_blue = 255 - blue
    i_color = f'#{i_red:02x}{i_green:02x}{i_blue:02x}'
    label_color.config(bg=color, fg=i_color, text=color)
    color_box.insert(0, color)


frame_RGB = LabelFrame(text='Choose color',height=250, width=250)
frame_RGB.place(x=20, y=20)

frame_color = LabelFrame(text='Color', height=250, width=250)
frame_color.place(x=300, y=20)

label_color= Label(font=('Arial',15,'bold'),height=8, width=20,background='black', fg='white')
label_color.place(x=330,y=60)


red_scale=Scale(frame_RGB, label='Red',from_=0, to=255, orient=HORIZONTAL, width=20,length=200, fg='red',command=color_generate)
red_scale.place(x=10, y=10)

green_scale=Scale(frame_RGB, label='Green',from_=0, to=255, orient=HORIZONTAL, width=20,length=200, fg='green',command=color_generate)
green_scale.place(x=10, y=80)

blue_scale=Scale(frame_RGB, label='Blue',from_=0, to=255, orient=HORIZONTAL, width=20,length=200, fg='blue',command=color_generate)
blue_scale.place(x=10, y=150)

color_box = Entry(frame_color, width=6, justify=LEFT, relief=RAISED,)
color_box.place(x=59,y=180)




# passwordbox = LabelFrame() 
# passwordbox.pack(padx=80, pady=80)

# label1 = Label(passwordbox, text='Enter password:')
# label1.pack(padx=20)
# inputbox = Entry(passwordbox, background='black', fg='white', justify=CENTER, relief=RAISED, width=20, state=NORMAL)
# inputbox.pack(padx=20)
# label2 = Label(passwordbox, text='Your password:')
# label2.pack(padx=20)
# outputbox = Entry(passwordbox, justify=CENTER, relief=RAISED, width=20,)
# outputbox.pack(padx=20)

# showbutton = Button(passwordbox, text='Show')
# showbutton.pack(side=BOTTOM)

# password = inputbox.get()

# outputbox.insert(0, password)





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