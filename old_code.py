# name = input("Wie heist du? ")
# alter = input("Wie alt bist du? ")
# gewicht = input("Wie schwer bist du? ")
# print(f'Hallo {name}!Ich kenne dich du bist {alter} Jahre alt und {gewicht} kilo schwer.')

# wort = 'hallo'
# print(wort)
# print(wort)

# abc = input('wort')

# print(abc,abc,abc,abc,sep=' ')

# wort1 = input('wort ')
# wort2 = input('wort ')
# wort3 = input('wort ')

# print(wort1,wort2,wort3,sep='\n')

# name = input('Film? ')
# kino = input('Wo? ')
# zeit = input('Uhr? ')

# print(f'Hallo.Die Tikets zu dem Film {name} wurde in Kino {kino} um {zeit} reserviert.')

# name = input('name ')
# geburtstag = input('geburtstag ')
# monat = input('geburtsmonat ')
# jahr = input('geburtsjahr ')
# username = input('username ')

# print(f'name: {name}\n{geburtstag}.{monat}.{jahr}')
# print(username,end='@web.de')

# number1 = float(input('kommazahl '))
# number2 = int(input('ganze zahl '))

# print(number1 + number2)

# first = int(input('gib mir first'))
# second = float(input('gib mir second'))

# print(round(second / first,3))
# print(second % first)
# print(second ** first)

# ubung 1
# barb = int(input('Was ist 4*(8-6) / 2 ?  ' ))
# # 4
# print(f'Du hast mir {barb} gegeben')
# print('Das richtige Ergebnis ist 4')

# ubung2
# lisa = int(input('Gib mir eine Zahl '))
# result = lisa % 10

# print(result)

# ubung3

# a = int(input('Gib mir eine Zahl '))
# b = float(input('Gib mir eine Zahl '))

# zahl1 = a + b
# zahl2 = a - b
# zahl3 = a * b
# zahl4 = a / b
# zahl5 = a // b
# zahl6 = a ^ b

# print(f'{zahl1}|{zahl2}|{zahl3}|{zahl4}|{zahl5}|{zahl6}')

# Aufgabe 4
# a = int(input('Gib a: '))
# b = int(input('Gib b: '))
# c = int(input('Gib c: '))
# a1 = a + b
# b1 = c - a
# c1 = a + b + c
# print(a,b,c)
# # c = a + b + c
# # b = c - a
# # a = a + b
# a = a1
# b = b1
# c = c1
# print(a,b,c)

# Aufgabe 5
# a = int(input('Gib a '))
# b = int(input('Gib b '))
#
# c = (a + 4 * b) * (a - 3 * b) + a ^ 2
# print(c)

# print('Hello Rita!'

# HA : A - B
#
# a = int(input('Gib mir die km '))
# # 24
# b = int(input('Gib mir die min '))
# # 3
#
# c = a * 1000
# # 24000
# d = b * 60
# # 180
#
# print(f'{c} m/{d} s')

# # HA : mars
# #
# alter = int(input("Wie alt bist du? "))
# m = (365 * alter) // 687
#
# print(f'In Marsjahren bist du {m} jahre alt.')

# HA 3
# a = int(input('gib mir eine Zahl '))
#
# print(a % 2)

# mport
# random
# print(random.randint(1, 10))

# import random
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = random.shuffle(a)
# print(b)
# print(a)

#  ubung A,B,C

# import random
# a = random.randint(1, 10)
# b = random.randint(10, 50)
# c = random.randint(a, b)
# print(a,b,c)


# import turtle
# t = turtle.Pen()
#
# t.width(10)
# t.color('pink')
#
# t.begin_fill()
# t.left(90)
# t.forward(150)
# t.right(90)
# t.forward(250)
# t.right(90)
# t.forward(150)
# t.right(90)
# t.forward(250)
# t.end_fill()
#
# t.color('grey')
# t.begin_fill()
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.end_fill()
#
# t.color('black')
# t.up()
# t.forward(45)
# t.down()
# t.forward(10)
# t.up()
# t.forward(95)
# t.down()
#
# t.color('red')
# t.begin_fill()
# t.right(45)
# t.forward(176)
# t.right(90)
# t.forward(176)
# t.end_fill()
#
# t.color('grey')
# t.up()
# t.right(45)
# t.forward(50)
# t.right(90)
# t.forward(25)
# t.down()
#
# t.forward(50)
# t.left(90)
#
# t.forward(50)
# t.left(90)
#
# t.forward(50)
# t.left(90)
#
# t.forward(50)
# t.left(90)
#
# t.forward(25)
# t.left(90)
# t.forward(50)
# t.right(90)
# t.forward(25)
# t.right(90)
# t.forward(25)
# t.right(90)
# t.forward(50)
#
#
# t.color('brown')
#
# t.right(180)
# t.up()
# t.forward(300)
# t.down()
#
# t.begin_fill()
# t.left(90)
# t.forward(75)
# t.right(90)
# t.forward(24)
# t.right(90)
# t.forward(75)
# t.right(90)
# t.forward(12)
# t.end_fill()
#
# t.color('green')
# t.begin_fill()
# t.circle(50)
# t.end_fill()
#
# t.color('yellow')
# t.up()
# t.left(90)
# t.forward(175)
# t.down()
# t.begin_fill()
# t.circle(25)
# t.end_fill()
#
# t.right(90)
# t.forward(25)
# t.right(180)
# t.forward(100)
# t.backward(50)
#
# t.right(90)
# t.forward(50)
# t.right(180)
# t.forward(100)
# t.backward(50)
#
# t.right(45)
# t.forward(50)
# t.right(180)
# t.forward(100)
# t.backward(50)
#
# t.right(90)
# t.forward(50)
# t.right(180)
# t.forward(100)
# t.backward(50)


