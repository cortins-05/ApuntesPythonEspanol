#Necesitaras instalar la libreria: pip install pymupdf

import fitz as pdf

#Abrir un pdf
doc = pdf.open("ejemplo.pdf")

#Obtener información del pdf
print(f"Paginas: {doc.page_count}")#Numero de paginas
doc_metada = doc.metadata
print(doc_metada)#Metadatos del pdf

#Extraer de un pdf
for numero_pagina in range(len(doc)):
    pagina = doc[numero_pagina]
    texto = pagina.get_text("text")
    print(texto)
    
#Extraer imagenes de un pdf
for numero_pagina in range(len(doc)):
    pagina = doc[numero_pagina]
    imagenes = pagina.get_images(full=True)
    for indice_imagen, img in enumerate(imagenes):
        xref = img[0]
        imagen_base = doc.extract_image(xref)
        imagen_bytes = imagen_base["image"]
        with open(f"imagen_{numero_pagina+1}_{indice_imagen}.png", "wb") as imagen:
            imagen.write(imagen_bytes)

#Agregar texto a un pdf
pagina = doc[0]
pagina.insert_text((100, 100), "Hola mundo", fontsize=20, color=(1, 0, 0))
doc.save("ejemplo_modificado.pdf")

#Agregar imagen a un pdf
rect = pdf.Rect(100, 100, 200, 200) #Posicion y tamaño de la imagen
pagina.insert_image(rect, filename="imagen.jpg")
doc.save("documento_con_imagen.pdf")

doc.close()
