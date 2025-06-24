def count_vowels(text):
    how_many = 0
    for char in text.lower():
        if char in "aeiou":
            how_many += 1
    return how_many

print(count_vowels("Hallo Welt")) 



def is_palindrom(word):
    word = word.lower() 
    return word == word[::-1]

print(is_palindrom("LagerregaL"))  


def find_min(numbers):
    smallest = numbers[0]
    for number in numbers:
        
        if number < smallest:
            smallest = number
    
    return smallest

print(find_min([5, 3, 8, 2, 9]))



def group_by_length(list):
    result_dict = {}
    
    for word in list:
         length = len(word)
         if length not in result_dict:
                result_dict[length] = [word]
         else:
                result_dict[length].append(word)

    return result_dict

print(group_by_length(["hi", "hello", "yo", "yes"]))




def is_valid_date(date):
    valide = False

    splted_word= date.split("-")
    if int(float(splted_word[0])) > 0 and  int(float(splted_word[0])) < 32:
         if int(float(splted_word[1])) > 0 and  int(float(splted_word[1])) < 13:
            if int(float(splted_word[2])) > 0 and  int(float(splted_word[1])) < 9999:
                valide = True

   
    
    return valide



print(is_valid_date("31-02-2024"))


def clean_list(items: list[str]) -> list[str]:
    duplicate = []
    sorted_list = []
    new_items = [item.lower() for item in items]
    for item in new_items:
        if item not in duplicate:
            duplicate.append(item)
            print(duplicate)
            sorted_list = duplicate.sort()
       
        

  
    

    return sorted_list
    


print(clean_list(["Banane", "Apfel", "Banane", "apfel", "Orange"]))




def word_length_counter(text: str) -> dict[int, int]:
    result_dict = {}
    
    for word in list:
         length = len(word)
         if length not in result_dict:
                result_dict[length] = [word]
         else:
                result_dict[length].append(word)

    return result_dict

print(group_by_length(["Hi there you cool dev"]))