# x = int(input())
# if x == 0:
#     print('null')
# if x > 0:
#     print('positiv')
# if x < 0:
#     print('negativ')
# if x != 0:
#     print('keine null')

# a = 0
# if a == 0:
#     print("yes")
# elif a >= 0:
#     print("+")
# else:
#     print("-")

# a = int(input())
# b = 10
# if a % 2 == 0:
#     print(b * 2)
# else:
#     print(b / 2)
#
# b = b * 2 if a % 2 == 0 else b / 2
# print(b)

# a = 15
# if a % 2 == 0 and a % 3 == 0 and a % 5 == 0:
#     print('2,3,5')
# elif a % 2 == 0 and a % 3 == 0:
#     print('2,3')
# elif not (a % 2 == 0 and a % 3 == 0 and a % 5 == 0):
#     print('0')

# Aufgabe 1.

# a = str(input())
# if a == 'python':
#     print('Yes')
# else:
#     print('No')

# 2.

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == 1 and b == 2 and c == 3:
#     print('start')
# else:
#     print('stop')

# 3

# a = str(input())
# if 'gold' in a:
#     print('Ja')
# else:
#     print('Nein')
# 4.

# a = float(input())
# b = str(input())
#
# if 'zentimeter' in b:
#     print(a * 100)
# elif 'kilometer' in b:
#     print(a / 1000)
# else:
#     print(a)

# 5
# a = str(input())
# nr1 = 'Das ist ja toll!'
# nr2 = 'Das ist ja schade!'
# nr3 = 'Entschuldigung, ich habe dich leider nicht verstanden.'
#
# if 'gut' in a:
#     print(nr1)
# elif 'schlecht' in a:
#     print(nr2)
# else:
#     print(nr3)


# 6

# a = float(input())
#
# if a == 0:
#     print('0')
# if a < 0:
#     print('-')
# if a > 0:
#     print('+')
# 7

# a = int(input())
#
# if a % 2 == 0:
#     print('gerade')
# else:
#      print('ungerade')

# 8

# a = float(input())
# b = float(input())
# c = str(input())
#
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == '/':
#     print(a / b)
# else:
#     print('error')









#1.
# import random
# a = ''
# while a != 'ja':
#     print(random.randint(1, 9))
#     a = input('Ist das deine lieblings Zahl?')



# from random import randint as rn
# print('Glückspelmen')
# pelmen_zahl = 10
# while pelmen_zahl <= 10:
#     versuch = (rn(1,10))
#     print(f'Ich nehme pelmen nummer {versuch}.')
#     if versuch % 5 == 0:
#         print('Ich habe den Glückspelmen gefunden!!!')
#         break
#     else:
#         print('Ich habe ihn nicht gefunden.')


############################################
#### Wurfel spiel ####

# from random import randint as rn
# a = 0
# antwort = int(input('Spielen wir? '))
# while antwort != 0:
#     versuch1 = (rn(1,20))
#     versuch2 = (rn(1,20))
#     versuch3 = (rn(1,20))
#     if antwort == 1:
#         print(f'Erster zug: {versuch1}')
#         print(f'Zweiter zug: {versuch2}')
#     elif antwort != 1 and antwort != 0 and antwort != 2 and antwort != 3:
#         print('Versuchen sie es noch einmal.')
#     elif antwort == 2:
#         print(f'Erster zug: {versuch1}')
#         print(f'Zweiter zug: {versuch2}')
#         print(f'Dritter zug: {versuch3}')
#     elif antwort == 3:
#         while a != 100:
#             versuch4 = (rn(1,20))
#             a += 1
#             print(versuch4,a)
#     antwort = int(input('Spielen wir? '))

