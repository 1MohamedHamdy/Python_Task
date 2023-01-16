from datetime import datetime
#Pola 2Sab shop 

#only Try Nice Format
print("                                             loading 0%...")
print("                                             -"*30)
print("                                             loading ..100%")
print("\n")
f1 = open("format.txt" , "r")
print(f1.read())
total = 0 
br = 0
#Exit = 1
#while(Exit):
#List of available drinks 
list_drinks = ["2Sab","6Mr Hendy","Mango","Strawberry"]
drink_size = ["small","meduim","large"]
drink_list = { 
                "2Sab":{
                        0 : 3 ,
                        1 : 5 ,
                        2 : 7
                },
                "6Mr Hendy":{
                        0 : 3 ,
                        1 : 5 ,
                        2 : 7 ,
                },
                "Mango":{
                        0 : 5 ,
                        1 : 7 ,
                        2 : 10 ,
                },
                "Strawberry":{
                        0 : 6 ,
                        1 : 8 ,
                        2 : 12 ,
                }        
            } 

f1 = open("2Sab_Shop_Menu.txt",'w')
f1.write("-"*85+"\n")
f1.write("drinks"+"                |                 "+"Size"+"                  |            "+"cost"+"                                  "+"\n")
f1.write("-"*85+"\n")

for i in range(0,3,1):
    if drink_size[i] == "meduim" : 
        f1.write(str(list_drinks[0])+"                  |                 "+str(drink_size[i])+"                |              "+str(drink_list["2Sab"][i])+"\n")
    else : 
        f1.write(str(list_drinks[0])+"                  |                 "+str(drink_size[i])+"                 |              "+str(drink_list["2Sab"][i])+"\n")
        
f1.write("-"*85+"\n")
for i in range(0,3,1):
    if drink_size[i] == "meduim" : 
        f1.write(str(list_drinks[1])+"             |                 "+str(drink_size[i])+"                |              "+str(drink_list["6Mr Hendy"][i])+"\n")
    else : 
        f1.write(str(list_drinks[1])+"             |                 "+str(drink_size[i])+"                 |              "+str(drink_list["6Mr Hendy"][i])+"\n")
        
f1.write("-"*85+"\n")
for i in range(0,3,1):
    if drink_size[i] == "meduim" :   
        f1.write(str(list_drinks[2])+"                 |                 "+str(drink_size[i])+"                |              "+str(drink_list["Mango"][i])+"\n")
    else : 
        f1.write(str(list_drinks[2])+"                 |                 "+str(drink_size[i])+"                 |              "+str(drink_list["Mango"][i])+"\n")
        
f1.write("-"*85+"\n")
for i in range(0,3,1):
    if drink_size[i] == "meduim" : 
        f1.write(str(list_drinks[3])+"            |                 "+str(drink_size[i])+"                |              "+str(drink_list["Strawberry"][i])+"\n")
    else : 
        f1.write(str(list_drinks[3])+"            |                 "+str(drink_size[i])+"                 |              "+str(drink_list["Strawberry"][i])+"\n")
        
f1.write("-"*85+"\n")


