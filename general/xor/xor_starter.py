from re import I


label = "label"
xor_value = 13

chars = [ord(i) for i in label]
xor_result = [elem ^ 13 for elem in chars]
string_result = [chr(i) for i in xor_result]

print(string_result)