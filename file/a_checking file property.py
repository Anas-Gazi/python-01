f=open("demo.txt","r")
print("filename:",f.name)
print("mode:",f.mode)
print("is Closed?",f.closed)

f.close()
print("is Closed?",f.closed)