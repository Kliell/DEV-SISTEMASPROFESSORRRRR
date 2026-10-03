from app.database import engine, SessionLocal
from app import models
from app.models import Genero, Autor, Livro

# Cria as tabelas definidas nos modelos
models.Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso")

db = SessionLocal()

# generos
gen1 = Genero(nome="Romance")
gen2 = Genero(nome="Terror")
gen3 = Genero(nome="Drama")

db.add(gen1)
db.add(gen2)
db.add(gen3)
db.commit()
db.refresh(gen1)
db.refresh(gen2)
db.refresh(gen3)
print(f'Generos criados: {gen1.id}, {gen2.id}, {gen3.id}')

# autores: inserir todos de uma vez
autores = [
    Autor(nome="Collen Hoover", nacionalidade="Estadunidense"),
    Autor(nome="Stephen King", nacionalidade="Estadunidense"),
    Autor(nome="William Shakespeare", nacionalidade="Inglês"),
]
db.add_all(autores)
db.commit()   # depois do commit, cada autor já tem seu id

# ler um por um na hora de imprimir
print("\nAutores criados:")
for a in autores:
    print(f" [{a.id}] {a.nome} - {a.nacionalidade}")

autor1, autor2, autor3 = autores   # para usar nos livros

# # autores
# autor1 = Autor(nome="Collen Hoover", nacionalidade="Estadunidense")
# autor2 = Autor(nome="Stephen King", nacionalidade="Estadunidense")
# autor3 = Autor(nome="William Shakespeare", nacionalidade="Inglês")

# db.add(autor1)
# db.add(autor2)
# db.add(autor3)
# db.commit()
# db.refresh(autor1)
# db.refresh(autor2)
# db.refresh(autor3)
# print(f'Autores criados: {autor1.id}, {autor2.id}, {autor3.id}')

# livros
livros = [
    Livro(titulo="Verity", ano_publicacao=2018,
            genero_id=gen1.id, autor_id=autor1.id),
    Livro(titulo="It: A Coisa", ano_publicacao=1986, 
            genero_id=gen2.id, autor_id=autor2.id),
    Livro(titulo="Carrie", ano_publicacao=1974,
            genero_id=gen2.id, autor_id=autor2.id),
    Livro(titulo="Hamlet", ano_publicacao=1599,
            genero_id=gen3.id, autor_id=autor3.id),
    Livro(titulo="Romeu e Julieta", ano_publicacao=1592, 
            genero_id=gen3.id, autor_id=autor3.id)
]

db.add_all(livros)
db.commit()
print(f"{len(livros)} livros inseridos")

# listar para confirmar
print("\nLivros no banco:")
for l in db.query(Livro).all():
    autor = db.get(Autor, l.autor_id)   # busca o autor pelo id, um por vez
    print(f" [{l.id}] {l.titulo} ({l.ano_publicacao}), {autor.nome}")

db.close()

# for l in livros:
#     db.add(l)
# db.commit()
# print(f' {len(livros)} livros inseridos')

# # Listar pra confirmar
# todos = db.query(Livro).all()
# print("\n Livros no banco")
# for l in todos:
#     print(f' [{l.id}] {l.titulo} ({l.ano_publicacao}), {autor.nome}')
# db.close()