############################################
#### spiel ####

# from random import randint as rn
# a = 0
# b = 3
# print('Errate die ausgedachte zahl mit den wenigst moglichen versuchen.')
# from_num = int(input('Von: '))
# to_num = int(input('Bis: '))
# secret = (rn(from_num,to_num))
# while a <= 3:
#     guess = int(input('Ihre vermutungen: '))
#     if guess < secret:
#         print('Meine zahl ist groser.')
#         a += 1
#         b -= 1
#         print(f'Du hast noch {b} fehler')
#     elif guess > secret:
#         print('Meine zahl ist kleiner.')
#         a += 1
#         b -= 1
#         print(f'Du hast noch {b} fehler')
#     elif guess == secret:
#         print('Super!')
#         a += 1
#         b -= 1
#         print(f'Super,sie haben es mit {a} fehlern geschaft.')
#         print(f'Sie haben die zahl in {a} vermutungen gelost.')
#         break


############################################
#### nr. 1 ####

# x = int(input())
# while x != 0:
#     print(x ** 3)
#     x = int(input())

#### nr. 2 ####

# a = int(input())
# b = int(input())
# while True:
#     c = b - a
#     print(c)
#     break

#### nr. 3 ####

# a = int(input())
# b = 0
# while a != 1:
#     a /= 3
#     b += 1
#     if a == 1:
#         print('Ja')
#         print(f'Potenz :{b}')

#### nr. 5 ####

# z1 = 1
# z2 = 0
# while z1 != 0:
#     if (z1 % 3 == 0) and (z1 % 10 == 8):
#         print('Ja')
#         z2 = z2 + z1
#         print(z1, z2)
#     z1 = int(input())
# print(z2)


#### nr. 4 ####

# a = int(input())
# while a > 0:
#     b = int(input())
#     if a != b:
#         break

# name = '''Rita'''
# print(f'Hallo ich heise {name}')
# greeting = '''Ich lerne Pyhton \nIch habe schon viele themen gelernt
# aber jetzt lerne ich strings.'''
# print(greeting)

# s = '''Python '''
# s1 = s * 7
# s2 = s + s1
# print(s,s1,s2)

# string = str(input())
# first = (string[0])
# last = (string[-1])
# print(f'{first}|{last}')

# string = str(input())
# first = (string[0])
# last = (string[-1])
# new_string = (f'{last} -> {first}')
# print(new_string)

# string = str(input())
# new_sting = (string [::-1])
# print(new_sting)


# a = str(input())
# b = (a[])
#

# wort= 'rita pavel marina'
# loch1 = wort.find(" ")
# print(loch1)
# wort1 = wort[:loch1]
# print(wort1)
# print(wort1.count("a"))
# loch2 = wort.find(" ", loch1 + 1, -1)
# wort2 = wort[loch1 + 1:loch2]
# wort2 = wort2.replace("a", "A")
# print(wort2)
# wort3 = wort[loch2:-1]
# print(len(wort3))
# wort


# a = str(input())
# if 'hoch' in a:
#     print(a.upper())
# if 'runter' in a:
#     print(a.lower())

# passwort = str(input())
# if passwort.isalnum() == True and passwort.isspace() == False:
#     print('True')
# else:
#     print(False)

# wort = str(input())
# if wort.startswith('hallo') == True:
#     print('Hallo')
# if wort.endswith('tschuss') == True:
#     print('Tschuss')


# name = input("Wie heist du? ")
# alter = input("Wie alt bist du? ")
# gewicht = input("Wie schwer bist du? ")

# print(f'Hallo {name}!Ich kenne dich du bist {alter} Jahre alt und {gewicht} kilo schwer.') 

# wort = 'hallo'
# print(wort)
# print(wort)

# abc = input('wort ')

# print(abc,abc,abc,abc,sep=' ')

# wort1 = input('wort ')
# wort2 = input('wort ')
# wort3 = input('wort ')

# print(wort1,wort2,wort3,sep='\n')

# name = input('Film? ')
# kino = input('Wo? ')
# zeit = input('Uhr? ')

# print(f'Hallo.Die Tikets zu dem Film {name} wurde in Kino {kino} um {zeit} reserviert.')

# name = input('name ')
# geburtstag = input('geburtstag ')
# monat = input('geburtsmonat ')
# jahr = input('geburtsjahr ')
# username = input('username ')

# print(f'name: {name}\n{geburtstag}.{monat}.{jahr}')
# print(username,end='@web.de')

# number1 = float(input('kommazahl '))
# number2 = int(input('ganze zahl '))

# print(number1 + number2)

# first = int(input('gib mir first'))
# second = float(input('gib mir second')) 

# print(round(second / first,3))
# print(second % first)
# print(second ** first)

