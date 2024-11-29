from flask import Blueprint, render_template, request, redirect, flash
from models import Vagas, Candidatos
from database import db

bp_vaga = Blueprint('vagas', __name__, template_folder="templates")

@bp_vaga.route('/')
def index():
    dados = Vagas.query.all()
    return render_template('vaga.html', vagas = dados)
    
@bp_vaga.route('/add')
def add():
    c = Candidatos.query.all()
    return render_template('vaga_add.html', candidatos = c)

@bp_vaga.route('/save', methods=['POST'])
def save():
    titulo = request.form.get('titulo')
    salario = request.form.get('salario')
    id_candidato = request.form.get('id_candidato')
    if titulo and salario and id_candidato:
        bd_vagas = Vagas(titulo, salario, id_candidato)
        db.session.add(bd_vagas)
        db.session.commit()
        flash('Salvo com sucesso!!!')
        return redirect('/vagas')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/vagas/add')

@bp_vaga.route("/remove/<int:id>")
def remove(id):
    dados = Vagas.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Excluido com sucesso!')
        return redirect("/vagas")
    else:
        flash("Item não encontrado")
        return redirect("/vagas")