class pen:
  def use(self):
    return "Writing"
  
class Eraser:
  def use(self):
    return "Erase"

def perform_task(tool):
  print(tool.use())

perform_task(pen())
perform_task(Eraser())