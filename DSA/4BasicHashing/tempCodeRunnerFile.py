
def build_hash(s):
    dict1 = {}

    for character in s:
        if character in dict1:
            dict1[character] +=1
        else:
            dict1[character] =1
    
    return dict1

def fetching(hash_table, query):
    return hash_table.get(query, 0)


# Sample string and queries
s = "abcdabefc"
char_queries = ['a', 'g', 'h', 'b', 'c']

hash_table = build_hash(s)
print(hash_table)

for query in char_queries:
    print(f"{query} occurs {fetching(hash_table, query)} times")