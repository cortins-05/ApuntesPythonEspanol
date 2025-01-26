import threading
import time

def desayunar():
    print("Iniciando desayunar")
    time.sleep(3)
    print("Finalizado")
    pass

def tomar_cafe():
    print("Iniciando tomar café")
    time.sleep(4)
    print("Finalizado")
    pass

def estudiar():
    print("Iniciando estudio")
    time.sleep(5)
    print("Finalizado")
    pass

inicio = time.perf_counter() #Inicio del temporizador

#CREAR E INICIAR HILOS

x = threading.Thread(target=desayunar)
x.start()
y = threading.Thread(target=tomar_cafe)
y.start()
z = threading.Thread(target=estudiar)
z.start()

x.join() #Espera a los demás hilos se unan al programa principal
y.join()
z.join()

#desayunar()
#tomar_cafe()
#estudiar()

print(threading.active_count()) #Sirve para contar los hilos en ejecución
print(threading.enumerate()) #Enlista los hilos activos

fin = time.perf_counter()

tiempo = fin -inicio
print(tiempo)