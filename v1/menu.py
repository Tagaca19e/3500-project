#----------------------------------------------
# Main menu and sub-menu's for interface
# Incomplete, still needs to be implemented into main/proj.py files
# Needs to be cleaned up / redone
#----------------------------------------------

#for main function
def menu():
    print("Main Menu:")
    print("********************")
    print("[1] - Load Data")
    print("[2] - Explore the Data")
    print("[3] - Describe the Data")
    print("[4] - Data Analysis")
    print("[5] - Exit")
    print()

#for describe_data function(Section 2)
def menu2():
    print("Describe Columns:")
    print("********************")
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
    print()
    #print("name column to describe: ")
    #select the column and do the statistical operation from there
    #TODO: do ALL statistical operations for the chosen column.

#for analysis function(Section 4)
def menu3():
    print("Data Analysis:")
    print("********************")
    print('[1] - How many airlines are included in the data set?'
          'Print the first 5 in alphabetical order.')
    print('[2] - How many departing airports are included in the data set?'
          ' Print the last 5 in alphabetical order.')         
    print('[3] - What airline has the oldest plane?')
    print('[4] - What was the greatest delay ever recorded?'
          ' Print the airline and airpots of this event.')
    print('[5] - What was the smallest delay ever recorded? '
          ' Print the airline and airports of this event.')
    print('[6] -What was the month of the year in 2019 with most delays overall?'
          ' And how many delays were recorded in that month?')
    print('[7] -What was the month of the year in 2019 with most delays overall?'
          'And how many delays were recorded in that day?')
    print('[8] - What airline carrier experience the most delays in'
          ' January, July and December')
    print('[9] - What was the average plane age of all planes with'
          ' delays operated by American Airlines inc.?')
    print('[10] - How many planes were delayed for more than 15 minutes during'
          ' days with "heavy snow" (Days when the inches of snow on ground were 15 or more)?')
    print('[11] - What are the 5 airports (Deaprting Airpots) that had the'
          ' most delays in 2019? Print the airports and the number of delays')
    print('[12] - Go back.')
    print()

#----------------------------------------------
#functionality for loading the data 
#----------------------------------------------
def load_data():
    print("Data Exploration done by Eidmone. Implement the functionality later")

#----------------------------------------------
#functionality for data exploration 
#----------------------------------------------
def explore_data():
    print("Data Exploration done by Eidmone. Implement the functionality later")

#----------------------------------------------
#functionality for all statistical analysis
#----------------------------------------------
def describe_data():
    menu2()
    x = (input("Name a Column to describe: "))

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
        x = int(input("Name a Column to describe: "))

#----------------------------------------------
#functionality for answering the analysis section of the project
#----------------------------------------------

def analysis():
    menu3()
    print()
    ans = int(input("What would you like to do?: "))

    while ans!=12:
        if ans == 1:
            pass
        elif ans == 2:
            pass
        elif ans == 3:
            pass
        elif ans == 4:
            pass
        elif ans == 5:
            pass
        elif ans == 6:
            pass
        elif ans == 7:
            pass
        elif ans == 8:
            pass
        elif ans == 9:
            pass
        elif ans == 10:
            pass
        elif ans == 11:
            pass
        else:
            print("Invalid Selection. PLease try again.")
        print()
        menu3()
        ans = int(input("What would you like to do?: "))




def main():
    print()
    menu()
    option = int(input("What would you like to do?: "))

    while option != 5:
        if option == 1:
            #do the data loading
            load_data()
        elif option == 2:
            #show menu for data exploration
            explore_data()
        elif option == 3:
            #show menu for statistical analysis
            describe_data()
        elif option == 4:
            #do third
            analysis()
        else:
            print("Invalid Selection. PLease try again.")
        print()
        menu()
        option = int(input("What would you like to do?: "))
    print()
    print("Program End.")
    print()

main()
