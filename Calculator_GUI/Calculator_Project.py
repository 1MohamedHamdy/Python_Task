'''
Created on Dec 20, 2022

@author: moham'''

from tkinter import *
from math import *
window=Tk()
window.geometry("350x480")
window.title("Calculator")
window.config(bg='white')
window.resizable(False, False)


txt=StringVar()
expression= ""

def NewWindow():
    newWindow = Toplevel(window)
    newWindow.title("Calculator")
    newWindow.geometry("415x480")
    newWindow.resizable(False, False)
    window.withdraw()
    frame1=Frame(newWindow,width=480,height=115,bg="black")
    frame1.pack(side=TOP)
    frame2=Frame(newWindow,width=480,height=368,bg="black")
    frame2.pack(side=BOTTOM)
    e1=Entry(frame1,textvariable=txt,width=30,bd=0,font=("Arial Bold",40),
         fg="white",bg="black",relief=SUNKEN,justify=RIGHT)
    e1.place(x=-530,y=50)
    e1.insert(0,"0")
    
    but1=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
            command=lambda:click(7),text="7",font=("Courier New",16,'bold'))

    but1.place(x=5,y=81)
    
    but2=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                command=lambda:click(4),text="4",font=("Courier New",16,'bold'))
    but2.place(x=5,y=152)
    
    but3=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                command=lambda:click(1),text="1",font=("Courier New",16,'bold'))
    but3.place(x=5,y=223)
    
    but4=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                command=lambda:click(0),text="0",font=("Courier New",16,'bold'))
    but4.place(x=72,y=294)
    
    but5=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                command=lambda:click(8),text="8",font=("Courier New",16,'bold'))
    but5.place(x=72,y=81)
    
    but6=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                command=lambda:click(5),text="5",font=("Courier New",16,'bold'))
    but6.place(x=72,y=152)
    
    but7=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                command=lambda:click(2),text="2",font=("Courier New",16,'bold'))
    but7.place(x=72,y=223)
    
    but8=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                command=lambda:click("."),text=".",font=("Courier New",16,'bold'))
    but8.place(x=139,y=294)
    
    but9=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                command=lambda:click(9),text="9",font=("Courier New",16,'bold'))
    but9.place(x=139,y=81)
    
    but10=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                 command=lambda:click(6), text="6", font=("Courier New", 16,'bold'))
    but10.place(x=139,y=152)
    
    but11=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                 command=lambda:click(3),text="3",font=("Courier New",16,'bold'))
    but11.place(x=139,y=223)
    
    but12=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                 command=lambda:click("*"),text="*",font=("Courier New",16,'bold'))
    but12.place(x=205,y=223)
    
    but13=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                 command=lambda:click("+"),text="+",font=("Courier New",16,'bold'))
    but13.place(x=205,y=81)
        
    but14=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                 command=lambda:click("-"),text="-",font=("Courier New",16,'bold'))
    but14.place(x=205,y=152)
    
    but15=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                 command=lambda:click("/"),text="/",font=("Courier New",16,'bold'))
    but15.place(x=205,y=294)
    
    butand=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                 command=lambda:click("&"),text="&",font=("Courier New",16,'bold'))
    butand.place(x=270,y=81)
    
    butor=Button(frame2,padx=1,pady=14,bd=4,fg="white",bg='#00061a',
                 command=lambda:pos_neg(e1.get()),text="+/-",font=("Courier New",16,'bold'))
    butor.place(x=270,y=294)
        
    butxor=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                 command=lambda:click("|"),text="|",font=("Courier New",16,'bold'))
    butxor.place(x=270,y=152)
    
    butnot=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                 command = lambda:click("^"),text="^",font=("Courier New",16,'bold'))
    butnot.place(x=270,y=223)
   
    but16=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                 command=clearAll,text="CE",font=("Courier New",16,'bold'),activebackground="red")
    but16.place(x=335,y=81)
    
    but17=Button(frame2,padx=20,pady=14,bd=4,fg="white",bg='red',
                 command=equal,text="=",font=("Courier New",16,'bold'),activebackground="green")
    but17.place(x=335,y=294)
    
    but18=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
                 command=clr,text="CA",font=("Courier New",16,'bold'))
    but18.place(x=335,y=152)
    but19=Button(frame2,padx=7,pady=14,bd=4,fg="white",bg='#00061a',
                 command=lambda:click("**"),text="POW",font=("Courier New",16,'bold'))
    but19.place(x=335,y=223)
    
    but20=Button(frame2,padx=7,pady=14,bd=4,fg="white",bg='#00061a',
                 command=window,text="ST",font=("Courier New",16,'bold'))
    but20.place(x=5,y=294)
    # start the GUI
    window.mainloop()   
   
    


    
