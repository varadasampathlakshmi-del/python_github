#Varada Sampath lakshmi
#logical operators

percentage=float(input("Enter the percentage: "))
attendance=float(input("Enter the attendance: "))
eligible =percentage>75 and attendance>90
print("Eligible for scholarship:",eligible)

#output
#Enter the percentage: 78.9
#Enter the attendance: 92.5
#Eligible for scholarship: True