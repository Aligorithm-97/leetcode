# Important python usages
"""

Abstract Class : A class that can contain abstract methods and cannot be instantiated directly. It can have both abstract and regular methods.

Interface : A structure that contains only method signatures. It supports multiple inheritance.

Polymorphism : Allows the same method to behave differently. It is divided into Overriding and Overloading.

Overloading : Methods defined in the same class with the same name but different parameters.

"""

def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    output_dict = {}

    for key, value in zip(keys, values):
        output_dict[key] = value
      
    return output_dict



my_dict = {"a": 1, "b": 2, "c": 3}

for key, value in my_dict.items():
    print(key, value)




nums = [1, 2, 4, 3, 2, 1]
freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)  # {1: 2, 2: 2, 4: 1, 3: 1}



from collections import defaultdict

nums = [1, 2, 4, 3, 2, 1]
freq = defaultdict(int)

for num in nums:
    freq[num] += 1

print(freq)  # {1: 2, 2: 2, 4: 1, 3: 1}


def count_chars(s: str) -> Dict[str, int]:
    count = defaultdict(int)
    for char in s:
        count[char] += 1
    return count




def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    output = defaultdict(list)
    for sublist in nums:
        first = sublist[0]
        for i in range(1,len(sublist)):
            output[first].append(sublist[i])
    return output