#Week-7
#Lab-2-task-4( Keyword varaiable-length)
#Sampath lakshmi

def build_profile(**details):
    print("----- PROFILE CARD -----")
    for key, value in details.items():
        print(key.title(), ":", value)
    print("------------------------")
build_profile(name="Hasini", age=20, city="Hyderabad", hobby="Reading")
print()
build_profile(name="Lasya", branch="CSE", college="GMRIT")
print()
build_profile(name="Keerthi", age=21, hobby="Painting")


#output:
#----- PROFILE CARD -----
#Name : Hasini
#Age : 20
#City : Hyderabad
#Hobby : Reading
#------------------------
#----- PROFILE CARD -----
#Name : Lasya
#Branch : CSE
#College : GMRIT
#------------------------
#----- PROFILE CARD -----
#Name : Keerthi
#Age : 21
#Hobby : Painting
#------------------------
