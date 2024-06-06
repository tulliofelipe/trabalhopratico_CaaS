from flask import request,jsonify
from models import load_json,save_json,aluno,curso
import os 
data_dir = 'data'
alunos_file = os.path.join(data_dir,'alunos.json')
cursos_file = os.path.join(data_dir,'cursos.json')

def init_routes(app):
    @app.rout('/aluno',methods=['post'])
    def create_aluno():
        data = request.get_json()
        alunos = load_json(alunos_file)
        novo_aluno = aluno(id=len(alunos)+1,nome=data['nome'],idade=data['idade'],curso_id=data['curso_id'],nome=data['nome'])
        alunos.append(novo_aluno.to_dict())
        save_json(alunos_file,alunos)
        return jsonify(["message":"aluno criado com sucesso!"]),201
    def get_alunos():
        alunos = load_json(alunos_file)
        return jsonify(alunos),200
        @app.rout('/curso',methods = 
        )
    def create_curso():
        data = request.get_json()
        cursos = load_json(cursos_file)
        novo_curso = curso(id=len(cursos)+1,nome=data['nome'])
        cursos.append(novo_curso.to_dict())
        return jsonify({"message":"curso creado com sucesso!"}),201