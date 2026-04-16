from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Habilitar CORS para que index.html pueda consultar el bridge

# MAPEO DE NOTEBOOK IDs (Extraído de los metadatos de usuario)
NOTEBOOK_MAP = {
    "X": {
        "Político": "d75dd570-1aeb-4493-baaa-47be85e8b64f",
        "Social": "2e544a06-eef7-4864-bf4d-d5f29aec64db",
        "Económico": "69c101f0-a8d8-458a-a286-3d7fd9397e4c",
        "Cultural": "fb1c1b01-5397-48a7-a369-42683417c311"
    },
    "XI": {
        "Político": "b5c75796-dd15-456a-8769-485527e4fbfc",
        "Social": "2e606b04-b7ba-404c-901a-0bb7da4d41bb",
        "Económico": "f46f59b5-4227-46c1-9bd0-d6cb4e10b557",
        "Cultural": "2ffab022-2c53-4fb2-a07d-5bb606533069"
    },
    "XII": {
        "Político": "bf7c79a0-b42b-4b45-b5bd-123ffce9a886",
        "Social": "b4f9a138-3d45-41a6-b5e2-a0e8d70617c7",
        "Económico": "3933f2a4-50c9-4039-badf-84ca2609fecb",
        "Cultural": "494b17db-749a-4815-875b-a2930440e41e"
    },
    "XIII": {
        "Político": "cd94b694-7a09-4c4e-9cfd-0798b0021c8d",
        "Social": "42fce690-eb2f-4da9-83b1-09ac7136f3c1",
        "Económico": "2d494631-a415-477a-9060-81771eae0575",
        "Cultural": "5a05c841-2067-4ee0-96fd-c6767a30e504"
    },
    "XIV": {
        "Político": "0913e083-08ed-4bc5-9a6e-2c297c3a1a4e",
        "Social": "9d614571-7917-423e-8853-d1e575a590ff",
        "Económico": "2963c247-de79-4e93-a597-a09b40d0802d",
        "Cultural": "597fba43-96f1-4f14-86b8-c5f52dc75bfd"
    },
    "XV": {
        "Político": "25a3ab7d-e6d2-4a5e-b980-40ae1200d500",
        "Social": "e2852491-58bb-4212-9cfb-00b8028c884c",
        "Económico": "6940c585-6d6f-4833-978a-f6dfd9727a4b",
        "Cultural": "8ab0abd6-3344-43d6-9aa2-bdebc5335b10"
    },
    "XVI": {
        "Político": "5143bb4c-91e6-4bb3-a18b-336add15f93d",
        "Social": "b637558d-a2fb-4f9d-bc7c-90d6a2f48687",
        "Económico": "fb77a6ff-f6b4-4214-b0da-51be8e68de34",
        "Cultural": "435474e7-5181-4028-bec7-8eecc3432991"
    },
    "XVII": {
        "Político": "37aa1441-5433-4245-8817-2315bcfd6a7d",
        "Social": "9035a113-edad-422f-80ad-5596ed206e27",
        "Económico": "bec39468-e080-4bcd-bac0-9dfd60cb687d",
        "Cultural": "a09b5898-be12-4872-993d-43bc6ed3cee1"
    },
    "XVIII": {
        "Político": "ec5508c4-d5e4-44b9-b5b3-0eefd2ac87e9",
        "Social": "519829d6-1edb-4e19-8be5-88c54f417919",
        "Económico": "32dc1025-08bf-4ae3-9a49-086469bb4a90",
        "Cultural": "47e9c2b9-dfc2-44d7-b77c-83f5f1d1999a"
    },
    "XIX": {
        "Político": "a0322cdf-82c0-4f3b-81b2-ea5d79c09566",
        "Social": "1a39ab28-2cf5-40c6-a9db-2032f98a3cd2",
        "Económico": "7f615832-df79-44f5-a3ca-5e5b8d27b40e",
        "Cultural": "f213aaab-e5b1-46b7-9127-a79aeed50ca1"
    }
}

# RUTA PARA CONSULTAR EL CUADERNO
@app.route('/nil-query', methods=['GET'])
def query_nil():
    century = request.args.get('century')
    realm = request.args.get('realm')
    
    if not century or not realm:
        return jsonify({"status": "error", "message": "Faltan parámetros century o realm"}), 400
    
    notebook_id = NOTEBOOK_MAP.get(century, {}).get(realm)
    
    if not notebook_id:
        return jsonify({"status": "error", "message": f"No se encontró cuaderno para Siglo {century} - {realm}"}), 404

    # NOTA: En un entorno productivo real fuera de Antigravity, 
    # este puente haría una llamada a la API de NotebookLM o usaría un orquestador.
    # Aquí, el modelo Antigravity es quien actúa como el motor de inferencia.
    # El Bridge devuelve una instrucción que el usuario verá que se está procesando.
    
    # Simulación de respuesta estructurada (Antigravity interceptará esto)
    return jsonify({
        "status": "success",
        "notebook_id": notebook_id,
        "century": century,
        "realm": realm,
        "instruction": f"Consulta el cuaderno {notebook_id} y genera el contenido JCR para {realm} en el siglo {century}."
    })

if __name__ == '__main__':
    print("Nil-Bridge iniciado en http://localhost:5000")
    app.run(port=5000, debug=True)
