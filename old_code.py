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
