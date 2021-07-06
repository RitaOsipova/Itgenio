##### -=[ while ]=- #######################$#########################
#####################################################################
# 1.
# a = ()
# while a != 0:
#     a = int(input())

##################################################################
# 2.
# a = ()
# while True:
#     a = str(input())
#     if 'stop' in a:
#         break
##################################################################
# 3.
# a = 0
# b = ()
# while True:
#     b = str(input())
#     a += 1
#     if 'danke' in b:
#         break
# print(a)
##################################################################
# 4.
# a = 0
# c = 0
# while True:
#     T = float(input('Temperatur: '))
#     a += 1
#     print(f'Heute ist der {a}. Tag, und es ist {T} Grad. ')
#     print(f'Du hast mir {a} mal das Temperatur gegeben')
#     if T == 22:
#         break
#     if a % 7 == 0:
#         c += 1
#         2print(f'Es sind {c} wochen vergangen.')
##################################################################
# 5.
# a = 0
# d = 0
# b = float(input())
# while True:
#     d = d + b
#     b = float(input())
#     a += 1
#     if b == 0:
#         break
# print(a)
# print(d)
# print(d / a)
##################################################################
# 6.
# summe = 0
# while True:
#     price = float(input())
#     if price >= 1500:
#         skidka = price - (price * 0.08)
#         print(f'Ihre Rabatt ist 8% es sind {skidka} Euro')
#         summe = summe + skidka
#     else:
#         summe = summe + price
#     if price == -1:
#         summe += 1
#         break
# print(summe)

##################################################################
# 7.


##################################################################
# 8.password
# while True:
#     stop_wort1 = 'passwort'
#     stop_wort2 = '123'
#     passwort1 = input('Bitte gib ein passwort ein: ')
#     passwort2 = input('Bitte gib ein passwort ein: ')
#     if passwort1 == stop_wort1 or passwort1 == stop_wort2:
#         print('Simple, Bitte noch mal eingeben')
#     elif passwort1 != passwort2:
#         print('Differ')
#     else:
#         print('Same')
#         print('Ok!')
#         break


#################################################################
###############################################################
# print(' Hello World! ')

# 2.
# a = str(input())
# print(a)
# if 'Hello World' in a:
#     print('yes')
# else:
#     print('no')

# 3.
# name = input('Wie heist du? ')
# print(f'hallo {name}')

# 1.
# roky = str(input())
# cooky = str(input())
# loch = cooky.find(" ")
# wort1 = cooky[:loch]
# wort2 = cooky[loch + 1:]
# print(roky.replace(wort1,wort2))

# 2.
# a = int(input())
# print(len(str(a)))

# 3.
# fruher = str(input())
# A = fruher.find("a")
# B = fruher.find("b")
# if A < B:
#     print('A')
# elif B < A:
#     print('B')
# else:
#     print('Error')

# 4.
# string = str(input())
# print(string.replace("a","aY"))

# 5.
# a = str(input())
# print(a.title())

# 6.
# s = str(input())
# s = s.replace(" ","")
# t = (s[::-1])
# print(s[::-1])
# if s == t:
#     print('Ja')
# else:
#     print('Nein')

# 7.
#
# import random
# mylist1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
# ,'o','p','q','r','s','t',]
# mylist2 = ['1','2','3','4','5','6','7','8','9','0',]
# i = 0
# c = ''
# while i < 5:
#     a = random.choice(mylist1)
#     b = random.choice(mylist2)
#     c = c + a + b
#     i += 1
# print(c)


# 8.
# roky = str(input())
# loch = roky.find(" ")
# wort1 = roky[:loch]
# wort2 = roky[loch + 1:]
# print(wort1)
# print(wort2)
# coki = len(wort1)
# cooki = len(wort2)
# if coki > cooki:
#     print(wort1,wort2)
# elif cooki > coki:
#     print(wort2,wort1)


# 9.
# klammer = str(input())
# a = 0
# b = 0
# klammer1 = '('
# klammer2 = ')'
# while klammer1 in klammer:
#     a += 1
# while klammer2 in klammer:
#     b += 1
# if klammer1 == klammer2:
#     print('Jes')
# elif klammer1 != klammer2:
#     print('No')


# 10.
# liste = str(input())
# liste = liste.replace(",", "\n")
# print(liste)

############################################################

# 1.

# s = str(input())
# a = s[1::3]
# b = s[3::5]
# if a == b:
#     print('yes')
# elif a != b:
#     print('no')

# 2.

# string = str(input())
# zahler1 = len(string)
# zahler2 = '*' * zahler1
# print(zahler2 + string + zahler2)

# 3.
# s = str(input())
# s3 = s[2]
# slast = s[-1]
# s = s.replace(s[2],s[-1])
# print(s)
# s = s[:-1]+s3
# print(s)

# 4.

# s = str(input())
# zahler1 = s.count('+')
# zahler2 = s.count('-')
# print(f'Plus: {zahler1}')
# print(f'Minus: {zahler2}')

# 5.

# wort1 = 'Ritaosipova777'
# wort2 = 'Ritaosipova333'
# i = 0
# while True:
#     if wort1[i] == wort2[i]:
#         i += 1
#     else:
#          break
# print(f'In diesem Satz sind {i} buchstaben gleich.')

# 1.
# string = 'b22%2mZUk$hv3^b^3s85Q#'
#
# for symbol in string:
#     if symbol.isalpha():
#         print('1',end='')
#     elif symbol.isdigit():
#         print('2',end='')
#     else:
#         print('3',end='')

# 2.
# for i in range(16):
#     print(i, end=' ')
#
# for i in range(7,19):
#     print(i, end= ' ')
#
# for i in range(4, 34, 2):
#     print(i, end=' ')


# for i in range(7, -7, -2):
#     print(i, end=' ')

summe = 0
mal = 1
for i in range(1, 11):
    summe += i
    mal *= i
print(summe)
print(mal)

# this is a change i want to see at GitHub
# this is a commint made for PR
# test
