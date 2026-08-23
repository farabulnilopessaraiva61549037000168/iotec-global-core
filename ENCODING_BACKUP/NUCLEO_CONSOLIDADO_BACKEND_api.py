import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt

# ConfiguraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do JWT
SECRET_KEY = "chave_secreta_super_segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

class UsuarioLogin(BaseModel):
    email: str
    senha: str

def criar_token_jwt(email: str):
    expira = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dados = {"sub": email, "exp": expira}
    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

@app.post("/login")
def login(usuario: UsuarioLogin):
    # SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio vÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lido (em breve usaremos banco de dados)
    if usuario.email == "bruno@email.com" and usuario.senha == "minhaSenha123":
        token = criar_token_jwt(usuario.email)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Credenciais invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lidas!")
@app.post("/login")
def login(usuario: UsuarioLogin):
    if usuario.email == "bruno@email.com" and usuario.senha == "minhaSenha123":
        token = criar_token_jwt(usuario.email)
        return {"access_token": token, "token_type": "bearer"}
 from fastapi import FastAPI
import sqlite3

app = FastAPI()  # Inicializa o FastAPI

# ConexÃƒÆ'Ã†â€™o com o banco de dados SQLite
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Criar tabela de usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios se nÃƒÆ'Ã†â€™o existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT UNIQUE,
    senha TEXT
)
""")
conn.commit()

# Endpoint para verificar se a API estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ funcionando
@app.get("/")
def home():
    return {"mensagem": "API funcionando corretamente!"}

# Endpoint para cadastro de usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios
@app.post("/cadastro")
def cadastro(nome: str, email: str, senha: str):
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conn.commit()
        return {"mensagem": "Cadastro realizado com sucesso!"}
    except sqlite3.IntegrityError:
        return {"mensagem": "Erro: Email jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ cadastrado!"}

# Endpoint para listar usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios cadastrados
@app.get("/usuarios")
def listar_usuarios():
    cursor.execute("SELECT id, nome, email FROM usuarios")
    usuarios = cursor.fetchall()
    return {"usuarios": [{"id": u[0], "nome": u[1], "email": u[2]} for u in usuarios]}


