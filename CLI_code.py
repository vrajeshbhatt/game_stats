import json
import sys
import pandas as pd

try:
    # Code used to store our dictionary into a txt file
    pl_dict = {
            'joel':{'Wins':41, 'Losses':3, 'Ties':22},
            'elizabeth':{'Wins':32,'Losses':14,'Ties': 17},
            'mike':{'Wins':8,'Losses':19,'Ties': 11}
            }

    json.dump(pl_dict, open("player_stats.txt",'x'))
except:
    print("Loading previously stored dictionary...")


# Reading the dictionary stored in the file
pl_dict = json.load(open("player_stats.txt"))

print("\n############### GAME STATS PROGRAM ###############")

def opt1():
    while(True):
        x=input("\nEnter a player name or enter 'exit' to return to options menu: ").lower().strip()
        if(x in pl_dict.keys()):
            print("Wins\t:",pl_dict[x]["Wins"])
            print("Losses\t:",pl_dict[x]["Losses"])
            print("Ties\t:",pl_dict[x]["Ties"])
            opt1()

        elif x=='exit':
            options()
            
        else:
            print("Player does not exist in the list! Kindly enter again.")            
            opt1()

def opt2():
    name = input("Enter player name\t: ").lower().strip()
    while True:
        try:
            wins = int(input("Enter player wins\t: ").strip())
            loss = int(input("Enter player losses\t: ").strip())
            ties = int(input("Enter player ties\t: ").strip())
            break
        except:
            print("Invalid data entered, Kindly enter numeric data.")

    pl_dict[name] = {'Wins':wins, 'Losses':loss, 'Ties':ties}

    print('Player info added!')
    options()

def opt3():
    name=input("\nEnter a player name to delete from records or enter 'exit' to return to options menu: ").lower().strip()
    if name=='exit':
        options()
    
    if(name in pl_dict.keys()):
        confirm = input("Are you sure? enter 'yes' to proceed or 'exit' to return to options menu: ").lower().strip()
        if confirm=='exit':
            options()
            
        elif confirm=='yes':
            del pl_dict[name]
            print(f"Player {name} record deleted! \nReturning to options menu...")
            options()

        elif x=='exit':
            options()
            
        else:
            print("Player does not exist in the list! Kindly enter again.")
            opt3()

    
def options():
    # Printing sorted names
    print("\nPlayers list: ")
    for key in sorted(pl_dict.keys()):
        print("\t\t",key.capitalize())    

    print("\nOptions: ")
    print("1. View specific player's detailed stats")
    print("2. Add a player to the list")
    print("3. Delete a player from the list")
    print("4. Credits")
    print("5. Exit")

    while True:
        opt = input('\nEnter option number: ')
        if opt == '1':
            opt1()
            options()
            
        elif opt == '2':
            opt2()
            options()

        elif opt == '3':
            opt3()
            options()

        elif opt == '4':
            print('\n2022S-T1 AISC1000 - Python 01\nWeek 10 - Case Study 2')
            print('Course Professor - Mr. Qasim Ali\n')
            credits_df = pd.DataFrame({'Member name':['Dalveer Kaur', 'Priyanka Sharma', 'Saghithya S. Nateson','Surya Bansal','Vrajeshkumar Bhatt'],
                                       'ID':[500208166,500208166,500203662,500210660,5009114],
                                       'Tasks':['Coding','CLI Formatting','File Handling','Coding','Web GUI'],
                                       'Contribution':['20%','20%','20%','20%','20%']})

            print(credits_df)
            
        elif opt == '5' :
            print("Saving updated player dict...")
            json.dump(pl_dict, open("player_stats.txt",'w'))
            print("Good Bye!")

            sys.exit()

        else:
            print("Invalid input! Enter again... ")

options()
