#Cleyder Soto-Reyes

#MidTerm

#Intermediate Python SE126
#####################################################################################################################

'''For your Midterm Project in SE126 you will be building a program of your own design! 
You must work individually to design a program and file of your choosing.  
The program must include the following:

a file to be read and processed, data stored into respective lists .csv or .txt
import csv will work for both of these file types, but all data must be separated with a comma! >= 2 lists
these can be populated from a file or by hand showcase understanding of control flow structures
showcase understanding of self-built functions
Starting Documentation
include a brief program description
include a variable dictionary with data types including your lists!
Documentation for anything used not introduced in the course Creativity!'''

########################################################################################################################

import csv
import random
import time


#List Creation
mName = [] #Name of the monster

atk = [] #Attack value of the monster

defe = [] #Defense value of the monster

typ = [] #The monster's type

lvl = [] #The monster's level

#Connection to csv file
with open("Mid/yugioh.csv") as yugioh:
    file = csv.reader(yugioh)

    for rec in file:
        #Appending rec to respective list
        mName.append(rec[0])
        atk.append(int(rec[1]))
        defe.append(int(rec[2]))
        typ.append(rec[3])
        lvl.append(int(rec[4]))

def menu(): #Main Menu function
    print("\n1. DUEL")
    print("\n2. Monster Search")
    print("\n3. Monster List")
    print("\n4. EXIT")

    choice = int(input("\nPlease Choose: "))

    while choice < 0 or choice > 4: #In case of an error
        print("\n\tSorry, not a valid choice.")
        choice = int(input("\nPlease Choose: "))

    return choice

def seq_search(search_term): #Subsequential Search function

   
    found_index = "" 

    for i in range(0, len(mName)):
        
        if mName[i] == search_term:
            found_index = i 

    return found_index

def duel(): #Main game function
     
    #Randomly picks a monster and assigns a variable to it
     mon1 = random.choice(mName)
     mon2 = random.choice(mName)
    #------------------------------------------------------
     
    #Assigns an index to each of the randomly picked monsters from above
     index1 = seq_search(mon1)
     index2 = seq_search(mon2)
    #--------------------------------------------------------------------
     print("\nSearching for opponent.....")
     time.sleep(3) #Makes a 3 sencond pause after choosing to duel 
     
     print("\n\n\tA Monster Approaches!!")
     print(f"\n\t{mon1} | Attack: {atk[index1]} | Defense: {defe[index1]} | Type: {typ[index1]} | Level: {lvl[index1]}")

     if atk[index1] >= 3000 and atk[index1] < 3999:#sorry katie
            print("\n\tThis is gonna be tough!")

     elif atk[index1] >= 4000:
            print("\n\tYou should probably run away!!")
     
     play = input("\nDo you accept? (y/n): ")
      
     while play != "y" and play != "n": #In case of an error ---- sorry Katie 
          print("\n\tNot a valid choice, please try again (y/n): ")
          play = input("\nDo you accept? (y/n)")

     if play == "n":
          end = input("\n\tReturn to main menu? (y/n): ")

          if end == "n":
               duel()
          elif end == "y":
               menu()
          else:
               print("\nNot a valid choice, please try again")
     
     #Starts the game a in a while loop-----------------------------------
     while play == "y":
    
      #Randomizer inside the loop so that finding another matchup is possible
      mon2 = random.choice(mName)
      index2 = seq_search(mon2)

    
      #Displays first monster along with its stats
      print(f"\n\t{mon1} | Attack: {atk[index1]} | Defense: {defe[index1]} | Type: {typ[index1]} | Level: {lvl[index1]} - has challenged you to battle!")
      
       
       
      #Displays second monster along with its stats
      print(f"\n\t{mon2} | Attack: {atk[index2]} | Defense: {defe[index2]} | Type: {typ[index2]} | Level: {lvl[index2]} - will help you out.")
         
      if atk[index2] >= 3000 and atk[index2] < 3999:
            print("\n\tThey're a strong one!")
         
      elif atk[index2] >= 4000:
             print("\n\t*They're one of a kind!!*")
      
      #This feature gives the player a second chance to find an easier, or harder opponent.
      esc = input("\nWould you like to escape? (y/n): ")
      if esc == "y":
           duel()
           
      #Dislays both the program's and user's monsters
      print(f"\n{mon1} | Attack: {atk[index1]} | Defense: {defe[index1]} | Type: {typ[index1]} | Level: {lvl[index1]}")
      print(f"\n{mon2} | Attack: {atk[index2]} | Defense: {defe[index2]} | Type: {typ[index2]} | Level: {lvl[index2]}")
    

      #The player will Win, Lose or Draw depending on the monster's attack value
      if atk[index1] > atk[index2]:
            print(f"\n{mon1} wins!")
            print("\n\tGame Over")
        
      elif atk[index2] > atk[index1]:
             print(f"\n{mon2} wins!")
             print("\n\tCongratualions you win!!")
        
      else:
             print("\nIt's a draw!")
      
      
      #If play is 'Y' the user will be put through the while loop again
      play = input("\nExit Game?")
      
      if play == "y":
           return
      elif play == "n":
           duel()
      else:#In case of an error
           print("\n\tNot a valid input return to menu")
           menu()
     #End of while loop---------------------------------------------------------------



menu_choice = menu()

while menu_choice != 4:
    
    if menu_choice == 1: #Commences the Main game function
        duel()


    elif menu_choice == 2: #Searches for a specific monster using subsequential search
        
        print("\n\tSearch")
        
        search = input("\nPlease Enter the Name of the Monster: ")
        
        found = seq_search(search)

        if found != "":
           print(f"\n{mName[found]} | Attack: {atk[found]} | Defense: {defe[found]} | Type: {typ[found]} | Level: {lvl[found]}")
        
        else:
            print(f"\n{search} has not been found")

        while found == "":
              search = input("\nPlease Enter the Name of the Monster: ")
        
              found = seq_search(search)

              if found != "":
                 print(f"\n{mName[found]} | Attack: {atk[found]} | Defense: {defe[found]} | Type: {typ[found]} | Level: {lvl[found]}")
                 search2 = input("Would you like to search again? (y/n): ")
                 
                 while search2 == "y":
                      search = input("\nPlease Enter the Name of the Monster: ")
                      found = seq_search(search)
                      print(f"\n{mName[found]} | Attack: {atk[found]} | Defense: {defe[found]} | Type: {typ[found]} | Level: {lvl[found]}")
                 if search2 == "n":
                      menu()
                
            
              else:
                  print(f"\n{search} has not been found")

             
        
        

        


    elif menu_choice == 3:#Displays list of all monsters
        
        print(f"{'Monster':33} \t {'ATK':5} \t {'DEF':5} \t {'Type':20} \t {'Level':4}")

        for i in range(0, len(mName)):
            print("--------------------------------------------------------------------------------------")
            print(f"{mName[i]:30} \t {atk[i]:10} \t {defe[i]:5} \t {typ[i]:20} \t {lvl[i]:4}")
            print()

    elif menu_choice == 4: #Exits the program
        print("Thanks for Playing!!")

    
            
    menu_choice = menu()
