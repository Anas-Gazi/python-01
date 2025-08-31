from datetime import time

a= time(13,24,56)
print("Entered time: ",a)

a= time(minute=12)
print(a)

a= time()
print(a)

#Get hours, minutes, seconds and microseconds

Time =time(11,34,56)
print("Hour = ", Time.hour)
print("Hour = ", Time.minute)
print("Hour = ", Time.second)
print("Hour = ", Time.microsecond)
