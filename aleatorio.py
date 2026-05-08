import time
import random
import os
os.system("cls")


# lata = 0
# plancha =0

# pecesCap=random.randint(10,20)
# print(f"el total de peces capturados es: {pecesCap}")
# time.sleep(1)

# for i in range(pecesCap):
#     peso=random.randint(300,3000)

#     print(f"\nPez {i+1} pesa {peso} gramos")

#     if peso <= 800:

#         lata+=1
#     elif peso >= 801 and peso <=3000: 

#         plancha += 1

#     else:

#         print("peso invalido")    

# time.sleep(2)
# print(f"El total de peces en la lata ason {lata}")
# time.sleep(2)
# print(f"El total de peces en la plancha son {plancha}")





# cantidad_peces = random.randint(10, 20)

# print("Cantidad de peces capturados:", cantidad_peces)

# # Contadores
# lata = 0
# plancha = 0


# for i in range(1, cantidad_peces + 1):
  
#     peso = random.randint(500, 1500)

#     print(f"Pez {i}: {peso} grs")

#     if peso <= 800:
#         print(" -> Se envasa en lata")
#         lata += 1
#     else:
#         print(" -> Se vende a la plancha")
#         plancha += 1


# print("\nRESUMEN FINAL")
# print("Peces para lata:", lata)
# print("Peces para la plancha:", plancha)



# num =random.randint(1,9)

# while abs(-3)!=num:
#     print(num)
#     time.sleep(1)
#     num =random.randint(1,9)



# n1=int(input("ingrese el valor de limite inferior: "))
# n2=int(input("ingrese el valor de limite superior: "))
# #validar  que el limite superior sea mayor que el limite inferior
# #hay un limite qe rompe el deseo

# while n1>=n2:
#     print("error, el limite superior debe se mayor ")
#     n2=int(input("ingrese el valor de limite superior: "))  

# num=random.randint(n1,n2)
# print(num)

# lata = 0
# plancha =0


# pecesCap=random.randint(10,20)
# print(f"El total d peces capturados es: {pecesCap}")

# peso=random.randint(300,3000)

# if peso <= 800:
#     lata=+1
# elif peso >= 801 and peso <= 3000:
#     plancha=+1
# else:
#     print("peso invaido")        

# time.sleep(2)
# print(f"El total de peces en lata son: {lata}")
# time.sleep(2)
# print(f"El total de peces en plancha son {plancha}")



#forma 2

# peces=random.randint(10,20)
# p_lata=0
# p_plancha=0
# print(f"capturados {peces} peces ")
# time.sleep(2)

# for p in range(peces):
#  pez=random.randint(257,3000)

# if pez<=800:
#  p_lata=+1
# else:
#  p_plancha=+1

#  print(f"")




# peso =int(input("ingrese l peso del producto"))

# sodio=int(input("ingrese el porentaje de sopdio: "))

# mercado=int(input("ingrese el mercado del producto 1.- Nacional - 2.-internacional")) 

# if peso <500:
  
#   lata="lata normal"

# elif 501<peso<1500:
  
#   lata="lata mediana"

# else:
  
#   lata="lata grande"

#   if sodio<5:
   
#    sod=""

#   elif 5<=sodio<=8:
   
#    sod="lata especial"

#   else:
   
#    sod="acorazada" 

#    if mercado ==1:

#     sticker=""

#    else:

#     sticker="con stcker saniario"

#     print(f"{lata} {sod} {mercado}")







# intentos=0


# respuesta = "no" 

# while respuesta != "si" and intentos <5:
    
#     num=random.randint(1,20)
#     print("¿tu numero es?", num)
#     respuesta = input("Responde si o no: ")
#     intentos +=1
# if respuesta == "si":
#     print("¡ADIVINE TU NUMERO!")
# else:
#     print("no pude adivinar tu numero en los 5 intentos")  
  


# dado=random.randint(1,6)
# print(f"el dado cayo en: {dado}")

# if dado >= 6:

#     print("¡¡¡JACPOK!!!")

# cara="cara"
# sello="sello"

# moneda=random.randint(1,2)

# if moneda == 1:
#     print("cara")
# else:  
#     print("sello")  



# opciones =["piedra","papel","tijera"]

# computador=random.choice(opciones)

# usuario = input("elije piedra, papel o tijera: ")
# print("computador elijio:", computador)

# if usuario == computador:
#     print("empate")
# elif usuario == "piedra" and computador== "tijera":
#     print("ganaste")
# elif usuario == "papel" and computador == "piedra":
#     print("ganaste")
# elif usuario == "tijera" and computador == "papel":
#     print("ganaste")
# else:
#     print("perdiste")






