# ubung 1
# barb = int(input('Was ist 4*(8-6) / 2 ?  ' ))
# # 4
# print(f'Du hast mir {barb} gegeben')
# print('Das richtige Ergebnis ist 4')

# ubung2
# lisa = int(input('Gib mir eine Zahl '))
# result = lisa % 10 

# print(result)

# ubung3

# a = int(input('Gib mir eine Zahl '))
# b = float(input('Gib mir eine Zahl '))

# zahl1 = a + b
# zahl2 = a - b
# zahl3 = a * b
# zahl4 = a / b
# zahl5 = a // b 
# zahl6 = a ^ b

# print(f'{zahl1}|{zahl2}|{zahl3}|{zahl4}|{zahl5}|{zahl6}')

# # aufgabe4

# a = int(input('Gib a '))
# b = int(input('Gib b '))
# c = int(input('Gib c '))
# a1 = a + b
# b1 = c - a
# c1 = a + b + c
# print(a,b,c)
# # c = a + b + c
# # b = c - a
# # a = a + b
# a = a1
# b = b1
# c = c1
# print(a,b,c)

# ubung5
# a = int(input('Gib a '))
# b = int(input('Gib b '))

# c = (a + 4 * b) * (a - 3 * b) + a ^ 2
# print(c)


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
#################################################################
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

###########################################################
# 1.

# s = str(input())
# a = s[1::3]
# b = s[3::5]
# if a == b:
#     print('yes')
# elif a != b:
#     print('no')

###########################################################
# 2.

# string = str(input())
# zahler1 = len(string)
# zahler2 = '*' * zahler1
# print(zahler2 + string + zahler2)

###########################################################
# 3.
# s = str(input())
# s3 = s[2]
# slast = s[-1]
# s = s.replace(s[2],s[-1])
# print(s)
# s = s[:-1]+s3
# print(s)

###########################################################
# 4.

# s = str(input())
# zahler1 = s.count('+')
# zahler2 = s.count('-')
# print(f'Plus: {zahler1}')
# print(f'Minus: {zahler2}')

###########################################################
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

###########################################################
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

###########################################################
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

# summe = 0
# mal = 1
# for i in range(1, 11):
#     summe += i
#     mal *= i
# print(summe)
# print(mal)
###########################################################

###########################################################
# 4 a

# a = 'rot'
# b = 'orange'
# c = 'gelb'
# d = 'grun'
# e = 'hellblau'
# f = 'blau'
# g = 'lila'
# for i in a, b, c, c, d, e, f, g:
#     print(i)

###########################################################
# 4 b

# zahl = ()
# while True:
#     zahl = int(input())
#     if zahl == 0:
#         break

###########################################################
# 4c

# for i in range(0, 51, 2):
#     print(i)

###########################################################
# 4d

# z = 1
# for i in range(100, -100, -1):
#     if i % 3 == 0:
#         z = i / 3
#         print(i,z, sep=' / 3 = ')

###########################################################
# 5a

# while True:
#     zeile = str(input())
#     if zeile == 'a':
#         break
#     zeile = str(input())

###########################################################
# 5b
 
# zeile = 'qwertyuiopsdfghjkl->a<-zxcvbnm'
# a = zeile.rfind("a")
# wort1 = zeile[:a]
# print(wort1)

###########################################################
# 1

# satz = str(input())
# zahl = int(input())
# for i in range (zahl):
#     print(satz)

###########################################################
# 2

# zahl = int(input())
# zahl += 1
# for i in range(0, zahl):
#      print(i, end=' ')

###########################################################
# 3

# string = str(input())
# for symbol in string:
#      print(symbol)

###########################################################
# 4

# result = 1
# for i in range(1, 7):
#     zahl = int(input())
#     if zahl != 0 :
#         result = result * zahl
# print(result)

###########################################################
# 5

# zahl = int(input())
# zahler = 0
# for i in range(1, zahl + 1): 
#     if zahl % i == 0:
#         print(i, end=' ')
#         zahler += 1
# if zahler == 2:
#     print('JA')
# else:
#     print('NEIN')

###########################################################
# 7

# zahl = int(input())
# zahler = 1
# for i in range(1, zahl + 1):
#     for a in range(1, zahl + 1):
#         erg = i * a
#         print(f'{i} * {a} = {erg}')
###########################################################
# 8

# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

###########################################################

# 1.
# i = str(input())
# end = i.find(-1)
# for i in range(1,end , 3):
#     print(i, end=' ')

###########################################################
# nr. 2
# string = str(input())
# zahl = int(input())
# print(string * zahl)

###########################################################
# 3.

