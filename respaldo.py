from flask import Flask,render_template, request, send_file
from werkzeug.utils import secure_filename
import re
app = Flask(__name__)



def limpiezaDatos(file):
    file_content = file.read()
    file_content = file_content.decode('utf-8')
    file_content = '\n'.join([line.strip() for line in file_content.split('\n') if line.strip()])
    file_content = re.sub(r'\s+', ' ', file_content.strip())
    return file_content

def codeASCCI(file_content):
    ascii_vector = []
    for char in file_content:
        ascii_vector.append(ord(char))
    return ascii_vector

def decodeASCCI(ascii_vector):
    text_string = ""
    for ascii_val in ascii_vector:
        text_string += chr(ascii_val)
    return text_string

def codeBinary(ascii_vector):
    binary_values = []
    for number in ascii_vector:
        binary_value = bin(number)[2:]  
        binary_values.append(binary_value)
    return binary_values

def decodeBinary(binary_values):
    decimales = [int(b, 2) for b in binary_values]
    return decimales

def completList(lista):
    while( len(lista) != 7):
        lista.insert(0,0)
    return lista


def xorFuncion(binary_values,binary_valuesClave):
    xor_result = []
    contador = 0
    for binaryV in binary_values:
        if(contador == len(binary_valuesClave) ):
            contador = 0
        lista = [int(d) for d in list(binaryV)]
        listaC = [int(d) for d in list(binary_valuesClave[contador])]
        lista = completList(lista)
        listaC = completList(listaC)
        contador+=1
        aux_xor=[]
        for x, y in zip(lista, listaC):
            aux_xor.append(x ^ y)
        xor_result.append(aux_xor)
    return xor_result


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        clave = request.form['clave']
        with open(f.filename, 'rb') as file:
            file_content = file.read()
            file_content_unicode = file_content.decode('utf-8')
        
        
        file_content = file_content_unicode
        print("Mensaje")
        #print(file_content_unicode)
        #print(file_content)
        ascii_vector = codeASCCI(file_content)
        print(ascii_vector)
        binary_values = codeBinary(ascii_vector)
        print(binary_values)

        ##clave
        print("Clave")
        ascii_vectorClave = codeASCCI(clave)
        print(ascii_vectorClave)
        binary_valuesClave = codeBinary(ascii_vectorClave)
        print(binary_valuesClave)
        
        xor_result =xorFuncion(binary_values,binary_valuesClave)
        xor_result = [''.join(map(str, sublist)) for sublist in xor_result]
        
        print("Resultado XOR")
        print(xor_result)

        decimales = decodeBinary(xor_result)
        print(decimales)
        textoCodificado = decodeASCCI(decimales)
        print(textoCodificado)

        new_filename = secure_filename('cifrado.des')
        with open(new_filename, 'w', encoding="UTF-8") as file:
            file.write(textoCodificado)
        
        path = 'cifrado.des' 
        return send_file(path, as_attachment=True)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()