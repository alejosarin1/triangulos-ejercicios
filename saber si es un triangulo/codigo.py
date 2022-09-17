# Determinar si es un triangulo

# input
print("\n\n")
print("Determinar si es un triangulo")

a = int(input("\ndigite el lado a: "))
b = int(input("\ndigite el lado b : "))
c = int(input("\ndigite el lado c : "))

#proceso

if (a+b < c and c+a<b):
    print("\n NO ES UN TRIANGULO")
else:
    print("\n SI ES UN TRIANGULO")


