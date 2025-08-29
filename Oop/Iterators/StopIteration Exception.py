li =[100,200,300]
it = iter(li)

while True:
  try:
    print(next(it))

  except StopIteration:
    print("End of iteration")
    break