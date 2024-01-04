a=[233,23,66,42,5,65,2,45,47,98,102,8,7,99]
# b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

#Approach-2:Using list comprehension
b=[i for  i in a if i%2==0]
print(b)

