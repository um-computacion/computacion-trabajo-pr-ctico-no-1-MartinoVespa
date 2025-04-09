#Fase 2

def decimal_to_roman(num):
   
    # Definir los valores y símbolos romanos
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    # Inicializar la cadena de números romanos
    roman_num = ""
    i = 0
    
    # Mientras el número sea mayor que 0
    while num > 0:
        # Dividir para obtener repeticiones
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
        
    return roman_num
