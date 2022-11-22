print("Alle Angaben in Binär!\n")
eingabe = input("Eingabe: ")
#vz = input("Vorzeichen: ")
#exponent = input("Exponent: ")
#mantisse = input("Mantisse: ")
#eingabe = "0b" + eingabe


num_list = [int(x) for x in str(eingabe)]


vz = str(num_list[0])
exponent = []
for x in range(8):
    exponent.append(str(num_list[x+1]))

mantisse = []
for x in range(23):
    mantisse.append(str(num_list[x+9]))

mantissebin = ''
for x in mantisse:
    mantissebin = str(mantissebin) + str(x)

exponentbin = ''
for x in exponent:
    exponentbin = str(exponentbin) + str(x)

print("Mantisse_b: " + mantissebin)
print("Exponent_b: " + exponentbin)

man = int(mantissebin, 2)

if vz == '1':
    vz = "-"
elif vz == '0':
    vz = "+"
else:
    print("Error beim Vorzeichen!")
print("Vorzeichen: " + vz)
if vz == str(1):
  vz = "-"
elif vz == str(0):
  vz = "+"
exp = int(exponentbin, 2)
print("Mantisse_d: " + str(man))
print("Exponent_d: " + str(exp),end='')
exp = int(exp) - int(127)
print("(n^" + str(exp) + ")")

zahl = ((int(man)/2**23) + 1)*(2**exp)
print( "\nAusgabe: " + vz + str(zahl) )

