import sys

if len(sys.argv)<4:
    print("error, faltan argumentos")
else:
    factor={
        "sol":float(sys.argv[1]),
        "peso_argentino":float(sys.argv[2]),
        "dolar":float(sys.argv[3])
    }
    peso_cl=float(sys.argv[4])
    
print(f'''
        TABLA DE CONVERSION
        
        CLP {peso_cl:,.0f} equivale a :
        
        {(factor["sol"]*peso_cl):.1f}  Soles Peruanos.
        {(factor["peso_argentino"]*peso_cl):.1f}  Peso Argentino.
        {(factor["dolar"]*peso_cl):.1f}  Dolares Americanos.
        ''')