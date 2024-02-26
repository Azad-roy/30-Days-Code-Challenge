# # 6.Find the intersection of two sets.

# set1={4,5,2,7,8}
# set2={1,2,3,5,4}

# convert1=list(set1)
# convert2=list(set2)
# for i in range (len(set1)):
#     if (convert1[i] == convert2[i]):
#         print(convert1[i])
#     else:
#         print(convert1[i])
# # convert=list(set1)
# # print(type(convert))
# # print(convert[0])
# # print(convert[1])
# # print(convert[2])
# # print(convert[3])
# # print(convert[4])

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Find the intersection using the & operator
intersection_set = set1 & set2

# Print the intersection
print("Intersection of set1 and set2:", intersection_set)
 