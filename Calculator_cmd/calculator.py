
print("\nITI Calculator")
print("-"*100)
print("Select Mode ")
print("1-Mode Scientific\n2-Mode Programming")
mode = int(input("Enter Mode = "))
print("-"*50)
brk = 1
#For Scientific Mode
if mode == 1 : 
    print("List of Avaliable key name and operations ")
    print("-"*60)
    my_dict = {
        '+  '     : "sum" ,
        '-  '     : "Subtraction" ,
        '*  '     : "multiplication" ,
        '/  '     : "Division" ,
        '%  '     : "Modulus" ,
        '** '     : "Exponentiation" ,
        '$  '     : "root(Square,Cubist)" ,
        '1/x'     : "Multiplicative_inverse" ,
        '|x|'     : "Absolute_value" ,
        '// '     : "Floor_division" ,	
        '!  '     : "Factorial" 
        
        


        
        
    }
    list = ['+  ' ,'-  ' ,'*  ','/  ','%  ','** ','$  ','1/x','|x|','// ','!  '] 
    #n = range(1,len(my_dict)+1,1)
    for i in list:
        print(i +"       "+ my_dict[i])
    print("-"*60)
    
    while(brk):
        op  = input("Enter key name of Operation = ")
        f_num = float(input("Enter First Number = "))
   
   
        if op == '+':
            s_num = float(input("Enter Second Number = "))
            result = f_num + s_num 
            print("Result = %f"%(result))
   
        elif op == '-':
            s_num = float(input("Enter Second Number = "))
            result = f_num - s_num 
            print("Result = %f"%(result))
        
        elif op == '*':
            s_num = float(input("Enter Second Number = "))
            result = f_num * s_num 
            print("Result = %f"%(result))    
        
        elif op == '/':
            s_num = float(input("Enter Second Number = "))
            if(s_num == 0):
                print("Error invaild operation(divison by zero)")
            else :     
                result = f_num / s_num 
                print("Result = %f"%(result))  
        elif op == '%':
            s_num = float(input("Enter Second Number = "))
            result = f_num % s_num 
            print("Result = %f"%(result))  
        
        elif op == '**':
            s_num = float(input("Enter base = "))
            result = f_num ** s_num 
            print("Result = %f"%(result))  
    
        elif op == '$':
            root_dg = int(input("Enter degree of root = "))
            if root_dg == 2 :
                result = f_num*(1/root_dg) 
            elif root_dg == 3 :     
                result = f_num*(1/root_dg)*(1/root_dg)
            print("Result = %f"%(result)) 
        
        elif op == '1/x':
            result = 1/f_num
            print("Result = %f"%(result)) 
    
        elif op == '|x|':
            if f_num>0 :
                result = f_num 
            elif f_num<0 :
                result = f_num*-1 
            print("Result = %f"%(result)) 
    
        elif op == '//':
            s_num = float(input("Enter Second Number = "))
            result = f_num // s_num 
            print("Result = %f"%(result))  
        
        elif op == '!':
            nuum = int(f_num)
            result = int(f_num)
            n = range(int(f_num),1,-1) 
            for i in n : 
                nuum-=1
                result *=nuum
            print("Result = %d"%(result))   
               
    
        else :
            print("Invalid operation try again...")
        brk = int(input("Press 1 For More Operations and 0 To Exit = "))    
        print("-"*50)    
        