# a = int(input())
# if a >= 12:
#     zeit = a - 12
#     if zeit >= 12:
#         print(f'In Amerika ist es gerade {zeit} Uhr nachmittags')
#     if zeit <= 12:
#        print(f'In Amerika ist es gerade {zeit} Uhr vormittags') 

###########################################################
# 4

# string = str(input())
# for i in string:
#     if string.count(i) == 1:
#         print(i, end='')

###########################################################
# nr. 5

# string = 'hbrygu654unt8tng89gjt'
# zahler = '0'
# while True:
#     print(string.replace(zahler, ''))
#     zahler = zahler + '1'
#     if zahler == 9:
#         break
###########################################################
###########################################################
###########################################################
#########################turtle############################


#import turtle
# t = turtle.Pen()
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.left(90)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.left(90)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.left(90)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# t.down()
# t.forward(10)
# t.up()
# t.forward(10)
# a = input()

# #treppen
# t.left(90)
# t.forward(10)
# t.right(90)
# t.forward(30)
# t.left(90)
# t.forward(10)
# t.right(90)
# t.forward(15)
# t.forward(15)
# t.left(90)
# t.forward(10)
# t.right(90)
# t.forward(15)
# t.forward(15)
# t.left(90)
# t.forward(10)
# t.right(90)
# t.forward(15)
# t.forward(15)
# t.left(90)
# t.forward(10)
# t.right(90)
# t.forward(15)
# t.forward(15)
# t.left(90)
# t.forward(10)
# t.right(90)
# t.forward(15)
# t.forward(15)
# t.left(90)
# t.forward(10)
# t.right(90)
# t.forward(15)
# t.forward(15)
# t.left(90)
# t.forward(10)
# t.right(90)
# t.forward(15)
# t.forward(15)
# t.left(90)
# t.forward(10)
# t.right(90)
# t.forward(15)
# t.forward(15)
# t.left(90)
# t.forward(10)
# t.right(90)
# t.forward(15)
# a = input()


# labyrinth
# t.forward(100)
# t.left(90)
# t.forward(95)
# t.left(90)
# t.forward(90)
# t.left(90)
# t.forward(85)
# t.left(90)
# t.forward(80)
# t.left(90)
# t.forward(75)
# t.left(90)
# t.forward(70)
# t.left(90)
# t.forward(65)
# t.left(90)
# t.forward(60)
# t.left(90)
# t.forward(55)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(45)
# t.left(90)
# t.forward(40)
# t.left(90)
# t.forward(35)
# t.left(90)
# t.forward(30)
# t.left(90)
# t.forward(25)
# t.left(90)
# t.forward(20)
# t.left(90)
# t.forward(15)
# t.left(90)
# t.forward(10)
# t.left(90)
# t.forward(5)
# t.left(90)
# a = input()

# t.forward(100)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(400)
# t.left(90)
# t.forward(200)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(200)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(150)
# t.left(90)
# t.forward(300)
# t.right(90)
# t.forward(50)
# t.left(45)
# t.forward(80)
# t.left(98)
# t.forward(80)
# t.up()
# t.goto(100,150)
# t.down()
# t.right(180)
# t.forward(215)
# t.right(95)
# t.forward(230)
# t.goto(400,200)
# t.left(90)
# t.forward(75)
# t.right(95)
# t.forward(85)
# a = input()


###########################################################
###########################################################
###########################################################

# 1).
# string = '4###5abn^RrRy%5^aaAn9@444GCdDD%M'
# length = len(string)
# counter = 0
# for i in range(length-1):
#     string = string.lower()
#     if string[i] == string[i + 1] == string[i + 2]:
#         counter += 1
# print(f'Es gibt {counter} gleiche paare')

# 2).
# string = 'hello world!'
# string = string[::-1]
# print(string.rstrip('h'))
###########################################################
###########################################################
###########################################################

