import time
import random
lata = 0
plancha =0


PecesCap=random.randint(10,20)
print(f"El total d peces capturados es: {PecesCap}")

time.sleep()

for i in range (PecesCap):
 peso=random.randint(300,3000)
if peso <= 800:
   
    lata+=1
elif peso >= 801 and peso <= 3000:
    plancha+=1
else:
    print("peso invaido")        

time.sleep(2)
print(f"El total de peces en lata son: {lata}")
time.sleep(2)
print(f"El total de peces en plancha son {plancha}")


