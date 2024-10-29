from morse_dicts import text_to_morse_dict

# implement input feature
text = str(input('Which text do you want to convert to morse code? ').lower())

# implement conversion feature
for letter in text:
    print(text_to_morse_dict[letter])

#Test - Result for "Hello World" is:
# h : o o o o
# e : o
# l : o - o o
# l : o - o o
# o : - - -

# w : o - -
# o : - - -
# r : o - o
# l : o - o o
# d : - o o
