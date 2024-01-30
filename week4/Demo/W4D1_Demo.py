import csv

#create 1D lists [will be parallel to eachother]
#base lists on fields in file

fname = []
lname = []
test1 = []
test2 = []
test3 = []



with open("week4/Demo/listPractice1-1.txt") as csvfile:

    file = csv.reader(csvfile)

    #come back and show print(file) later

    for rec in file:
        #store data from file fields to their respcetive lists
        '''by PARALLEL - storing initial file record data at same position
        (index) in each list --> use the same [index] across each list
        to find "matching" data'''

        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3])) #cast as int for math
        test3.append(int(rec[4]))

#disconnect from file --------------------

#procss the lists --> for loop
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'Test3'}")

for i in range(0, len(fname)): #len() --> for lists, it is the # of items in the list
    print("-----------------------------------------------------------------------------------")

    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")
print("-----------------------------------------------------------------------------------")

#calculate and store each student's average test score

avg = 0
total_count = 0
average = []

for i in range(0, len(test1)):

    #calculate avg for student
    avg = (test1[i] + test2[i] + test3[i]) /3

    #append this avg to the average[]
    average.append(avg)

#display students's fname and test average
print(f"\n{'FIRST':15}\t{'AVERAGE'}")
for i in range(0, len(fname)):
    print("---------------------------------------")
    print(f"{fname[i]:14} \t {average[i]:8.1f}")


#sequential search: "in sequence" --> from beginning through the end

low_name = " "
low_avg = 100 #start with highest value to drop to find lowest


for i in range(0, len(average)):

    #determine if current vergae is lower than cureent low_avg

    if average[i] < low_avg:
    
        low_avg = average[i]#current acergae is lower, so becomes new low value
        #low value
        low_name = fname[i]
print("---------------------------------------")


#DISPLAY: total students in file
print(f"\nSTUDENTS IN FILE: {len(fname)}")
print(f"LOWEST AVERAGE: {low_name} - {low_avg:.1f}")


#----2D--Lists--------------------------------------------------------------
#use your 1D parallel lists to populate a new, 2D list
#HINT: the 2D list is a list ... populated with lists 8D

all_students = []

for i in range(0, len(fname)):
    
    #add each students data to their  (index) place in the all_students[] list
    all_students.append([fname[i], lname[i], test1[i], test2[i], test3[i], average[i]])

#display the 2D list to the console - for now, just get the list to display ie ['floyd', 'eastham', '100'. 85', '93']
for i in range(0, len(all_students)):
    print(f"{all_students[i]}")

print(f"{'FIRST':7} \t {'LAST':8} \t {'TEST1':12} \t {'TEST2':8} \t {'TEST3':8} {'AVERAGE':12}")
print("---------------------------------------------------------------------")
    #display the 2D list to the console where each value for each list appears as a value and not a list item
for i in range(0, len(all_students)):
        #we have lists wuthin a list - outter for handles main list (all_students)

    for x in range(0, len(all_students[i])):
            
        #inner for handles each value found at current list (all_students[i])

        print(f"{all_students[i][x]:12} ", end="")

    #include an extra empty print() to cancel the interior print's end=""
    print()