
# for i in range(int(n) + 1):
#     m = m + i 
# print(m)



username = input('username ')
password = input('password ')
count = 0
while True:
    if count > 7:
        print('time over')
        break 
    if username == 'mindx' and password == 'mdp':
        print('welcome')
        break
    else:
        count = count + 1

    
    