import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import shutil
from datetime import datetime
from pathlib import Path
from flask import Flask, jsonify, render_template, request

BASE = Path(r"C:\IOTEC")
CORE = BASE / "CORE"
STATE = CORE / "state"
LOGS = CORE / "logs"
CHECKPOINTS = CORE / "checkpoints"
BACKUPS = CORE / "backups"
RELATORIOS = CORE / "relatorios"

STATE_FILE = STATE / "nucleo_estado.json"
CHECKPOINT_FILE = CHECKPOINTS / "checkpoint_migracao.json"
MODELO_FALHAS_FILE = RELATORIOS / "modelo_relatorio_falhas.json"
EVENT_LOG = LOGS / "eventos_nucleo.log"

app = Flask(__name__)

def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ensure_file(path: Path, default_data):
    if not path.exists():
        path.write_text(json.dumps(default_data, ensure_ascii=False, indent=2), encoding="utf-8")

def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path: Path, data):
    backup_name = path.stem + "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + path.suffix
    backup_path = BACKUPS / backup_name
    if path.exists():
        shutil.copy2(path, backup_path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def append_log(msg: str):
    linha = f"[{now_str()}] {msg}\n"
    with open(EVENT_LOG, "a", encoding="utf-8") as f:
        f.write(linha)

def bootstrap_runtime():
    ensure_file(STATE_FILE, {
        "nucleo": {"nome": "IOTEC", "status_geral": "INDEFINIDO"},
        "performance": {},
        "gateways": {},
        "fila_regulagem": [],
        "produtos": [],
        "incidentes": [],
        "eventos_recentes": []
    })
    ensure_file(CHECKPOINT_FILE, {
        "migracao": {
            "status": "PRONTA",
            "ultimo_item_processado": None,
            "ultima_etapa": "BOOTSTRAP",
            "retomada_habilitada": True,
            "ultimo_checkpoint_em": now_str()
        }
    })
    ensure_file(MODELO_FALHAS_FILE, {"estrutura": []})

def load_state():
    bootstrap_runtime()
    return load_json(STATE_FILE)

def save_state(data):
    save_json(STATE_FILE, data)

def load_checkpoint():
    bootstrap_runtime()
    return load_json(CHECKPOINT_FILE)

def save_checkpoint(data):
    save_json(CHECKPOINT_FILE, data)

def next_error_id(state):
    existentes = [x.get("erro_id", "") for x in state.get("incidentes", [])]
    nums = []
    for item in existentes:
        try:
            nums.append(int(item.replace("ERR-", "")))
        except:
            pass
    novo = max(nums) + 1 if nums else 1
    return f"ERR-{novo:04d}"

def next_event_id(state):
    existentes = [x.get("evento_id", "") for x in state.get("eventos_recentes", [])]
    nums = []
    for item in existentes:
        try:
            nums.append(int(item.replace("EVT-", "")))
        except:
            pass
    novo = max(nums) + 1 if nums else 1
    return f"EVT-{novo:04d}"

def registrar_evento(state, tipo, mensagem, nivel="INFO"):
    evento = {
        "evento_id": next_event_id(state),
        "tipo": tipo,
        "mensagem": mensagem,
        "nivel": nivel,
        "gerado_em": now_str()
    }
    state.setdefault("eventos_recentes", []).insert(0, evento)
    state["eventos_recentes"] = state["eventos_recentes"][:50]
    append_log(f"{tipo} | {nivel} | {mensagem}")
    return state

def registrar_incidente(
    titulo,
    modulo,
    produto_id,
    criticidade,
    descricao,
    impacto,
    causa,
    acao_automatica,
    status_atual,
    prioridade,
    solucao_imediata,
    solucao_corretiva,
    solucao_preventiva,
    solucao_estrutural
):
    state = load_state()
    erro_id = next_error_id(state)
    incidente = {
        "erro_id": erro_id,
        "titulo": titulo,
        "modulo": modulo,
        "produto_id": produto_id,
        "criticidade": criticidade,
        "status": status_atual,
        "prioridade": prioridade,
        "gerado_em": now_str(),
        "relatorio": {
            "1_identificacao_da_ocorrencia": {
                "id": erro_id,
                "data_hora": now_str(),
                "modulo": modulo,
                "produto_id": produto_id,
                "contexto": titulo
            },
            "2_descricao_objetiva_do_problema": {
                "descricao": descricao
            },
            "3_impacto_operacional": {
                "impacto": impacto
            },
            "4_causa_provavel_ou_detectada": {
                "causa": causa
            },
            "5_acao_automatica_tentada_pelo_nucleo": {
                "acao": acao_automatica
            },
            "6_status_atual": {
                "status": status_atual
            },
            "7_prioridade_de_resposta": {
                "prioridade": prioridade
            },
            "8_solucao_imediata": {
                "sugestao": solucao_imediata
            },
            "9_solucao_corretiva": {
                "sugestao": solucao_corretiva
            },
            "10_solucao_preventiva": {
                "sugestao": solucao_preventiva
            },
            "11_solucao_estrutural": {
                "sugestao": solucao_estrutural
            }
        }
    }
    state.setdefault("incidentes", []).insert(0, incidente)
    registrar_evento(state, "INCIDENTE", f"{erro_id} registrado: {titulo}", "ALERTA")
    save_state(state)
    return incidente

@app.route("/")
def home():
    dados = load_state()
    checkpoint = load_checkpoint()
    return render_template("cockpit_iotec.html", dados=dados, checkpoint=checkpoint)

@app.route("/api/status")
def api_status():
    return jsonify(load_state())

@app.route("/api/checkpoint")
def api_checkpoint():
    return jsonify(load_checkpoint())

@app.route("/api/start", methods=["POST"])
def api_start():
    state = load_state()
    state["nucleo"]["status_geral"] = "OPERANDO"
    state["nucleo"]["operacao_plena"] = True
    state["performance"]["saude"] = "ATIVA"
    registrar_evento(state, "START", "Nucleo colocado em operacao.", "SUCESSO")
    save_state(state)

    cp = load_checkpoint()
    cp["migracao"]["status"] = "EM_EXECUCAO"
    cp["migracao"]["ultima_etapa"] = "NUCLEO_START"
    cp["migracao"]["ultimo_checkpoint_em"] = now_str()
    save_checkpoint(cp)

    return jsonify({"ok": True, "status": "OPERANDO"})

@app.route("/api/stop", methods=["POST"])
def api_stop():
    state = load_state()
    state["nucleo"]["status_geral"] = "PAUSADO"
    state["nucleo"]["operacao_plena"] = False
    registrar_evento(state, "STOP", "Nucleo pausado manualmente.", "INFO")
    save_state(state)

    cp = load_checkpoint()
    cp["migracao"]["status"] = "PAUSADO"
    cp["migracao"]["ultima_etapa"] = "NUCLEO_STOP"
    cp["migracao"]["ultimo_checkpoint_em"] = now_str()
    save_checkpoint(cp)

    return jsonify({"ok": True, "status": "PAUSADO"})

@app.route("/api/produto/promover", methods=["POST"])
def api_produto_promover():
    body = request.get_json(force=True)
    produto_id = body.get("produto_id", "").strip()

    state = load_state()
    achou = False

    for produto in state.get("produtos", []):
        if produto.get("produto_id") == produto_id:
            produto["camada"] = "OPERACAO_PLENA"
            produto["pronto_para_subir"] = True
            produto["ativo"] = True
            achou = True
            registrar_evento(
                state,
                "PROMOCAO",
                f"Produto {produto_id} promovido para operacao plena.",
                "SUCESSO"
            )

    for item in state.get("fila_regulagem", []):
        if item.get("produto_id") == produto_id:
            item["status"] = "APROVADO"
            item["apto_operacao_plena"] = True
            item["problemas_detectados"] = 0

    if not achou:
        return jsonify({"ok": False, "erro": "Produto nao encontrado."}), 404

    save_state(state)
    return jsonify({"ok": True, "produto_id": produto_id})

@app.route("/api/incidente/registrar", methods=["POST"])
def api_incidente_registrar():
    body = request.get_json(force=True)

    incidente = registrar_incidente(
        titulo=body.get("titulo", "Ocorrencia sem titulo"),
        modulo=body.get("modulo", "INDEFINIDO"),
        produto_id=body.get("produto_id", "SEM_PRODUTO"),
        criticidade=body.get("criticidade", "MEDIA"),
        descricao=body.get("descricao", "Sem descricao."),
        impacto=body.get("impacto", "Sem impacto descrito."),
        causa=body.get("causa", "Em investigacao."),
        acao_automatica=body.get("acao_automatica", "Nenhuma acao automatica registrada."),
        status_atual=body.get("status_atual", "NOVO"),
        prioridade=body.get("prioridade", 3),
        solucao_imediata=body.get("solucao_imediata", "Avaliar e conter impacto."),
        solucao_corretiva=body.get("solucao_corretiva", "Ajustar modulo afetado."),
        solucao_preventiva=body.get("solucao_preventiva", "Criar monitoramento e barramento."),
        solucao_estrutural=body.get("solucao_estrutural", "Revisar arquitetura do fluxo.")
    )

    return jsonify({"ok": True, "incidente": incidente})

@app.route("/api/health")
def api_health():
    state = load_state()
    return jsonify({
        "ok": True,
        "service": "IOTEC_COCKPIT_PLENO",
        "nucleo": state.get("nucleo", {}),
        "gateways": state.get("gateways", {}),
        "incidentes_abertos": len(state.get("incidentes", [])),
        "produtos_total": len(state.get("produtos", []))
    })

if __name__ == "__main__":
    bootstrap_runtime()
    app.run(host="0.0.0.0", port=5080, debug=False)


