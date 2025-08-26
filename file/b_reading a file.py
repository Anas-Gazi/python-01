file = open("demo.txt","r")
content = file.read()
print(content)

file.close()

# using with statement
with open("demo.txt",'r') as file:
  a = file.read()
  print(a)