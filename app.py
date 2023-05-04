from flask import Flask,render_template, request, send_file
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)


def cifrar(texto_plano, clave):
    # Convertir el texto plano y la clave a listas de números
    texto_plano_ascii = [ord(caracter) for caracter in texto_plano]
    clave_ascii = [ord(caracter) for caracter in clave]
    
    # Convertir la clave en una cadena binaria del mismo tamaño que el texto plano
    clave_binaria = ''.join([bin(caracter)[2:].zfill(8) for caracter in clave_ascii])
    clave_binaria_completa = clave_binaria * ((len(texto_plano_ascii) // len(clave_ascii)) + 1)
    clave_binaria_completa = clave_binaria_completa[:len(texto_plano_ascii)]
    
    # Realizar la operación XOR entre el texto plano y la clave binaria
    texto_cifrado_binario = [texto_plano_ascii[i] ^ int(clave_binaria_completa[i], 2) for i in range(len(texto_plano_ascii))]
    
    # Convertir el texto cifrado a una cadena de caracteres
    texto_cifrado = ''.join([chr(caracter) for caracter in texto_cifrado_binario])
    
    return texto_cifrado


def descifrar(texto_cifrado, clave):
    # Convertir el texto cifrado y la clave a listas de números
    texto_cifrado_ascii = [ord(caracter) for caracter in texto_cifrado]
    clave_ascii = [ord(caracter) for caracter in clave]
    
    # Convertir la clave en una cadena binaria del mismo tamaño que el texto cifrado
    clave_binaria = ''.join([bin(caracter)[2:].zfill(8) for caracter in clave_ascii])
    clave_binaria_completa = clave_binaria * ((len(texto_cifrado_ascii) // len(clave_ascii)) + 1)
    clave_binaria_completa = clave_binaria_completa[:len(texto_cifrado_ascii)]
    
    # Realizar la operación XOR entre el texto cifrado y la clave binaria
    texto_descifrado_binario = [texto_cifrado_ascii[i] ^ int(clave_binaria_completa[i], 2) for i in range(len(texto_cifrado_ascii))]
    
    # Convertir el texto descifrado a una cadena de caracteres
    texto_descifrado = ''.join([chr(caracter) for caracter in texto_descifrado_binario])
    
    return texto_descifrado

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encriptarhtml')
def encriptarhtml():
    return render_template('encriptar.html')


@app.route('/decodificarhtml')
def decodificarhtml():
    return render_template('decodificar.html')


@app.route('/encriptar', methods=['GET', 'POST'])
def encriptar():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        clave = request.form['clave']

        with open(f.filename, 'r') as file:
            file_content = file.read().replace('\n', '')
        
        print(file_content)


        textoCodificado= cifrar(file_content,clave)

        new_filename = secure_filename(os.path.splitext(f.filename)[0]+".des")
        with open(new_filename, 'w', encoding="UTF-8") as file:
            file.write(textoCodificado)
        
        path = str(os.path.splitext(f.filename)[0]+".des") 
        return send_file(path, as_attachment=True)
    else:
        return render_template('index.html')

@app.route('/decodificar', methods=['GET', 'POST'])
def decodificar():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        clave = request.form['clave']

        with open(f.filename, 'r') as file:
            file_content = file.read().replace('\n', '')
        
        print(file_content)

        textoCodificado= descifrar(file_content,clave)

        new_filename = secure_filename(os.path.splitext(f.filename)[0]+".txt")
        with open(new_filename, 'w', encoding="UTF-8") as file:
            file.write(textoCodificado)
        
        path = str(os.path.splitext(f.filename)[0]+".txt") 
        return send_file(path, as_attachment=True)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()