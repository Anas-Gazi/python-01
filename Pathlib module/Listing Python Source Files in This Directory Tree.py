from pathlib import Path
p= Path('/')
files = p.rglob('*.py')
for f in files:
  print(f)


#To find all Python files (.py) within a folder and its subfolders, use rglob() method from pathlib. It performs a recursive search, making it easy to scan entire directory trees for specific file types.