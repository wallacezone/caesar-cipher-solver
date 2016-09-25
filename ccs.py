alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print "Input first the encoded character and then the original character."

encoded = raw_input('> ')
original = raw_input('> ')

print "Now input the encoded string to decipher."

encoded_string = raw_input('> ')

# compute the shift between the two alphabets
shift = alphabet.index(encoded) - alphabet.index(original)

decoded_string = ""

# convert each encoded char to the decoded char
for char in encoded_string:

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
raw_input()
