"""

1 = LeetCode Problem 217 - Contains Duplicate : Create a set with given numbers and compare their lengths.

2 = LeetCode Problem 242 - Valid Anagram : Can use sorted() function and compare them but better solution is using hash table. Use ord('a') etc. Traverse both strings and if the letter occurs in first string count[ord(i) - ord('a')] + 1 if the letter also occurs in second string count[ord(i) - ord('a')] -1 so if it is an anagram all values should be 0.

3 = LeetCode Problem 1 - Two Sum : Create a map and use enumerate() function with for loop and if diff value is in map simply return pmap[diff] , i.

4 = LeetCode Problem 49 - Group Anagrams : 
    1 - Sorting : Create a default dictionary and sort them in a for loop and use join function to generate also string because sorted() function returns an array. Then append every same sorted value into dictionary with their original values. Finally return list(res.values())
    2 - Hash Table : To efficiently group anagrams, we use a hash table where the key is a tuple representing letter frequencies. Each word is processed by counting occurrences of letters in a fixed-size array (26 elements), ensuring anagrams share the same key. Since tuples are immutable and hashable, they serve as unique identifiers for anagram groups.

5 = LeetCode Problem 347 - Top K Frequent Elements : 
    1 - Sorting : Create a frequency table and group it with the values. Then sort it. Pop k times.
    2 - Heap : Use heap to get rid of sorting phase. Pop until k elements remains. Append remainings to res.
    3 - Bucket Sort : Create a bucket -> freq = [[] for i in range(len(nums)+1)] then Use bucket sorting to avoid other types of sorting. With bucket sort we achieve o(n) instead of o(nlog(n))

6 = LeetCode Problem 271 - Encode Decode Strings : Create a simple encode algorithm like # + len + string etc and the decode the value according to the pattern. 

7 = LeetCode Problem 238 - Product of Array Except Self : Can be solve with brute force but it has n2 time complexity. Another solution is using division o(n) time o(1) space. And finally it can be solved with prefix suffix it is also o(n) time and o(1) space.

8 = LeetCode Problem 36 - Valid Sudoku : Use Hashset aka defaultdict(set) check same value exists in 3 sets rows cols squares. If it is exists then return False. Optimal and advanced solution = Use bitmask.

9 = LeetCode Problem 128 - Longest Consecutive Sequence : Can be solved with hashSet -> check if the num -1 in the set and also check num + length and while it has num + length reassign longest value with max function. Also it has a solution with hashmap but hashset is enough.

"""