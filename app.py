from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'STRINgqUENINGUémsAbe'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/Candidatos_Vagas"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLACHEMY_TRACK_MODIFICATIOS'] = False
from database import db
from flask_migrate import Migrate
from models import Vagas, Candidatos
db.init_app(app)
migrate = Migrate(app, db)
from modulos.candidatos.candidatos import bp_candidato
app.register_blueprint(bp_candidato, url_prefix='/candidatos')
from modulos.vagas.vagas import bp_vaga
app.register_blueprint(bp_vaga, url_prefix='/vagas')

@app.route('/')
def index():
    return render_template("index.html")


