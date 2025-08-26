#process 1
file= open("demo.txt",'r')

line= file.readline() #read only 1st line and count \n
print(line)
file.close()