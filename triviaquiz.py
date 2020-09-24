
def output():
       print("congrats you earned  1 point")

def line():
       print("**************************************************************************************************")
def total():
       return count
def entered(a):
       print(f"you entered option - {a}")

       

point=[]

print("\n\n                  welcome to this quiz show\n\n")
name = input("Enter your name to start this game")
print(f"\n\nHello {name} you will get one point when you choose the correct answer\nType your answer in a or A,b or B,c or C ,d or D")
count = 0
print("\n Que : 1) What is the worst case time complexity of linear search algorithm?\nA - Ο(1)\nB - Ο(n)\nC - Ο(log n)\nD - Ο(n2) ")
opt1= ['d','D',]
opt = (input("ENTER OPTION "))
entered(opt)
if opt in opt1:
       output()
       line()
       point.append(1)
       
else:
    print("Wrong answer")
    print("correct answer is d" )
    line()
print("\n Que : 2. Which of the following is invalid?\na) _a = 1\nb) __a = 1\nc) __str__ = 1\nd) none of the mentioned  ")
opt1= ['d','D']
opt = (input("ENTER OPTION "))
entered(opt)
if opt in opt1:
       output()
       line()
       point.append(1)
else:
    print("Wrong answer")
    print("correct answer is d" )
    line()
print("\n Que : 3) Which of the following cannot be a variable?\na) __init__\nb) in\nc) it\nd) on")
opt1= ['b','B']
opt = (input("ENTER OPTION "))
if opt in opt1:
       output()
       line()
       point.append(1)
       
else:
    print("Wrong answer")
    print("correct answer is b" )
    line()

print("\n Que : 4) Suppose list1 is [2445,133,12454,123], what is max(list1)?\na) 2445\nb) 133\nc) 12454\nd) 123")
opt1= ['c','C']
opt = (input("ENTER OPTION "))
entered(opt)
if opt in opt1:
       output()
       line()
       point.append(1)
else:
    print("Wrong answer")
    print("correct answer is c" )
    line()

print("\n Que : 5) Which of the following is a Python tuple\na) [1, 2, 3]\nb) (1, 2, 3)\nc) {1, 2, 3}\nd) {}")
opt1= ['b','B']
opt = (input("ENTER OPTION "))
entered(opt)
if opt in opt1:
       output()
       line()
       point.append(1)
else:
    print("Wrong answer")
    print("correct answer is b" )
    line()

print("\n Que : 6)  What arithmetic operators cannot be used with strings?\na) +\nb) *\nc) –\nd) All of the mentioned")
opt1= ['c','C']
opt = (input("ENTER OPTION "))
entered(opt)
if opt in opt1:
      output()
      line()
      point.append(1)
else:
    print("Wrong answer")
    print("correct answer is c" )

sum=0
for i in point:
       sum+=i

       
print(f"congrats {name} you earned {sum} point<< keep learning")