# print('-------------------- 8 ---------------------')
# print('------------------- 8 8 --------------------')
# print('------------------ 8 8 8 -------------------')
# print('----------------- 8 8 8 8 ------------------')
# print('---------------- 8 8 8 8 8 -----------------')
# print('--------------- 8 8 8 8 8 8 ----------------')
# print('-------------- 8 8 8 8 8 8 8 ---------------')
# print('------------- 8 8 8 8 8 8 8 8 --------------')
# print('------------ 8 8 8 8 8 8 8 8 8 -------------')
# print('----------- 8 8 8 8 0 0 8 8 8 8 ------------')
# print('---------- 8 8 8 8 0 0 0 8 8 8 8 -----------')
# print('--------- 8 8 8 8 8 0 0 8 8 8 8 8 ----------')
# print('-------- 8 8 8 8 8 8 8 8 8 8 8 8 8 ---------')
# print('------- 8 8 8 8 8 8 8 8 8 8 8 8 8 8 --------')
# print('------ 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 -------')
# print('----- 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 ------')
# print('---- 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 -----')
# print('--- 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 ----')
# print('--- 00000000000000000000000000000000000 ----')
# print('--- 00000000000000000000000000000000000 ----')
# print('--- 00000000000000000000000000000000000 ----')
# print('--- 00000000000000000000000000000000000 ----')
# print('--- 00000000000000000000000000000000000 ----')
# print('--- 00000000000000000000000000000000000 ----')
# print('--- 00000000000000000000000000000000000 ----')
# print('--- 00000000000000000000000000000000000 ----')
# print('--- 00000000000000000000000000000000000 ----')
# print('--- IIIIIIIIIIII00000000000000000000000 ----')
# print('--- I0000000000I00000000000000000000000 ----')
# print('--- I0000000000I00000000000000000000000 ----')
# print('--- I0000000000I00000000000000000000000 ----')
# print('--- I&000000000I00000000000000000000000 ----')
# print('--- I0000000000I00000000000000000000000 ----')
# print('--- I0000000000I00000000000000000000000 ----')
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
# for a in range(0, len(mylist)-1):
#     if int(mylist[a]) > int(mylist[a+1]):

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

# import random

# players = []
# marbles = []
# pnumber = 100
# cplayer = 0
# cmarble = ''
# taken = 0
# rules = 'Welcome to Russian Rulette\n-------------------------- \n'

# print(rules)
# for i in range(0, 6):
#     marbles.append('green')

# marbles[random.randint(0, 5)] = 'white'
# random.shuffle(marbles)

# while pnumber >= 4:
#     pnumber = int(input('enter number of players: '))

# for r in range(0, pnumber):
#     players.append(str(input(f'whats your name #{r+1} : ')))

# while taken < 6:
#     print(f'\nplayer is {players[cplayer]}')
#     input('press enter to continue ...\n')
#     cmarble = random.choice(marbles)
#     if cmarble == 'white':
#         print(f'white ball, GAME OVER for {players[cplayer]}\n')
#         break
#     else:
#         print(f'green ball for {players[cplayer]}')
#         marbles.remove('green')
#         taken += 1
#         cplayer += 1
#         if cplayer == pnumber:
#             cplayer = 0
#         print(f'next player is {players[cplayer]}\n')


# 1.#########################################################

# import random

# players = []
# marbles = []
# pnumber = 100
# cplayer = 0
# cmarble = ''
# taken = 0
# rules = 'regeln'

# print(rules)
# for i in range(0, 6):
#     marbles.append('green')
# marbles[5] = 'lila'
# marbles[random.randint(0, 4)] = 'white'
# random.shuffle(marbles)
# while pnumber >= 4:
#     pnumber = int(input('players: '))
# for r in range(0, pnumber):
#     players.append(str(input(f'whats your name #{r+1} : ')))
# while taken < 6:
#     print(f'\nplayer is {players[cplayer]}')
#     input('press enter to continue ...\n')
#     cmarble = random.choice(marbles)
#     if cmarble == 'white':
#         print(f'white ball, GAME OVER for {players[cplayer]}\n')
#         break
#     elif cmarble == 'lila':
#         print(f'lila ball, GAME OVER for {players[cplayer]}\n')
#         players.remove(players[cplayer])
#         taken += 1
#         pnumber -= 1
#         cplayer += 1
#         if cplayer == pnumber:
#             cplayer = 0
#         print(f'next player is {players[cplayer]}')
#         input('press enter to continue ...\n')
#     else:
#         print(f'green ball for {players[cplayer]}')
#         marbles.remove('green')
#         taken += 1
#         cplayer += 1
#         if cplayer == pnumber:
#             cplayer = 0
#         print(f'next player is {players[cplayer]}\n')

# 2.#########################################################


# import random

# balls = 0
# players = []
# marbles = []
# pnumber = 100
# cplayer = 0
# cmarble = ''
# taken = 0
# rules = 'regeln'

# print(rules)
# balls = int(input('How many balls we play: '))
# for i in range(0, balls):
#     marbles.append('green')
# marbles[5] = 'lila'
# marbles[random.randint(0, 4)] = 'white'
# random.shuffle(marbles)
# while pnumber >= 4:
#     pnumber = int(input('players: '))
# for r in range(0, pnumber):
#     players.append(str(input(f'whats your name #{r+1} : ')))
# while taken < 6:
#     print(f'\nplayer is {players[cplayer]}')
#     input('press enter to continue ...\n')
#     cmarble = random.choice(marbles)
#     if cmarble == 'white':
#         print(f'white ball, GAME OVER for {players[cplayer]}\n')
#         break
#     elif cmarble == 'lila':
#         print(f'lila ball, GAME OVER for {players[cplayer]}\n')
#         players.remove(players[cplayer])
#         taken += 1
#         pnumber -= 1
#         cplayer += 1
#         if cplayer == pnumber:
#             cplayer = 0
#         if len(players) == 1:
#             print(f'the winner is {players[cplayer]}')
#             break
#         print(f'next player is {players[cplayer]}')
#         input('press enter to continue ...\n')

