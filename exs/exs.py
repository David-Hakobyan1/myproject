# Homework1 EXAMPLE1 #######################################################################
number = int(input("enter number from 1 to 9 : "))
my_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
res = sorted(my_dict,key=my_dict.get,reverse=True)[:number]
print(res)
# Homework1 EXAMPLE2 #######################################################################
number = int(input("enter number from 1 to 9 : "))
number = -number
x = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
sorted_x = sorted(x.items(), key=lambda kv: kv[1])
print(sorted_x[number:])
############################################################################################

# Homework2 #####################################################################################
name = raw_input("enter a word--- Math or Science : ")
mylist = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
res = [el[name] for el in mylist if name in el]
print(res)
#################################################################################################
