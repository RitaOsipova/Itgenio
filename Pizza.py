#  -------------------------------
#  Hausaufgabe 2. Pizza
#  -------------------------------
freunde = int(input('Wie viele Freunde teilen sich eine Pizza? '))
stucke = int(input('Wie viele Stucke teilen sich die Frunde? '))

# gteil = stucke // freunde
# result = freunde * gteil
# rest = stucke - result
rest = stucke - (freunde * (stucke // freunde))
print(f'Es sind {freunde} Freunde.')
print(f'Es sind {stucke} Stucke.')
print(f'Es bleiben {rest} Stucke ubrig.')