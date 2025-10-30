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
# Estilos FEID (verde neón super potente) + animaciones intensas
# =============================
page_bg = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Urbanist:wght@300;400;600;800&display=swap');

:root {
  --neon:#00FF33;              /* Verde neón brillante */
  --neon-strong:#00ff66;       /* Verde ultra neón */
  --neon-soft:#aaffaa;         /* Fondo verde claro más potente */
  --ink:#051405;
  --ink-soft:#112c11;
}

[data-testid="stAppViewContainer"] {
  background: radial-gradient(circle at 20% 20%, var(--neon-strong), #aaffaa 50%, #ccffcc 100%);
  color: var(--ink);
  font-family: 'Urbanist', sans-serif;
  position: relative;
  overflow: hidden;
}
[data-testid="stHeader"]{ background: transparent; }

/* Partículas más brillantes y animadas */
.neon-particles {
  position: fixed; inset: 0; pointer-events: none; z-index: 0;
}
.neon-particles span{
  position: absolute; display:block; width:9px; height:9px;
  background: var(--neon-strong); border-radius: 50%; opacity: .45;
  filter: blur(2px) brightness(1.4);
  animation: floatMove linear infinite;
  box-shadow: 0 0 12px var(--neon-strong), 0 0 25px var(--neon);
}
@keyframes floatMove {
  0% { transform: translateY(100vh) translateX(0) scale(1); opacity:.15; }
  50% { transform: translateY(50vh) translateX(25px) scale(1.5); opacity:.6; }
  100% { transform: translateY(-10vh) translateX(-25px) scale(1); opacity:.3; }
}

h1,h2,h3,h4,h5,h6{ color: var(--ink); text-align:center; letter-spacing: 0.5px; }

h1 {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(44px, 6vw, 92px);
  text-shadow: 0 0 25px rgba(0,255,80,.8), 0 0 45px rgba(0,255,100,.6);
  margin-bottom: .5rem;
}

.subhead { font-weight: 800; letter-spacing: .8px; text-transform: uppercase; color: var(--ink-soft); text-align:center; }

p, li { color: var(--ink); text-align:center; }

.stImage>img {
  display:block; margin:auto; border-radius:18px; width:300px !important; height:400px !important;
  object-fit:cover !important; object-position:center !important;
  box-shadow: 0 0 20px rgba(0,255,100,.6), 0 0 6px rgba(0,0,0,.25);
}

button, .stButton>button {
  background: #031c03 !important; color: var(--neon-strong) !important;
  border-radius: 12px; border: 2px solid var(--neon-strong) !important;
  font-weight: 700; letter-spacing:.4px;
  display:block; margin: 0.25rem auto; padding: .5rem 1rem;
  transition: transform .25s ease, box-shadow .25s ease, filter .25s ease;
  box-shadow: 0 0 18px rgba(0,255,80,.45);
}
button:hover{
  transform: translateY(-2px) scale(1.05);
  filter: brightness(1.4);
  box-shadow: 0 0 30px rgba(0,255,100,.8);
}

.hr { height:1px; background: linear-gradient(90deg, transparent, rgba(0,255,100,.8), transparent); margin: 20px 0; }

.neon-link{ color: var(--ink); font-weight:700; text-decoration:none; position:relative; }
.neon-link:after{ content:""; position:absolute; left:0; right:0; bottom:-2px; height:2px; background: var(--neon-strong); box-shadow:0 0 16px rgba(0,255,100,.85); }

.section-chip{ display:inline-block; padding:.25rem .6rem; border:1.5px solid var(--neon-strong); border-radius:999px; font-size:.8rem; font-weight:800; letter-spacing:.4px; text-transform:uppercase; color:var(--ink-soft); background:rgba(0,255,100,.2); }

.section-title { text-align:center; color: var(--ink); }
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Más partículas en el fondo
particle_html = "<div class='neon-particles'>" + ''.join([
    f"<span style='left:{i*2.5}%;animation-duration:{7+i%5}s;animation-delay:{i*.15}s;'></span>" for i in range(80)
]) + "</div>"
st.markdown(particle_html, unsafe_allow_html=True)

# =============================
# Encabezado
# =============================
st.markdown("<h1>⚡ Portafolio de Aplicaciones con Inteligencia Artificial ⚡</h1>", unsafe_allow_html=True)
st.markdown("<div class='subhead'>Edición FEID — para <b>Felipe Osorno</b></div>", unsafe_allow_html=True)
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =============================
# Cuerpo (imágenes 1-15)
# =============================
imagenes = [f"{i}.jpg" for i in range(1,16)]

secciones = [
    ("Intro", "🟢 Introducción", "Primera aplicación.", "https://1-intro-w6eubfucnyzmtme8uxjvpc.streamlit.app/"),
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
        if i + j < len(secciones):
            with col:
                cat, titulo, desc, link = secciones[i + j]
                st.markdown(f"<div class='section-chip'>{cat}</div>", unsafe_allow_html=True)
                st.subheader(titulo)
                st.image(Image.open(imagenes[i + j]))
                st.write(desc)
                st.markdown(f"<a class='neon-link' href='{link}' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)
    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =============================
# Pie de página
# =============================
st.markdown("""
<p style='text-align:center; color:#051405; font-weight:800;'>
  ⚡ Fin del portafolio — FEID Vibes para <span style='color:#00FF66;'>Felipe Osorno</span> ⚡
</p>
""", unsafe_allow_html=True)
