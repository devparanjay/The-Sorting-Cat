import json, time, string

# Initiation and Declaration of Variables

run = int()
i = int()
# Questions
nofq = int()
ques = dict()
qtypes = ["text", "number", "multiple", "time"]


def greeting():

    print("\n\nYou will be asked to provide input for setting up the bot, please provide accurate input.\nAfter this program finishes executing, a settings.json file will be created to be used by the bot.\nYou can run this file again anytime to create a settings.json file or edit the JSON yourself too.\nHave fun, but be careful!\n\n")

def start():

    global run

    choice = input("Please press Y/y if you want to set up the bot now, or press N/n for aborting the set-up: ")

    if choice == "Y" or choice == "y" or choice == "Yes" or choice == "yes":
        run = 1
        print("The loop is working.", choice, ", ", run)
    elif choice == "N" or choice == "n" or choice == "No" or choice == "no":
        print("Good bye!", choice, ", ", run)
        exit
    else:
        print("I'll take that as a 'no', good bye!")

def ask():

    global run
    global nofq
    global ques
    global qtypes

    if run == 1:
        nofq = int(input("How many questions do you want to ask the new member?\n"))
        print("Code is working till line 41.")
        for i in range(nofq):
            print("\nPlease enter Question No.", i+1, ":\n")
            q = input()
            print("What is the type of this question?\n\t1. Text\n\t2. Number\n\t3. Multiple Choice\n\t4. Time and Date")
            # Acceptable types - text, number, multiple, time.
            qtype_num = int(input("Enter your choice number: "))

            # print("Code is working till line 49.")

            qdata = {
                    "Question": q,
                    "Type": qtypes[qtype_num-1]
                }

            ques[i+1] = qdata


def quesJSON():

    with open('questions.json', 'w') as save:
        json.dump(ques, save, indent = 4)

if __name__ == "__main__":

    greeting()
    start()
    ask()

    quesJSON()

    print(ques)
    time.sleep(6)