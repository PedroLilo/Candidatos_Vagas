from database import db

class Candidatos(db.Model):
    __tablename__ = 'candidato'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    profissao = db.Column(db.String(50))

    def __init__(self, nome, profissao):
        self.nome = nome
        self.profissao = profissao

    def __repr__(self):
        return "<Candidato {}>".format(self.nome)

class Vagas(db.Model):
    __tablename__ = 'vaga'
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100))
    salario = db.Column(db.Numeric(10,2))
    id_candidato = db.Column(db.Integer, db.ForeignKey('candidato.id'))
    
    candidato = db.relationship('Candidatos', foreign_keys=id_candidato)

    def __init__(self, titulo, salario, id_candidato):
        self.titulo = titulo
        self.salario = salario
        self.id_candidato = id_candidato

    def __repr__(self):
        return "<Candidato {}>".format(self.titulo)