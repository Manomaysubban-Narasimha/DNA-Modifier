# Program Name: Project A
# My Name: Manomaysubban Narasimha
# CS22A
# 11/18/2021
# A program that prompts the user to enter two DNA sequences and
# allows the user to add an indel, delete an indel(if it exists in
# the sequence), and finds the match/scores the dna sequences. This
# can be repeated multiple times until the user decides to quit
import re

string1 = ""
string2 = ""


def get_first_dna_sequence():
    # get first DNA sequence from the user and keeps asking until
    # entered sequence is actually correct(has only A, T, G, and C)
    print("Hello, ", end='')
    while True:
        dna = input("please enter 1st DNA sequence (must only have"
                        " A, T, G, and C): ")
        not_match = re.search(r"[^ATGC]", dna, re.IGNORECASE)
        if not_match:
            print("Please enter only a DNA sequence.")
        else:
            # if the dna sequence only has ATGC, then store the sequence
            # in the global variable string1 and break out of the while loop
            global string1
            string1 = dna
            break


def get_second_dna_sequence():
    # get the second DNA sequence from the user and keeps asking until
    # entered sequence is actually correct(has only A, T, G, and C)
    print("Thank you. ", end='')
    while True:
        dna = input("Please enter 2nd DNA sequence (must only have"
                        " A, T, G, and C): ")
        not_match = re.search(r"[^ATGC]", dna, re.IGNORECASE)
        if not_match:
            print("Please enter only a DNA sequence.")
        else:
            # if the dna sequence only has ATGC, then store the sequence
            # in the global variable string2 and break out of the while loop
            global string2
            string2 = dna
            break


def score():
    # gets the matches and mismatches. Prints the matches in lower case
    # and mismatches in upper case while printing indels as they are.
    # if a string is smaller than the other string, adds dashes to
    # the smaller string so that it matches the length of the longer string
    global string1
    global string2
    string1_local = string1.lower()
    string2_local = string2.lower()
    # save the lengths of each string in 2 different variables
    len_string1 = len(string1_local)
    len_string2 = len(string2_local)
    if len_string1 < len_string2:
        # store the difference of length between the two strings in a variable
        diff = len_string2 - len_string1
        # iterate through from the end of smaller string till the length of
        # the longer string and keep adding indels
        # to the smaller string until the i reaches length of larger string
        for i in range(len_string1, len_string2):
            string1_local += '-'
        len_string1 = len(string1_local)
        # create two lists and add elements of each string to those lists
        list_str1 = []
        list_str2 = []
        for i in range(len_string2):
            list_str1 += string1_local[i]
            list_str2 += string2_local[i]
        count_match = 0
        count_mismatch = 0
        # iterate through each element in each list and if they match,
        # then increase count_match by 1 and turn that element in each
        # list into lowercase. If does not match, then leave the element
        # as it is, and increase count_mismatch by 1
        for i in range(len(list_str1)):
            if list_str1[i] == list_str2[i] and list_str1[i] != '-':
                count_match += 1
                list_str1[i] = list_str1[i].lower()
                list_str2[i] = list_str2[i].lower()
            else:
                count_mismatch += 1
                list_str1[i] = list_str1[i].upper()
                list_str2[i] = list_str2[i].upper()
                
        # convert the list with modified characters into a string and
        # assign back to string1 and string2
        string1_local = ''.join(list_str1)
        string2_local = ''.join(list_str2)
        print("Matches: %i correct and %i errors" %(count_match, count_mismatch))
        print("String 1 :", string1_local)
        print("String 2 :", string2_local)
        
    elif len_string1 > len_string2:
        # store the difference of length between the two strings in a variable
        diff = len_string1 - len_string2
        # iterate through from the end of smaller string till the length of
        # the longer string and keep adding indels
        # to the smaller string until the i reaches length of larger string
        for i in range(len_string2, len_string1):
            string2_local += '-'
        len_string2 = len(string2_local)
        # create two lists and add elements of each string to those lists
        list_str1 = []
        list_str2 = []
        for i in range(len_string1):
            list_str1 += string1_local[i]
            list_str2 += string2_local[i]
        count_match = 0
        count_mismatch = 0
        # iterate through each element in each list and if they match,
        # then increase count_match by 1 and turn that element in each
        # list into lowercase. If does not match, then leave the element
        # as it is, and increase count_mismatch by 1
        for i in range(len(list_str1)):
            if list_str1[i] == list_str2[i] and list_str1[i] != '-':
                count_match += 1
                list_str1[i] = list_str1[i].lower()
                list_str2[i] = list_str2[i].lower()
            else:
                count_mismatch += 1
                list_str1[i] = list_str1[i].upper()
                list_str2[i] = list_str2[i].upper()
        # convert the list with modified characters into a string and
        # assign back to string1 and string2
        string1_local = ''.join(list_str1)
        string2_local = ''.join(list_str2)
        print("Matches: %i correct and %i errors" %(count_match, count_mismatch))
        print("String 1 :", string1_local)
        print("String 2 :", string2_local)
    else:
        # create two lists and add elements of each string to those lists
        list_str1 = []
        list_str2 = []
        for i in range(len_string1):
            list_str1 += string1_local[i]
            list_str2 += string2_local[i]
        count_match = 0
        count_mismatch = 0
        # iterate through each element in each list and if they match,
        # then increase count_match by 1 and turn that element in each
        # list into lowercase. If does not match, then leave the element
        # as it is, and increase count_mismatch by 1
        for i in range(len(list_str1)):
            if list_str1[i] == list_str2[i] and list_str1[i] != '-':
                count_match += 1
                list_str1[i] = list_str1[i].lower()
                list_str2[i] = list_str2[i].lower()
            else:
                count_mismatch += 1
                list_str1[i] = list_str1[i].upper()
                list_str2[i] = list_str2[i].upper()
        # convert the list with modified characters into a string and
        # assign back to string1 and string2
        string1_local = ''.join(list_str1)
        string2_local = ''.join(list_str2)
        print("Matches: %i correct and %i errors:" %(count_match, count_mismatch))
        print("String 1 :", string1_local)
        print("String 2 :", string2_local)

    
