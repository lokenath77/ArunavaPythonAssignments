user_writing = []
while True:
    line = input('enter :')
    if not line.strip(): #if line is blank
        break
    else:
        user_writing.append(line)

user_writing = '\n'.join(user_writing)
#user_writing = user_writing.upper()
#print(user_writing)
s= user_writing
print(s.upper())