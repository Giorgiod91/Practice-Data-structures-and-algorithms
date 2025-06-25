

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
    