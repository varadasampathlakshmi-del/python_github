#Week-7
#Lab-5-task-3(unboundlocalerror demonstration)
#Sampath lakshmi


counter = 0
def wrong_increment():
    try:
        counter += 1
    except UnboundLocalError as e:
        print("Error:", e)
wrong_increment()
def correct_increment():
    global counter
    counter += 1
correct_increment()
print("Counter after fixing:", counter)


#output:
#Error: cannot access local variable 'counter' where it is not associated with a value
#ssCounter after fixing: 1
