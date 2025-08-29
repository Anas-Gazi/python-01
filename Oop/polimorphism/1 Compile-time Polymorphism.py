class calculator:
  def multiply(self, a=1,b=1, *args):
    result= a * b
    for num in args:
      result *= num
    return result

# Create object
calc = calculator()

print(calc.multiply())
print(calc.multiply(4))
print(calc.multiply(2,4))
print(calc.multiply(2,4,4))