if mode == 2 : 
    print("List of Avaliable key name and operations ")
    print("-"*60)
    my_dict = {
        'bin'     : "Binary" ,
        'oct'     : "Octal" ,
        'hex'     : "Hexadecimal" ,
        'dec'     : "Decimal" ,
        '&  '     : "And" ,
        '|  '     : "Or" ,
        '~  '     : "Not" ,
        '^  '     : "Xor" ,
        '~& '     : "Nand" ,
        '~| '     : "Nor"  ,
        '<< '     : "Shift_Left" ,	
        '>> '     : "Shift_Right" 
        
        


        
        
    }
    list = ['bin' ,'oct' ,'hex','dec','&  ','|  ','~  ','^  ','~& ','~| ','<< ','>> '] 
    #n = range(1,len(my_dict)+1,1)
    for i in list:
        print(i +"       "+ my_dict[i])
    print("-"*60)
    while(brk):
        op  = input("Enter Operation = ")
        f_num = int(input("Enter First Number = "))
        if op == 'bin' : 
            result = bin(f_num)
            print("Result = %s"%(result)) 
        
        elif op == 'oct' : 
            result = oct(f_num)
            print("Result = %s"%(result)) 
    
        elif op =='hex' : 
            result = hex(f_num)
            print("Result = %s"%(result))     
     
        elif op == 'dec' : 
            result = f_num
            print("Result = %s"%(result))   
    
        elif op == '&' : 
            s_num = int(input("Enter Second Number = "))
            sh_num = input("For Show Result in decimal press d and in binary press b and in hexdecimal press h = ")
            if sh_num == 'd' :
                result = f_num & s_num 
            elif sh_num == 'b' :     
                result = bin(f_num & s_num)
            elif sh_num == 'h' :     
                result = hex(f_num & s_num)    
            else : 
                print("invaild input try again....")

            print("Result = %s"%(result)) 
            
        elif op == '~&' : 
            s_num = int(input("Enter Second Number = "))
            sh_num = input("For Show Result in decimal press d and in binary press b and in hexdecimal press h = ")
            if sh_num == 'd' :
                result = ~(f_num & s_num) 
            elif sh_num == 'b' :     
                result = bin(~(f_num & s_num))
            elif sh_num == 'h' :     
                result = hex(~(f_num & s_num))    
            else : 
                print("invaild input try again....")

            print("Result = %s"%(result)) 
        
        elif op == '~|' : 
            s_num = int(input("Enter Second Number = "))
            sh_num = input("For Show Result in decimal press d and in binary press b and in hexdecimal press h = ")
            if sh_num == 'd' :
                result = ~(f_num | s_num) 
            elif sh_num == 'b' :     
                result = bin(~(f_num | s_num))
            elif sh_num == 'h' :     
                result = hex(~(f_num | s_num))    
            else : 
                print("invaild input try again....")

            print("Result = %s"%(result))     
            
        elif op == '|' : 
            s_num = int(input("Enter Second Number = "))
            sh_num = input("For Show Result in decimal press d and in binary press b and in hexdecimal press h = ")
            if sh_num == 'd' :
                result = f_num | s_num 
            elif sh_num == 'b' :     
                result = bin(f_num | s_num)
            elif sh_num == 'h' :     
                result = hex(f_num | s_num)    
            else : 
                print("invaild input try again....")

            print("Result = %s"%(result))   
        
        elif op == '^' : 
            s_num = int(input("Enter Second Number = "))
            sh_num = input("For Show Result in decimal press d and in binary press b and in hexdecimal press h = ")
            if sh_num == 'd' :
                result = f_num ^ s_num 
            elif sh_num == 'b' :     
                result = bin(f_num ^ s_num)
            elif sh_num == 'h' :     
                result = hex(f_num ^ s_num)    
            else : 
                print("invaild input try again....")

            print("Result = %s"%(result))   

        elif op == '~' : 
            sh_num = input("For Show Result in decimal press d and in binary press b and in hexdecimal press h = ")
            if sh_num == 'd' :
                result = ~f_num 
            elif sh_num == 'b' :     
                result = bin(~f_num)
            elif sh_num == 'h' :     
                result = hex(~f_num)    
            else : 
                print("invaild input try again....")

            print("Result = %s"%(result)) 
        
        elif op == '<<' : 
            s_num = int(input("Enter Number of bits= "))
            sh_num = input("For Show Result in decimal press d and in binary press b and in hexdecimal press h = ")
            if sh_num == 'd' :
                result = f_num << s_num 
            elif sh_num == 'b' :     
                result = bin(f_num << s_num)
            elif sh_num == 'h' :     
                result = hex(f_num << s_num)    
            else : 
                print("invaild input try again....")

            print("Result = %s"%(result))  

        elif op == '>>' : 
            s_num = int(input("Enter Number of bits= "))
            sh_num = input("For Show Result in decimal press d and in binary press b and in hexdecimal press h = ")
            if sh_num == 'd' :
                result = f_num >> s_num 
            elif sh_num == 'b' :     
                result = bin(f_num >> s_num)
            elif sh_num == 'h' :     
                result = hex(f_num >> s_num)    
            else : 
                print("invaild input try again....")

            print("Result = %s"%(result))   
        else :
            print("Invalid operation try again...")
        brk = int(input("Press 1 For More Operations and 0 To Exit = "))    
        print("-"*50)         
         
            
        
        
        
        
    
       

        
            
   
        
          