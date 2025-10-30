import streamlit as st
from PIL import Image

# =============================
# Configuración de la página
# =============================
st.set_page_config(
    page_title="Portafolio IA — FEID Vibes",
    page_icon="🟢",
    layout="wide",
)

# =============================
# Estilo FEID + CaFerxxo (Fondo verde suave, botones negros premium, bordes neon)
# =============================
page_bg = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Chakra+Petch:wght@400;700&family=Urbanist:wght@300;400;700&display=swap');

:root {
  --neon: #00FF6A;
  --bg1: #b8ffbf;
  --ink: #011b08;
  --shadow: rgba(0,255,106,.8);
}

[data-testid="stAppViewContainer"] {
  background: linear-gradient(180deg, #b8ffbf, #c5ffd1, #e2ffe7);
  color: var(--ink);
  font-family: 'Urbanist', sans-serif;
}
[data-testid="stHeader"]{ background: transparent; }

h1 {
  font-family: 'Bebas Neue', sans-serif;
  text-align: center;
  font-size: clamp(60px, 7vw, 110px);
  color: #000;
  text-shadow: 0 0 25px var(--neon), 0 0 40px var(--shadow);
}
.subhead {
  font-family: 'Chakra Petch', sans-serif;
  text-align: center;
  color: #033d12;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  margin-top: -10px;
}

/* Tarjetas */
.stImage>img {
  display: block;
  margin: 0 auto;
  border-radius: 20px;
  width: 330px !important;
  height: 400px !important;
  object-fit: cover;
  border: 4px solid var(--neon);
  box-shadow: 0 0 20px var(--shadow), inset 0 0 10px var(--neon);
  transition: transform .3s ease, box-shadow .3s ease;
}
.stImage>img:hover {
  transform: scale(1.05);
  box-shadow: 0 0 35px var(--neon), 0 0 70px var(--shadow);
}

/* Botones premium */
.stButton>button {
  background: #000 !important;
  color: var(--neon) !important;
  border: 2px solid var(--neon) !important;
  border-radius: 10px;
  font-family: 'Chakra Petch', sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  padding: .6rem 1.4rem;
  display: block;
  margin: 0.7rem auto;
  box-shadow: 0 0 20px rgba(0,255,106,.4);
  transition: all .3s ease-in-out;
}
.stButton>button:hover {
  background: rgba(0,255,106,.1) !important;
  color: #000 !important;
  border: 2px solid #000 !important;
  box-shadow: 0 0 40px var(--shadow), inset 0 0 15px var(--neon);
  transform: scale(1.08);
}

.section-chip {
  display:inline-block; margin-bottom:6px; padding:.25rem .6rem;
  border:2px solid var(--neon); border-radius:999px;
  font-family:'Chakra Petch', sans-serif; font-size:.8rem; letter-spacing:.8px;
  background:rgba(0,255,77,.1); color:#022c0e; text-transform:uppercase;
}

.hr { height:1px; background: linear-gradient(90deg, transparent, var(--neon), transparent); margin: 28px 0; }
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Header
offset_html = """
<h1>⚡ Portafolio de Aplicaciones con Inteligencia Artificial ⚡</h1>
<div class='subhead'>Edición CaFerxxo — por <b>Felipe Osorno</b></div>
<div class='hr'></div>
"""
st.markdown(offset_html, unsafe_allow_html=True)

# === Diseño de apps (3 por fila) ===
imagenes = [f"{i}.jpg" for i in range(1,16)]
apps = [
    ("Intro", "💿 Introducción", "Primera aplicación.", "https://1-intro-w6eubfucnyzmtme8uxjvpc.streamlit.app/"),
    ("Audio", "🎧 Texto a Voz", "Convierte texto a audio.", "https://2---texto-a-voz-bbbq7gbxyukgrfeg6ehsmw.streamlit.app/"),
    ("Audio", "🎙️ Voz a Texto", "Convierte voz en texto usando IA.", "https://pbeo6cxaxwky2mxj3cxj57.streamlit.app/"),
    ("Visión", "👁️ Interfaz OCR", "Reconocimiento óptico de caracteres.", "https://ocr-audio-sunwazxyy3htz7w8eqm7yn.streamlit.app/"),
    ("NLP", "💬 Análisis de Sentimiento", "Reconoce emociones de un texto.", "https://3uxhnpwvxuwdawcd85n3ee.streamlit.app/"),
    ("NLP", "🧠 Análisis de Texto (Inglés)", "Explora la relación entre textos y una pregunta.", "https://aafml3fw2lsqviu7k6dyjm.streamlit.app/"),
    ("NLP", "🗣️ Análisis de Texto (Español)", "Analiza el texto desde preguntas.", "https://uzvwnqkgpdvyafmupea9fu.streamlit.app/"),
    ("Visión", "📸 Reconocimiento de Objetos", "Reconoce los objetos de una imagen.", "https://7gfmxhghfykz3hqwd5rtgw.streamlit.app/"),
    ("Visión", "✋ Reconocimiento de Gestos", "Interpreta movimientos usando visión computacional.", "https://bzllgjxt9zzhxw72snvu7p.streamlit.app/"),
    ("Docs", "📄 Chat PDF", "Analiza el contenido de un documento PDF.", "https://ajjmaezetnmmeds42r2ttl.streamlit.app/"),
    ("Visión", "🧩 Interpretación de Imagen", "Análisis avanzado de imágenes con IA.", "https://yz2rgx5rxrqsnrjbegaw8d.streamlit.app/"),
    ("UX", "🎨 Interfaz Táctil", "Dibuja en un tablero interactivo.", "https://tablero-6pbavfx8iqfyobyfffug4g.streamlit.app/"),
    ("Visión", "✏️ Reconocimiento de Bocetos", "Analiza los dibujos hechos en el tablero.", "https://drawrecog-htvmekqhjm2psqx3huthk9.streamlit.app/"),
    ("IoT", "🔘 Control MQTT (Botones)", "Control de dispositivos mediante MQTT y botones.", "https://sendcmqtt-cvddr5bndohn3vf69tazjd.streamlit.app/"),
    ("IoT", "🎤 Control MQTT (Voz)", "Control de dispositivos mediante comandos de voz.", "https://ctrlvoice-cwg7b2khfj2a7r2q4trjtu.streamlit.app/")
]

for i in range(0, 15, 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(apps):
            cat, title, desc, link = apps[i + j]
            with col:
                st.markdown(f"<div class='section-chip'>{cat}</div>", unsafe_allow_html=True)
                st.subheader(title)
                st.image(Image.open(imagenes[i + j]))
                st.write(f"<p style='text-align:center; font-family:Urbanist; font-weight:500;'>{desc}</p>", unsafe_allow_html=True)
                st.markdown(f"<div style='text-align:center;'><a href='{link}' target='_blank'><button>Ir a la aplicación</button></a></div>", unsafe_allow_html=True)
    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<p style='text-align:center; color:var(--ink); font-weight:900;'>
  ⚡ Hecho con cariño por <span style='color:var(--neon); text-shadow:0 0 12px var(--neon);'>Felipe Osorno</span>. Estética CaFerxxo
</p>
""", unsafe_allow_html=True)
