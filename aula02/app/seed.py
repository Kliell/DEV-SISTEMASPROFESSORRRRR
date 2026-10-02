from app.database import SessionLocal
from app.models import Departamento, Cargo, Funcionario

def popular_banco():
    db = SessionLocal()   # abrir sessão
    try:
        # Se já tem dados, não inserir de novo
        if db.query(Departamento).count() > 0:
            print('Banco já preenchido. Pulando...')
            return

        db.add_all([
            Departamento(nome='Tecnologia da Informação', sigla='TI'),
            Departamento(nome='Recursos Humanos', sigla='RH'),
            Departamento(nome='Financeiro', sigla='FIN'),
            Departamento(nome='Comercial', sigla='COM'),
        ])

        db.add_all([
            Cargo(titulo='Desenvolvedor', nivel='Junior', salario_min=2500, salario_max=4000),
            Cargo(titulo='Desenvolvedor', nivel='Pleno', salario_min=4000, salario_max=7000),
            Cargo(titulo='Designer', nivel='Junior', salario_min=2200, salario_max=3500),
            Cargo(titulo='Analista RH', nivel='Pleno', salario_min=3500, salario_max=6000),
        ])

        db.add_all([
            Funcionario(nome='Kevin', email='kevincamposliell@gmail.com', telefone=61981890752, salario=50000),
            Funcionario(nome='Thiago', email='thiagoh280708@gmail.com', telefone=61986563146, salario=500),
            Funcionario(nome='Gustavo', email='gustavomamando@gmail.com', telefone=61987251145, salario=100),
            Funcionario(nome='Igor', email='kevincamposliell@gmail.com', telefone=61981666666, salario=50000),
        ])

        db.commit()     # confirma tudo no banco de uma vez
        print('Banco preenchido com sucesso')

    except Exception as erro:
        db.rollback()   # desfaz tudo se der erro
        print(f'Erro: {erro}')
    finally:
        db.close()      # lembre-se sempre de fechar a sessão
if __name__=='__main__':
    popular_banco()