import random

STRING_LENGTH = 100

print("""Please provide AI some data to learn...
The current data length is 0, 100 symbols left""")

# taking in the first input
input_string = ""
while len(input_string) < STRING_LENGTH:
    input_line = input("Print a random string containing 0 or 1:")
    input_string += ''.join(char for char in input_line if char == '1' or char == '0')
    print(f"""Current data length is {len(input_string)}, {STRING_LENGTH - len(input_string)} symbols left.""")
print(f"""Final data string:
{input_string}""")

# learning from the input

# generating all binary triads in a list
triads = [bin(i).lstrip('0').lstrip('b').zfill(3) for i in range(0, 8)]

# initializing the triads dictionary with the number of 0s and 1s following each triad being zero in the beginning
triads_dict = {key: {'occurrences': 0, '0': 0, '1': 0} for key in triads}

# iterating over the input string and updating the number of 0s and 1s that follow each triad in the string
for i in range(len(input_string) - 3):
    triads_dict[input_string[i: i + 3]]['occurrences'] += 1
    triads_dict[input_string[i: i + 3]][input_string[i + 3]] += 1

# calculating probabilities for 0s and 1s following triads and replacing the probability value in place of occurrence
# numbers
for triad in triads:
    triads_dict[triad]['0'] = triads_dict[triad]['0'] / triads_dict[triad]['occurrences']
    triads_dict[triad]['1'] = triads_dict[triad]['1'] / triads_dict[triad]['occurrences']

print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")

balance = 1000
while True:
    # getting a random string and making sure it's length is more than 3
    random_string = ""
    while len(random_string) < 4:
        random_string = input("Print a random string containing 0 or 1:")
        if random_string == "enough":
            print("Game over!")
            exit()
        random_string = "".join(char for char in random_string if char == '1' or char == '0')

    # generating predicting string based on the calculated probability of whether a 0 or 1 follows each triad
    predicting_string = ""
    for i in range(len(random_string) - 3):
        if triads_dict[random_string[i: i + 3]]['0'] > triads_dict[random_string[i: i + 3]]['1']:
            predicting_string += '0'
        elif triads_dict[random_string[i: i + 3]]['1'] > triads_dict[random_string[i: i + 3]]['0']:
            predicting_string += '1'
        else:
            predicting_string += random.choice('01')

    # counting our correct guesses
    correct_guesses = 0
    for i in range(3, len(random_string)):
        if random_string[i] == predicting_string[i - 3]:
            correct_guesses += 1

    # updating balance
    balance -= correct_guesses - (len(random_string) - 3 - correct_guesses)

    # printing predicting string and its accuracy rate
    accuracy = correct_guesses * 100 / (len(random_string) - 3)
    print(f"""predictions:
{predicting_string}

Computer guessed {correct_guesses} out of {len(random_string) - 3} symbols right ({round(accuracy, 2)} %)
Your balance is now ${balance}""")