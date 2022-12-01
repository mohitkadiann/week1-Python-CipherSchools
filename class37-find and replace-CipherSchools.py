# replace() method
string= "Mohit kadian is a student of LPU"
print(string.replace("is","was",1))

# find() method
print(string.find("is",1))
is_pos1= string.find("is")
is_pos2= string.find("is", is_pos1+1)
print(is_pos2)