import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import shutil
import webbrowser
from datetime import datetime
from pathlib import Path
from threading import Timer
from flask import Flask, jsonify, render_template, request

BASE = Path(r"C:\IOTEC")
CORE = BASE / "CORE"
STATE = CORE / "state"
LOGS = CORE / "logs"
CHECKPOINTS = CORE / "checkpoints"
BACKUPS = CORE / "backups"
RELATORIOS = CORE / "relatorios"

for pasta in [CORE, STATE, LOGS, CHECKPOINTS, BACKUPS, RELATORIOS]:
    pasta.mkdir(parents=True, exist_ok=True)

STATE_FILE = STATE / "nucleo_estado.json"
CHECKPOINT_FILE = CHECKPOINTS / "checkpoint_migracao.json"
MODELO_FALHAS_FILE = RELATORIOS / "modelo_relatorio_falhas.json"
EVENT_LOG = LOGS / "eventos_nucleo.log"

app = Flask(__name__)

def agora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def garantir_arquivo(path: Path, default_data):
    if not path.exists():
        path.write_text(json.dumps(default_data, ensure_ascii=False, indent=2), encoding="utf-8")

def carregar_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_json(path: Path, data):
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if path.exists():
        backup = BACKUPS / f"{path.stem}_{stamp}{path.suffix}"
        shutil.copy2(path, backup)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def registrar_log(msg: str):
    with open(EVENT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{agora()}] {msg}\n")

def bootstrap_runtime():
    garantir_arquivo(STATE_FILE, {
        "nucleo": {
            "nome": "IOTEC",
            "status_geral": "EM_REGULAGEM_ESTRUTURAL",
            "start_habilitado": True,
            "operacao_plena": False,
            "identidade_visual": "COCKPIT_PLENO_V2",
            "maturidade": "EM_CONSTRUCAO_SANEADA",
            "ultima_atualizacao": agora()
        },
        "performance": {
            "saude": "PARCIAL",
            "latencia_ms": 0,
            "eventos_ao_vivo": 0,
            "modulos_online": 0,
            "modulos_degradados": 0,
            "modulos_offline": 0
        },
        "gateways": {
            "paypal": {
                "status": "EM_VALIDACAO",
                "aceitando_pagamentos": False,
                "travamento_detectado": True,
                "prioridade": 1
            },
            "picpay": {
                "status": "PENDENTE_DE_CONFIRMACAO",
                "aceitando_pagamentos": False,
                "travamento_detectado": False,
                "prioridade": 1
            }
        },
        "fila_regulagem": [
            {
                "produto_id": "PROD-0001",
                "nome": "Gateway PayPal Oficial",
                "status": "EM_REGULAGEM",
                "problemas_detectados": 1,
                "prioridade": 1,
                "apto_operacao_plena": False
            },
            {
                "produto_id": "PROD-0002",
                "nome": "Cockpit Pleno de Operacoes",
                "status": "EM_CONSTRUCAO",
                "problemas_detectados": 0,
                "prioridade": 1,
                "apto_operacao_plena": False
            }
        ],
        "produtos": [
            {
                "produto_id": "PROD-0001",
                "nome": "Gateway PayPal Oficial",
                "camada": "REGULAGEM",
                "maturidade": "ALTA",
                "setor": "PAGAMENTOS",
                "vinculo_gateway": "PAYPAL",
                "pronto_para_subir": False,
                "ativo": False
            },
            {
                "produto_id": "PROD-0002",
                "nome": "Cockpit Pleno de Operacoes",
                "camada": "REGULAGEM",
                "maturidade": "ALTA",
                "setor": "NUCLEO",
                "vinculo_gateway": "NAO_APLICAVEL",
                "pronto_para_subir": False,
                "ativo": False
            }
        ],
        "incidentes": [
            {
                "erro_id": "ERR-0001",
                "titulo": "Falha na segunda etapa da rota PayPal",
                "modulo": "Gateway PayPal Oficial",
                "produto_id": "PROD-0001",
                "criticidade": "ALTA",
                "status": "AGUARDANDO_REGULAGEM",
                "prioridade": 1,
                "resolucao_automatica_tentada": False
            }
        ],
        "eventos_recentes": [
            {
                "evento_id": "EVT-0001",
                "tipo": "DIAGNOSTICO",
                "mensagem": "Nova concha IOTEC criada com estrutura saneada.",
                "nivel": "INFO",
                "gerado_em": agora()
            }
        ]
    })

    garantir_arquivo(CHECKPOINT_FILE, {
        "migracao": {
            "status": "PRONTA_PARA_INICIAR",
            "ultimo_item_processado": None,
            "ultima_etapa": "BOOTSTRAP_INICIAL",
            "retomada_habilitada": True,
            "ultimo_checkpoint_em": agora()
        }
    })

    garantir_arquivo(MODELO_FALHAS_FILE, {
        "doutrina_relatorio": {
            "objetivo": "Registrar falhas com clareza tecnica, didatica e orientacao de recuperacao rapida.",
            "prioridade_geral": "Modulos que criam ou sustentam receita possuem prioridade maxima."
        }
    })

