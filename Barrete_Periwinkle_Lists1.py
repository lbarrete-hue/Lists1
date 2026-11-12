items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]

print ("Original List:", end="")
for item in items:
    print (item, ",", end=" ")
print()

indextoupdate = int(input("Input Index to Update: "))
newvalue = input("Input New Value: ")
startofslice = int(input("Enter Slice Range 1: "))
endofslice = int(input("Enter Slice Range 2: "))
searchitem = input("Enter Search Item: ")

sliced = items[startofslice:endofslice]

found = False
for item in sliced:
    if item == searchitem:
        found = True
        break

items[indextoupdate] = newvalue

print ("Index to Update: ", indextoupdate)
print ("New value: ", newvalue)

print (f"Sliced List: ({startofslice}:{endofslice})", sliced)

if found:
    print ("Search Result (from sliced array):", searchitem, "is found in the sliced list" )
else:
    print ("Search Result (from sliced array):", searchitem, "is not found in the sliced list" )

print ("Updated List:", end="")
for item in items:
    print (item, ",", end=" ")



