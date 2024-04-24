'''a=2
b=3
#not operator
print(not (a>b) or (a==b) and (a<b))
# or operator
print ((a<b)or (a==b))'''

    #type  converstion 


'''a=2 #int value
b=3.4 #float value
sum=a+b
print(sum)''' #give value in float

     #type casting
'''a=float('12')
b = 1.3
print(a + b)
'''
                  #  variable

# print(max(1,2,3,2,4,5,6))
'''
print(round(21.5))'''
                #     range()
    # range(start,stop,step)        point.3 step value increment the number type by user like 1 ka increment only use in integer value    




#input 
'''age=input('enter your age')
print ('welcome ',age)

number =int(input('input your number'))
print ('your number is',number)'''


#first question input 2 numbers $ print there sum 
'''num1 =int(input('first num number'))
num2= int(input('second number'))
print ('adittion of numbers is',num1+num2)'''


#indexing in python [2]
#positive slicing
# heres the syntax like str[starting_index : ending_index]
'''str='this is not air'
print (str[:4]) #it will give ( this)

#negative slicing
print(str[-5:-1])


#endwith() this function return boolen value like
print(str.endswith("ir"))'''

# captilize() it will convert first char into uppercase and remanng are lower
#replace(old string dani , yaha new string dani) ya replace string ko new vlue ka sath
# find(string dani) it will the index of that string

# 1st problem
'''a=input('enter your name')
print(len( a ))''' # len () count the langht of function

      #  conditional statament 
 # if statemint
'''a=7 
if(a>=10):
    print('good job you have passed')
elif(a>=6):
    print('you just got passing marks')
else:
    print('you failed')

'''

''' 
d= input('Enter your definition ')
if(d>=20):
    print('you are failed'
          )
else:
    print('welcome you are passed')'''

     
    



             # CHAPTER 3 list and tuples


# list

'''countries=['fad','multan','lhr', 'karachi'] '''  #it is like array in c++ or java
'''countries[0]= 'Pakistan'    '''                    #accessing value by using index number
'''countries[1]='Sindh'           ''' '''                
del countries[3]                  '''             #delete any element from list by using del keyword
'''countries.append('Balochistan') '''               #add elements at last position
'''countries.insert(1,'Punjab')      '''             #add elements at specific postion give  index no and  value 
'''countries.pop(1)        '''                       #remove element  from list by giving index number
"""
print(countries)"""




        
                                              #list method only for list 
'''
list1=[12,3,13242,543,43425,56,43]
list2=['apple','bananan','orange','mango','grapes']
list1.extend(list2)'''                               #   extend() combine  two lists


            



             # first is append() add element at the end of list 
# list=[2,1,3]

#print(list.append(9))

                   #2 is Sort() list in ascendind order
# list.sort()
                   #3 copy() give  a full copy of that list
# copied_list = list1.copy



# first problem
'''a=input("movie name")
list=[]
list.append(a)
print(list)

'''
# palndrome
'''
a=[1,2,3,4,1]
b=a.copy()
b.reverse()
  
if(a==b):
    print("pannaldrome")
else:
    print("not palandrome")

'''

                           #TUPLES
    #tuples are immutable means once we create tuple we can not change it . 

tup=(1,21,23,34,3,44,'ali',True)  
  

   #tuple method    
    #first is addition of two tuples 
    #second is len() gives length               
    #third is sort() method which sorts the elements in ascending order
    #fourth is str() converts the whole tuple into string
    #fifth is format() also convert the tuple into string but this time with a special character between every element
'''tup=() #empty tuple   
a=(1,12,3,4,53,2,2,2)
print(a.count(2))
'''

                #                      FUNCTIONS 
# practise functions  
  
'''a=('ali','ahmad','raza','hussan')
name=input('enter your name')
age=input('enter your age')

def greeting_function(a,name,age):
    print('welcome user ' + a[2] + name ,age)

greeting_function(a,name,age);
'''

'''def adding(num1,num2):
    return print( num1+num2)
    
adding(2,2)'''



#                                     IF-Statement in python
# a=False
# if(a==False):
#     print('hello')
# else :
#     print('its false')

# age=int(input('enter your age')) 
# if ( age>=30):
#     print('you can vote and get license')
# elif (age>=25):
#     print('confirm')
# elif ( age>=18):
#     print('you can vote')
# else :
#     print('you are to small') 


# num=int(input("Enter the number: "))
# if num%5==0:
#     print('mutiple of five')
# else:
#     print('not the mutiple of five')
'''
value=int(input ('input the value ='))

if value<10:
    print(value,'is lass than 10')
elif value>10:
    print(value,'value is greater thn 10')
else:
    print('value is too samll')    '''
   
   #                                      calculater code with if 

