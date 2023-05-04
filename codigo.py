def cifrado_simetrico(mensaje, clave):
    # Convertir el mensaje y la clave en listas de valores ASCII
    mensaje_ascii = [ord(c) for c in mensaje]
    clave_ascii = [ord(c) for c in clave]
    
    # Convertir la clave a una cadena binaria de la misma longitud que el mensaje
    clave_bin = ''.join('{:08b}'.format(clave_ascii[i % len(clave_ascii)]) for i in range(len(mensaje)))
    
    # Convertir el mensaje a una cadena binaria
    mensaje_bin = ''.join('{:08b}'.format(mensaje_ascii[i]) for i in range(len(mensaje)))
    
    # Realizar la operación XOR bit a bit entre la clave y el mensaje
    resultado_bin = ''.join(str(int(clave_bin[i]) ^ int(mensaje_bin[i])) for i in range(len(mensaje_bin)))
    
    # Convertir el resultado a una lista de valores enteros (ASCII)
    resultado_ascii = [int(resultado_bin[i:i+8], 2) for i in range(0, len(resultado_bin), 8)]
    
    # Convertir la lista de valores ASCII en una cadena
    resultado = ''.join(chr(c) for c in resultado_ascii)
    
    return resultado


def descifrado_simetrico(mensaje, clave):
    # Convertir el mensaje y la clave en listas de valores ASCII
    mensaje_ascii = [ord(c) for c in mensaje]
    clave_ascii = [ord(c) for c in clave]
    
    # Convertir la clave a una cadena binaria de la misma longitud que el mensaje
    clave_bin = ''.join('{:08b}'.format(clave_ascii[i % len(clave_ascii)]) for i in range(len(mensaje)))
    
    # Convertir el mensaje a una cadena binaria
    mensaje_bin = ''.join('{:08b}'.format(mensaje_ascii[i]) for i in range(len(mensaje)))
    
    # Realizar la operación XOR bit a bit entre la clave y el mensaje
    resultado_bin = ''.join(str(int(clave_bin[i]) ^ int(mensaje_bin[i])) for i in range(len(mensaje_bin)))
    
    # Convertir el resultado a una lista de valores enteros (ASCII)
    resultado_ascii = [int(resultado_bin[i:i+8], 2) for i in range(0, len(resultado_bin), 8)]
    
    # Convertir la lista de valores ASCII en una cadena
    resultado = ''.join(chr(c) for c in resultado_ascii)
    
    return resultado
