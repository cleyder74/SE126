#W3D1 Demo - text fle handling & storing to 1D lists

import csv

#total counters for records
total_records = 0

#cretew some lists
comp_type_list = []
manu_list = []
processor_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []


print(f" {'TYPE':8} {'MANU':5} {'PROC':8} {'RAM':8} {'HDD1':8} {'#HDD':8} {'HDD2':8} {'OS':4} {'YEAR':2}")
print("----------------------------------------------------------------------------------------------")
with open("Week3/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #print(rec) #shows as a list -> []

        #keep track of the rec count in the file

        total_records += 1
        #total_records = total_records + 1

        #filtering for display-------------
        #--comp type-- rec[0]
        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type == "Laptop"
        else:
            comp_type = "*ERROR --" + str(rec[0])

        #-manufacturer -- rec[1]
        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "Gateway"
        elif rec[1] == "HP":
            manu = rec[1]
        else:
            manu = "*ERROR --" + str(rec[1])

        #--processor / ram / hdd_1 / num_hdd - exact from file
        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]

        if rec[5] == "1":
            hdd_2 = "--" #"--" #"none"
            os = rec[6]
            year = rec[7]

        elif rec[5] == "2":
            hdd_2 = rec[6]
            od = rec[7]
            year = rec[8]
        else:
            hdd_2 = "*ERROR --" + str(rec[5])
            os = "EROOR"
            year = "ERROR"
        
        #append rescpective values to the appropriate field list
        comp_type_list.append(comp_type)
        manu_list.append(manu)
        processor_list.append(processor)
        ram_list.append(ram)
        hdd_1_list.append(hdd_1)
        num_hdd_list.append(num_hdd)
        hdd_2_list.append(hdd_2)
        os_list.append(os)
        year_list.append(year) 


        #final print for all records
        print(f" {comp_type:8} {manu:5} {processor:8} {ram:8} {hdd_1:10} {num_hdd:4} {hdd_2:4} {os:8} {year:10}")
        print("----------------------------------------------------------------------------------------------")
#------Disconnected from file-----------------------------

print(f"TOTAL RECORDS: {total_records}")

#process the list to: print the machine data
for index in range(0, total_records):
#for the index in range(0, len(comp_type_list)): --> len(comp_type_list) returns the INTEGER count of values
    print(f" {comp_type_list[index]:8} {manu_list[index]:5} {processor_list[index]:8} {ram_list[index]:8} {hdd_1_list[index]:10} {num_hdd_list[index]:4} {hdd_2_list[index]:4} {os_list[index]:8} {year_list[index]:10}")

#process the listrs to: count the number of desktops
desktop_count = 0
for index in range(0, len(comp_type_list)):

    #look through th comp-type-list to find "desktop"
    if comp_type_list[index] == "Desktop" and int(year_list[index]) <= 16:        desktop_count += 1 #add 1 for every time "Desktop" is found

print(f"TOTAL DESKTOPS IN FILE: {desktop_count}GB")


#process the lists to: find the average hdd_1 size
total_size = 0
count_size = 0

for index in range(0, len(hdd_1_list)):
    if hdd_1_list[index] == '001TB':
        total_size += 1
    else:
        total_size += 0.5
    
    count_size += 1


average = total_size / count_size
#could also use: len(hdd_1_list)' or 'total_records' in place of 'count_size'

print(f"AVERAGE HDD1 SIZE {average:.2f}TB or {average*1000:0.2f}GB")
    
    
