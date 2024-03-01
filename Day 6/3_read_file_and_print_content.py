# 3.Write a program to read a file and print its content.

with open("sample.txt","w") as f:
    data=f.write("Hello Coders!\n let's so some intresting things")

with open("sample.txt","r") as f:
    data=f.read()
    print(data)