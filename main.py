import os

file_to_work = open("hello.txt","w")
sub = "HElloooo Wilrd"
sobn =""
with open("hello.txt","r") as f:
   sobn = f.read()

print(sobn)