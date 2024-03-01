# 8.Implement a function to calculate the area of a circle.

def area(radius):
    return f"Area of the circle is: {(22/7)*radius*radius}" 
    
user=int(input("Enter radius of the circle: "))
print(area(user))