def user_input():
    # takes the input from user and depending on the choice the user makes
    # this method calls the respective methods: add(), delete(), score()
    # or breaks out of the while loop if the user chooses to quit
    while True:
        choice = input("Please pick a(add), d(delete), s(score) or q(quit): ")
        if choice == 'a'.casefold():
            add()
        elif choice == 'd'.casefold():
            delete()
        elif choice == 's'.casefold():
            score()
        elif choice == 'q'.casefold():
            print("Process Finished with exit code 0")
            break
        else:
            print("Please only pick between the choices a, d, s, and q.")
        print()


def delete():
    # ask the user which string to delete indel from and takes the valid index
    # at which the indel needs to be deleted. If at that index there is no
    # indel existing, then mentions to the user that there is no indel at
    # that index and does not do anything to the string. However, if the index
    # does have an indel, then the indel will be deleted at that index in that string
    while True:
        choice_string = input("Which string do you want to delete from (1 or 2)? ")
        if choice_string == "1".casefold():
            global string1
            print("You wish to remove an indel from:", string1)
            index = get_index(1, True)
            if string1[index] != '-':
                print("Cannot delete a character which is not an indel.")
            else:
                if index == 0:
                    string1 = string1[index+1:]
                elif index == len(string1)-1:
                    string1 = string1[:index]
                else:
                    string1 = string1[:index] + string1[index+1:]
            print("Your new code is:", string1)
            break
        elif choice_string == "2".casefold():
            global string2
            print("You wish to remove an indel from:", string2)
            index = get_index(2, True)
            if string2[index] != '-':
                print("Cannot delete a character which is not an indel.")
            else:
                if index == 0:
                    string2 = string2[index+1:]
                elif index == len(string2)-1:
                    string2 = string2[:index]
                else:
                    string2 = string2[:index] + string2[index+1:]
            print("Your new code is:", string2)
            break
        else:
            print("Please only pick between string 1 and string 2")


def add():
    # an infinite while loop keeps prompting until user chooses either
    # string 1 or string 2. 
    while True:
        choice_string = input("Which string do you want to add to (1 or 2)? ")
        if choice_string == '1':
            global string1
            index = get_index(1, False) # valid index is received
            newString = ''
            if index == 0:
                string1 = '-' + string1
            elif index == len(string1):
                string1 = string1 + '-'
            else:
                string1 = string1[:index] + '-' + string1[index:]
            print("Your new code is", string1)
            break
        elif choice_string == '2':
            global string2
            index = get_index(2, False) # valid index is received
            newString = ''
            if index == 0:
                string2 = '-' + string2
            elif index == len(string2):
                string2 = string2 + '-'
            else:
                string2 = string2[:index] + '-' + string2[index:]
            print("Your new code is", string2)
            break
        else:
            print("Please only type number 1 or 2 for string choice.")
            


def get_index(choice_string, is_del):
    # keeps prompting the user for valid index, and once gets the valid index
    # then it returns that index to the add() method or delete() method
    index = 0
    while True:
        try:
            if not is_del:
                index = int(input("Please enter an index to add the indel"
                                  "(0 <= index <= length): "))
            else:
                index = int(input("Please enter an index to delete the indel"
                                  "(0 <= index < length): "))
            if choice_string == 1:
                if not is_del:
                    if index < 0 or index > len(string1):
                        print("Please enter an index within the range"
                                "(0 <= index <= length)")
                        continue
                    else:
                        return index
                else:
                    if index < 0 or index >= len(string1):
                        print("Please enter an index within the range"
                                "(0 <= index < length)")
                        continue
                    else:
                        return index
            else:
                if not is_del:
                    if index < 0 or index > len(string2):
                        print("Please enter an index within the range"
                                "(0 <= index <= length)")
                        continue
                    else:
                        return index
                else:
                    if index < 0 or index >= len(string2):
                        print("Please enter an index within the range"
                                "(0 <= index < length)")
                    else:
                        return index
        except ValueError:
            print("Please enter only an integer index.")
    
        

# main method calls other functions and is the driver
# and starting point of the program
def main():
    get_first_dna_sequence()
    get_second_dna_sequence()
    user_input()


if __name__ == "__main__":
    main()
