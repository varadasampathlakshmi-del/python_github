#Varada Sampath lakshmi
#Operators-Identity operator

list1=[1,2,3]
list2=[1,2,3]
list3=list1
print(list1==list2)
print(list1 is list2)
print(list1 is list3)
print(id(list1),id(list2),id(list3))

#output
#True
#False
#True
#1574502381312 1574502264768 1574502381312
