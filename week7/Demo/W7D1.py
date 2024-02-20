#W7D1 - Comparing Searching  Methods 

import csv



id_stud = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open("week7/Demo/w7_demoFile.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        id_stud.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

    for i in range(0, len(id_stud)):
            
        print(f"{id_stud[i]}\t{lname[i]:10}\t{fname[i]}")

#sequential saerch


search_name = input("Enter the last name you are looking for: ")
#found = -1
found = [] #allows for multiple in search
seq_count = 0

#for loop allows review of each value in list (sequence)
for i in range(0, len(lname)):
    seq_count += 1

    #ask if search value matches current value in list 
    if search_name.lower() == lname[i].lower():

        #store the found values location (index)
        found.append(i)
print(f"\n\tSearching Complete. Search loop run ran {seq_count} iterations.")
if found[0] != "":
    print(f"\n\tWe found {search_name} at index position(s): {found} ")
    print("Here is thier info: ")

    for i in range(0, len(found)):
        print(f"\t\t{fname[found[i]]}\t {lname[found[i]]}\t {id_stud[found[i]]} \t{class1[found[i]]} \t{class2[found[i]]} \t{class3[found[i]]}\n")

else:
    print(f"We could not find {search_name}")
    print("Please rty again.\n")


'''Binary search --- take an ordered list and divide it into two sections (high , low) and based on a MIDDLE POINT 
will continually halve the search pool until a UNIQUE value is found (or one isnt)'''

search_name = input("Enter the LAST NAME you are looking for: ")

min = lname[0] #first osition of the list to be searched (ascending)
max = int(len(lname) -1 )#last position of the ist to be searched (ascending)
mid = int((0 + (len(lname) -1)) / 2)
#mid = int(min + max) / 2


while ((min < max and search_name != lname[mid])):
    bin_count = 0
    if search_name < lname[mid]:
        max = mid - 1
    else:
        min - mid + 1

    mid = int((min + max) / 2)

print(f"\n\tSearching Complete. Search loop run ran {bin_count} iterations.")
if search_name == lname[mid]:
    #found them! use 'guess' for index of found search term
     print(f"\t\t{fname[found[mid]]}\t {lname[found[mid]]}\t {id_stud[found[mid]]} \t{class1[found[mid]]} \t{class2[found[mid]]} \t{class3[found[mid]]}\n")

else:
    print("Not found")


#Bubble sort


nums = [100, 75, 32, 250, 47, 9, 2, 3, 99, 200]


print(f"Current list: {nums}")


for i in range(0, len(nums) - 1):#outter loop

    print("OUTER LOOP! i = ", i)


    for index in range(0, len(nums) - 1):#inner loop

        print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort

        #list used is the list being sorted

        # > is for increasing order, < for decreasing

        if(nums[index] > nums[index + 1]):

            print("\t\t SWAP! ", nums[index], "<-->", nums[index + 1])

            #if above is true, swap places!

            temp = nums[index]

            nums[index] = nums[index + 1]

            nums[index + 1] = temp


            #swap all other values

            '''temp = age[index]

            age[index] = age[index + 1]

            age[index + 1] = temp'''