#f1.write(str(drink_list)+"\n")
f1.close()
while(br==0):
    print(
'''
- Menu of drinks   Press 1 
- Purchase List    Press 2
- Print Bill       Press 3
- Exit             Press 4'''); 
    choice = int(input("Enter Your Choice : "))   
    print("-"*50)       
    if choice == 1 : 
        print('''
                        -----------------------------------------------------------------
                       |                        Menu of drinks                           |                 
                        -----------------------------------------------------------------''')    
        f2 = open("2Sab_Shop_Menu.txt",'r')
        print(f2.read())
        f2.close()     
        print("-"*150)       
        
    elif choice == 2 : 
        print('''
                        -----------------------------------------------------------------
                       |                        Purchase List                            |                 
                        -----------------------------------------------------------------''')    
    #br = 1  
    #count = 0
    
        num_order = int(input("Enter Number of orders : "))
        print("-"*30)
        f3 = open("2Sab_Shop_Purchase List.txt",'w')
        f3.write("-"*120+"\n")
        f3.write("drinks"+"              |             "+"Size"+"                  |            "+"Quantity"+"             |           "+"Cost"+"\n")
        f3.write("-"*120+"\n")
        f3.close()
        for order in range(0,num_order):
    
            print("Order No."+str(order+1)+"#")

        
            drink = input("drink name = ")    
            size  = input("drink size = ")
            if size.lower() == "small":
                conv_size = 0
            elif size.lower() == "meduim": 
                conv_size = 1
            elif size.lower() == "large":
                conv_size = 2
            else :
                print("Uncorrect drink size!")
        
            number = int(input("Number of drinks = "))
            total += number * drink_list[drink][conv_size]
            cost   = number * drink_list[drink][conv_size]
        
            f4 = open("2Sab_Shop_Purchase List.txt",'a')
   
            if drink == "2Sab" : 
        #f4.write(str(list_drinks[0])+"                  |                 "+str(drink_size[i])+"                |              "+str(drink_list["2Sab"][i])+"\n") 
                if size.lower() == "meduim" :
                    f4.write(drink+"                |             "+size+"                |               "+str(number)+"                 |            "+str(cost)+"\n")
                
                else :
                    f4.write(drink+"                |             "+size+"                 |               "+str(number)+"                 |            "+str(cost)+"\n")
            elif drink == "6Mr Hendy" :
                if size.lower() == "meduim" :
                    f4.write(drink+"           |             "+size+"                |               "+str(number)+"                 |            "+str(cost)+"\n")
                else : 
                    f4.write(drink+"           |             "+size+"                 |               "+str(number)+"                 |            "+str(cost)+"\n")
            elif drink == "Mango" :
                if size.lower() == "meduim" :
                    f4.write(drink+"               |             "+size+"                |               "+str(number)+"                 |            "+str(cost)+"\n")
            
                else :
                    f4.write(drink+"               |             "+size+"                 |               "+str(number)+"                 |            "+str(cost)+"\n")
            elif drink == "Strawberry" :
                if size.lower() == "meduim" :
                    f4.write(drink+"          |             "+size+"                 |               "+str(number)+"                 |            "+str(cost)+"\n")
                else : 
                    f4.write(drink+"          |             "+size+"                 |               "+str(number)+"                 |            "+str(cost)+"\n")
            print("-"*50)
        
    #print(total)   
        f5 = open("Total_Bill.txt",'w')
        f5.write("Total = " + str(total)+" L.E"+"                                           ")
        f5.close()
        

       
        
            #print(drink_l)
        f4.close()
        print("-"*150)       

            
        # drink_l.append(drink)  
        # size_l.append(size)
        # number_l.append(number)
        # count +=1     
        
        
       
       
        #print(total)
        
        #br = int(input("You want more ? "))
        # f3 = open("2Sab_Shop_Purchase List.txt",'w')
        # f3.write("-"*85+"\n")
        # f3.write("drinks"+"                |                 "+"Size"+"                  |            "+"cost"+"                                  "+"\n")
        # f3.write("-"*85+"\n")
        # f3.close()
        # f4 = open("2Sab_Shop_Purchase List.txt",'a')
   
           
        # f4.write(drink_l[count-1]+"                |                 "+size_l[count-1]+"                |                 "+str(number_l[count-1])+"\n")
       
        
    # print(drink_l)
    # f4.close()
        
        
    if choice == 3 : 
        print('''
                        -----------------------------------------------------------------
                       |                        Bill                                     |
                        -----------------------------------------------------------------''')   
        f1 = open("2Sab_Shop_Purchase List.txt",'r')
        print(f1.read())   
        print("-"*120)
        f2 = open("Total_Bill.txt",'r')
        now = datetime.now()

        print(f2.read()) 
        f2.close()
        print("-"*120)
        print(now)
        print("                                           "+"*"*30)
        print("                                                 THANK YOU COME AGAIN")
        print("                                           "+"*"*30)
        f3 = open("Total_Bill.txt",'w')
        f3.write("Total = 0"+" L.E"+"                                           ")
        f3.close()
        f4 = open("2Sab_Shop_Purchase List.txt",'w')
        f4.write("")
        f4.close()
        print("-"*150)       

    if choice == 4 :
        br = 1 
        #print("-"*150)       

    

    




    
    
                        
    
    
              
    
 