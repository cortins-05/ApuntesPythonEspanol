import threading
import time

# Variable global para la bandera (flag)
detener_hilo = False

def hilo_secundario():
    """Función que ejecuta el hilo secundario."""
    contador = 0
    while not detener_hilo:
        print(f"Hilo secundario: Contador = {contador}")
        contador += 1
        time.sleep(1)  # Simula un trabajo en el hilo secundario
    print("Hilo secundario: Detenido")


def hilo_principal():
    """Función que ejecuta el hilo principal."""
    global detener_hilo # permite modificar la variable detener_hilo
    print("Hilo principal: Iniciado")

    # Crear e iniciar el hilo secundario
    hilo = threading.Thread(target=hilo_secundario)
    hilo.start()

    # Simula un trabajo en el hilo principal
    time.sleep(5)

    print("Hilo principal: Indicando al hilo secundario que se detenga")
    detener_hilo = True # Cambia la bandera para parar el hilo

    hilo.join()  # Esperar a que el hilo secundario termine

    print("Hilo principal: Finalizado")

if __name__ == "__main__":
    hilo_principal()