num=[1,2,3,4,5]
reverse_list=[]
for i in range(len(num)-1,-1,-1):
    reverse_list.append(num[i])
print("The reverse of the list is:", reverse_list)