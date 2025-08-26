file= open("demo.txt","r")
line = file.read(5) # Read the first 5 bytes

print(line)

file.close()