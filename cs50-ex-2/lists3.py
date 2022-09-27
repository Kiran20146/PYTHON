thislist = ["apple", "banana", "cherry"] # removing by providing the value 
thislist.remove("banana")
print(thislist)

thislist1 = ["apple", "banana", "cherry"] # Removing by providing the indices 
thislist1.pop(1) # dont specify the index it removes the last item 
print(thislist1)

thislist2 = ["apple", "banana", "cherry"]
del thislist2[0]
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
del thislist3

thislist4 = ["apple", "banana", "cherry"]
thislist4.clear()
print(thislist4)