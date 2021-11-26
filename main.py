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

###########################################################
###########################################################
###########################################################

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

def sum_of_digets(n): 
    sum = 0
    for i in str(n):   
      sum += int(i)        
    return sum

zahl1 = int(input('1.: '))
zahl2 = int(input('2.: '))

sum_zahl1 = sum_of_digets(zahl1)
sum_zahl2 = sum_of_digets(zahl2)

print(f'zahl1: {zahl1}')
print(f'zahl2: {zahl2}')

if sum_zahl1 < sum_zahl2:
    print(f'Summ of {zahl2} is bigger.')

else:
    print(f'Summ of {zahl1} is bigger.')