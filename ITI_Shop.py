while (True) :
    total = 0
    deleted = 0
    
    product_id = {
        1 :{
            "Product name"                : "apple",
            "Number of kilos available"   :  50 ,
            "cost per kilo"               :  20 
        
        },
        2 :{
            "Product name"                : "banana",
            "Number of kilos available"   :  70 ,
            "cost per kilo"               :  15 
        },
        3 :{
            "Product name"                : "tomatoes",
            "Number of kilos available"   :  80 ,
            "cost per kilo"               :  10 
        }

    }
    print("                                             loading 0%...")
    print("                                             -"*30)
    print("                                             loading ..100%")
    print("\n")
    print("Welcome To ITI Shop ")
    print("\n")
    print("Select Mode : \n         -For Customer Press 1 \n         -For Owner Press 2 \n         -To Exit Press 0 ")
    mode = int(input("          Enter Your Mode = "))
    print("-"*40)


    if mode == 1 :
        back_1 = 1 
        back_2 = 1
        while(back_1!=0 or back_2!=0):
            print("Hello Customer....")
            print("         -To show our products press 1      \n         -To Buy from our products press 2   \n         -To print the bill press 3   \n         -To Exit press 0")
            choice = int(input("          Enter Your choice = "))
            print("-"*40)
            if choice == 1 :
                print("                                     Menu of Our Products     ")
                print("                                     --------------------")
                n = range(1,len(product_id)+1,1)
                for i in n:
                    print(product_id[i])
       
        
            elif choice == 2 :
                flag = 1 
                while(flag !=0) : 
                    buy_pro = input("Product name you Want to buy  : ")
                    buy_qua = int(input("Please Enter The Number of kilos = "))
                    n = range(1,len(product_id)+1,1)
        
                    
                    for i in n:
                        if buy_pro == product_id[i]["Product name"] :
                            product_id[i]["Number of kilos available"]-=buy_qua
                        #print(product_id[i]["Number of kilos available"])
                            brk = int(input("You want More ? "))
                            total += buy_qua*product_id[i]["cost per kilo"]
                        #print(total)
                            if (brk == 0):
                                flag = 0
                            break
                
                    bill = total    
                    
                 

             
                # product_id[i]["Number of kilos available"]-= buy_qua 
                # break
            #flag = int(input("You Want More ?"))            
            # print( product_id[i]["Number of kilos available"])    

            
            #if flag == 0 : 
                #break
            elif choice == 3 : 
                print("---------------------------------------------------------")
                print("                Your bill = %f"%(bill))
                print("|                                                        |")

                print("---------------------------------------------------------")
            elif choice == 0 : 
                break
            print("-"*90)    

            
           
 


    if(mode == 2):
        corr_user = "admin"
        corr_pass = "1234"
        back_1 = 1 
        back_2 = 1
        user_name = input("UserName : ")
        password = input("Password : ")
        if((user_name == corr_user) and (password == corr_pass)):
            while(back_1!=0 or back_2!=0):
                print("         -Add new products press 1      \n         -show products press 2   \n         -change cost press 3   \n         -remove product press 4 \n         -Exit press 0   ")
                choc = int(input("          Enter Your choice = "))
                if choc == 1 : 
                    pr_name = input("Enter Product name : ")
                    num_killos = int(input("Enter Number of kilos available "))
                    cost_k = int(input("Enter cost per kilo  "))
                    product_new = {"Product name"                : pr_name,
                                   "Number of kilos available"   :  num_killos ,
                                   "cost per kilo"               :  cost_k }
                    product_id[len(product_id)+1] = product_new               
                #product_id.update({4})
                    #print(product_id ) 
                    #owner_list = product_id.copy()
                    #back_1 = int(input("For back press 1 : "))
            #print(owner_list)    
                
                elif choc == 2 : 
                    print("                                     Menu of Our Products     ")
                    print("                                     --------------------")
                    # n = range(1,len(product_id)+1,1)
                    # print(deleted)
                    # for i in n:
                        # print(i)
                    print(product_id)
                            
                    
                    #back_2 = int(input("For back press 1 : "))
                    print("-"*90)    

                
                elif choc == 3 : 
                    
                    pr_nme = input("Product name you Want to change cost : ")
                    cost_chg = int(input("Enter New Cost : "))
                    x = range(1,len(product_id)+1,1)
                    for j in x:
                        if pr_nme == product_id[j]["Product name"] :
                            product_id[j]["cost per kilo"] = cost_chg
                            #print(product_id)     
                            break
                            
                elif choc ==4 :
                    pr_nme = input("Product name you Want remove from list : ")
                    x = range(1,len(product_id)+1,1)
                    for j in x:
                        if pr_nme == product_id[j]["Product name"] :
                            del product_id[j]
                            #product_id[j+1] = 1
                            deleted = j 
                            
                            #print(product_id)
                            break
                    
                 
                elif choc == 0 : 
                    break            
                            
                           
                    

                
            
        
        else:
            print("UserName or Password incorrect try again..")
    
    if(mode == 0) :
        break
    