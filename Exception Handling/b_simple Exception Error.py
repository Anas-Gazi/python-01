try:
  n=0
  res =100/0

except ZeroDivisionError:
  print("can't be devided by zero")

except ValueError:
  print("Enter a valid number")

else:
  print("result is", res)

finally:
  print("Execution complete.")