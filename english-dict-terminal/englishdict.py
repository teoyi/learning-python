import json
import os
import difflib


def title():
    print('''
    Welcome to the dictionary!
    - Type in the word you are searching for when prompted!
    - Input x if you would like to exit the application!
    ''')

###
### Loading dictionary file that contains words in key and value format
###

os.chdir('/Users/luke/Desktop/Python/GitClone/PROJECT-English-Dictionary/Data')
#print(os.getcwd())
f = open('data.json','r')
dict = json.load(f)
# print(dict)



###
### Input/Output
###
def search():
    searching = True
    while searching:
        # Variable
        restart = True
        choosing = True

        # User Input
        word = input('\nWhat would you like to search?: ')
        suggestion = difflib.get_close_matches(word,dict) #Provide suggestion for bad word

        if word == 'x':
            print('\nThank you for using this dictionary!')
            print('\nExiting Dicitonary...')
            searching = False
            exit()

        elif word in dict:
            print(dict[word.lower()])

        elif word not in dict:
            print('\nDid you mean: ' + str(suggestion[0]) + '?')

            while choosing:
                choice1 = input('(Y/N) : ')

                if choice1.lower() == 'y':
                    print('\n' + str(dict[suggestion[0]]))
                    choosing = False
                    break

                elif choice1.lower() == 'n': # provide more suggestions
                    print('\nHere are some other possible words that you might be looking for:')
                    index = range(len(suggestion[:]))

                    for number in index:
                        print(str(number+1) + '. ' + str(suggestion[number]))

                    while choosing:
                        choice2 = input('\nChoose one (input the value corresponding to the word): ')

                        if (int(choice2)-1) in list(index):
                            print(str(dict[suggestion[int(choice2) - 1]]))
                            break

                        else:
                            print("Sorry, that is an invalid number. Please try again!")
                            continue

                    break

                else:
                    print('\nSorry, that is an invalid input. Please Try again!')
                    continue
                    
        else:
            print('Sorry, the word you are looking for is not in the dictionary!')

        while restart:
            choiceend = input('\nWould you like to search another word? (Y/N) : ')
            if choiceend.lower() == 'y':
                break
            elif choiceend.lower() == 'n':
                print('\nThank you for using this dictionary!')
                print('\nExiting Dictionary...')
                searching = False
                exit()
            else:
                print('\nSorry, that is an invalid input. \nPlease try again!')
                continue
        continue

title()
search()
