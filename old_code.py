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



