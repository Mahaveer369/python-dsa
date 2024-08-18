stack = []
def push():
 element=input("enter the element : ")
 stack.append(element)
 print(stack)
 return push
def pop():
 if not stack:
  print("stack is empty")
 else:
  pop_element=stack.pop()
  print("poped elemt is : ",pop_element)
  return pop
while   True: 
 print("select the operation 1.push 2.pop 3.qit")
 choice=int(input())
 if choice==1:
  push()
 elif choice==2:
  pop()
 elif choice==3:
  break
 else:
  print("enter the coreecr operation!")
 
  
 