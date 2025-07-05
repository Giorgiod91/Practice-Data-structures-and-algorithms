


from typing import List

s = "abcabcbb"
def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])  # shrink from the left
            left += 1
        seen.add(s[right])        # expand to the right
        max_len = max(max_len, right - left + 1)
    return max_len





def length(s:str):
    seen = set()
    left= 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left +=1
        seen.add(s[right])
        max_len = max(max_len, right - left +1)

    return max_len


   
def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    
    left = 0
    max_len = 0
    char_count = {}

    for right in range(len(s)):
        char  = s[right]
        
        char_count[char] = char_count.get(char, 0) + 1
        while len(char_count) >k:     
              left_char = s[left]
              char_count[left_char] -= 1
              if char_count[left_char] == 0:
                del char_count[left_char]
              left += 1       
      
        max_len = max(max_len, right - left +1)

    return max_len




def lololo(s:str, k:int) -> int:
    left = 0
    max_len = 0
    char_count = {}
    max_char =0

    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) +1
        max_char_freq = max(max_char_freq, char_count[char])
        while len(char_count) >k :
            left_char = s[left]
            char_count[left_char] -=1
            if char_count[left_char] ==0:
                del char_count[left_char]
            left +=1
        max_len = max(max_len, right - left +1)

    return max_len




def findMaxAverage(nums: List[int], k: int) -> float:
    # Anfangsfenster der Länge k
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for right in range(k, len(nums)):
        # Schiebe das Fenster weiter: ziehe linke Zahl ab, füge rechte hinzu
        window_sum += nums[right] - nums[right - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


print(findMaxAverage(nums = [1,12,-5,-6,50,3], k=4))







def max_sum_k_window(nums: List[int], k: int) -> int:
    max_sum = sum(nums[:k])

    window_sum = max_sum

    for right in range(k ,len(nums)):
        window_sum += nums[right] - nums[right -k]
        max_sum = max(max_sum, window_sum)


    return max_sum

print(max_sum_k_window(nums = [2, 3, 5, 1, 6, 2, 4], k = 3))



def min_sum_k_window(nums: List[int], k: int) -> int:
    min_sum = sum(nums[:k])

    window_sum = min_sum

    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right -k]
        min_sum = min(min_sum,window_sum)

    return min_sum


print(min_sum_k_window(nums = [4, 2, 1, 7, 8, 1, 2, 8, 10], k = 3))



def count_subarrays_with_avg_at_least_t(nums: List[int], k: int, t: float) -> int:
    window_sum = sum(nums[:k])

    count = 0
    if window_sum / k >= t:
        count += 1

   

    for right in range(k , len(nums)):
        window_sum += nums[right] - nums[right -k]
        if window_sum / k >= t:
            count +=1
        

    return count


print(count_subarrays_with_avg_at_least_t(nums = [2, 1, 3, 4, 1, 5],k = 3,
t = 3))
    







def count_subarrays_with_sum(nums: List[int], k: int, t: int) -> int:

    window_sum = sum(nums[:k])

    count = 0

    if window_sum ==t:
        count +=1

    
    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right -k]
        if window_sum ==t:
            count +=1

    return count

print(count_subarrays_with_sum(nums = [1, 2, 3, 1, 2],
k = 2,
t = 3))

print(count_subarrays_with_sum([1, 1, 1, 1], k=2, t=2))  # → 3
print(count_subarrays_with_sum([0, 0, 0], k=2, t=0))     # → 2

    


def min_subarray_len(target: int, nums: List[int]) -> int:
    left = 0
    
    window_sum = 0
    min_len = float('inf')


    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            
            min_len = min(min_len, right - left +1)
            window_sum -= nums[left]
            left +=1
        
    if min_len == float('inf'):
        return 0
    
    return min_len


print(min_subarray_len(nums = [2, 3, 1, 2, 4, 3],
target = 7))



def min_subarray_sum_at_least_target(nums: List[int], target: int) -> int:
    left = 0
    window_sum = 0

    min_len = float("inf")

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            min_len = min(min_len, right - left +1)
            window_sum -= nums[left]
            left+= 1
            
        
    if min_len == float('inf'):
            return 0
        
    return min_len

print(min_subarray_sum_at_least_target(nums = [1, 4, 4],
target = 7))


def max_length_subarray_sum_leq_target(nums: List[int], target: int) -> int:
    left = 0
    window_sum = 0
    max_len =0


    for right in range(len(nums)):
        window_sum += nums[right]
    
    while window_sum > target:
        window_sum -= nums[left]
        left += 1

    
    max_len = max(max_len, right - left + 1)


    return max_len

        

print(max_length_subarray_sum_leq_target(nums = [2, 3, 5, 6],
target = 4))
   
def max_sum_subarray_fixed_k(nums: List[int], k: int) -> int:
    max_sum = sum(nums[:k])

    window_sum = max_sum

    for right in range(k,len(nums)):
        window_sum += nums[right] - nums[right -k]
        max_sum = max(max_sum, window_sum)

    return max_sum

print(max_sum_subarray_fixed_k(nums = [5, 2, -1, 0, 3],
k = 3))


def min_subarray_len(target: int, nums: List[int]) -> int:
    min_len = float("inf")
    left = 0
    window_sum = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            window_sum -= nums[left]
            min_len = min(min_len, right - left +1)
            left +=1

    if min_len == float("inf"):
        return 0
    
    return min_len




print(min_subarray_len(nums = [2, 3, 1, 2, 4, 3],
target = 7
))




def longestOnes(nums: List[int], k: int) -> int:
    left = 0
    max_num = 0
    zero_count = 0
    max_len = 0
   


    for right in range(len(nums)):
      
        if nums[right] == 0:
            zero_count += 1
     

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)

            

    return max_len

print(longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))





def maxFrequency(nums: List[int], k: int) -> int:
    sorted_nums = nums.sort()
    left =0
    window_sum = 0
    max_len =0
    moved = 0



    for right in range(len(sorted_nums)):
        window_sum += nums[right]

        while window_sum < k:
       #     if wi
            window_sum -= nums[right]

        left +=1

        max_len = max(max_len, right -left +1)


#print(maxFrequency(nums = [1,2,4], k = 5))

def firstUniqChar(s: str) -> int:
    left = 0
    not_unique = {}
    unique = {}
    index = 0
    unique_counter = 0
    count ={}


    for char in s:
        count[char] = count.get(char,0) +1
    for i in range(len(s)):
        if count[s[i]] == 1:
            print(i)
            return i


           
            
       
            

    return -1



print(firstUniqChar(s="leetcode"))



def isAnagram(s: str, t: str) -> bool:

    anaGram = {}
    


    for char in s:
        anaGram[char] = anaGram.get(char, 0) +1
    for charTwo in t:
        anaGram[charTwo] = anaGram.get(charTwo, 0) -1
    for j in  anaGram:
        if anaGram[j] !=0:
         return False
    

    return True
        

            
            
        


print(isAnagram( s = "anagram", t = "nagaram"))


from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    new_anaGram = defaultdict(list)

    for char in strs:
        key = "".join(sorted(char))
        
        new_anaGram[key].append(char)
    return list(new_anaGram.values())
        




print(groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))

def frequencySort(s: str) -> str:
    count = {}
    index = 0
   


    for char in s:
        count[char] = count.get(char, 0) + 1
    sorted_items =sorted(count.items(), key=lambda x: x[1], reverse=True)

    result = ""
    for char, freq in sorted_items:
        result += char * freq   

        
                       
        
    
    
    

    return result

print(frequencySort(s = "tree"))