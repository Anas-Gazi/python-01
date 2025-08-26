bin = b'\x00\x01\x02\x03'
with open("binary.bin","wb") as f:
  f.write(bin)
f= open("binary.bin",'r')
print(f.read())