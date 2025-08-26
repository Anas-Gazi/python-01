  #it automatically handles closing, reduces the risk of file corruption and resource leakage.

#Read Mode ('r')
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

#write mode()
with open('demo.txt','w') as file:
    file.write("Hello world! ")

# Append Mode ('a')
with open("demo.txt",'a') as file:
    file.write('\n this is')

#binary mode()
