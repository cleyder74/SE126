import csv

Mname = []
atk = []
defense = []
lvl = []
type = []
text_file_list = []



with open("MidTerm/Midtermtxt.txt") as yugioh:

    file = csv.reader(yugioh)


    for rec in file:

        text_file_list.append(rec)

        Mname.append(rec[0])
        atk.append(int(rec[1]))
        defense.append(int(rec[2]))
        lvl.append(int(rec[3]))
        type.append(rec[4])



    for i in range(0, len(Mname)):

        print(f"{Mname[i]:12} \t{atk[i]:12} \t{defense[i]:12} \t{lvl[i]:4} \t{type[i]:4}")

        






    
    
    