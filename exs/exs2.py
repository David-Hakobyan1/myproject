import random
#1 ###################################################################
my_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
d={}
for key,value in my_dict.items():
    d[value]=len(value)
print(d)
######################################################################

#2 #######################################################################
my_dict={'v':11,'k':34,'l':3,'hj':5}
mymax = max(my_dict.keys(), key=(lambda k: my_dict[k]))
mymin = min(my_dict.keys(), key=(lambda k: my_dict[k]))
print("minimum = "+str(my_dict[mymin]),"maximum = "+str(my_dict[mymax]))
##########################################################################

#3 ############################
lis = [1,4,5,6,7,8,8,8,10]
s = random.randrange(len(lis))
print(lis[s])
###############################

#4 ###################################################
lis1 = ["red", "orange", "green", "blue", "white"]
lis2 = ["black", "yellow", "green", "blue"]
l=[]
l1=[]
for i in lis1:
    if i not in lis2:
        l.append(i)
for j in lis2:
    if j not in lis1:
        l1.append(j)
print(l,l1)
######################################################

#5 ####################################################

lis = ['Python', 3, 2, 4, 5, 'version']
l=[]
st=''
for i in lis:
    if type(i)==int:
        l.append(i)
ls = sorted(l)
print("minimum = "+str(ls[0]),"maximum ="+str(ls[-1]))
#######################################################

#6 #################################
my_list = [1, 1, 3, 4, 4, 5, 6, 7]
l=[]
for i in range(1,len(my_list)):
    m=my_list[i-1]
    l.append(my_list[i]-m)
print(l)
####################################

#7 ########################################################
my_list = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
if len(my_list) > len(set(my_list)):
    print(False)
else:
    print(True)
###########################################################
