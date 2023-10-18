import random

STRING_LENGTH = 100
input_string = ""
while len(input_string) < STRING_LENGTH:
    input_line = input("Print a random string containing 0 or 1:")
    input_string += ''.join(char for char in input_line if char == '1' or char == '0')
    print(f"""Current data length is {len(input_string)}, {STRING_LENGTH - len(input_string)} symbols left.""")
print(f"""Final data string:
{input_string}""")

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

# getting test string and making sure it's length is more than 3
test_string = ""
while len(test_string) < 4:
    test_string = input("Please enter a test string containing 0 or 1:")
    test_string = "".join(char for char in test_string if char == '1' or char == '0')

# generating predicting string based on the calculated probability of whether a 0 or 1 follows each triad
predicting_string = ""
for i in range(len(test_string) - 3):
    if triads_dict[test_string[i: i + 3]]['0'] > triads_dict[test_string[i: i + 3]]['1']:
        predicting_string += '0'
    elif triads_dict[test_string[i: i + 3]]['1'] > triads_dict[test_string[i: i + 3]]['0']:
        predicting_string += '1'
    else:
        predicting_string += random.choice('01')

# counting our correct guesses
correct_guesses = 0
for i in range(3, len(test_string)):
    if test_string[i] == predicting_string[i-3]:
        correct_guesses += 1

# printing predicting string and its accuracy value
accuracy = correct_guesses * 100 / (len(test_string) - 3)
print(f"""predictions:
{predicting_string}
Computer guessed right {correct_guesses} out of {len(test_string) - 3} symbols ({round(accuracy, 2)} %)""")
