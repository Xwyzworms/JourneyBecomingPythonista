''' This code only Randomize dice rolling , well basic :D ,''' 

import random

if __name__ == "__main__":
    print("Dice Simulator")
    ans = "y"
    while(ans == "y"):
        numb = random.randint(1,6)

        if(numb == 1):
            print("------------------------")
            for i in range(0,5):
                print("| {:<20} |".format(""))
                for j in range(0,5):
                    if(i == 2 and j == 3):
                        print("| {:^20} |".format("0"))
            print("------------------------")
        elif(numb == 2):
            print("------------------------")
            for i in range(0,5):
                print("| {:<20} |".format(""))
                for j in range(0,5):
                    if  (i == 1 and j == 1):
                        print("| {:^10s} {:^10s}|".format("0" , "0"))
            print("------------------------")
        elif(numb == 3):
            print("------------------------")
            for i in range(0,5):
                print("| {:<20} |".format(""))
                for j in range(0,5):
                    if  (i == 1 and j == 1):
                        print("| {:^10s} {:^10s}|".format("0" , "0"))
                    if ( i == 2 and  j ==1):
                        print("| {:^20s} |".format("0")) 
            print("------------------------")
        elif(numb == 4):
            print("------------------------")
            for i in range(0,5):
                print("| {:<20} |".format(""))
                for j in range(0,5):
                    if  (i == 1 and j == 1):
                        print("| {:^10s} {:^10s}|".format("0" , "0"))
                    if ( i == 3 and  j ==1):
                        print("| {:^10s} {:^10s}|".format("0", "0")) 
            print("------------------------")
        elif(numb == 5):
            print("------------------------")
            for i in range(0,5):
                print("| {:<20} |".format(""))
                for j in range(0,5):
                    if  (i == 1 and j == 1):
                        print("| {:^10s} {:^10s}|".format("0" , "0"))
                    if ( i == 2 and j == 1):
                        print("| {:^20} |".format("0"))
                    if ( i == 3 and  j ==1):
                        print("| {:^10s} {:^10s}|".format("0", "0")) 
            print("------------------------")
        elif(numb == 6):
            print("------------------------")
            for i in range(0,5):
                print("| {:<20} |".format(""))
                for j in range(0,5):
                    if  (i == 1 and j == 1):
                        print("| {:^10s} {:^10s}|".format("0" , "0"))
                    if ( i == 2 and j == 1):
                        print("| {:^10s} {:^10s}|".format("0" , "0"))
                    if ( i == 3 and  j ==1):
                        print("| {:^10s} {:^10s}|".format("0", "0")) 
            print("------------------------")
        ans = input("Mo men lagi gak ? ")
