name = input ("what is your name? \n")
allowedUsers = ['seyi', 'mike', 'love']
allowedPassword =  ('passwordseyi','passwordmike', 'passwordlove')  

if(name in allowedUsers):
    password = input ('your password?  \n')
    UserId = allowedUsers.index(name)
    
    if (password == allowedPassword[UserId]):
        
        import datetime as dt

        currentDatetime =  dt.datetime.now()

        print (currentDatetime)

        print ('welcome %s'  % name)

        print ('these are the following options;')
        
        print ('1. cashDeposit')
        print ('2. withdrawal')
        print ('3. complaints')

        selectedOptions = int( input('please select an option; \n'))

        if (selectedOptions == 1 ):
            print ('you have selected %s' % selectedOptions)
            
            cashDeposit = int(input('how much do you want deposit? \n '))
            
            print ('outbalance')
            print (cashDeposit)

          
            
        elif (selectedOptions == 2 ):
            print ('you have selected %s' % selectedOptions)

            withdrawal = int (input ('how much do you want to withdraw? \n'))
            cashDeposit = 300000

            if ( withdrawal <= cashDeposit):
                print ('Take you cash')

            else:
                print ('Insufficient balance')

        
      
        elif (selectedOptions == 3):
            print ('you have selected %s' % selectedOptions)
            complaint = input ('what issue would you like to report? \n')
            print ('Thank you for contacting us')


        else:
            print ('Invalid selection, please try again')


    else:
     print ('password incorrect, please try again')


else:
    print ('name not found, please try again') 