'''num1=int(input('enter first digit : '))
num2=int(input('enter first digit : '))
op=input('enter operator : ')

if op== '+':
    print(num1+num2)

elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(abs(num1/num2))
else:
    print('invalid opreator')'''








                                        # DICTONARY AND SETS
                            #dictonary

 # dictonary is combined key and value
'''dic={
    "key":"value",
    'name':'azmat',
     'subject':['math','english'],
     'roll':(1,2,34,5,6)
 }
print(dic["name"])
print(dic['subject'][1]) # in dictonary '''

                            #add value in dictonary
# '''dic['age']=12
# print(dic)
# '''
                              #nested dictonary

'''info={
    "nme":"ali",
    "city":{
        "country":'fsd',
         "state":"punjab"
    }

}

print(info["city"]["country"])

dic={
    'cat':'small animal',
    'table':('wooden','metal','plastic')
}


'''

                         #dictonary method
               # update()  method add new item to dict or update existing item
                #key() method is return all the keys  present inside a dictionary
                #  values() method returns all the values present inside a dictionary
                # items () method returns a list of tuples containing key and its corresponding value


'''print(info.keys())
print(info.values())
print(info.items())''' 
'''print(info.get('city'))
info.update({'city':'karachi'})
'''



                                     #SET
       # in set dictonery are not used
      #set  doublicate value ko ik hi bar store karta hy  and tey are mutable but its element are imutable
collection={'h','h',1,32,24,3223,4,2,1,234,1234,2,34,25} # set has un order 



       # problem
obj={'python','python','c++','c++','c'}
'''print(len(obj),' classes  needed')'''





               # create a empty set
empty=set()
empty.add(2)
empty.add('sagyfghf')
'''print(collection.pop())'''


            # set method
                  #add() use  for adding an element in set
                 #remove() use for removing an element from set
                 #pop()    use for pick any random element from set
                 # clear()   use for remove all elements form set
                  # union()   use for combine two sets
                 #intersection()  use for get common element between two sets

                        
                        
                          # chp no 5
                      
                      
                      # loops  in  python

             # WHile loop  is used when we don't know how many times the condition will be true
              # it keep on running until the condition become false

                # syntax : while condition:
                         # code block to be executed

                        # example 1
'''count =1
while count<=100:
    print(count)
    count +=1'''

                     # ex 2 100 to 1
'''count =100
while count>=1:
    print(count)
    count -=1'''
    

                # ex3 table
"""n=int( input('enter number') );
i=1 
while i<=11:
    print(n*i)
    i+=1    ;       
"""

                                             #For LooP
# for ch in "hello":
#     print(ch)

# for cha in '423':
#     print(cha)

my_list=[
       12,213,23,21,321,123,12
]
'''
for list in my_list:
     if list==21:
        break
     print(list)
    '''
'''
for num in range(4):
    print(num)
else:
    print('finished')'''


#                             nested for loop in list
'''my_lists=[
    [21,23,213,3],
    [123,123,12213,]
]
for list in my_lists:
    for num in list:
        print()'''
    #     print(num) 
    # print('finished')

                #               TRY AND EXCCEPT
'''try:
    x =int(input('enter '))
    print(x)    
  
except:
    print('not a number')'''







                                        # first problem of python

'''
a=[1,2,3,4,3,2]
b=[3,4,54,6,57]'''
#set and give in object form
'''print(set(a+b)) 
print(sorted(set(a+b)))'''#sorted will remove all the dublicate and give an arry'''

                    # second  problem

# replacing the world 
'''a=input("Enter a word")
w1=input('enter a word you want to replace ')
w2=input('enter the world which you want replace with w1')
print(a.replace(w1,w2))
'''

#                    READ A FILE

# count_file=open('E:/-python/countries.txt','r')
# for lines in count_file.readlines():
#     print(lines)
# count_file.close()



#                      WRITE A FILE 
# write_file=open('E:/python/countries.txt','w')

# write_file.write('print(\'thus is new line \ ')')
 





#                                          OOP started





 #                        CLASSS AND OBJECTS  IS CALLED OOP
                        #    instance is also called object and objects are
# the function are writen in class is called methods.


class person():
   def __init__(self,name,age):       # this init function is also called CONSTRUCTER
        self.name=name
        self.age=age

   def marks(self):        #  function are using in function is called methods.
       print ('you get 20 marks', self.name)

   def welcome(self):
       print('you are wellcome and your age ', self.age)

p1=person('john',23)    # this is called object
# print(p1.name,p1.age)        
# p1.marks()          
# p1.welcome()

 
# 1st  problem in class print the avarage of three students

# class student:
   
#     def __init__  (self ,name,marks) :
#         self.name=name
#         self.marks=marks

#     def get_avg(self):
#        sum=0
#        for val in self.marks:
#            sum+=val

