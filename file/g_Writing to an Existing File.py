## Writing to an existing file (content will be overwritten)
with open("new.txt","w") as f:
  f.write("New line")

f=open("new.txt","r")
print(f.read())

# Writing multiple lines to an existing file using writelines()
s=["1st line\n",'2nd line\n','3rd line']
with open("nex.txt",'w') as file:
  file.writelines(s)
f= open('nex.txt','r')
print(f.read())