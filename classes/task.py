s1 = int(input("Enter (Telugu) Subject Marks= "))
s2 = int(input("Enter (Hindi) Subject Marks= "))
s3 = int(input("Enter (English) Subject Marks= "))
s4 = int(input("Enter (Maths) Subject Marks= "))
s5 = int(input("Enter (Science) Subject Marks= "))
s6 = int(input("Enter (Social) Subject Marks= "))
Total = s1+s2+s3+s4+s5+s6
percentage = float(Total/600)*100
Percentage = round(percentage, 2)
# print(Percentage,"%")

if Percentage >= 90:
    Grade = "A1"
elif Percentage >= 80:
    Grade = "A2"
elif Percentage >= 50:
    Grade = "B2"
else:
    Grade = "F"

print("Total Marks : ", Total)
print("Percentage : ", Percentage, "%")
print("Grade : ", Grade)
