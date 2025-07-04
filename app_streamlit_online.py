
import streamlit as st

st.set_page_config(page_title="Assistente Técnico de Licitações", layout="centered")

st.title("📡 Assistente Técnico de Licitações - Equipamentos de Rede")
st.markdown("Preencha os requisitos técnicos do edital e veja os modelos mais compatíveis disponíveis.")

# Requisitos do edital
req_portas = st.number_input("🔌 Portas Gigabit", value=48, min_value=0)
req_uplinks = st.number_input("🔗 Uplinks SFP+", value=4, min_value=0)
req_poe = st.selectbox("⚡ Suporte a PoE?", ["Sim", "Não"]) == "Sim"
req_stack = st.selectbox("📚 Empilhável (Stack)?", ["Sim", "Não"]) == "Sim"
req_snmp = st.selectbox("📡 Gerenciamento SNMP?", ["Sim", "Não"]) == "Sim"
req_auth = st.selectbox("🔐 Autenticação 802.1X?", ["Sim", "Não"]) == "Sim"

requisitos = {
    "portas_gigabit": req_portas,
    "uplinks_sfp+": req_uplinks,
    "poe": req_poe,
    "empilhamento": req_stack,
    "snmp": req_snmp,
    "autenticacao_8021x": req_auth
}

# Banco de equipamentos simulados
equipamentos = [
    {
        "fabricante": "Huawei",
        "modelo": "S5735S-L48T4X-A1",
        "portas_gigabit": 48,
        "uplinks_sfp+": 4,
        "poe": False,
        "empilhamento": True,
        "snmp": True,
        "autenticacao_8021x": True,
        "observacoes": "Sem PoE. Indicado para ambientes com alimentação externa."
    },
    {
        "fabricante": "Huawei",
        "modelo": "S5735S-L48P4X-A1",
        "portas_gigabit": 48,
        "uplinks_sfp+": 4,
        "poe": True,
        "empilhamento": True,
        "snmp": True,
        "autenticacao_8021x": True,
        "observacoes": "PoE+ até 370W. Ideal para APs e telefones IP."
    },
    {
        "fabricante": "TP-Link",
        "modelo": "T2600G-52TS",
        "portas_gigabit": 48,
        "uplinks_sfp+": 4,
        "poe": False,
        "empilhamento": False,
        "snmp": True,
        "autenticacao_8021x": True,
        "observacoes": "Switch L2+ avançado. Sem PoE, sem empilhamento físico."
    }
]

# Lógica de análise
def analisar(equip, reqs):
    compat, score = [], 0
    for k, v in reqs.items():
        if equip.get(k) == v:
            compat.append(f"✅ {k.replace('_',' ').title()}")
            score += 1
        else:
            compat.append(f"❌ {k.replace('_',' ').title()} (esperado: {v}, encontrado: {equip.get(k)})")
    return score, "\n".join(compat)

if st.button("🔍 Analisar Equipamentos"):
    resultados = []
    for eq in equipamentos:
        score, compat = analisar(eq, requisitos)
        resultados.append((score, eq["modelo"], eq["fabricante"], compat, eq["observacoes"]))

    resultados.sort(reverse=True, key=lambda x: x[0])

    for score, modelo, fabricante, compat, obs in resultados:
        st.subheader(f"{modelo} ({fabricante})")
        st.text(compat)
        st.markdown(f"**Pontuação:** {score} | **Conclusão:** {'✅ Compatível' if score == 6 else '⚠️ Parcialmente compatível'}")
        st.markdown(f"**Observações:** {obs}")
        st.markdown("---")
