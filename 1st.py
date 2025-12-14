# PTOGRAM 1
# num1 = "100"
# num2 ="25"
# num1 = int(num1)
# num2 = int(num2)
# sum =  num1+num2
# dif = num1- num2 
# p = num1 * num2
# q=int ( num1/num2)
# print ("sum  ", sum , "difference", dif , "product ", p , "quotient" , q)

# PROGRAM 2
# num = "2"
# num = int(num)
# if (num % 2 == 0):
#                print("even")
# else:
#                print("odd")
# print("even") if num%2==0 else print("odd")

# program 3
# data = "pythonprogramming"
# print(data[0:1])
# print(data[6: ])
# print(data[-16:-1])

# #prog 4
# word =  "racecar"
# rev = word[ ::-1]
# print("palindrome") if word == rev else print("not palindrome")

# nm = " mu me le devansh"
# print(nm.replace("devansh "," arsh"))

# nm = "mera desh mahan"
# print(nm.endswith("mahan"))

# nm = "nadia"
# print(nm.find("a") )

# nm = " nadia meri baggo meri soni suhani"
# print(nm.count("a"))

# fn  = input("fn  ")
# print (len(fn))

# nm =  " sarika "
# print(nm.find("s"))

# fs= input("fs  ")
# if(fs == "the smiths"):
#                    print("mat  kar lala")  #indentation
# else:
#                      print("goodd")

# marks = int(input("marks  "))
# if(marks>=90):
#               print("bkl kitabi keeda")
# elif(marks<90 and marks>=80):
#                print("tumse ho  jayega")
# elif(marks<80 and marks>=70):
#             print("mere jaise ho ap")
# else:
#             print("tumari naiiya  dub gyi betaji")  

# n1=  int(input("n1  "))
# n2  = int(input("n2  "))
# n3 = int(input("n3   "))
     
# if(n1>n2 and n1>n3):
#                    print(n3 , " is largest")
# elif(n2>n3):
#                    print(n2 , "is largest")
                   
# else :
#                    print (n3 , "is largst")
                   

# num = 49
# if(num%7==0):
#            print("it is a mulltiple")
# else:
#             print("ni ha")

# CHAPTER 3

#list(array) in python

# nm =[2,3,4,5,87]
# print(nm[:: -1])

#methods

# colours = ["red", "green", "blue"]
# title =  "my colour list"
# print(colours[1])
# print(colours[0])
# colours[2]= "yellow"
# print(colours)

# sc = ["apple ", "banna"]
# sc.append("orange")
# sc.pop(0)
# print(sc)

# typ  = (2, 3 , 4)
# print(typ[0])
 
# a = input("a  ")
# b= input("b ")
# c= input("c ")
# mo =[a, b, c] 
# print(mo)

# a = input("a  ")
# b= input("b ")
# c= input("c ")
# d= input("d  ")
# li =[a, b, c, d] 
# li2 = li.copy()
# li2.reverse()
# if(li==li2):
#            print("pal")
# else:
#            print("not pal")

# tup =["c", "a", "a", "b", "c", "d"]
# tup.sort()
# print(tup)

#CHHAPTER 4
#dictonary in java

# info ={
#     2:   "jaa",
#     "hah" : "lala",
# }
# info["hah"]=  "chole"
# print(infoff)

# student = {
#     "name": "chaddi",
#     "subjects": {
#          "phy":7373,
#          "cgem": 266,
#     } 
# }
# print(student["subjects"]["phy"])
# st ={
#     "ek k=mota" : "hathi",
# }
# st2 =  {"lala" : "lalds"}
# st.update(st2)
# print(st)

#SETS


# co = {1,23,4,564,3,2}               #()=tuppple {}=sets  []=list 
# print(len(co))
# sa = {3,4,2,3}
# # sa.add((1,2,3) )

# sa.__sizeof__()
# print(sa)

