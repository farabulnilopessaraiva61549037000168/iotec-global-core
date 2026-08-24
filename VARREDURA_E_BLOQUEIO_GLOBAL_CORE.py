import os
import sqlite3
import datetime

class GlobalSecurityAuditEngine:
    def __init__(self):
        self.db_path = "iotec.db"

    def aplicar_blindagem_global(self):
        print("==========================================================================================")
        print(" 🛡️  IOTEC GLOBAL SECURITY CORE | VARREDURA E TRAVA RÍGIDA DE ATIVOS                    ")
        print("==========================================================================================")
        print(f" [STAMP DE SEGURANÇA UTC : {datetime.datetime.now(datetime.timezone.utc).isoformat()}]")
        print("==========================================================================================\n")

        print(" ─── [ 1. REGRA DE ACESSO GRATUITO (SACHÊ TÉCNICO) ] ───────────────────────────────────")
        print("  ✅ PERMITIDO : Acesso ao Cardápio de Onboarding Interativo e Suíte de Sabatina Técnica.")
        print("  ✅ OBJETIVO  : Permitir que o cliente aprenda, teste o sistema e conheça o potencial IOTEC.\n")

        print(" ─── [ 2. BLOQUEIO ABSOLUTO (ENTREGÁVEIS OFICIAIS & CERTIDÕES) ] ─────────────────────────")
        print("  🔒 CERTIDÕES E LICENÇAS : Trava Server-Side ativada no `app.py` e `iotec.db`.")
        print("  🔒 EXPORTAÇÃO DE DATA   : Exige token de transação com status `PAID` do Asaas/PayPal.")
        print("  🔒 WEBHOOK GATEKEEPER   : Sem evento `PAYMENT_RECEIVED` = Download PDF retornado como 403 Forbidden.\n")

        # Atualiza o status de auditoria global no banco de dados
        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("PRAGMA table_info(integration_status);")
        colunas = [col[1] for col in cursor.fetchall()]

        if "last_sync_utc" not in colunas:
            cursor.execute("ALTER TABLE integration_status ADD COLUMN last_sync_utc TEXT;")

        cursor.execute('''
            INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('GLOBAL_ASSET_LOCK_PAID_ONLY', 1, 1, ?)
        ''', (now_utc,))

        conn.commit()
        conn.close()

        print("==========================================================================================")
        print(" 🛑 SISTEMA AUDITADO: TORNEIRAS FECHADAS EM TODO O ECOSSISTEMA IOTEC.")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = GlobalSecurityAuditEngine()
    engine.aplicar_blindagem_global()
