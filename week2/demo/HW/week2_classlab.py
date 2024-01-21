#Cleyder Soto-Reyes

#Week2 Class Lab

#Intermediate Python SE126

######################################################################################################################

#variables
#over = The amount of rooms that are over filled

#overnum = are the total number of people that are over the limit

#max = the amount of space the available for the room

#min = the amount of people attending 

#room = the Name of the room

########################################################################################################################

'''Write a program that displays all rooms that are over the maximum limit of people and the number of people 
that have to be notified that they will have to be put on the wait list. After the file is completely 
processed the program should display the number of records processed and the number of rooms that are over the limit.'''

##########################################################################################################################
import csv

total_records = 0
over = 0
overnum = 0
max = [] 
min = []
room = []





with open("week2/demo/HW/lab2a.csv") as csvfile:

    file = csv.reader(csvfile)
    print(f"{'ROOM':20}  \t{' MAX':3} \t{' ATTENDING':10}")

    for rec in file:
         

         print (f"{rec[0]:20} \t{rec[1]:3} \t{rec[2]:20}")

         room.append(rec[0]) 
         max.append(int(rec[1])) 
         min.append(int(rec[2])) 

         total_records += 1
         
        
         if int(rec[2]) > int(rec[1]):
            overnum = int(rec[2]) - int(rec[1]) * -1
              
            over += 1


print(f'\n{total_records} records were processed.')

print(f'There are {over} rooms that are over the limit, and {overnum} people will have to be put on a wait list.')

print("\nPress any any ket to quit....")
quit()

    
              
        


    
              
         



