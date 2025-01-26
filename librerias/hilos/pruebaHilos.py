import threading
variable = 0

def bucle():
    while variable != 1:
        variable += 2
        
prueba = threading.Thread(target=bucle)
prueba.start()

while variable != 1:
    print("ey")
    variable = int(input())