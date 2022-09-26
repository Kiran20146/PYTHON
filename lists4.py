thislist = ["apple", "banana", "cherry"]
for fruits in thislist:
    print(fruits)

thislist1 = ["apple", "banana", "cherry"] # See the output 
for i in thislist1:
    print(i[0])

for i in range(len(thislist1)):
  print(thislist1[i])

# using while loop 
thislist = ["apple", "banana", "cherry"]
i = 0 # intilization is mandatory
while i < len(thislist):
  print(thislist[i])
  i = i + 1 