#     else:
#         print(f'green ball for {players[cplayer]}')
#         marbles.remove('green')
#         taken += 1
#         cplayer += 1
#         if cplayer == pnumber:
#             cplayer = 0
#         print(f'next player is {players[cplayer]}\n')

# 1.#########################################################


# with open('poems.txt', 'r') as myfile:

#     # myfile.write('''
#     # Hörst du, wie die Flammen flüstern,
#     # Knicken, knacken, krachen, knistern,
#     # Wie das Feuer rauscht und saust,
#     # Brodelt, brutzelt, brennt und braust?''')
#     poem = myfile.read()
#     print(poem)

# 4.#########################################################

# import pickle
# import random
# mylist = []
# summe = 0

# for i in range(0, 11):
#    mylist.append(random.randint(0, 1000))

# with open('nums', 'wb') as myfile:
#     pickle.dump(mylist, myfile)

# with open('nums', 'rb') as myfile:
#     loadlist = pickle.load(myfile)
# print(loadlist)

# for elment in loadlist:
#     summe = summe + elment
# print(summe)

###########################################################
###########################################################
###########################################################
# from PIL import Image
# image = Image.open('task1.jpg')
# w = image.width
# h = image.height
# print(w,h)
# image.show()
# image.thumbnail((1024, 768))
# image.save('pic-1024x768.jpg')
# image.thumbnail((600, 400))
# image.save('pic-600x400.jpg')
# image.thumbnail((100, 100))
# image.save('pic-100x100.jpg')

#2#########################################################
# from PIL import Image
# image = Image.open('task2.jpg')
# region1 = image.crop((0, 0, 150, 150))
# region2 = image.crop((0, 150, 150, 300))
# region3 = image.crop((150, 0, 300, 150))
# region4 = image.crop((150, 150, 300, 300))
# region1 = region1.transpose(Image.ROTATE_90)
# region2 = region2.transpose(Image.ROTATE_180)
# region3 = region3.transpose(Image.ROTATE_180)
# region4 = region4.transpose(Image.ROTATE_270)
# image.paste(region1, (0, 0))
# image.paste(region2, (0, 150))
# image.paste(region3, (150, 0))
# image.paste(region4, (150, 150))
# image.save('new_cat.jpg')
# image.show()

#3#########################################################

# from PIL import Image
# im1 = Image.open('cat.jpg')
# im2 = Image.open('flashback.jpg')
# w = im1.width
# h = im1.height
# im2 = im2.resize((w, h))
# res = Image.blend(im1, im2, 0.25)
# res.show()

###########################################################

# from PIL import Image, ImageDraw
# image = Image.new('RGB', (500, 600), 'white')
# draw = ImageDraw.Draw(image)
# draw.rectangle([0, 0, 500, 600], fill = 'white', outline = 'black', width = 7)
# draw.rectangle([100, 0, 500, 450], fill = 'red', outline = 'black', width = 7)
# draw.rectangle([0, 442, 106, 600], fill = 'blue', outline = 'black', width = 7)
# draw.rectangle([0,0, 105, 125], fill = 'white', outline = 'black', width = 7)
# draw.rectangle([420, 445, 500, 600], fill = 'white', outline = 'black', width = 7)
# draw.rectangle([420, 520, 500, 600], fill = 'yellow', outline = 'black', width = 7)
# image.show()

###########################################################
###########################################################

# from PIL import Image, ImageDraw, ImageFont
# f = ImageFont.truetype("Arial", 40)
# image = Image.open("cat2.jpg").convert("RGBA")
# txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
# draw = ImageDraw.Draw(txt)
# draw.text((200, 350),'Merry\nChristmas!', font = f, fill = (255, 200, 200, 100))
# result = Image.alpha_composite(image, txt)
# result.show()

###########################################################
###########################################################

# import datetime
# a = datetime.datetime.today().strftime('%B %d, %Y, %I:%M %p')
# print(a) 

###########################################################

# import datetime
# year = int(input('please enter year: '))
# month = int(input('please enter month: '))
# day = int(input('please enter day: '))
# a = datetime.date.today()
# b = datetime.date(year, month, day)
# print(a - b)

###########################################################

# import datetime
# year = int(input('please enter year: '))
# l = 0
# for r in range(1, 13):
#     day = datetime.date(year, r, 13)
#     if day.weekday() == 4:
#         l += 1
#         print(f'Friday the 13th found {day}')
# print(f'There are {l} friday 13th in {year}')

