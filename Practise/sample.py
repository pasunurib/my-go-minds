print("======================")
print("Grade System in Python")
print("======================")
Mar=int(input("Enter the marks: "))
print("----------------------")
if Mar>=90:
    print("Marks:",Mar,"Grade : A")
elif Mar>=80 and Mar<90:
    print("Marks:",Mar,"Grade : B")
elif Mar>60 and Mar<80:
    print("Marks :",Mar,"Grade: C")
elif Mar>50 and Mar<60:
    print("Marks:",Mar,"Grade : D")
else:
    print("Marks:",Mar,"Fail")
