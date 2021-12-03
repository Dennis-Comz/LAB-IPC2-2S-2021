from flask_restful import Api
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

# GET, POST, PUT y DELETE

@app.route('/metodo_get', methods=['GET'])
def metodo_get():
    print('Usando metodo GET.')
    return {"message": "Peticion hecha con Get."}

@app.route('/metodo_post', methods=['POST'])
def metodo_post():
    contenido = request.get_json()
    print(contenido['message'])
    return {"message": "Peticion hecha con POST."}

@app.route('/metodo_delete', methods=['DELETE'])
def metodo_delete():
    print('Usando metodo DELETE.')
    return {"message": "Peticion hecha con DELETE."}

@app.route('/metodo_put', methods=['PUT'])
def metodo_put():
    contenido = request.get_data()
    print('Usando metodo PUT, parametro: ' + str(contenido))
    return {"message": "Peticion hecha con PUT."}

if __name__ == '__main__':
    app.run()