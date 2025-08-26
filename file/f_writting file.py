#creating new line
with open("new.txt","w") as file:
  file.write("created using write mode: ")

file= open("new.txt","r")
print(file.read())

#append. join new line
with open("new.txt","a") as file:
  file.write(" Append this line")
file= open("new.txt","r")
print(file.read())