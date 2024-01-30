#Cleyder Soto-Reyes

#Week2 Lab2

#Intermediate Python SE126

#######################################################################################################################

#variables
#comp_type = type of computer
#manu = the manufacturer
#ram = the amount of ram
#hdd_1 = the first hard drive
#hdd_2 = the second hard drive
#num_hdd = number of hardrives
#os = operation system
#year = year of the computer
#proccesor = procesor type

########################################################################################################################

''' You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. 
Each row will have 8 or 9 columns. The number of columns depends on how many hard disk drives a
computer has.'''

########################################################################################################################

import csv

total_records = 0
desk_cash = 0
total_desk = 0
lap_cash = 0
total_lap = 0
comp_type_list = []
manu_list = []
processor_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []

print(f" {'TYPE':8} {'MANU':5} {'PROC':8} {'RAM':8} {'HDD1':10} {'#HDD':8} {'HDD2':10} {'OS':8} {'YEAR':10}")

with open("week2/demo/HW/lab2b.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1

        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            comp_type = "*ERROR --"+ str(rec[0])

        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "Gateway"
        elif rec[1] == "HP":
            manu = rec[1]
        else:
            manu = "*ERROR --"+ str(rec[1])

        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]

        if rec[5] == "1":
            hdd_2 = "--"
            os = rec[6]
            year = rec[7]

        elif rec[5] == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec[8]
        else:
            hdd_2 = "*ERROR --" + str(rec[5])
            os = "ERROR"
            year = "ERROR"

        year == int(year)
        
        if comp_type == "Desktop" and year <= "16":

            desk_cash += 2000
            total_desk += 1
        
        elif comp_type == "Laptop" and year <= "16":

            lap_cash += 1500
            total_lap += 1

        comp_type_list.append(comp_type)
        manu_list.append(manu)
        processor_list.append(processor)
        ram_list.append(ram)
        hdd_1_list.append(hdd_1)
        num_hdd_list.append(num_hdd)
        hdd_2_list.append(hdd_2)
        os_list.append(os)
        year_list.append(year)

        

       

        print("----------------------------------------------------------------------------------------------")
        print(f" {comp_type:8} {manu:5} {processor:8} {ram:8} {hdd_1:12} {num_hdd:8} {hdd_2:8} {os:10} {year:10}")

print("----------------------------------------------------------------------------------------------")

print(f"\nTo replace {total_desk} Desktops, it will cost ${desk_cash}.")
print(f"\nTo replace {total_lap} Laptops, it will cost ${lap_cash}.")

print("\nThank You.....")