# di={
#     "table": ("a piece of furniture","list of  facts and figures"),
#     "cat":"a small animal"
# }
# print(di)
# ha =  {"python", "java", "c++", "python", "javascript", "java", "python,", "java","c++","c"}
# print(len(ha))
# a= int(input("a "))
# b =int(input("b "))
# c= int(input("c "))
# dic ={
    
# }
# dic.update({"physics" : a}),
# dic.update({"chem" : b}),
# dic.update({"bio" : c}),
# print(dic)

# co = {int(9), float(9.0)}                           
# print(co)

#LOOPS
# c=5
# while c <6:
#     print("hddh")
# i=1
# n=int(input("i "))
# while i<=10:
#     p = i*n
#     print(p)
#     i+=1


# nums = [1,4,9,16,25,36,49,64,81,100]
# i=0

# while i< 10:
#     print(nums[i])
#     i+=1

# n = (1,4,9,16,25,36,49,64,81,100)
# x =  int(input("x "))
# i=0
# while i<len(n):
#     if(x==n[i]):                        merese ni hua tha ye
#         print("found")
#         break
#     i+=1

# i =0
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1
    
    #FOR LOOP
    
# n = [1,2,34,4]
# for el in n:
#     print(el)

# n = [1, 4 , 16 , 2, 36, 100]
# for el in n :
#     print(el)

# n =  (1,4,9,17,1942,194,23,4,2,)
# i=0
# x= int(input("x  "))
# for tupple in n :
#     if(x==tupple):
#         print("found")
#     i+=1
# for i in range(2,12,2):
#     print(i)
# for i in range(100,1,-2):
#     print(i)
#QUESTIONS ON DICTIONARIES AND SETS

# car ={
#     "make": "ford",
#     "model": "mustang",
#     "year" : 1964,
#         }
# print(car)

# nl = [10,30,20,10,20,50]
# nm = set(nl)
# print(nm)

# up = {
#     "username": "jdoe",
#     "email": "jdoe@example.com",
#     }
# up.update({"hdddh" : "dhdh"})
# print(up)

# ac= {"alice", "bob"}
# ac.add("charlie")
# print(ac)
# if("naitik" in ac):
#       print("ys")
# else:
#       print("no")

# users = [
#     {"id": "001", "name": "  Alex ", "status": "active"},
#     {"id": "002", "name": " Brenda", "status": "inactive"},
#     {"id": "003", "name": "Casey ", "status": "active"}
# ]
# su= users[1]
# un = su["name"]
# un.strip().lower()
# print(un)

# team_alpha = ["Ana", "Bob", "Chen", "David"] 
# team_beta = ["Chen", "Eva", "Bob", "Frank"]
# sa = set(team_alpha)
# sb= set(team_beta)
# print(sa.intersection(sb))
# print(sa.difference(sb))
# print(sa.union(sb))

# n = int(input("n" ))
# i =  0
# s=0
# while i<=n:
#     s+=i
#     i=i+1
# print(s)
    
# nm =  int(input("nm "))
# f=1
# i=1
# while i<=nm:
#     f*=i
#     i+=1
#     i 
#     print(f)

#FUNCTIONS 
# def revdecode(a):
    
#     rev =""
#     b= a[::-1]
#     for i in range(0 , len(b), 2):
#        c = b[i : i+2]
#        if len(c)==2:
#            u =  int(c)
#            rev +=chr(u)
    
#     return rev
    
# haha = "9767679627"
# rev = revdecode(haha)
# print(rev)

# def avg(a , b, c):
#     avg = (a+b+c)/3
#     return avg
# a = avg(2,4,4)
# print(a)

# def l(a):
#     q =len(a)
#     return q
# a = [1,2,3,4,11,33]
# le = l(a)
# print(le)

# a = [ "dhs" , "sjd", "naitik"]
# def same(a):
#     for i in a:
#         print(i, end=" ")

