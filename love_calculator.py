print("welcome to my love calculator\n")
print("do you wanna test your love ?")
name1 = input("what is your name?\n")
name2 = input("what  is your name?\n")
combined_string = name1+ name2
print(combined_string)
l_combined_string = combined_string.lower()
#print(l_combined_string)
t = l_combined_string.count("t")
r = l_combined_string.count("r")
u = l_combined_string.count("u")
e = l_combined_string.count("e")
true = t+r+u+e
print(true)
l = l_combined_string.count("l")
o = l_combined_string.count("o")
v = l_combined_string.count("v")
e = l_combined_string.count("e")
love = l+o+v+e
print(love)
truelove = int(str(true) + str(love))
print(truelove)
if truelove >= 10 & truelove <= 90:
    print("you are like coke and mentos")
elif truelove >= 40 & truelove <= 50:
    print("you are perfect together")
else: 
    print("you are ok")


#print(l_name1)