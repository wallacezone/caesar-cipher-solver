alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print "Input first the coded character and then the original character."

coded = raw_input('> ')
original = raw_input('> ')

print "Now input the coded string to decipher."

coded_string = raw_input('> ')

# compute the shift between the two alphabets
shift = alphabet.index(coded) - alphabet.index(original)

decoded_string = ""

# convert each coded char to the decoded char
for char in coded_string:

    # if char is not inside the alphabet, skip it
    if not (char in alphabet):
        decoded_string += char

    # if the shift overflows the range of the alphabet
    elif alphabet.index(char) - shift >= len(alphabet):
        decoded_string += alphabet[alphabet.index(char) - shift - 26]

    else:
        decoded_string += alphabet[alphabet.index(char) - shift]

print "DECODED STRING:"
print decoded_string
