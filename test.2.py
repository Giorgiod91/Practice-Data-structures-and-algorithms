def how_many_word(text):
    result_dict = {}
    words = text.split()  
    
    for word in words:
        word = word.lower().strip(".,!?") 
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1
            
    return result_dict




def TemperaturDaten(temperatures):
    new_dict = {}
    durchschnitt = sum(temperatures) / len(temperatures)
    highest = 0
    index = 0
    tageueber = 0

    for temp in temperatures:
        if temp > 22:
            new_dict[index] = temp
            index += 1
            tageueber += 1

    new_dict["anzahl"] = tageueber

    
    for temp in temperatures:
        if temp > highest:
            highest = temp

   
    new_dict["max"] = highest
   

    return durchschnitt, new_dict

        
       



def most_frequent(list):
    new_dict = {}
    index= 0
    for item in list:
        
        if item not in new_dict:
            new_dict[index] = item
            index +=1


    for item in new_dict:
        print("lol")
       
    
    return new_dict

print(most_frequent(["a", "b", "a", "c", "a", "b"]))



