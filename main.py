#1.########################################################

# mylist = input() .split()
# print(mylist[0])
# print(mylist[round(len(mylist) / 2)])
# print(mylist[-1])

#2.########################################################

# mylist = input() .split()
# for i in range(0, len(mylist)):

#     if i % 2 == 0:
#         print(mylist[i])

#3.######################################################## 

# import random
# m = int(input())
# n = []
# for i in range(0, m):
#     a = random.randint(1, 10000)
#     n.append(a)
# print(n)

#4.########################################################

# mylist = input() .split()
# n = int(input())
# print(int(mylist[n]) ** n)

#5.########################################################

# mylist = input() .split()
# if len(mylist) == 0:
#     print('ERROR')
# summe = 0
# for i in range(0, len(mylist), 2):
#     summe = summe + int(mylist[i])
#     print(mylist[i])
# print(summe)
# print(summe * int(mylist[0]))

#6.########################################################

# erg = []
# mylist = input() .split()
# for i in range(0, len(mylist)-1):
#     if int(mylist[i]) > int(mylist[i + 1]):
#         erg.append('Yes')
#     else:
#         erg.append('No')
# if 'No' in erg:
#     print('No')
# else:
#     print('Yes')

#7.########################################################

# mylist = input() .split()
# erg = input() .split()
# for i in range(0, len(mylist)):
#     if mylist[i] in erg:
#         print(mylist[i])

#8.########################################################

#mylist = input() .split()
#ans = []
#for i in range(0, len(mylist)):
 

#9.########################################################

# mylist = ['1','8','6','4','12','1','22','15']
# n = 5
# m = []
# mylist.append(n)
# for a in range(0, len(mylist)):
#     if int(mylist[a] > mylist[a+1]):

#10.#######################################################

# mylist = input() .split()
# n = input() .split()
# if n in mylist:
#     print('Ja')
# else:
#     print('no')

###########################################################
#################### alchemie projekt #####################

#step.1.###################################################
# import random
# caldron = ['wasser','lavendel','schipozwet','kaktusmilch']
# i = 0
# flask = []
# for i in range(0, len(caldron)):
#     flask.append(caldron[i])
# flask = caldron
# flask.append(caldron)
# print(flask)
# while i < len(caldron):
#     if caldron[i] != 'wasser' and caldron[i] != 'kaktusmilch':
#         caldron.pop(i)
#     else:
#         i += 1
# i = 0
# print(caldron)
# caldron.append('nüsse')
# caldron.append('nüsse')
# for i in range(0, 74):
#     caldron.append('schischka')

# random.shuffle(caldron)
# print(caldron)
# flask2 = random.choice(caldron)
# print(flask2)

#1.########################################################

# flask3 = []
# flask3.append(flask)
# flask3.append(flask2)
# print(flask3)

#2.########################################################

# while i < len(caldron):
#     if caldron[i] == 'schischka':
#         caldron.pop(i)
#     else:
#         i += 1
#     if i == 32:
#         break
# print(caldron)

#3.########################################################

# for r in range(0, 3):
#     caldron.pop(r)
# print(caldron)

###########################################################
#1.########################################################

# null = []
# for r in range(100):
#     null.append(0)
# print(null)
# null.insert(0, '1')
# null.insert(-1, '1')

###########################################################
###########################################################
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

mylist = ['1','8','6','4','5','4','14','16','16','8','9','36']
ans = []
for i in range(0, len(mylist)-1):
    for r in range(i + 1, len(mylist)):
        if mylist[i] == mylist[r]:
            ans.append(mylist[i])
print(ans)
print(mylist)