from app import db
class Curso(db.Model):
    __tablename__ = 'cursos'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f"Curso: {self.nome}"
