STRING_LENGTH = 100
input_string = ""
while len(input_string) < STRING_LENGTH:
    input_line = input("Print a random string containing 0 or 1:")
    input_string += ''.join(char for char in input_line if char == '1' or char == '0')
    print(f"""Current data length is {len(input_string)}, {STRING_LENGTH - len(input_string)} symbols left.""")
print(f"""Final data string:
{input_string}""")

triads = [bin(i).lstrip('0').lstrip('b').zfill(3) for i in range(0, 8)]
triads_dict = {key: {'0': 0, '1': 0} for key in triads}
for i in range(0, len(input_string) - 3):
    triads_dict[input_string[i: i + 3]][input_string[i + 3]] += 1
for i in range(0, 8):
    print(f"{triads[i]}: {triads_dict.get(triads[i]).get('0')},{triads_dict.get(triads[i]).get('1')}")
