# 4. Se asume que todas las letras se van a repetir
no_repeat = False
def review_text(text):
    # 5. Se activa el uso global de la variable, para poderla modificar mas adelante
    global no_repeat
    # 6. Se almacenaran las letras "unicas" (sin repetirse) en esta variables, en un diccionario
    unique_letter = {}
    # 7. Se recorre toda la cadena de caracteres que nos pasaron
    for idx, i in enumerate(text):
        # 8. Si no la hemos agregado antes, se crea una llave la letra y el numero 0
        if i not in unique_letter:
            unique_letter[i] = 0
        # 9. En caso de ya haberla encontrado, se le cambia el valor de la llave a 1
        else:
            unique_letter[i] = 1
    # 10. Se recorre el "diccionario"
    for word, repeat in unique_letter.items():
        # 11. Si el valor se mantuvo en 0, significa que la letra no se utilizó mas de una vez
        if repeat == 0:
            # 12. Se indica que en este caso si se cumplío la regla, de que al menos una letra no se repitio
            no_repeat = True
            print("")
            # 13. Se indica la letra que no se haya repetido
            print("La letra que no se repite es la: {}".format(word))
    # 14. En caso de que todas las letras se hayan repetido, el valor de "no_repeat", se queda en false
    if no_repeat == False:
        print("")
        # 15. Se indica que todas las letras se repitieron
        print("Todas las letras se repiten")
if __name__ == "__main__":
    # 1. Inicio del programa
    print("")
    print("Este programa te dirá la primera letra que no se repite del texto")
    print("")
    # 2. Solicitamos la cadena de carateres que deseamos revisar
    text = input("Escribe las letras que deseas que revisemos: ")
    # 3. Lo ingresamos a la siguiente funcion
    review_text(text)
