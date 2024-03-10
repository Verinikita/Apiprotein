import base64
import os
from flask import Flask, request, send_file
from flask_cors import CORS

from src.fetch_pdb import phi_psi
from src.plot import plot
from src.functions import allowed_file, extractFileByExtension

app = Flask(__name__).run()

# Configuración de CORS (ajústala según sea necesario)
if os.getenv('VERCEL_ENV') != 'production':
    cors = CORS(app, supports_credentials=True, resources={r'/*': {'origins': 'http://localhost:5000'}})

UPLOAD_FOLDER = '/tmp'  # Directorio temporal para Vercel

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return {'msg': 'No se encontró el archivo en la solicitud'}, 400

    file = request.files['file']

    if file.filename == '':
        return {'msg': 'No se seleccionó ningún archivo'}, 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        return {'msg': 'Archivo subido exitosamente', 'filename': filename}

    return {'msg': 'Error al procesar la solicitud'}, 500