#        print( 'hi',round(sum/3),'is the sum in the list of given number ')

# s1=student('john',[23,23,234]) 
# s1.get_avg() 




#
#                                                            METHOD

# THERE ARE three type of methods   1. @staticmethod  2. @classmethod  3.
 
#                                               1.        @STATICSMETHOD

# class man:
#     def __init__(self):
#         print('hte is not same')
#     @staticmethod                 # DECORATOR FUNCTion ko class level par lana ka liya 
#     def main():           # function ka andar parameter na diya ho  tu osa staticmethod apply kar ka use karta 
#         print('avg')    
    
# s1=man()
# s1.main()




#                                         2.         @classMethod  (cls)  parameter


#  to change directly the class attribute  like  in parameter is   (cls)

# class person:
#     name='ali'
#     @classmethod                # this method is used for 
#     def change(cls,name):
#         cls.name=name
# per=person()
# per.change('azmat')
# print(per.name)
# print(person.name )
        

#                                        3.    instance method or simple method      (self)  parameter
#  instance method parameter is   (self)
  
# class public:
#     def __init__(self,name):
#         self.name=name

          
# pub=public('ali')
# print  (pub.name)      



            #                                        @property


# if we change the value at the end of class  

class public:
    def __init__(self,phy,sci,math):
        self.phy=phy
        self.sci=sci
        self.math=math
    @property
    def main(self):
        return str((self.phy+self.sci+self.math)/3)      
ad=public(12,12,23)
ad.phy=9        #    change value  of  attributes  and give the result with  @property    method
print(ad.main)     




                                                     
                                                         #OOP   Pillor




#  oop consist of class,object and are below line



# thses are the four pillor of oop... 1 abstraction      2  Encapsulation         3 inheritance            4  polymorphism          




 #Abstraction hiding the unacessries thing and showing only essential features to the user.
   


# class car:
    # def __init__(self):                   # self parametre iss also called an object
#         self.acc=False
#         self.brake=False
#         self.race=False
#     def start(self):
#         self.acc=True
#         self.brake=True
#         print('car is started') 
# c1=car()           
# c1.start()

        

   #                                           encapsulation

   
        
# making things private or public  and we cannot change prite method o attribute  ouside of object



 # public or private   ,,/ private attributes or methods are used within the class and are not accesible  ouside of the class no one can change it etc...

class private:
    def __init__(self,amount):
        self.amount=amount

#     def __main(self):
#         print(self.amount)
#     def second(self):
#       self.__main()        
s1=private(20)

# print(s1.amount)









    #                                     polymorphism

    

































#                                     Inheritance

#   TYPES       1Single       2 multi-level             3  multiple inhritance

#   ik class ki propertise dosri class ko dana inheritance khalata hy
  


#    Single  inheritance example
# class car:
#     @staticmethod
#     def start():
#         print('car is starting on the road side')
#     @staticmethod
#     def stop():
#         print('car is stopped')        
 
# class second (car):
#     def __init__(self,name) :
#         self.name=name

# car1=second('fortuner')
# car2=second('prius')
# print(car1.name)
# print(car1.start())


#                                            multi-level inheritance


    
# class car:
#     @staticmethod
#     def start():
#         print('car is starting on the road side')
#     @staticmethod
#     def stop():
#         print('car is stopped')        
 
# class second (car):
#     def __init__(self,name) :
#         self.name=name
#         print(name)  

# class toyota(second):
#     def __init__(self,type):
#         self.type=type

# car1=toyota('prius')
# print(car1.start())




#                                          3 Multiple inheritance

class A:
    var1='welcome to the class 1'

class B:
    var2='welcome to the class 2 '

class C(A,B):
    var3='welcome to the class 3'

d=C()
# print(d.var1)
# print(d.var2)
# print(d.var3)


#                               super() 
#  in super method we are talking about parent class.. example are listed below
class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print('car is starting on the road side')

    @staticmethod
    def stop():
        print('car is stopped')        
 
class second (car):
    def __init__(self,name,type) :
        super().__init__(type)
        self.name=name


car1=second('fortuner','elctric')
# print(car1.name)







   #   problem create method for credit debit and printing balance
# class bank:
#     def __init__(self,balance,acc):

#         self.balance=balance
#         self.acc_no=acc

#     def debit(self,amount):
#         self.balance+=amount
#         print(amount ,'was debited')
#         print('total balance',self.get_balance())
    
    
#     def credit(self,amonut):
#         self.balance-=amonut
#         print(amonut,'credited amount')
        
#         print('total balance',self.get_balance())

#     def get_balance(self):
#         return self.balance
        
      

# a1=bank(10000,12345)
# print('your present balance is',a1.get_balance(),'credit or debit your founds')

# a1.debit(1000)
# a1.credit(6000)