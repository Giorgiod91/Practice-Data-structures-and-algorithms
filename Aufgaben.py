

Liste = [5, 12, 7, 20, 3]

def bigger_then_10(List):
    bigger_it = {}
    bigger_then = 0
    for num in Liste:
        if num > 10:
            bigger_then +=1
            bigger_it["there are"] = bigger_then

    
    return bigger_it



print(bigger_then_10(List=[5, 12, 7, 20, 3]))


Liste2 =  [1, 2, 3, 4, 5]

def even_or_uneven(List):
    new_dict = {"even": [], "uneven": []}
    
    for num in List:
        if num % 2 == 0:
            new_dict["even"].append(num)
            
            
        else:
            new_dict["uneven"].append(num)
       
    
    return new_dict


print(even_or_uneven(List=Liste2))



def sum_und_durchschnitt(list):
    summe = 0
    leange = 0
    
    for zahl in list:
        summe = zahl + summe
        leange += 1
    durchschnitt = summe / leange
    return summe, durchschnitt


print(sum_und_durchschnitt(list= [5, 10, 20, 8]))







def klein_und_gross(Liste):
    gross = 0
    klein = 4
    for zahl in Liste:
        if zahl > gross:
            gross = zahl
        elif zahl < klein and zahl > 0:
            klein = zahl

    return gross, klein

print(klein_und_gross(Liste=[7, 3, 12, 9, 1, 15]))






#1. Zaehle, wie oft jeder Buchstabe im String "hallo welt" vorkommt (Gross-/Kleinschreibung beachten).




def how_often_in(Text):
    new_dict = {"solo": [], "more": []}
    index= 0
    num = 0
    counter = 0
   
    
    for i in Text:
        if Text.count(i) > 1:
            counter +=1
            new_dict["more"].append(i)
                    
        else:
            new_dict["solo"].append(i)
            counter +=1  
                     
     
            
        

    return new_dict

print(how_often_in(Text="hallo welt"))

#2. Zaehle, wie oft jedes Wort im Satz "Hallo Welt hallo" vorkommt (Gross-/Kleinschreibung ignorieren).


def how_many_word(Text):
    result_dict = {}
    words = Text.split()  
    
    for word in words:
        word = word.lower().strip(".,!?") 
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1
            
    return result_dict


print(how_many_word(Text="Hallo Welt hallo"))