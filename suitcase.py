#create a list of items called "suitcase"
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
#modify the "suitcase" list to display the first two items in the "suitcase" list
beginning = suitcase[0:2]
#Display items in the new list called "beginning"
print(beginning)
#Slice the "suitcase" list to contain the middle two items
sliced_list = suitcase[2:4]
#Create a new list called "middle" from the sliced "suitcase" list
middle = sliced_list
#Display the new list called "middle"
print(middle)
#Slice the "suitcase" list to contain the last two elements in the "suitcase" list
slice_list = suitcase[-2:]
#Name the new sliced "suitcase" list "last_two_elements"
last_two_elements = slice_list
#Display the new "last_two_elements" list
print(last_two_elements)
#Slice the "suitcase" list to eliminate the last three items in the "suitcase" list
slice_list = suitcase[:-3]
#Name the new sliced "suitcase" list "slice_off_last_three"
slice_off_last_three = slice_list
#Display the new "slice_off_last_three" list
print(slice_off_last_three)
