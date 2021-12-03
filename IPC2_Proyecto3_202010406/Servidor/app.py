import os
import json
from lector import Reader
from analizador import Analizador
from flask_restful import Api
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

lista_autorizaciones = list()
lista_inicial = list()

@app.route('/cargar-archivo', methods= ['POST'])
def cargar_Archivo():
    leer = Reader()
    analisis = Analizador()
    file = request.get_data()
    global lista_autorizaciones
    global lista_inicial

    if len(file) != 0:
        leer.read_file(file)
        lista = leer.get_lista()
        lista_inicial = lista
        analisis.analizar(lista)
        lista_autorizaciones = analisis.get_lista()
        return {'message': 'leido'}
    else:
        return {'message': 'error no valido'}

@app.route('/delete-file', methods=['DELETE'])
def delete_file():
    if os.path.exists('autorizaciones.xml'):
        os.remove('autorizaciones.xml')
        return {'message': 'TRUE'}
    else:
        return {'message': 'FALSE'}

@app.route('/get-info', methods=['GET'])
def get_infor():
    if os.path.exists('autorizaciones.xml'):
        f = open('autorizaciones.xml')
        content = f.read()
        return {'message': 'True', 'contenido': content}
    else:
        return {'message': 'FALSE'}

@app.route('/get-dict', methods=['GET'])
def get_dict():
    global lista_autorizaciones
    global lista_inicial
    if len(lista_autorizaciones) != 0 and len(lista_inicial) != 0:
        autorizaciones = [obj.to_dict() for obj in lista_autorizaciones]
        facturas = [obj.to_dict() for obj in lista_inicial]
        jsdata = json.dumps({"message": "True","autorizaciones": autorizaciones, "facturas": facturas})
        return jsdata
    else:
        return {"message": "False"}




if __name__ == '__main__':
    app.run()