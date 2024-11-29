from flask import Blueprint, render_template, request, redirect, flash
from models import Candidatos
from database import db

bp_candidato = Blueprint('candidatos', __name__, template_folder="templates")

@bp_candidato.route('/')
def index():
    dados = Candidatos.query.all()
    return render_template('candidato.html', candidatos = dados)
    
@bp_candidato.route('/add')
def add():
    return render_template('candidato_add.html')

@bp_candidato.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    profissao = request.form.get('profissao')
    if nome and profissao:
        bd_candidato = Candidatos(nome, profissao)
        db.session.add(bd_candidato)
        db.session.commit()
        flash('salvo com sucesso!!!')
        return redirect('/candidatos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/candidatos/add')