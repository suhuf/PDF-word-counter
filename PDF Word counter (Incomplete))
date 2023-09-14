import requests
import os

set2 = 0

set = 0

y_response = ["Yes", "ye", "y", "yes"]
n_response = ["No", "no", "n", "na"]


while set2 == 0:

    if os.getcwd() != r"C:\Users\seca\Documents\pdf_test":
        os.chdir(r"C:\Users\seca\Documents\pdf_test")
        print("You are currently in directory... " + (os.getcwd()))

        set2 = + 1

    else:
        print(r"You are not in C:\Users\seca\Documents\Programming_Etc")  # Change.

while set == 0:

    chc = input("Would you like to list directories? Yes/No ")

    if chc not in y_response and chc not in n_response:
        print("Your input is invalid, requiring a yes or no. ")

    else:
        pass

    if chc in y_response:
        set += 1
        print(r"Listing directory of " + (os.getcwd()))
        d_list = (os.listdir())

        print("\n", *d_list, sep = "\n")

    if chc in n_response:
        print("Cancelling") # Create loop back menu
        set += 1

        break



    input("Would you like to extract word count of ... " + str() )

    continue
