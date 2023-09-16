str1 = "once upon a time a princess"
str2 = ""
while str1.find(" ") != -1:
    i = str1.find(" ")
    str2 = str1[0:i]
    str1 = str1[(i+1):]
    print(str2[0],str2)
print(str1[0],str1)
