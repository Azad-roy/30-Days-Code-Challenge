#  9.Add a new key-value pair to the dictionary. 

dict={
    "Mango":"Yellow",
    "Guava":"Green",
    "Orange":"Orange",
}

print(f"Before changing the dictionary: {dict}")

food={
    "rice":"White",
    "Tomato":"Red",
}

dict.update(food)
print(f"After adding key value pairs: {dict}")