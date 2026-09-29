#Week-7
#Lab-5-task-1(local vs global scope)
#Sampath lakshmi



counter = 0
def show_local():
    counter = 25
    print("Local counter:", counter)
show_local()
print("Global counter:", counter)


#output:
#Local counter: 25
#Global counter: 0
