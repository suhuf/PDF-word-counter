import requests
import re
import os
from pdfminer.high_level import extract_pages, extract_text
import sys
import string

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


def pdfhunter(x):

    data = extract_text(x)



    w_dict = dict()

    out=sys.stdout
   
    out.write(data)

    word_count = len(re.findall(r'\w+', data))    # check for find regex word match in data count.

    word_list = re.split(r'\W', data)

    print(word_list) # think i got it

    print("\n" "There are " + str(word_count) + " words in "  + x )

    # Testing

        #words = line.split(" ")

    for r_word in word_list:
        
        word = r_word.lower()

        if word in w_dict:
            w_dict[word] = w_dict[word] + 1
        else:
            w_dict[word] = 1

    for key in list(w_dict.keys()):
        print(key, ":", w_dict[key]) 

while set == 0:

    chc = input("Would you like to list directories? Yes/No ")

    if chc not in y_response and chc not in n_response:
        print("Your input is invalid, requiring a yes or no. ")

    if chc in y_response:
        print(r"Listing directory of " + (os.getcwd()))
        d_list = (os.listdir())
        print("\n", *d_list, sep = "\n")
        set =+ 1

    if chc in n_response:
        print("Cancelling") # Create loop back menu

        break

while set == 1:

    chc2 = input("\n" "Would you like to extract word count of ... " + str(len(d_list)) + " files? ")

    a_list = []

    if chc2 in y_response:
        set = 2

        for i in d_list:
            ext_n = os.path.splitext(i)[-1]
            if ext_n == ".pdf":
                a_list.append(i)

            else:
                print(r"This Item: " + str(i) + " will not be parsed as it is not a .pdf file."
                                                " (This may be an extension naming issue)" "\n")
        if len(a_list) == 0:
            print("There are no files identified as .PDF files. Cancelling script")

            break

        print("\n" "These are your .PDFs primed for analysis: " + "\n", *a_list, sep = "\n")

        x = 0
        
        for file in a_list: #directory add that
            pdfhunter(file)
            
            if file != a_list[-1]:
                chc3 = input("\n" "Would you like to continue this output? ")

            if chc3 in y_response:
                continue
            
            if chc3 in n_response:
                break
    
    if chc2 in n_response:
        print("Cancelling")  # Create loop back menu
        set =+ 1

        break



