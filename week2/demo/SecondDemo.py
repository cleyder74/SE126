import csv

#intialize variables
total_records = 0
total_salaries = 0

#initialize empty lists - 1 list per field
names = []
ages = []
salaries = []

#connct to the file
with open("week2/demo/example.csv") as csvfile:

    #read the file

    file = csv.reader(csvfile)

    #go in and read each record

    for rec in file:
        #for every record found in file (entire row of field data)

        #display data values in neat columns
        print (f"{rec[0]:10} \t{rec[1]:3} \t${rec[2]:10}")

        #store data from rec list (current record being read) to list 
        #adding data to a list --> .append() ; required LISt NAMES as starting object

        names.append(rec[0]) #NAME
        ages.append(int(rec[1])) #AGE
        salaries.append(float(rec[2])) #SALARY
    




        #keep literal count number of records
        total_records += 1

        #keep running total of salaries
        total_salaries += float(rec[2])

#final total displays
print (f"TOTAL RECORDS: {total_records} | TOTAL SALARY: $ {total_salaries:.2f}")


#process the lists to display the text file information
#process the list --> FOR loop!

for index in range(0, total_records):
    #for each value inthe range of 0 to # of values in total records
    print(f"INDEX: {index} \t {names[index]} is {ages[index]} years old")

#process through the list to to create a total age value 
total_age = 0

for index in range(0, total_records):
    #add each age to a total age variable
    total_age += ages[index]

#determine th average age, then display
average_age = total_age / total_records
print(f"Average Age:{average_age:.2f} ")


