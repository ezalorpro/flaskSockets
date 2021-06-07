import os
import os.path as op

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_socketio import SocketIO

static_files = op.join(op.dirname(__file__), "static")

app = Flask(__name__, static_folder="../frontend/dist", template_folder="../frontend/dist")
app.config.from_pyfile("../config/config.py")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app, prefix="/api/")
socketio = SocketIO(app, cors_allowed_origins="*")

class Users(Resource):
    def get(asd):
        response = [
            {
                "nombre": "kleiver carrasco",
                "ocupacion": "ingeniero" 
            },
            {
                "nombre": "kleiver carrasco",
                "ocupacion": "ingeniero" 
            },
            {
                "nombre": "kleiver carrasco",
                "ocupacion": "ingeniero" 
            },
            {
                "nombre": "kleiver carrasco",
                "ocupacion": "ingeniero" 
            },
            {
                "nombre": "kleiver carrasco",
                "ocupacion": "ingeniero" 
            }
        ]
        return jsonify(response)
    
    def post(self):
        data = request.get_json(force=True)
        print(data)
        socketio.send("myEvent", data)   

api.add_resource(Users, "/users/")

@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")
def frontend(path):
    return "hola"

@socketio.on("my event")
def my_event_handler():
    socketio.emit("myEvent", {"nombre": "jesus", "ocupacion": "vago"})

@socketio.on('connect')
def test_connect():
    socketio.emit('connect', {'data': 'Connected'})