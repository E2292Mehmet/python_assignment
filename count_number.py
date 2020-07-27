# takes a sentence from the user,
# counts the number of each letter of the sentence,
# collects the letters/chars as a key and the counted numbers as a value in a dictionary.
# hippo runs to us!	
#{'s': 2, 'r': 1, 't': 1, 'h': 1, 'n': 1, 'i': 1, 'u': 2, 'o': 2, 'p': 2, ' ': 3, '!': 1}

word = input('Please enter a sentence : ')
d = {}
for i in word :
    if i not in d.keys() :
        d[i] = 1 
    else :
        d[i] = d[i] + 1
        
print(d)
        