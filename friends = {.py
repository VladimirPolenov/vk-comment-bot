# task with polindrom number
polindrom = '1000001' #put polindrom number
nopolindrom = '102000001' #put not polindrom number for test


def polindrom_chek (number):
    number = str (number)
    number_massive = list (number) #read number as is sum of symbols 
    total = range(len(number_massive)) #variable equal quantity of symbols
    answer  = True
    for i in total: # cycle 
        if not number_massive [i] == number_massive [-i-1]:
            answer = False
    return print (answer)            




polindrom_chek (1300000031)