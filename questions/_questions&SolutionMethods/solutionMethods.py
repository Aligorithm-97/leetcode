"""

1 = LeetCode Problem 217 - Contains Duplicate : Create a set with given numbers and compare their lengths.

2 = LeetCode Problem 242 - Valid Anagram : Can use sorted() function and compare them but better solution is using hash table. Use ord('a') etc.

3 = LeetCode Problem 1 - Two Sum : Create a map and use enumerate() function with for loop and if diff value is in map simply return pmap[diff] , i.

4 = LeetCode Problem 49 - Group Anagrams : 
    1 - Sorting : Create a default dictionary and sort them in a for loop and use join function to generate also string because sorted() function returns an array. Then append every same sorted value into dictionary with their original values. Finally return list(res.values())
    2 - Hash Table : To efficiently group anagrams, we use a hash table where the key is a tuple representing letter frequencies. Each word is processed by counting occurrences of letters in a fixed-size array (26 elements), ensuring anagrams share the same key. Since tuples are immutable and hashable, they serve as unique identifiers for anagram groups.

5 = LeetCode Problem 347 - Top K Frequent Elements : 
    1 - Sorting : Create a frequency table and group it with the values. Then sort it. Pop k times.
    2 - Heap : Use heap to get rid of sorting phase. Pop until k elements remains. Append remainings to res.
    3 - Bucket Sort : Create a bucket -> freq = [[] for i in range(len(nums)+1)] then Use bucket sorting to avoid other types of sorting. With bucket sort we achieve o(n) instead of o(nlog(n))

6 = LeetCode Problem 271 - Encode Decode Strings : Create a simple encode algorithm like # + len + string etc and the decode the value according to the pattern. 

"""