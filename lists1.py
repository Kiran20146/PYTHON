thislist = ["apple", "banana", "cherry", "apple", "cherry"]
thislist1 = list(("apple", "banana", "cherry")) # note the double round-brackets list constructor

print(thislist1)

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist)
print(len(thislist))
print(type(thislist))

print(thislist2[2:5])
#The search will start at index 2 (included) and end at index 5 (not included).
print(thislist2[-3:-1]) # it reads list from left to right --->
print(thislist2[:4])
print(thislist[2:])

if "apple" in thislist2:
  print("Yes, 'apple' is in the fruits list")
