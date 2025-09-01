lst = [ 'apple','mango','pineapple','banana','avocado']
print ("lenght of list:",len(lst))
print("first element:",lst[0])
print("last element:",lst[-1])

lst.append('apple')
print("updated list:", lst)

lst.remove('mango')
print("updated list:", lst)

lst.sort()
print("sorted list:", lst)

lst.pop('banana')
print("updated list:", lst)

lst.reverse()
print("reversed list:", lst)

lstt= lst*2
print("multiplication on list:", lst)

lst=lst[2:5]
print("sliced list:", lst)

lst.clear()
print("updated list:", lst)