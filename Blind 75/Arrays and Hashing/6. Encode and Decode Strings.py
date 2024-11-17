"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""

#TC: Encoding:- O(N), Decodin:- O(N)
#SC: Encoding:- O(1), Decoding:- O(N)
# Encoding:- Add Length of word and "#" before that word in a list, while encoding
def encode(strs):
    temp = ""
    for i in strs:
        temp += f"{len(i)}#{i}"
    
    return temp

"""   4#neet4#code4#love3#you  """

# Decoding:- Search for #, char before hash is the length , much length time forward to get the word.
def decode(s):
        res = []
        i = 0
        
        while i < len(s):

            #Finding the length of the string
            j = i
            while s[j] != '#':  # Searching for # in the string
                j += 1   
            length = int(s[i:j]) #Char befor hash is the length of string
            #-------------------

            i = j + 1            # Moving i after j
            j = i + length       # Moving j one char after where word ends
            res.append(s[i:j])   # now char from i to j is our required word , so appending it to result
            i = j
            
        return res


# Example usage
strs = ["neet", "code", "love", "you"]
encode_str = encode(strs)  

print("Original-> ", strs)
print("Encoded-> ", encode_str)

print("Encoded-> ",decode(encode_str))


