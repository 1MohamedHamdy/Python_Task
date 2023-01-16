'''
Created on Dec 5, 2022

@author: mohamed
'''
import os
while(1):
    print('''
To create folder                                         press1
To remove empty folder                                   press2
To create file in folder                                 press3      
To remove file from folder                               press4
To Write To file                                         press5
To Append To file                                        press6
To Read Content of file                                  press7
To Remove Content of file                                press8
To copy file from directory to another                   press9
To Move file from directory to another                   press10
To search for file contain name in the database system   press11
To search for file contain name in the directory         press12
To check space of directory                              press13
To show path of current working directory                press14
To go to another directory                               press15
to list all content of current directory                 press16''')
    choice = int(input("Enter Your Choice : "))
    if choice == 1 :
        os.system("echo you run mkdir command....")
        name = input("Enter Name of directory : ")
        os.system("echo you Now create directory with name {}".format(name))
        
        y = os.popen("mkdir {}".format(name))
        y = y.read()
        print(y)   
    elif choice == 2 :
        os.system("echo you run rmdir command...")
        name = input("Enter Name of directory : ")
        os.system("echo you Now remove empty created directory with name {}".format(name))
        y = os.popen("rmdir {}".format(name))
        y = y.read()
        print(y)    
    elif choice == 3 :
        os.system("echo you run touch command...")
        name1 = input("Enter Name of directory : ")
        name2 = input("Enter Name of file : ") 
        os.system("echo you Now create empty file with name {} in chosen directory  {}".format(name2,name1))
        y = os.popen("touch {}/{}".format(name1,name2))
        y = y.read()
        print(y)       
    elif choice == 4 :
        os.system("echo you run rm command...")
        name1 = input("Enter Name of directory : ")
        name2 = input("Enter Name of file : ") 
        os.system("echo you Now remove file with name {} in chosen directory  {}".format(name2,name1))
        y = os.popen("rm {}/{}".format(name1,name2))
        y = y.read()
        print(y)  
    elif choice == 5 :
        os.system("echo you run echo command...")
        name1 = input("Enter Name of directory : ")
        name2 = input("Enter Name of file : ") 
        txt = input("Enter text you want write : ") 
        os.system("echo you Now write to file with name {} in chosen directory  {}".format(name2,name1))
        y = os.popen("echo {} >{}/{} ".format(txt,name1,name2))
        y = y.read()
        print(y)     
    elif choice == 6 :
        os.system("echo you run echo command...")
        name1 = input("Enter Name of directory : ")
        name2 = input("Enter Name of file : ") 
        txt = input("Enter text you want write : ") 
        os.system("echo you Now append to file with name {} in chosen directory  {}".format(name2,name1))
        y = os.popen("echo {} >>{}/{} ".format(txt,name1,name2))
        y = y.read()
        print(y)         
    elif choice == 7 :
        os.system("echo you run cat command...")
        name1 = input("Enter Name of directory : ")
        name2 = input("Enter Name of file : ") 
        os.system("echo you Now read content of file with name {} in chosen directory  {}".format(name2,name1))
        y = os.popen("cat {}/{} ".format(name1,name2))
        y = y.read()
        print(y)  
    elif choice == 8 :
        os.system("echo you run echo command...")
        name1 = input("Enter Name of directory : ")
        name2 = input("Enter Name of file : ") 
        os.system("echo you Now remove content of file with name {} in chosen directory  {}".format(name2,name1))
        y = os.popen("echo >{}/{} ".format(name1,name2))
        y = y.read()
        print(y)  
    elif choice == 9 :
        os.system("echo you run cp command....")
        name1 = input("Enter Name of directory1 : ")
        name2 = input("Enter Name of file : ") 
        name3 = input("Enter Name of directory2 : ")
        os.system("echo you Now copy file with name {} from directory  {} in directory {}".format(name2,name1,name3))
        
        y = os.popen("cp {}/{} {}".format(name1,name2,name3))
        y = y.read()
        print(y)  
    elif choice == 10 :
        os.system("echo you run mv command....")
        name1 = input("Enter Name of directory1 : ")
        name2 = input("Enter Name of file : ") 
        name3 = input("Enter Name of directory2 : ")
        os.system("echo you Now move file with name {} from directory  {} in directory {}".format(name2,name1,name3))
        
        y = os.popen("mv {}/{} {}".format(name1,name2,name3))
        y = y.read()
        print(y) 
    elif choice == 11 :
        os.system("echo you run locate command....")
        name1 = input("Enter Name of file : ") 
        os.system("echo you Now search for file contain name {} in the database system".format(name1)) 
        y = os.popen("locate {}".format(name1))
        y = y.read()
        print(y)   
    elif choice == 12 :
        os.system("echo you run find command....")
        name1 = input("Enter Name of file : ") 
        path  = input("Enter the path of directory : ")
        os.system("echo you Now search for file contain name {} in the directory {}".format(name1,path)) 
        y = os.popen("find {} -name {}".format(path,name1))
        y = y.read()
        print(y)     
    elif choice == 13 :
        os.system("echo you run du command....")
        path  = input("Enter the path of directory : ")
        os.system("echo you Now check space of directory {}".format(path)) 
        y = os.popen("du -h {}".format(path))
        y = y.read()
        print(y)                            
        
    elif choice == 14 :
        os.system("echo you run pwd command...")
        os.system("echo you Now show path of current working directory")
        y = os.popen("pwd")
        y = y.read() 
        print(y)      
    elif choice == 15:
        os.system("echo you run cd command...")
        path = input("Enter path you want to go : ")
        os.system("echo you Now going to this directory")
        y = os.popen("cd {} ".format(path))
        y = y.read()  
        print(y)
    elif choice == 16 :
        os.system("echo you run ls command...")
        y = os.popen("ls")
        y = y.read()
        print(y)