def carregar_estado():
    bootstrap_runtime()
    return carregar_json(STATE_FILE)

def salvar_estado(data):
    data["nucleo"]["ultima_atualizacao"] = agora()
    salvar_json(STATE_FILE, data)

def carregar_checkpoint():
    bootstrap_runtime()
    return carregar_json(CHECKPOINT_FILE)

def salvar_checkpoint(data):
    salvar_json(CHECKPOINT_FILE, data)

def proximo_id(state, prefixo, chave):
    if chave == "evento_id":
        existentes = [x.get("evento_id", "") for x in state.get("eventos_recentes", [])]
    else:
        existentes = [x.get("erro_id", "") for x in state.get("incidentes", [])]

    nums = []
    for item in existentes:
        try:
            nums.append(int(item.replace(prefixo, "")))
        except Exception:
            pass
    novo = max(nums) + 1 if nums else 1
    return f"{prefixo}{novo:04d}"

def traduzir(texto):
    mapa = {
        "EM_REGULAGEM_ESTRUTURAL": "Em regulagem estrutural",
        "EM_CONSTRUCAO_SANEADA": "Em construcao saneada",
        "EM_VALIDACAO": "Em validacao",
        "PENDENTE_DE_CONFIRMACAO": "Pendente de confirmacao",
        "EM_REGULAGEM": "Em regulagem",
        "EM_CONSTRUCAO": "Em construcao",
        "AGUARDANDO_REGULAGEM": "Aguardando regulagem",
        "OPERANDO": "Operando",
        "PAUSADO": "Pausado",
        "REGULAGEM": "Regulagem",
        "OPERACAO_PLENA": "Operacao plena",
        "NAO_APLICAVEL": "Nao aplicavel",
        "ALTA": "Alta",
        "MEDIA": "Media",
        "BAIXA": "Baixa",
        "INFO": "Info",
        "SUCESSO": "Sucesso",
        "ALERTA": "Alerta",
        "ATIVA": "Ativa",
        "PARCIAL": "Parcial"
    }
    if texto is None:
        return "-"
    if not isinstance(texto, str):
        return texto
    return mapa.get(texto, texto.replace("_", " ").capitalize())

def percentual_nucleo(state):
    total = len(state.get("produtos", []))
    ativos = len([p for p in state.get("produtos", []) if p.get("ativo")])
    if total == 0:
        return 0
    return int((ativos / total) * 100)

def nivel_visual(percentual):
    if percentual >= 80:
        return "ALTO"
    if percentual >= 40:
        return "MEDIO"
    return "INICIAL"

def registrar_evento(state, tipo, mensagem, nivel="INFO"):
    evento = {
        "evento_id": proximo_id(state, "EVT-", "evento_id"),
        "tipo": tipo,
        "mensagem": mensagem,
        "nivel": nivel,
        "gerado_em": agora()
    }
    state.setdefault("eventos_recentes", []).insert(0, evento)
    state["eventos_recentes"] = state["eventos_recentes"][:100]
    registrar_log(f"{tipo} | {nivel} | {mensagem}")

@app.route("/")
def home():
    state = carregar_estado()
    checkpoint = carregar_checkpoint()
    progresso = percentual_nucleo(state)
    return render_template(
        "cockpit_iotec_v2.html",
        dados=state,
        checkpoint=checkpoint,
        traduzir=traduzir,
        progresso=progresso,
        nivel_visual=nivel_visual(progresso)
    )

@app.route("/api/status")
def api_status():
    return jsonify(carregar_estado())

@app.route("/api/checkpoint")
def api_checkpoint():
    return jsonify(carregar_checkpoint())

