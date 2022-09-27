# changing the list values based on the indices ::: 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] # bannana and cherry replaced by balckcurrent and watermellon
print(thislist)

thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist1[1:2] = ["blackcurrant", "watermelon"] # bannana is replaced by balckcurrent and watermellon
print(thislist1)

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist2[1:4] = ["watermelon"] # bannan cherry orange is replaced by watermelon
print(thislist2)
# see the difference 
# -------------------------------------------------------------------------------------------------------
thislist3 = ["apple", "banana", "cherry"]
thislist3.insert(2, "watermelon")
print(thislist3) # adds the item before the specified indices 

thislist4 = ["apple", "banana", "cherry"] # adds an item at  the end of the list 
thislist4.append("orange")
print(thislist4)

thislist5 = ["apple", "banana", "cherry"] # extending the list 
tropical = ["mango", "pineapple", "papaya"]
thislist5.extend(tropical)
print(thislist5)

thislist6 = ["apple", "banana", "cherry"] # extending the list by adding the tuple
thistuple = ("kiwi", "orange")
thislist6.extend(thistuple)
print(thislist6)
