# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import os

CSV_PATH = r"C:\IOTEC\esteira_leads.csv"
CAIXA_PATH = r"C:\IOTEC\caixa.csv"

st.set_page_config(page_title="IOTEC - Central Unificada", layout="wide")
st.title("🏛️ CENTRO DE OPERAÇÕES IOTEC - CENTRAL UNIFICADA DE MONITORAMENTO")

# BARRA LATERAL - PAINEL DE CONTROLADORIA
st.sidebar.header("🕹️ Painel de Operações")
st.sidebar.info("Modo: Localhost Ativo\nIntegracao: PicPay / PayPal / Pix")

tab1, tab2 = st.tabs(["📊 Funil & Disparos", "💰 Caixa & Alertas Financeiros"])

with tab1:
    if os.path.exists(CSV_PATH):
        try:
            df = pd.read_csv(CSV_PATH, sep=';', encoding='utf-8-sig')
            if not df.empty and 'Status' in df.columns:
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Base Total", len(df))
                col2.metric("Fila de Entrada", len(df[df['Status'] == 'NOVO']))
                col3.metric("Prontos p/ Disparo", len(df[df['Status'] == 'PRONTO_PARA_CONTATO']))
                col4.metric("Contatados", len(df[df['Status'] == 'CONTATADO']))

                st.subheader("📋 Estado Atual da Esteira")
                st.dataframe(df, use_container_width=True)
            else:
                st.warning("Base sem registros processados.")
        except Exception as e:
            st.error(f"Erro ao ler base: {e}")
    else:
        st.error("Arquivo esteira_leads.csv nao encontrado.")

with tab2:
    st.subheader("🚨 Alertas de Receita e Conciliação Financeira")
    if os.path.exists(CSV_PATH):
        try:
            df = pd.read_csv(CSV_PATH, sep=';', encoding='utf-8-sig')
            clientes = df[df['Status'] == 'CLIENTE_ATIVO'] if 'Status' in df.columns else []
            faturamento = len(clientes) * 297.00

            m1, m2 = st.columns(2)
            m1.metric("Clientes Convertidos", len(clientes))
            m2.metric("Receita Confirmada", f"R$ {faturamento:.2f}")

            if len(clientes) > 0:
                st.success(f"🎉 Alerta Prioritario: {len(clientes)} pagamento(s) confirmado(s)!")
                st.dataframe(clientes)
            else:
                st.info("Aguardando novas confirmacoes de pagamento via PicPay/PayPal/Pix.")
        except Exception as e:
            st.error(f"Erro ao carregar caixa: {e}")

    if os.path.exists(CAIXA_PATH):
        st.subheader("📈 Historico de Auditoria do Caixa")
        df_caixa = pd.read_csv(CAIXA_PATH, sep=';', encoding='utf-8-sig')
        st.dataframe(df_caixa.tail(10), use_container_width=True)