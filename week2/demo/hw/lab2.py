import csv
total_records = 0 

machine = []
manu = []
intel = []
ram = []
disk1 = []
disknum = []
disk2 = []
os = []
yr = []

with open("week2/demo/hw/lab2b.csv") as lab2:
    file = csv.reader(lab2)

    for rec in file:
         #variable for each field
         

        #-------------------------------------------------
        machine.append(rec[0])
        manu.append(rec[1])
        intel.append(rec[2])
        ram.append(rec[3])
        disk1.append(rec[4])
        disknum.append(rec[5])
        disk2.append(rec[6])
        os.append(rec[7])
        yr.append(rec[8])

    print(rec)





    
    



    #final printed message for each machine
    print(rec)