# same(a)
# def c(dollers):
#     rupees = dollers *83
#     return rupees
# haha = c(1)
# print(haha)

# def oddeven(num):
#     if(num%2==0):
#         return "true"
#     else:
#         return "false"
# num = oddeven(int(input("num ")))
# print(num)
 
# def show(n):
#     if(n==0 or n==1):
#         return 1
    
#     return n*show(n-1)
    
# print (show(2))      

# def sum(n):
#     s=0
#     if(n==0):
#         return 0
#     else:
#        return sum(n-1)+n
    
# print (sum(5))

#SOME QUESTIONS

# def cp(b , t=0.05):              tax calculating
#       tax = b *t
#       total = tax+b 
#       return total

# t = cp(100)
# print(t)

# def cd(data):
#     if(isinstance(data,str)):
#           return "this is a string"
#     if(type(data)==dict):
#           return "this is a dictionary"
#     if(type(data)==set or list):
#           return "this is a collection"  
#     else:
#          return "unknown"
     
# l = cd([1,23,2])
# d = cd({1:23})
# st =cd("lapata")
# stt = cd({1,2,3})
# print (l , d , st , stt)

# ub = [
#     {"username": "alice", "email": "alice@web.com", "posts": 5},
#     {"username": "bob", "email": "bob@web.com", "posts": 0},
#     {"username": "charlie", "email": "char@web.com", "posts": 12}
# ]     
# def fu(db , username):
#     for i in db:
#         if(username == i["username"]):
#             return i["email"]
        
#     return "user not found"
        
# a = fu (ub , "naitik")
# print(a)
        
# def rs(nl):
#     if(len(nl)== 0):
#         return 0
#     f =  nl[0]
#     r = nl[1::]
#     return f + rs(r)

# nl = rs([1,2,3,44])
# print(nl)

# def rs(s):
#     if(s== ""):
#         return s 
#     f = s[0]
#     r = s[1 ::]
#     return rs(r) + f
# a = "hello"
# print(rs(a))

#FILE I/O

# f = open("ji" , "a")
# data = f.write()
# print(data)
# print(type(data))
# f.close

# def rep(pathfile, old , new):
#     with open(pathfile , "r") as f:
#         data = f.read()
#         rev = data.replace(old , new)
#     with open(pathfile , "w") as f:
#        f.write(rev)
#     return rev 
# r = rep("practice.txt" , "python" , "java")
# print(r) 
# c =0
# with open("practice.txt" , "r") as f:
#     data = f.read()
#     print(data)

# n = data.split(",")
# for i in n:
#     cl = i.strip()
#     if(int(cl) % 2 == 0 ):
#          c+=1
         
# print(c)
             
# n= ""
# for i in range(len(data)):
#     if(data[i]== ","):
#      num = int(n)
#      if num % 2 ==0 :
#          print(num)
#      n = ""
#     else:
#         n+=data[i]

#OOps in python

# class apple:
    # fruit ="apple"
    # hob = "red"
    
    # def  __innit__ (self, hob, nm):
    #     self.hob = hob ,         
        # object attributes >>> class attributes
        # self . n = nm
    # def mango(self , ho , nm ):
    #     self. m = ho
    #     self . n = nm
        
                                
# s1 = apple()
# s1.mango("3 " , "2")

# s2 =apple*( "2 m " , "h=2")
# print(s1.)
# print(s2)

# class student:
#     def __init__(self , name , p , c , m):
#         self.name = name
#         self.p= p
#         self.c = c
#         self.m = m 
#     def avg(self):
#         s=0
#         s = self.p + self.c + self.m
#         print( s/3)
       
        
    
# s1 = student("naitik " , 90 , 92 , 98)      #mutable
# s1.avg()
# s1.name ="lado"

#STATIC METHOD

