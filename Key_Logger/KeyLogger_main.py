'''
Created on Dec 19, 2022

@author: mohamed
'''
import os 

while(1):
    print('''
To KeyLogger                     Press1
To MouseLogger                   Press2''')
    choice = int(input("Enter Your Choice : "))
    if choice == 1 :
        os.system("echo You run KeyLogger Script...")
        #os.popen("touch /home/mohamed/Desktop/Key_Logger")
        os.popen("ln -s /dev/input/event2 /home/mohamed/Desktop/Key_LoggerKey_Logger")
    elif choice == 2 :
        os.system("echo You run Stdout Script...")
        #os.popen("touch /home/mohamed/Desktop/Key_Logger")
        os.popen("ln -s /dev/input/mouse2 /home/mohamed/Desktop/mouse_Logger")
            
    
