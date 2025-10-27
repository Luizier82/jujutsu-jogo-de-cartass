import streamlit as st
import random

# ======== DADOS DAS CARTAS ========
cartas_dados = [
    ("Yuji Itadori", {"Força Maldita": 60, "Técnica Amaldiçoada": 80, "Domínio Expandido": 65, "Energia CE": 55, "Velocidade": 75}),
    ("Megumi Fushiguro", {"Força Maldita": 73, "Técnica Amaldiçoada": 70, "Domínio Expandido": 68, "Energia CE": 62, "Velocidade": 60}),
    ("Nobara Kugisaki", {"Força Maldita": 70, "Técnica Amaldiçoada": 72, "Domínio Expandido": 74, "Energia CE": 66, "Velocidade": 72}),
    ("Satoru Gojo", {"Força Maldita": 95, "Técnica Amaldiçoada": 85, "Domínio Expandido": 90, "Energia CE": 92, "Velocidade": 80}),
    ("Sukuna", {"Força Maldita": 94, "Técnica Amaldiçoada": 88, "Domínio Expandido": 86, "Energia CE": 93, "Velocidade": 74}),
    ("Maki Zenin", {"Força Maldita": 67, "Técnica Amaldiçoada": 82, "Domínio Expandido": 78, "Energia CE": 80, "Velocidade": 70}),
    ("Panda", {"Força Maldita": 75, "Técnica Amaldiçoada": 76, "Domínio Expandido": 72, "Energia CE": 74, "Velocidade": 80}),
    ("Aoi Todo", {"Força Maldita": 78, "Técnica Amaldiçoada": 73, "Domínio Expandido": 77, "Energia CE": 79, "Velocidade": 84}),
    ("Kento Nanami", {"Força Maldita": 77, "Técnica Amaldiçoada": 75, "Domínio Expandido": 71, "Energia CE": 81, "Velocidade": 80}),
    ("Mahito", {"Força Maldita": 76, "Técnica Amaldiçoada": 87, "Domínio Expandido": 83, "Energia CE": 85, "Velocidade": 75}),
    ("Yuta Okkotsu", {"Força Maldita": 89, "Técnica Amaldiçoada": 84, "Domínio Expandido": 88, "Energia CE": 90, "Velocidade": 82}),
]

# ======== FUNÇÕES ========

def escolher_carta():
    return random.choice(cartas_dados)

def mostrar_carta(nome, atributos):
    st.markdown(f"### 🃏 {nome}")
    for atributo, valor in atributos.items():
        st.write(f"**{atributo}:** {valor}")

# ======== APP STREAMLIT ========

st.set_page_config(page_title="Super Trunfo: Jujutsu Kaisen", page_icon="🔥", layout="centered")
st.title("🃏 Super Trunfo - Jujutsu Kaisen")

if "pontos_jogador" not in st.session_state:
    st.session_state.pontos_jogador = 0
    st.session_state.pontos_pc = 0

if st.button("Nova Rodada"):
    jogador = escolher_carta()
    computador = escolher_carta()
    st.session_state.jogador = jogador
    st.session_state.computador = computador

if "jogador" in st.session_state:
    jogador = st.session_state.jogador
    computador = st.session_state.computador

    st.subheader("Sua carta:")
    mostrar_carta(jogador[0], jogador[1])

    atributo_escolhido = st.selectbox("Escolha um atributo para competir:", list(jogador[1].keys()))

    if st.button("Comparar"):
        valor_jogador = jogador[1][atributo_escolhido]
        valor_pc = computador[1][atributo_escolhido]

        st.subheader("Carta do Computador:")
        mostrar_carta(computador[0], computador[1])

        st.write(f"### 🔸 Atributo escolhido: **{atributo_escolhido}**")
        st.write(f"**{jogador[0]}:** {valor_jogador} vs **{computador[0]}:** {valor_pc}")

        if valor_jogador > valor_pc:
            st.success("🎉 Você venceu esta rodada!")
            st.session_state.pontos_jogador += 1
        elif valor_jogador < valor_pc:
            st.error("💀 O computador venceu esta rodada!")
            st.session_state.pontos_pc += 1
        else:
            st.info("⚖️ Empate!")

st.markdown(f"## 🧮 Placar: Você **{st.session_state.pontos_jogador}** x **{st.session_state.pontos_pc}** Computador")
