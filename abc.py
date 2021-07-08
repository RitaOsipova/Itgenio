#  -------------------------------
#  Hausaufgabe 3. a,b,c
#  -------------------------------
abc = int(input('Gib mir eine dreistellige Zahl '))

a = abc // 100   
a1 = 100 * a
a2 = abc - a1
b = a2 // 10
b1 = 10 * b
c = a2 - b1

print(a)
print(b)
print(c)
print(a + b + c)