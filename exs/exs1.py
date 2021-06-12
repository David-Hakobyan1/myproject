############################################################################################
my_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
lis = []
for i in range(len(my_list)):
    if i+1 < len(my_list) and (my_list[i] == my_list[i+1]) or (my_list[i] == my_list[i-1]):
        lis.append(my_list[i])

    elif i+1 == len(my_list) and my_list[-1] == my_list[-2]:
        lis.append(my_list[-1])
print(lis)
# OUTPUT [0, 0, 4, 4, 6, 6, 6, 4, 4] #######################################################


#####################################################################
my_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l=set(my_list)
print(list(l))
# OUTPUT [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #############################


#####################################################################
my_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
lis=[]
for i in range(len(my_list)):
    if i+1 < len(my_list):
        if my_list[i] != my_list[i+1] and my_list[i] != my_list[i-1]:
            lis.append(my_list[i])
    elif i+1 == len(my_list):
        if my_list[-1] != my_list[-2]:
            lis.append(my_list[-1])
print(lis)
# OUTPUT [1, 2, 3, 5, 7, 8, 9] ######################################


####################################################################
number = 3 #int(input('Number : '))
my_list = [1, 1, 2, 3, 4, 4, 5, 1]
print(my_list[:number-1]+my_list[number:])
# OUTPUT [1, 1, 3, 4, 4, 5, 1] #####################################


#######################################################################
def roman_to_decimal(roman_number,my_dict):
    rev = list(reversed(list(roman_number)))
    my_sum = 0
    sec_num = my_dict[rev[0]]
    for el in rev:
        fir_num = my_dict[el]
        if fir_num < sec_num:
            my_sum -= fir_num
        else:
            my_sum += fir_num
        sec_num = fir_num
    return my_sum
roman_number = 'XVII' #raw_input('Enter roman number : ')
my_dict ={'I': 1, 'V': 5,'X': 10, 'L': 50,'C': 100, 'D': 500,'M': 1000}
print(roman_to_decimal(roman_number,my_dict))
# OUTPUT 17 ###########################################################


#######################################################################
def decimal_to_roman(number,my_list):
    lis = []
    for my_sum,roman_number in my_list:
        while number >= my_sum:
            number -= my_sum
            lis.append(roman_number)
    return "".join(lis)

number = 26 #int(input('Enter number'))
my_list = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
           (100, 'C'),(90, 'XC'),  (50, 'L'), (40, 'XL'),
           (10, 'X'), (9, 'IX'),(5, 'V'), (4, 'IV'), (1, 'I')]
print(decimal_to_roman(number,my_list))
# OUTPUT XXVI #########################################################
