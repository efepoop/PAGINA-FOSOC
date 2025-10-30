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
# Estilos FEID (ultra neón) + botones centrados transparentes + borde verde
# =============================
page_bg = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Urbanist:wght@300;400;700;900&family=Chakra+Petch:wght@400;700&display=swap');

:root{
  --neon:#00FF4D;
  --bg-1:#caffbf;
  --ink:#041004;
  --ink-soft:#163b16;
}

[data-testid="stAppViewContainer"]{
  background: radial-gradient(circle at 15% 10%, var(--bg-1), #d6ffd6 45%, #eaffea 85%);
  color: var(--ink);
  font-family:'Urbanist', system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
}
[data-testid="stHeader"]{ background: transparent; }

.neon-particles{ position:fixed; inset:0; pointer-events:none; z-index:0; }
.neon-particles span{ position:absolute; display:block; width:8px; height:8px; background:var(--neon); border-radius:50%; opacity:.45; filter:blur(2px) brightness(1.4); animation:floatMove linear infinite; box-shadow: 0 0 14px var(--neon), 0 0 28px var(--neon); }
@keyframes floatMove{ 0%{ transform: translateY(100vh) translateX(0) scale(1); opacity:.2;} 50%{ transform: translateY(50vh) translateX(28px) scale(1.6); opacity:.7;} 100%{ transform: translateY(-10vh) translateX(-28px) scale(1); opacity:.35;} }

h1,h2,h3,h4,h5,h6{ color: var(--ink); text-align:center; letter-spacing: 0.5px; font-family:'Chakra Petch', sans-serif; }

h1 {
  font-family:'Bebas Neue', sans-serif;
  font-size: clamp(48px, 7vw, 110px);
  text-shadow:0 0 28px rgba(0,255,77,.85), 0 0 48px rgba(0,255,120,.55);
  margin:.25rem 0;
}

.subhead { font-weight:900; letter-spacing:.8px; text-transform:uppercase; color:var(--ink-soft); text-align:center; }

.stImage>img {
  display:block; margin:auto; border-radius:18px; width:300px !important; height:400px !important;
  object-fit:cover !important; box-shadow:0 0 14px rgba(0,255,77,.45);
  border: 5px solid var(--neon); /* Borde verde neón alrededor de las imágenes */
}

.stButton>button {
  background-color: transparent !important;
  color: var(--neon) !important;
  border: 2px solid var(--neon) !important;
  border-radius: 12px;
  font-weight: 900;
  letter-spacing: .4px;
  padding: .6rem 1.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0.5rem auto;
  box-shadow: 0 0 18px rgba(0,255,77,.4);
  transition: all .3s ease;
}

.stButton>button:hover {
  transform: scale(1.05);
  background-color: rgba(0,255,77,.15) !important;
  box-shadow: 0 0 30px rgba(0,255,77,.8);
  filter: brightness(1.2);
}

.hr { height:1px; background: linear-gradient(90deg, transparent, rgba(0,255,77,.85), transparent); margin: 22px 0; }

.section-chip{ display:inline-block; padding:.25rem .6rem; border:1.5px solid var(--neon); border-radius:999px; font-size:.8rem; font-weight:800; text-transform:uppercase; color:var(--ink-soft); background:rgba(0,255,77,.12); }
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Partículas neon
particle_html = "<div class='neon-particles'>" + ''.join([
    f"<span style='left:{(i*3)%100}%;animation-duration:{7 + (i%6)}s;animation-delay:{i*.12}s;'></span>" for i in range(60)
]) + "</div>"
st.markdown(particle_html, unsafe_allow_html=True)

# Encabezado
offset_html = """
<h1>⚡ Portafolio de Aplicaciones con Inteligencia Artificial ⚡</h1>
<div class='subhead'>Edición FEID — para <b>Felipe Osorno</b></div>
<div class='hr'></div>
"""
st.markdown(offset_html, unsafe_allow_html=True)

# Mostrar apps en filas de 3 columnas (como antes)
imagenes = [f"{i}.jpg" for i in range(1,16)]
apps = [
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
        if i + j < len(apps):
            cat, title, desc, link = apps[i + j]
            with col:
                st.markdown(f"<div class='section-chip'>{cat}</div>", unsafe_allow_html=True)
                st.subheader(title)
                st.image(Image.open(imagenes[i + j]))
                st.write(desc)
                st.markdown(f"<div style='text-align:center;'><a href='{link}' target='_blank'><button>🚀 Ir a la aplicación</button></a></div>", unsafe_allow_html=True)
    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<p style='text-align:center; color:var(--ink); font-weight:900;'>
  ⚡ Hecho con cariño por <span style='color:var(--neon); text-shadow:0 0 12px var(--neon);'>Felipe Osorno</span>. Estética CaFerxxo
</p>
""", unsafe_allow_html=True)
