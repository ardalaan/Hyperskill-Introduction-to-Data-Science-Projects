STRING_LENGTH = 100
input_string = ""
while len(input_string) < STRING_LENGTH:
    input_line = input("Print a random string containing 0 or 1:")
    input_string += ''.join(char for char in input_line if char == '1' or char == '0')
    print(f"""Current data length is {len(input_string)}, {STRING_LENGTH - len(input_string)} symbols left.""")
print(f"""Final data string:
{input_string}""")
