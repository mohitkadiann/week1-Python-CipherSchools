# strings are immutable
# immutable means which can not be changed at the original location
string = "string"
new_string = string.replace('t','T')#does not change in the original string the change is at temporary location
print(new_string)