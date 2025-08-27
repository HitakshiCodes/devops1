print("Hello, Python!")
user_name=input("Enter your name:")
print("Hi",user_name)
age=int(input("Enter age:"))
if age >=18:
    print("Adult")
else:
    print("Minor")   
for i in range(5):
    print(i)
i=0
while i<5:
    print(i)
    i+=1
fruits=["apple","banana","cherry"] 
print(fruits[1])
fruits.append("mango")
def greet(name):
    print("Hello",name)
greet ("Bhoomi")    
greet ("Hita")  
print(fruits)  