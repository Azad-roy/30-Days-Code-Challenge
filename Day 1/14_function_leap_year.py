def leap(num):
    if((num%100!=0) or (num%4==0 and num%400==0)):
        print(num,"is leap year")
    # elif(num%4==0):
    #     print(num,"is leap year")
    else:
        print(num,"is not leap year")

num=int(input("Enter a year: "))
leap(num)