#User-defined Modules (files you create with your own functions/classes).
import add
import sub
import mul
import div
import mod

while True:
  choice=int(input("enter the operation 1.add 2.sub 3.mul 4.div 5.mod 6.exit :"))
  if choice == 1:
    n = list(map(int, input("input:").split())) 
    res = add.addition(*n)
    print(res ,"\n")
  elif choice == 2:
    a,b=map(int,input("a,b input:").split())
    res = sub.substraction(a,b)
    print(res ,"\n")
  elif choice ==3:
    n = list(map(int, input("input:").split())) 
    res = mul.multiply(*n)
    print(res)
  elif choice == 4:
    a,b=map(int,input("a,b input:").split())
    res = div.divide(a,b)
    print(res ,"\n")
  elif choice == 5:
    a,b=map(int,input("a,b input:").split())
    res = mod.moduls(a,b)
    print(res ,"\n")
  elif choice == 6:
    print("exit")
    break
  else:
    print("invalid choice")
    print("please enter a valid choice between 1 to 6")
    break








