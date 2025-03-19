"""

LeetCode Problem 217 - Contains Duplicate : Create a set with given numbers and compare their lengths.

LeetCode Problem 242 - Valid Anagram : Can use sorted() function and compare them but better solution is using hash table. Use ord('a') etc.

LeetCode Problem 1 - Two Sum : Create a map and use enumerate() function with for loop and if diff value is in map simply return pmap[diff] , i.

LeetCode Problem 49 - Group Anagrams : 
    1 - Sorting : Create a default dictionary and sort them in a for loop and use join function to generate also string because sorted() function returns an array. Then append every same sorted value into dictionary with their original values. Finally return list(res.values())
    2 - Hash Table : To efficiently group anagrams, we use a hash table where the key is a tuple representing letter frequencies. Each word is processed by counting occurrences of letters in a fixed-size array (26 elements), ensuring anagrams share the same key. Since tuples are immutable and hashable, they serve as unique identifiers for anagram groups.

"""