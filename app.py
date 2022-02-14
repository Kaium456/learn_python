# Python Boolean value
isProgrammer = True  # python is case sensecativ language
print(isProgrammer)

names = "Kaium"
print(names)
print(len(names))
print(names[4])
print(names[0])
print(names[-1])
print(names[0:4])
print(names[0:])
print(names[:4])

# Escap Secquen
#  \"
# \'
# \n

course = "Python \"Programming "
course2 = "Python \'Programming "
course3 = "Python \n Programming \n Language"
course4 = "Python \\ Programming Language"
print(course)
print(course2)
print(course3)
print(course4)

# Formated String

first = "Kaium"
last = "Islam"
full = first + ' ' + last
full = f"{first}  {last}"
print(full)


# String Methods
myName = "   md kaium islam"
print(myName.capitalize())
print(myName.upper())
print(myName.lower())
print(myName.title())
print(myName.strip())
print(myName.rstrip())
print(myName.find("ka"))
print(myName.replace("md", "mr"))
print('md' in myName)
print("riya" not in myName)
