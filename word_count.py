import sys

if len(sys.argv)<2:
    print("debe indicar nombre de archivo")
else:
    with open(sys.argv[1],"r") as archivo:
        texto = archivo.read()
        
        palabras=len(set(texto.split(" ")))
        print(f"El numero de palabras distintas del texto {sys.argv[1]} es: {palabras}")
        
        letras=len(set(texto))
        print(f"las letras unicas {sys.argv[1]} es: {letras}")
        