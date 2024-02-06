#Week 5 LIST REVIEW

#

#----------------------------------------------------------------
import csv


#FUNCTION--------------------------------------------------------

def menu():

    print("1. SHOW NUMERIC AVERAGE")
    print("2. SHOW LETTER AVERAGE")
    print("3. Search")
    print("4. EXIT")

    choice = int(input("Please enter your selecton: "))

    while choice < 0 or choice > 4:

        print("**ERROR**ERROR**")
        choice = (input("Please enter your selecton: "))

    return choice

def seq_search(search_term):

    #search_term is a local var name and only exits in this definition block

    #SEQUENTIAL SEARCH - "in sequence" -> start at beginning (0) go to the end (len(listname))

    #initiaalize found_index variable
    found_index = "" #set as empty

    for i in range(0, len(lastname)):
        #look at each value in a list to find what you're looking for 

        if lastname[i] == search_term:
            found_index = i #store i (location)

    return found_index


#list creation -- create empty lists, one per field of data in the file we are storing from

firstname = []
lastname = []
test1 = []
test2 = []
test3 = []

records = 0

#connect to the file, read the data, and store data into lists
with open("week5/Demo/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #print(rec)     #test a print of records to make sure file is connected and can be read

        firstname.append(rec[0])
        lastname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

        records += 1 #records = records + 1

        

#below is no longer connected to file / LIST PROCESSING ONLY!

#process the lists to print to the console
#PROCESS THE LIST --> FOR LOOP! 

#for i in range(0, records):

    #print("{0:15} \t {1:15} \t {2:3} \t {3:3} \t {4:3} \t {5:3}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i], teacher[i]))


num_avg = []

#process the test scores for each student and find their average (numeric) then, store into a new list
for i in range(0, records):

    grade_sum = test1[i] + test2[i] + test3[i]

    grade_avg = grade_sum / 3 

    num_avg.append(grade_avg)


#for i in range(0, records):

#    print("{0:15} \t {1:15} \t {2:3} \t {3:3} \t {4:3} \t {5:3} \t {6:4.2f}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i], teacher[i], num_avg[i]))


letter_avg = []

for i in range(0, records):

    if num_avg[i] >= 90:

        letter = "A"

    else: 
        letter = "Not A"

    letter_avg.append(letter)



#for i in range(0, records):

#   print("{0:15} \t {1:15} \t {2:3} \t {3:3} \t {4:3} \t {5:3} \t {6:4.2f} \t {7:2}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i], teacher[i], num_avg[i], letter_avg[i]))






menu_choice = menu()

while menu_choice != 4: #while menu_choice is not the exit option 

    if menu_choice == 1: #printing numeric averages

        print("\n\t NUMERIC AVERAGES\n")
        
        for i in range(0, records):

            print("{0:15} \t {1:15} \t {2:3} \t {3:3} \t {4:3} \t {5:3}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i], num_avg[i]))


    elif menu_choice == 2: #printing letter averages

        print("\n\t LETTER AVERAGES\n")

        for i in range(0, records):

            print("{0:15} \t {1:15} \t {2:3} \t {3:3} \t {4:3} \t {5:3}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i], num_avg[i], letter_avg[i]))

    elif menu_choice == 3: #printing search

        print("\n\t Search\n")

        search = input("Enter the LAST name you are looking for: ")

        found = seq_search(search)

        if found != "":
            #display result to user
            print(f"{firstname[found]}, {lastname[found]}, {test1[found]}, {test2[found]}, {test3[found]}, {num_avg[found]}, {letter_avg[found]}")
        
        else:
            print(f"The student {search} has not been found")

           

    else: #exit -- wont be in the loop at all 

        print("\n\tERROR\n")


    menu_choice = menu()

print("\n\n\nthank you & goodbye!")