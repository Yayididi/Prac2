import random

print("--- Adivina el numero entre el 1 Y el 10 --- 4 intentos ---")
numero1 = random.randint(1,10)
usuario = int(input("Ingrese su propusta: "))
intentos = 1

while (intentos != 4):
    if(numero1 == usuario):
        print("Adivinast el numero!")
        break

    elif(usuario > numero1):
        print("Menos")
        intentos += 1
        usuario = int(input("Ingrese su propuesta: "))
        
    elif(usuario < numero1):
        print("Mas")
        intentos += 1
        usuario = int(input("Ingrese su propuesta: "))
else:
    print("Perdiste, se te han agotado los intentos :(")

        