@app.route("/api/health")
def api_health():
    state = carregar_estado()
    return jsonify({
        "ok": True,
        "service": "IOTEC_COCKPIT_PLENO_V2",
        "nucleo": state.get("nucleo", {}),
        "gateways": state.get("gateways", {}),
        "incidentes_abertos": len(state.get("incidentes", [])),
        "produtos_total": len(state.get("produtos", [])),
        "produtos_ativos": len([p for p in state.get("produtos", []) if p.get("ativo")])
    })

@app.route("/api/start", methods=["POST"])
def api_start():
    state = carregar_estado()
    cp = carregar_checkpoint()

    state["nucleo"]["status_geral"] = "OPERANDO"
    state["nucleo"]["operacao_plena"] = True
    state["performance"]["saude"] = "ATIVA"

    registrar_evento(state, "START", "Nucleo colocado em operacao.", "SUCESSO")

    cp["migracao"]["status"] = "EM_EXECUCAO"
    cp["migracao"]["ultima_etapa"] = "NUCLEO_START"
    cp["migracao"]["ultimo_checkpoint_em"] = agora()

    salvar_estado(state)
    salvar_checkpoint(cp)

    return jsonify({"ok": True, "status": "OPERANDO"})

@app.route("/api/stop", methods=["POST"])
def api_stop():
    state = carregar_estado()
    cp = carregar_checkpoint()

    state["nucleo"]["status_geral"] = "PAUSADO"
    state["nucleo"]["operacao_plena"] = False
    state["performance"]["saude"] = "PARCIAL"

    registrar_evento(state, "STOP", "Nucleo pausado manualmente.", "INFO")

    cp["migracao"]["status"] = "PAUSADO"
    cp["migracao"]["ultima_etapa"] = "NUCLEO_STOP"
    cp["migracao"]["ultimo_checkpoint_em"] = agora()

    salvar_estado(state)
    salvar_checkpoint(cp)

    return jsonify({"ok": True, "status": "PAUSADO"})

@app.route("/api/produto/promover", methods=["POST"])
def api_produto_promover():
    body = request.get_json(force=True)
    produto_id = body.get("produto_id", "").strip()

    state = carregar_estado()
    encontrado = False

    for produto in state.get("produtos", []):
        if produto.get("produto_id") == produto_id:
            produto["camada"] = "OPERACAO_PLENA"
            produto["pronto_para_subir"] = True
            produto["ativo"] = True
            encontrado = True
            registrar_evento(state, "PROMOCAO", f"Produto {produto_id} promovido para operacao plena.", "SUCESSO")

    for item in state.get("fila_regulagem", []):
        if item.get("produto_id") == produto_id:
            item["status"] = "APROVADO"
            item["apto_operacao_plena"] = True
            item["problemas_detectados"] = 0

    if not encontrado:
        return jsonify({"ok": False, "erro": "Produto nao encontrado."}), 404

    salvar_estado(state)
    return jsonify({"ok": True, "produto_id": produto_id})

@app.route("/api/incidente/registrar", methods=["POST"])
def api_incidente_registrar():
    body = request.get_json(force=True)
    state = carregar_estado()

    erro_id = proximo_id(state, "ERR-", "erro_id")
    incidente = {
        "erro_id": erro_id,
        "titulo": body.get("titulo", "Ocorrencia sem titulo"),
        "modulo": body.get("modulo", "INDEFINIDO"),
        "produto_id": body.get("produto_id", "SEM_PRODUTO"),
        "criticidade": body.get("criticidade", "MEDIA"),
        "status": body.get("status_atual", "NOVO"),
        "prioridade": body.get("prioridade", 3),
        "resolucao_automatica_tentada": body.get("resolucao_automatica_tentada", False),
        "gerado_em": agora()
    }

    state.setdefault("incidentes", []).insert(0, incidente)
    registrar_evento(state, "INCIDENTE", f"{erro_id} registrado: {incidente['titulo']}", "ALERTA")
    salvar_estado(state)

    return jsonify({"ok": True, "incidente": incidente})

def abrir_navegador():
    try:
        webbrowser.open("http://127.0.0.1:5080")
    except Exception:
        pass

if __name__ == "__main__":
    bootstrap_runtime()
    Timer(1.4, abrir_navegador).start()
    app.run(host="0.0.0.0", port=5080, debug=False)