###########################################################
# Homewok 
# 1.
# import datetime
# money = input() .split()
# result = 0.0
# for i in range(0, len(money)):
#     result = result + float(money[i])
# print(result)

###########################################################
# 2.
# gewicht = int(input('What is your weight at the Earth? '))
# print(f'Your weight at the Moon is {float(gewicht) / 9.81 * 1.622}')

##########################################################
##########################################################
##########################################################

# import time,random

# messeges = ['An apple a day keeps the doctor away.','Its better to be safe than sorry.','Actions speak louder than words.','The early bird catches the worm.']

# print(f'Text entery speed check.Enter next sentence.I will start a timer...')
# time.sleep(2)
# print('Ready...')
# time.sleep(1)
# print('Stedy...')
# time.sleep(1)
# print('Go!')
# sentence = random.choice(messeges)
# print(sentence)
# start_time = time.time()
# user_line = str(input())
# end_time = time.time()
# user_time = end_time - start_time
# answer = round(float(len(user_line)) / float(user_time), 6)
# print(f'you have {len(user_line)} symbols and {answer} seconds.\n that are {round(len(user_line) / answer, 2)} symbols in a second.')

# if user_line == sentence:
#     print('You did no mistake')
#     quit
# elif user_line != sentence:
#     print('You made at least one mistake')

#     for r in range(0, len(sentence)):
#             if sentence[r] != user_line[r]:
#                 print(f'You madea a mistake.you typed {user_line[r]} insted of {sentence[r]}')

#1.########################################################

# def equate(a, b):
#     return (a + 4*b)*(a - 3*b) + a

# print(equate(b = 3 ,a = 5))

#2.########################################################

# def find_speed(kilometers, hours):
#     return round((kilometers * 1000) / (hours * 3600) , 2)

# print(find_speed(100 ,3))

#3.########################################################

# from os import chdir



# def smallest(a, b , c):
#     result = 0
#     if a < b and a < c:
#         result = a
#     elif b < a and b < c:
#         result = b
#     elif c < a and c < b:
#         result = c
#     return result

# print(smallest(101, 101, 10))

#1. #######################################################

# name = str(input('Your name: '))
# def greeting():
#     print(f'Hello, {name}!')

# greeting()

#2. #######################################################

# def rectangle(a, b):
#     print(f'P = {a + b + a + b} \nS = {a * b}')

# rectangle(2, 5)

#3. #######################################################

# n = int(input())
# def get_random_array(n = 10):
#     import random
#     mylist = []
#     for i in range(0, n):
#         mylist.append(random.randint(0, 10))
#     print(mylist)

# get_random_array(n)

#4. #######################################################

# n = int(input())

# def get_random_array(n = 10):
#     import random
#     mylist = []
#     for i in range(0, n):
#         mylist.append(random.randint(0, 10))
#     print(mylist)
#     return mylist

# def reverse(newlist):
#     newlist.reverse()
#     print(newlist)

# # array = get_random_array(n)
# reverse(get_random_array(n))

#5. #######################################################

# result = 0

# def factorial(n = 1):
#     answer = 1
#     for i in range(1, n +1):
#         answer = answer * i
#     return answer

# result = ((2 * factorial(5)) + (3 * factorial(8))) / (factorial(6) * factorial(4))
# print(result)


#6. #######################################################

# def sum_of_digets(n): 
    # sum = 0
    # for i in str(n):   
    #   sum += int(i)        
    # return sum

# zahl1 = int(input('1.: '))
# zahl2 = int(input('2.: '))

# sum_zahl1 = sum_of_digets(zahl1)
# sum_zahl2 = sum_of_digets(zahl2)

# print(f'zahl1: {zahl1}')
# print(f'zahl2: {zahl2}')

# if sum_zahl1 < sum_zahl2:
#     print(f'Summ of {zahl2} is bigger.')

# else:
#     print(f'Summ of {zahl1} is bigger.')

#7. #######################################################

# import random

# def lucky(n): 
#     sum1 = 0
#     a = str(n)
#     for i in a[:3]:   
#       sum1 += int(i)  
#     sum2 = 0
#     for i in a[3:]:   
#       sum2 += int(i)  
#     if sum1 == sum2:
#         return True 
#     else:
#         return False

# def get_lucky():
#     while True:
#         r = random.randint(100000, 999999)
#         if lucky(r) == True:
#             print(r)
#             break

# get_lucky()

#8. #######################################################

# def average(*list):
#     sum = 0
#     result = 0
#     for i in list:   
#       sum += i     
#     result = sum / len(list)   
#     return result
# print(average(3, 4, 7, 8))
