
char_hash_table = [0] * 26
str1 = "abcdabefc"
for i in str1:
    hash_value = ord(i)-ord('a')
    char_hash_table[hash_value] +=1

print(char_hash_table)