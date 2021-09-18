###########################################################
###########################################################
###########################################################

# 1 + 2####################################################
# star = '⭐️'
# for i in range(0, 6):
#     print(star, end=' ')
# print(end='\n') 
# for i in range(0, 21):
#     print(star, end=' ')
# print(end='\n')
# 3 #######################################################
# star = '⭐️'
# for i in range(0, 11):
#     print(end='\n')
#     for i in range(0, 11):
#         print(star, end=' ')
# 4 #######################################################
# star = '⭐️'
# for i in range(0, 11):
#     print(end='\n')
#     for i in range(0, 6):
#         print(star, end=' ') 
# 5 #######################################################     
# star = '⭐️'
# for i in range(0, 6):
#     print(end='\n')
#     for i in range(0, 21):
#         print(star, end=' ')       
# 6 #######################################################
# star = '0 1 2 3 4 5 6 7 8 9'
# for i in range(0, 11):
#     print(end='\n')
#     for i in range(0, 11):
#         print(i, end=' ')  
# 7 #######################################################
# for a in range(0, 11):
#      print(end='\n')
#      for i in range(0, 10):
#          print(a, end=' ') 
# 8 #######################################################
# for a in range(0, 11):
#      print(end='\n')
#      for i in range(0, a):
#          print(a, end=' ') 
# 9 #######################################################
# for a in range(9, -1, -1):
#      print(end='\n')
#      for i in range(0, a):
#          print(i, end=' ') 
# 10 ######################################################
# for a in range(9, -1, -1):
#     print(end='\n')
#     for k in range (0, 18-2*a):
#         print(' ', end=' ')
#     for i in range(0, a):
#         print(i, end=' ')
# 11 ######################################################
# for r in range(1,10):
#     for i in range(1, 10):
#         print(i*r,end='\t')
#     print(end='\n')
# 12 ######################################################
# num = 9
# for i in range(1, num+1):
#     for j in range(1, num-i+1):
#         print(end="  ")
#     for j in range(1, i):
#         print(j, end=" ")
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()
# 13 ######################################################
# num = 9
# for m in range(1, num+1):
#     for j in range(1, num-m+1):
#         print(end="  ")
#     for j in range(1, m):
#         print(j, end=" ")
#     for j in range(m, 0, -1):
#         print(j, end=" ")
#     print()
# for m in range(num, 1, -1):
#     for j in range(0, num-m+1):
#         print(end="  ")
#     for j in range(1, m):
#         print(j, end=" ")
#     print()   
# 14 ######################################################
# num = 9
# for m in range(1, num+1):
#     for j in range(1, num-m+1):
#         print(end="  ")
#     for j in range(1, m):
#         print(j, end=" ")
#     for j in range(m, 0, -1):
#         print(j, end=" ")
#     print()
# for m in range(num, 1, -1):
#     for j in range(0, num-m+1):
#         print(end="  ")
#     for j in range(1, m):
#         print(j, end=" ")
#     for j in range(m-1, 0, -1):
#         print(j, end=' ')
#     print()   

############################################################

#6.
# answer = 0
# gerade = 0
# ungerade = 0
# noll = 0

# for i in range(7):
#     number = int(input())
#     answer = answer + number
#     if number > 0:
#         gerade += 1
#     elif number < 0:
#         ungerade += 1
#     else:
#         noll += 1
# print(answer,gerade,ungerade,noll)

###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
##########################lists############################

#4.########################################################
# capitals = ['Berlin','London','Paris','Madrid','Rom']
# print(*capitals)

#4a.#######################################################
# capitals = ['Berlin','London','Paris','Madrid','Rom',]
# print(*capitals)
# stadt = str(input())
# if stadt in capitals:
#     print('ERROR')
# else:
#     capitals.append(stadt)
#     print(*capitals)

#4b.#######################################################

# capitals = ['Berlin','London','Paris','Madrid','Rom']
# print(*capitals)
# for element in capitals:
#     length = len(element)
#     if length < 4:
#         capitals.remove(element)
# print(*capitals)

#5.########################################################

# ans = 1

# x = str(input())
# xlist = x.split(' ')
# print(*xlist)
# for i in xlist:
#     ans = ans * int(i)
# print(ans)

#5c.#######################################################

# colors = ['rot','orange','gelb','grun','blau','lila','schwarz']
# for i in range(len(colors)):
#     print(f'{i + 1} - {colors[i]}')

#2.#######################################################

# rost = ['122','123','145','144','129','136','138','143']
# for i in range(0, len(rost)-1):
#     if rost[i] < rost[i+1]:
#         print(rost[i+1])

#3.########################################################

# menu = ['Salat','Pommes','Apfelsaft']
# konsonant = ['S','P']
# for element in menu:
#     if element[0] in konsonant:
#         print(element)

#5b.#######################################################

# namen = ['Anna','Sahra','Eva','Tim']
# vokal = ['A','E']
# for element in namen:
#     if element[0] in vokal:
#         print(element)
###########################################################
###########################################################
###########################################################

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
###########################################################
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