# class acc:
#      def __init__(self , balance, acc):
#          self.bal = balance
#          self.acc = acc
#      def debit(self , ab):
#          self.ab = ab
#          b = 0
#          b = self.bal - ab
#          print( b)
#      def credit(self, ac):
#         self.ac = ac
#         b = 0
#         b = self.bal + ac
#         print(b)

# a = acc(20000 , 10219327)
# a.debit(200)

#part 2 of oops

# class calculate:
#     def __init__(self, m , n):
#         # sum = 0
#         self.n = n
#         self.m = m
#         self.sum = m +n
#     def sub(self, n , m):
#         # s =0 
#         self.n , self.m = n , m
#         if(n>m):
#             s = n-m
#         else:
#             s = m-n
#             return s
# s2 = calculate(2,4)

# print(s2.sum)
# b = s2.sub(7,8)
# print(s2)
# print(b)

# class complex :
#     def __init__(self, r , i):
#         self.r = r
#         self.i=i 
        
#                                            # def show(self):
#                                            #     print(self.r, "i +" , self.i,"j")
        
#     def add(self , n):
#         re = self.r + n.r
#         im = self.i + n.i
#                                            # return complex(re , im)
#         print(re , "i +" , im , "j")
        
# n1= complex(2 , 4)
# n2 = complex(3,5)
# n3 = n1.add(n2)
                                          # n3.show()
                                          # print(n3)

# class circle:
#     def __init__(self , r ):
#         self.r = r
#     def area(self):
#         a = ((22/7) *pow(self.r , 2))
#         return a
#     def perimeter(self):
#         p = ((22/7)*7)
#         print(p)

# n1 = circle(7)
# print(n1.area())
# n1.perimeter()

# class emp:
#     def __init__(self, role , dep , sal ):
#         self.role = role
#         self.dep = dep
#         self.sal = sal
#     def showd(self):
#         print(self.role , self.dep , self.sal)
# s1 = emp("eng" ,"\n " "has" ,90000)
# s1.showd()

# class eng(emp):
#     def __init__(self, name , age):
#         self.name = name 
#         self.age = age
#         super().__init__("eng" , "wdhhdh" , 500)
        
# s2 = eng("ekom" , 57)
# s2.showd()
        
#MINI PROJECT                       1

# import random
# m =random.randint(0,10)

# while True:
#     n = (int)(input("guess the target you nigga"))
#     if(n>m):
#         print(n ,"is larger than the target no")
#     elif(n<m):
#         print(n , "is smaller than the target number")
#     elif(n ==m):
#         break
    
# print("target number found you white nigga")

# import random
# import string
# r = string.ascii_letters+ string.digits
# s =""
# l =12
# for i in range(l):
#     s+=random.choice(r)

# print(s)

# import numpy as n
# aa = n.array([[0,2],[3,0]])

# A = n.linalg.matrix_power(aa,10)
# print(A)

# b = float(input("enter base of triange"))
# h = float(input("enter height of trioangle"))
# area = .5*b*h
# print(area)

# a =  12 
# b = 21 
# temp =0
# temp = a 
# a = b 
# b = temp
# print (a)
# print(b)
# print(temp)

# import random as r 
# a = r.randint(1,100)
# print(a)

# import calendar as c
# # year = int(input("enter the year "))
# # month= int(input("enter the month"))
# cal =c.
# print(cal) 
# import math 
# print("enter a, b , c of quadratic")
# a= int(input(" a "))
# b = int(input("b "))
# c= int(input("c "))
# print (a,"x2",b,"x",c )
# roots1 = -b + (math.sqrt((b**2)-(4*a*c)))/2*a 
# root2=-b - (math.sqrt((b**2)-(4*a*c)))/2*a
# print(roots1)
# print(root2)

# a = 10
# b =11
 
# a, b = b, a
# print ( a , b)


# ll= int(input("lower limit"))
# ul = int(input("upper limit"))
# for i in range(ll, ul+1):
#     for j in range(2, i):
#         if(i%j==0):
#             break
#     else:
#             print(i)

        
        


        

