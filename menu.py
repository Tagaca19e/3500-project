def menu():
    print("[1] - Explore the Data")
    print("[2] - Describe the Data")
    print("[3] - Data Analysis")
    print("[4] - Exit")

def menu2():
    print("[1] - Count")
    print("[2] - Unique")
    print("[3] - Mean")
    print("[4] - Median")
    print("[5] - Mode")
    print("[6] - Standard Deviation(SD)")
    print("[7] - Variance")
    print("[8] - Minimum")
    print("[9] - Maximum")
    print("[10] - Find Percentile Values")
    print("[11] - Go back.")

def option1():
    print("Data Exploration done by Eidmone. Implement the functionality later")

def option2():
    menu2()
    x = int(input("Select a function: "))

    while x != 11:
        if x == 3:
            print("mean")
            #mean()
        elif x == 4:
            print("median")
            #median() 
        elif x == 5:
            print("mode")
            #mode()            
        elif x == 11:
            main()
            option = int(input("What would you like to do?: "))
        else:
            print("Invalid Selection. Please try again.")
        print()
        menu2()
        x = int(input("Select a function: "))


def menu3():
    print("[1] - What was the month of the year in 2019 with most delays overall? And how many delays were recorded that month?")
    print("[2] - What was the month of the year in 2019 with most delays overall? And how many delays were recorded that day?")
    print("[3] - What airline carrier experience the most delays in January, July, and December?")
    print("[4] - What was the average plane age of all planes with delays operated by American Airlines inc.")
    print("[5] - How many planes were delayed for more than 15 minutes during days with 'heavy snow' (Days when the inches of snow on ground were 15 or more)?")
    print("[6] - What are the 5 Airports that had the most delays in 2019?")
    print("[7] - Go back.")
    print()

def option3():
    menu3()
    analysis = int(input("What would you like to do?: "))

    while analysis!=7:
        if analysis == 1:
            pass
        elif analysis == 2:
            pass
        elif analysis == 3:
            pass
        elif analysis == 4:
            pass
        elif analysis == 5:
            pass
        elif analysis == 6:
            pass
        else:
            print("Invalid Selection. PLease try again.")
        print()
        menu3()
        analysis = int(input("What would you like to do?: "))


def main():
    menu()
    option = int(input("What would you like to do?: "))

    while option != 4:
        if option == 1:
            #do the first thing
            print("One has been selected.")
            option1()
        elif option == 2:
            #do second
            print("Two has been selected.")
            option2()
        elif option == 3:
            #do third
            option3()
        else:
            print("Invalid Selection. PLease try again.")
        print()
        menu()
        option = int(input("What would you like to do?: "))
    print("Program End.")

main()
