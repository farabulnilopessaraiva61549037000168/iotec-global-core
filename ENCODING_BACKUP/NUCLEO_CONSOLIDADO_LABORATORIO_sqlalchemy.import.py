import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
from sqlalchemy.orm import sessionmaker

# ConexÃƒÆ'Ã†â€™o
engine = create_engine('sqlite:///equip.db')
metadata = MetaData()

# Tabela
dados = Table('dados', metadata,
    Column('id', Integer, primary_key=True),
    Column('fonte', String),
    Column('informacao', String),
    Column('valor', Float)
)

metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o exemplo
def salvar_dado(fonte, informacao, valor):
    ins = dados.insert().values(fonte=fonte, informacao=informacao, valor=valor)
    conn = engine.connect()
    conn.execute(ins)
    conn.close()
    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Dado salvo: {informacao}")

salvar_dado('JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico', 'Processo congestionado', 3000.0)



