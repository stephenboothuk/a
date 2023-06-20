str1 = 'string built with single quotes'
str2 = "string built with double quotes"
str3 = '''string built with triple single quotes
that can span lines'''
str4 = """string built with triple double quotes
that can also span multiple lines"""
print('String 1 - ', str1, ' length', len(str1))
print('String 2 - ', str2)
print('String 3 - ', str3)
print('String 4 - ', str4)

#encoding
s = "This is üŋíc0de"
print('s is ', s)
print('type of s is ', type(s))
encoded_s = s.encode('utf8')
print('encoded_s is ', encoded_s, ' which is s changed to UTF8')
print('type of encoded-s is', type(encoded_s))
decoded_s = encoded_s.decode('utf8')
print('decoded_s is ', decoded_s)
print('type of decoded_s is ', type(decoded_s))

#Indexing and slicing
s1 = "The trouble is you think you have time"
print('full string is - ', s1)
print('first character (index 0) is - ', s1[0])
print('character at index 5 is - ', s1[5])
print('characters up to index 4 are - ', s1[:4])
print('characters from index 2 to index 14 are - ', s1[2:14])
print('every third character from index - ', s1[2:14:3])
print('will this reverse - ', s1[len(s1)::-1])
print('will this reverse - ', s1[::-1])
