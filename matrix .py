# list1=[1,2,3,4,5]
# list2=[6,7,8,9,2,4,1,10]
# list3=list1+list2
# print(list3)




# list1=[1,2,3,4,5]
# list2=[6,7,8,9,2,4,1,10]
# list1.extend(list2)
# newlist=[]
# for item in list1:
#     if item not in newlist:
#         newlist.append(item)
# print(newlist)








# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#output
# transposed_matrix=[
#     [1,4,7],
#     [2,5,8],
#     [3,6,9]
# ]
# transpose=[]
# col=len(matrix[0])
# for i in range (col):
#     t_row=[]
#     for row in matrix:
#         t_row.append(row[i])
#     transpose.append(t_row)
# print(transpose)    



# a=[1,2,3,4,5]
# b=[6,7,8,9,2,4,1,10]
# a.append(b)
# print(a)



# a.extend("pen")
# print(a)

# a=["apple","banana","cherry"]
# a.append("orange")
# print(a)

# a=["apple","banana","cherry"]
# a.extend("orange")
# print(a)


# a=["tanu","manu"]
# a.insert(1,"lalu")
# print(a)



# a=["apple","banana","cherry"]
# b=["mango","pineapple","papaya"]
# a.extend(b)
# print(a)



# a=["apple","banana","cherry"]
# b=["mango","pineapple","papaya"]
# a.append(b)
# print(a)



# a=["apple","banana","cherry"]
# a.remove("apple")
# print(a)

# a=["apple","banana","cherry"]
# a.pop()
# print(a)



# a=["raju","kaju","manu"]
# del a[0]
# print(a)

# a=["apple","banana"]
# a.clear()
# print(a)

# a=["tanu","mango","kiwi"]
# a.sort()
# print(a)


# a=[12,35,85,87,31432,67987]
# a.sort()
# print(a)

# a=["orange","mango","kiwi","pinapple"]
# a.sort(reverse=True)
# print(a)

# a=["orange","mango","kiwi","pinapple"]
# a.sort(reverse=False)
# print(a)


# a=[100,50,65,82,23]
# a.sort(reverse=False)
# print(a)

# a=["banana","orange","kiwi","cherry"]
# a.sort(key=str.upper)
# print(a)

# a=["apple","banana","kiwi","cherry"]
# a.reverse()
# print(a)

# a=[1,2,3,4]
# b=a.copy()
# print(b,a)


# a=[1,2,3,4,5]
# b=["a","b","c","d","e"]
# c=a+b
# print(c)