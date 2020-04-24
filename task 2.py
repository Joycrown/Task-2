import string
import random
container = []	
def user_login ():
    first_name = input ('Enter Your First Name: \n')
    last_name = input ('Enter Your Last Name: \n')
    email = input('Enter Your Email: \n')
    user_details = [first_name,last_name,email]
    character = string.ascii_letters
    length =5
    password_random= ''.join(random.choice(character)for i in range(length))
    password= (first_name[0:2] + last_name[-2:] + password_random)
    print('Your password is ' + password)
    user_checking = input("Enter 'YES' or 'NO'. Is The Above Password OK? \n").lower()
    print(user_checking)
    if user_checking =='yes':
        user_details.append(password)
        container.append(user_details)
        new_user= input("Enter 'YES' or 'NO'  Do You Want To Enter A New User? \n" ).lower()
        print(new_user)
        if new_user=='yes':
            user_login()
        elif new_user== 'no':
            print(container)
    	    
    elif user_checking=='no':
        new_password=input('Enter A SEVEN Password Character \n')
        print(new_password)
        if len(new_password)>=7:
            user_details.append(new_password)
            container.append(user_details)
            new_user=input('Enter YES or NO. Do You Want To Enter A New User \n')
            print(new_user)
            if new_user=='yes':
                user_login()
            elif new_user =='no':
                print(container)
        elif len(new_password)<7:
            print('PLS ENTER A SEVEN CHARACTER PASSWORD')
            print('pls start again')
            user_login()
            
                
     	     
         



user_login()