def click(num):
    global expression
    expression = expression + str(num)
    expressions = [str(expression)]
    txt.set(expression)   
    print(expressions) 
   
    
    
     
    
    
     
        
    

def equal():

    try:
       
        global expression
        add = str(eval(expression))
        txt.set(add)
        expression = " "

    except:
       
        expression = ""
        txt.set("")
        
        # expression.set("Error")
        # expression=""
        
def clr():
    global expression
    length = len(txt.get())
    e1.delete(length - 1, 'end')
    expression = expression[:-1]
    

    
    


def clearAll():
    global expression
    expression = ""
    txt.set("")
    
def pos_neg(number):
    try :   
        clearAll()
        number = int(number)
        if number != 0 :
            number = number * -1
            click(number) 
    except : 
        expression = ""
        txt.set("")
                   
   
        
        


frame1=Frame(window,width=390,height=115,bg="black")
frame1.pack(side=TOP)
frame2=Frame(window,width=390,height=368,bg="black")
frame2.pack(side=BOTTOM)
e1=Entry(frame1,textvariable=txt,width=30,bd=0,font=("Arial Bold",40),
         fg="white",bg="black",relief=SUNKEN,justify=RIGHT)
e1.place(x=-530,y=50)
e1.insert(0,"0")


 

but1=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
            command=lambda:click(7),text="7",font=("Courier New",16,'bold'))

but1.place(x=5,y=81)

but2=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
            command=lambda:click(4),text="4",font=("Courier New",16,'bold'))
but2.place(x=5,y=152)

but3=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
            command=lambda:click(1),text="1",font=("Courier New",16,'bold'))
but3.place(x=5,y=223)

but4=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
            command=lambda:click(0),text="0",font=("Courier New",16,'bold'))
but4.place(x=72,y=294)

but5=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
            command=lambda:click(8),text="8",font=("Courier New",16,'bold'))
but5.place(x=72,y=81)

but6=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
            command=lambda:click(5),text="5",font=("Courier New",16,'bold'))
but6.place(x=72,y=152)

but7=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
            command=lambda:click(2),text="2",font=("Courier New",16,'bold'))
but7.place(x=72,y=223)

but8=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
            command=lambda:click("."),text=".",font=("Courier New",16,'bold'))
but8.place(x=139,y=294)

but9=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
            command=lambda:click(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=139,y=81)

but10=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
             command=lambda:click(6), text="6", font=("Courier New", 16,'bold'))
but10.place(x=139,y=152)

but11=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
             command=lambda:click(3),text="3",font=("Courier New",16,'bold'))
but11.place(x=139,y=223)

but12=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
             command=lambda:click("/"),text="/",font=("Courier New",16,'bold'))
but12.place(x=205,y=223)

but13=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
             command=lambda:click("*"),text="x",font=("Courier New",16,'bold'))
but13.place(x=205,y=81)
    
but14=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
             command=lambda:click("-"),text="-",font=("Courier New",16,'bold'))
but14.place(x=205,y=152)

but15=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
             command=lambda:click("+"),text="+",font=("Courier New",16,'bold'))
but15.place(x=205,y=294)

but16=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
             command=clearAll,text="CE",font=("Courier New",16,'bold'),activebackground="red")
but16.place(x=270,y=81)

but17=Button(frame2,padx=20,pady=14,bd=4,fg="white",bg='red',
             command=equal,text="=",font=("Courier New",16,'bold'),activebackground="green")
but17.place(x=270,y=294)

but18=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#00061a',
             command=clr,text="CA",font=("Courier New",16,'bold'))
but18.place(x=270,y=152)
but19=Button(frame2,padx=7,pady=14,bd=4,fg="white",bg='#00061a',
             command=lambda:click("**"),text="POW",font=("Courier New",16,'bold'))
but19.place(x=270,y=223)

but20=Button(frame2,padx=7,pady=14,bd=4,fg="white",bg='#00061a',
             command=NewWindow,text="PR",font=("Courier New",16,'bold'))
but20.place(x=5,y=294)
# start the GUI
window.mainloop()
10