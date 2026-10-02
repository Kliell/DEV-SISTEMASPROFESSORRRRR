from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base, engine, SessionLocal

# --- Modelo Existente ---
class Departamento(Base):
    __tablename__ = 'departamentos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    sigla = Column(String(10), nullable=False)
    ativo = Column(Boolean, default=True)


# --- Parte 1: Criar o modelo Cargo ---
class Cargo(Base):
    __tablename__ = 'cargos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    nivel = Column(String(50), nullable=False)
    salario_min = Column(Float, nullable=False)
    salario_max = Column(Float, nullable=False)


# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inserir dados e realizar consultas via sessão
db = SessionLocal()

try:
    # --- Parte 2: Popular a tabela de cargos ---
    if db.query(Cargo).count() == 0:
        cargos = [
            Cargo(nome="Desenvolvedor Junior", nivel="Junior", salario_min=3000.0, salario_max=4500.0),
            Cargo(nome="Desenvolvedor Pleno", nivel="Pleno", salario_min=5000.0, salario_max=8000.0),
            Cargo(nome="Designer Junior", nivel="Junior", salario_min=2800.0, salario_max=4200.0),
            Cargo(nome="Designer Senior", nivel="Senior", salario_min=7000.0, salario_max=11000.0),
        ]
        db.add_all(cargos)
        db.commit()
        print("Cargos inseridos com sucesso!")
    else:
        print("Banco já populado")

    # --- Parte 3: Consultar cargos com filtros ---
    
    # 1. Filtro Junior -> retorna cargos de nível Junior
    cargos_junior = db.query(Cargo).filter(Cargo.nivel == "Junior").all()
    print("\n--- Cargos Junior ---")
    for cargo in cargos_junior:
        print(f"ID: {cargo.id} | Nome: {cargo.nome} | Nível: {cargo.nivel}")

    # 2. Busca por Designer -> retorna cargo com salario_max correto
    designer = db.query(Cargo).filter(Cargo.nome.like("%Designer%")).first()
    if designer:
        print(f"\n--- Detalhes do Designer ---")
        print(f"Nome: {designer.nome} | Salário Máximo: R$ {designer.salario_max:.2f}")

finally:
    db.close()