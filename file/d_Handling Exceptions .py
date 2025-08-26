try:
  file=open("demo.txt","r")
  a=file.read()
  print(a)
finally:
  file.close()