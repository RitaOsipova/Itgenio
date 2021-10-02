###########################################################
# 1.#######################################################

# mylist = ['144','146','150','152','154','156']
# x = int(input())
# for i in range(0, len(mylist)):
#     if x < int(mylist[i]):
#         print(i)
#         break
#     if i == 5:
#         print(i + 1)



# 2.#######################################################

# mylist = ['4','6','5','2','4','7','14','16','0','2','4','3']
# ans = 1
# if not mylist:
#     print("Empty")
# else:
#    for r in range(1, len(mylist), 2):
#         ans = ans * int(mylist[r])
# ans = ans * int(mylist[1])   
# print(ans)

# 3.#######################################################

# mylist = ['-4','+6','-6','+2','+4','-4','-14','+16','16','2','9','9']
# ans = 0
# for r in range(0, len(mylist)-1):
#     if mylist[r] == mylist[r + 1]:
#         ans += 1
# print(ans)

# 4.#######################################################

# mylist = ['-4','6','-6','2','4','-4','-14','16','16','-2','9','9']
# for g in range(0, len(mylist)-1):
#     if int(mylist[g]) < 0 and int(mylist[g + 1]) < 0:
#         print(mylist[g],mylist[g + 1])
#     elif int(mylist[g]) > 0 and int(mylist[g + 1]) > 0:
#         print(mylist[g],mylist[g + 1])

# 5.#######################################################

# mylist = ['4','5','6','2','4','18','14','16','26','2','9','8']
# ans = 0
# for i in range(2, len(mylist)-3):
#     if int(mylist[i]) > int(mylist[i + 1]) and int(mylist[i]) > int(mylist[i + 2]) and int(mylist[i]) > int(mylist[i - 1]) and int(mylist[i]) > int(mylist[i - 2]):
#         ans += 1
# print(ans)

# 6.#######################################################

# mylist = ['1','8','6','4','5','4','14','16','16','8','9','36']
# paar = []
# ans = []
# flag = 0
# for i in range(0, len(mylist)):
#     for r in range(0, len(mylist)):
#         if mylist[i] == mylist[r] and i != r:
#             paar.append(mylist[i])
#             flag = 1
#     if flag == 0:
#         ans.append(mylist[i])
#     flag = 0
# print(ans)

###########################################################
# 1.#######################################################

# mylist = [1,8,6,4,5,4,14,16,16,8,9,36]
# print(f'This is max {max(mylist)}')
# print(f'This is min {min(mylist)}')
# print(f'This is diff {max(mylist) - min(mylist)}')

# 2.#######################################################

# mylist = ['Osipova','Tolksdorf','Saca','Farbmacher']
# mylistsort = sorted(mylist)
# print(mylistsort)

# 3.#######################################################

# mylist = [1,8,6,4,5,2,16,16,8,9,3]
# mylistsort = sorted(mylist)
# for i in range(0, 3):
#     print(mylistsort[i])

# 3.#######################################################

# myline = 'pegwokfüosdsfhgvhglkloipoijjjjjjwefwerewrwerlpwr'
# ans = []
# mylistunsort = list(myline)
# print(mylistunsort)
# mylist = sorted(mylistunsort)
# print('---------------------------------')
# print(mylist)

# flag = 1
# for i in range(0, len(mylist)):
#     for r in range(0, len(mylist)):
#         if mylist[i] == mylist[r] and i != r:
#             flag += 1
#     ans.append(flag)
#     flag = 1
# print('---------------------------------')    
# print(ans)

# string = input('Введите строку: ').lower()
# x = max(string, key=string.count)
# print(x)


# 9.#######################################################

# mylist = [1,8,6,4,22,14,16,8,9]
# n = 5
# mylist.append(n)
# mylistsort = sorted(mylist)
# for a in range(0, len(mylistsort)):
#     if mylistsort[a] == n and mylistsort[a - 1] > mylistsort[a + 1]:
#         print(mylistsort[a + 1])
#     else:
#         if mylistsort[a] == n:
#             print(mylistsort[a - 1])

# 8.##########################################################

# mylistlong = ['Osipova','Tolksdorf','12','Farbmacher','Saca','51','83']
# mylistshort = ['Osipova','12','Farbmacher']
# mylist = mylistlong
# flag = 0
# for i in range(0, len(mylist)-1):
#     if mylist[i].isalpha() and mylist[i+1].isalpha():
#         print(mylist[i],mylist[i+1])
#         flag = 1
# if flag == 0:
#     print('zu wenig wörter')

# 10.#########################################################

# mystring = 'hallo ich heise rita und bin elf jahe alt'
# mylist = ['bin', 'elf']
# my = mystring.split()
# for i in range(0, len(mylist)-1):
#     if mylist[i] in my and mylist[i+1] in my and my.index(mylist[i]) < my.index(mylist[i+1]):
#         print('ja')
#     elif mylist[i] not in my and mylist[i+1] not in my:
#         print('keine gleichen')
#     else:
#         print('nein')

###########################################################
################## russische rullet #######################

import random

players = []
marbles = []
pnumber = 100
cplayer = 0
cmarble = ''
taken = 0

rules = 'Regeln'
for i in range(0, 6):
    marbles.append('green')
marbles[random.randint(0, 5)] = 'white'
while pnumber >= 4:
    pnumber = int(input())
for r in range(0, pnumber):
    players.append(str(input(f'whats your name #{r+1} : ')))
while taken < 6:
    print(f'player is {players[cplayer]}')
    input('press enter to continue ...')
    cmarble = random.choice(marbles)
    if cmarble == 'white':
        print(f'white ball, GAME OVER for {players[cplayer]}')
        break
    else:
        print(f'green ball for {players[cplayer]}')
        marbles.remove('green')
        taken += 1
        cplayer += 1
        if cplayer == pnumber:
            cplayer = 0
        print(f'next player is {players[cplayer]}\n')