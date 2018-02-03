no_repeat = False
def review_text(text):
    global no_repeat
    unique_letter = {}
    for idx, i in enumerate(text):
        if i not in unique_letter:
            unique_letter[i] = 0
        else:
            unique_letter[i] = 1
    for word, repeat in unique_letter.items():
        if repeat == 0:
            no_repeat = True
            print("")
            print("La letra que no se repite es la: {}".format(word))
    if no_repeat == False:
        print("")
        print("Todas las letras se repiten")
if __name__ == "__main__":
    print("")
    print("Este programa te dirá la primera letra que no se repite del texto")
    print("")
    text = input("Escribe las letras que deseas que revisemos: ")
    review_text(text)
