
from tkinter import *

def ButtonSengalPressTracker():
    text_box1.configure(state='normal')
    text_box1.delete('1.0',END)
    ButtonSengalPressTracker.counter +=1
    text_box1.insert('end', ButtonSengalPressTracker.counter)
    text_box1.configure(state='disabled')


ButtonSengalPressTracker.counter =0

def ButtonNetherlandPressTracker():
    text_box2.configure(state='normal')
    text_box2.delete('1.0',END)
    ButtonNetherlandPressTracker.counter +=1
    text_box2.insert('end', ButtonNetherlandPressTracker.counter)
    text_box2.configure(state='disabled')

 
ButtonNetherlandPressTracker.counter =0

window_1 = Tk() 

# adding title to the window 

window_1.title("Sengal vs Netherland")

# controlling window geometry in pixles 
window_1.geometry('1200x500')   # width X height 
window_1.resizable(False, False)

image_Background=PhotoImage(file='fifa.png')
image_Background = image_Background.subsample(2,2)
BackGround_frist_window=Label(window_1,image=image_Background).place(x=0,y=0)

# Adding lable widget to the window_1
Label(window_1 , text = "Sengal " , font = ('Verdana', 18)).place(x=670,y=300)
Label(window_1 , text = "Netherland " , font = ('Verdana', 18)).place(x=1010,y=300)
Label(window_1 , text = "- " , font = ('Verdana', 18)).place(x=880,y=190)


# Adding a photo image object to use image 
photo_1 = PhotoImage(file='R.png')
photo_2 = PhotoImage(file='netherland_flag.png')
image_Background1 = photo_1.subsample(2,2)
image_Background2 = photo_2.subsample(2,2)

# editing of the image resizing of it 
# resizing decreased by increasing the number
B_1  =Button(window_1 , bd = '0' ,image=image_Background1, command = ButtonNetherlandPressTracker)

B_1.place(x = 650,y=150)
B_2  =Button(window_1 , bd = '0' ,image=image_Background2, command = ButtonSengalPressTracker)

B_2.place(x = 1000,y=140)

# Adding button to a specific window with a specific name and specific button name 
# bd border size
# destroy : delete the application 
B_3  =Button(window_1 , bd = '5' , command = window_1.destroy)
B_3.place(x=200,y=470)

text_box1 = Text(
    window_1,
    height=2,
    width=2,
    bd = '0',
    font = ('Verdana', 18),
    bg = '#%02x%02x%02x' % (240, 240, 237)
)
text_box1.place(x=940 ,y=190)


text_box2 = Text(
    window_1,
    height=2,
    width=2,
    bd = '0',
    font = ('Verdana', 18),
    bg = '#%02x%02x%02x' % (240, 240, 237)


)
text_box2.place(x=820 ,y=190)


# Call the main loop which is used when the application is ready to run to keep the code displaying 
window_1.mainloop()
