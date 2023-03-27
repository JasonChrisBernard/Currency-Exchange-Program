#create variables
amt =0
opt=0
display=0
fDigit=0
sDigit=0
thDigit=0
fthDigit=0
fifDigit=0
next2Digits=0
next3Digits=0
next4Digits=0
h='Hundred'
t='Thousand'
a='and'
r='Rupees'

#converting the numbers to  lists for words
digits=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
teens=['ten','Eleven','Twelwe','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens=['','Ten','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']

#Finding a valid amount from the user
while True:
    try:
        amt=int(input('Please enter an amount less than hundred thousand LKR. : '))
        break
    except ValueError:
        print('Please enter a valid amount!!!.')

#Placing the variables between 0 to 10000             
if(amt>0 and amt<100000):
     
#getting a valid option from the user
    opt=str(input('Please enter (W) to display the amount in words or enter (C) to convert the amount into USD. : '))
       
#Choosing an option
    if opt=='c'or opt=='C':

#converting the amount into USD
        display=(amt/200)

#rounding off the US dollars

        display=round(display)
        print('The amount in Dollars :''USD',display)

#Selecting the decimal place of the amount given by the user 
    elif opt=='w' or opt=='W':
        
        if amt//10000!=0:
           fDigit=amt//10000
           next4Digits=amt%10000
           sDigit=next4Digits//1000
           next3Digits=next4Digits%1000
           thDigit=next3Digits//100
           next2Digits=next3Digits%100
           fthDigit=next2Digits//10
           fifDigit=next2Digits%10
           if sDigit==0 and thDigit==0 and fthDigit==0 and fifDigit==0:
               print(digits[fDigit],t,r)
           elif sDigit==0 and thDigit==0 and fthDigit==1:
               print(tens[fDigit],t,a,teens[fifDigit],r)
           elif thDigit==0 and fthDigit==1:
               print(tens[fDigit],digits[sDigit],t,a,teens[fifDigit],r)
           elif fthDigit==1:
               print(tens[fDigit],digits[sDigit],t,digits[thDigit],h,a,teens[fifDigit],r)
           elif thDigit==0 and fthDigit==0 and fifDigit==0:
               print(tens[fDigit],digits[sDigit],t,r)
           elif fthDigit==0 and fifDigit==0:
               print(tens[fDigit],digits[sDigit],t,digits[thDigit],h,r)
           elif fifDigit==0:
               print(tens[fDigit],digits[sDigit],t,digits[thDigit],h,a,tens[fthDigit],r)
           else:
                print(tens[fDigit],digits[sDigit],t,digits[thDigit],h,a,tens[fthDigit],digits[fifDigit],r)
           
#if the amount of dollars is lesser than ten thousand
        elif amt//1000!=0:
            fDigit=amt//1000
            next3Digits=amt%1000
            sDigit=next3Digits//100
            next2Digits=next3Digits%100
            thDigit=next2Digits//10
            fthDigit=next2Digits%10
            if sDigit==0 and thDigit==0 and fthDigit==0:
                print(digits[fDigit],t,r)
            elif thDigit==0 and fthDigit==0:
                print(digits[fDigit],t,digits[sDigit],h,r)
            elif thDigit==1 and sDigit==0:
                print(digits[fDigit],t,a,teens[fthDigit],r)
            elif sDigit==0 and thDigit==0:
                print(digits[fDigit],t,a,digits[fthDigit],r)
            elif thDigit==1:
                print(digits[fDigit],t,digits[sDigit],h,a,teens[fthDigit],r)
            else:
                print(digits[fDigit],t,digits[sDigit],h,a,tens[thDigit],digits[fthDigit],r)
                       
#if the amount of dollars is lesser than one thousand
        elif amt//100!=0:
            fDigit=amt//100
            next2Digits=amt%100
            sDigit=next2Digits//10
            thDigit=next2Digits%10
            if sDigit==0 and thDigit==0:
                print(digits[fDigit],h,r)
            elif sDigit==1:
                print(digits[fDigit],h,a,teens[thDigit],r)
            else:
                print(digits[fDigit],h,a,tens[sDigit],digits[thDigit],r)
                       
    #if the amount of dollars is lesser than hundred
        elif amt//10!=0:
            fDigit=amt//10
            sDigit=amt%10
            
    #if the amount of dollars is lesser than twenty
            if (amt<20):
                print(teens[sDigit],r)
                
            #if amount of dollars is greater than twenty 
            else:
                print(tens[fDigit],digits[sDigit],r)
                
    #if the amount of dollars is lesser than ten 
        else:
            print(digits[amt],r)
            
    else:
        print('Please enter a valid option!!!')
    
          
else:
    print('Restricted amount!!!...Please recheck and enter amount again.')




