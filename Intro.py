import streamlit as st
from PIL import Image

# =============================
# Configuración de la página
# =============================
st.set_page_config(
    page_title="Portafolio IA — FEID Vibes",
    page_icon="💚",
    layout="wide",
)

# =============================
# Estilos FEID (verde neón) + animaciones
# =============================
page_bg = r"""
<style>
/* Tipografías (Google Fonts) */
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Urbanist:wght@300;400;600;800&display=swap');

:root {
  --neon:#39FF14;              /* Verde neón intenso */
  --neon-soft:#ccffd9;         /* Verde neón muy claro para fondo */
  --ink:#0b0f0c;               /* Texto principal oscuro */
  --ink-soft:#1f2a22;          /* Sombras/texto suave */
  --card-bg:#f7fff9;           /* Tarjetas claras */
}

/* Fondo con gradiente suave y animación de partículas */
[data-testid="stAppViewContainer"] {
  background: radial-gradient(1200px 800px at 10% 10%, var(--neon-soft), #eaffef 45%, #f6fff8 80%);
  color: var(--ink);
  font-family: 'Urbanist', system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
  position: relative;
  overflow: hidden; /* para las partículas */
}

[data-testid="stHeader"]{ background: transparent; }

/* Contenedor de partículas */
.neon-particles {
  position: fixed; inset: 0; pointer-events: none; z-index: 0;
}
.neon-particles span{
  position: absolute; display:block; width:10px; height:10px;
  background: var(--neon); filter: blur(1px);
  border-radius: 50%; opacity: .25;
  animation: floatUp linear infinite;
}
@keyframes floatUp {
  from { transform: translateY(100vh) scale(1); opacity:.05; }
  to   { transform: translateY(-10vh) scale(1.4); opacity:.35; }
}

/* Títulos y texto */
h1,h2,h3,h4,h5,h6{
  color: var(--ink);
  text-align:center;
  letter-spacing: 0.5px;
}

h1 {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(42px, 6vw, 86px);
  line-height: 0.9;
  margin: 0.2rem 0 0.6rem;
  text-shadow: 0 0 10px rgba(57,255,20,.35), 0 0 24px rgba(57,255,20,.25);
}

.subhead {
  font-weight: 800; letter-spacing: .8px; text-transform: uppercase;
  color: var(--ink-soft); text-align:center; margin-top:-4px;
}

p, li { color: var(--ink); text-align:center; }

/* Tarjetas de imagen uniformes */
.stImage>img {
  display:block; margin-left:auto; margin-right:auto;
  border-radius:18px; width:300px !important; height:400px !important;
  object-fit:cover !important; object-position:center !important;
  box-shadow: 0 10px 28px rgba(0,0,0,.12), 0 0 0 2px rgba(57,255,20,.35);
}

/* Botones estilo neón */
button, .stButton>button {
  background: #0e1511 !important; color: var(--neon) !important;
  border-radius: 12px; border: 2px solid var(--neon) !important;
  font-weight: 700; letter-spacing:.4px;
  display:block; margin: 0.25rem auto; padding: .5rem 1rem;
  transition: transform .25s ease, box-shadow .25s ease, filter .25s ease;
  box-shadow: 0 0 14px rgba(57,255,20,.35);
}
button:hover{
  transform: translateY(-2px) scale(1.03);
  filter: brightness(1.05);
  box-shadow: 0 0 22px rgba(57,255,20,.55);
}

/* Divider */
.hr { height:1px; background: linear-gradient(90deg, transparent, rgba(57,255,20,.6), transparent); margin: 18px 0 8px; }

/* Enlaces con subrayado neón */
.neon-link{ color: var(--ink); font-weight:700; text-decoration:none; position:relative; }
.neon-link:after{ content:""; position:absolute; left:0; right:0; bottom:-2px; height:2px; background: var(--neon); box-shadow:0 0 10px rgba(57,255,20,.55); }

/* Chips de sección */
.section-chip{ display:inline-block; padding:.25rem .6rem; border:1.5px solid var(--neon); border-radius:999px; font-size:.8rem; font-weight:800; letter-spacing:.4px; text-transform:uppercase; color:var(--ink-soft); background:rgba(57,255,20,.10); }

/* Subtítulos de secciones */
.section-title { text-align:center; color: var(--ink); }

</style>
"""

# Inyecta CSS
st.markdown(page_bg, unsafe_allow_html=True)

# Genera partículas ("cositas") verdes en el fondo
particle_html = """
<div class='neon-particles'>
  <!-- 24 partículas con posiciones aleatorias -->
  <span style='left:5%;  animation-duration:10s; animation-delay:0s;'></span>
  <span style='left:12%; animation-duration:13s; animation-delay:1s;'></span>
  <span style='left:18%; animation-duration:11s; animation-delay:.2s;'></span>
  <span style='left:25%; animation-duration:9s;  animation-delay:.8s;'></span>
  <span style='left:31%; animation-duration:14s; animation-delay:1.8s;'></span>
  <span style='left:38%; animation-duration:12s; animation-delay:.4s;'></span>
  <span style='left:44%; animation-duration:16s; animation-delay:1.2s;'></span>
  <span style='left:50%; animation-duration:9.5s;animation-delay:.6s;'></span>
  <span style='left:56%; animation-duration:12.5s;animation-delay:1.1s;'></span>
  <span style='left:62%; animation-duration:10.5s;animation-delay:.3s;'></span>
  <span style='left:68%; animation-duration:15s; animation-delay:.9s;'></span>
  <span style='left:74%; animation-duration:11.5s;animation-delay:1.6s;'></span>
  <span style='left:80%; animation-duration:13.5s;animation-delay:.5s;'></span>
  <span style='left:86%; animation-duration:10.2s;animation-delay:1.3s;'></span>
  <span style='left:92%; animation-duration:12.8s;animation-delay:.7s;'></span>
  <span style='left:8%;  animation-duration:14.5s;animation-delay:1.9s;'></span>
  <span style='left:28%; animation-duration:12.2s;animation-delay:.1s;'></span>
  <span style='left:35%; animation-duration:11.1s;animation-delay:.55s;'></span>
  <span style='left:47%; animation-duration:9.8s; animation-delay:1.25s;'></span>
  <span style='left:53%; animation-duration:13.2s;animation-delay:.85s;'></span>
  <span style='left:60%; animation-duration:10.9s;animation-delay:.15s;'></span>
  <span style='left:71%; animation-duration:14.1s;animation-delay:1.45s;'></span>
  <span style='left:77%; animation-duration:9.9s; animation-delay:.35s;'></span>
  <span style='left:89%; animation-duration:13.8s;animation-delay:1.05s;'></span>
</div>
"""
st.markdown(particle_html, unsafe_allow_html=True)

# =============================
# Encabezado
# =============================
st.markdown("<h1>💚 Portafolio de Aplicaciones con Inteligencia Artificial</h1>", unsafe_allow_html=True)
st.markdown("<div class='subhead'>Edición FEID — para <b>Felipe Osorno</b></div>", unsafe_allow_html=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =============================
# Fila 1
# =============================
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='section-chip'>Intro</div>", unsafe_allow_html=True)
    st.subheader("💚 Introducción")
    st.image(Image.open("1.jpg"))
    st.write("Primera aplicación.")
    st.markdown("<a class='neon-link' href='https://1-intro-w6eubfucnyzmtme8uxjvpc.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='section-chip'>Audio</div>", unsafe_allow_html=True)
    st.subheader("💚 Texto a Voz")
    st.image(Image.open("2.jpg"))
    st.write("Convierte texto a audio.")
    st.markdown("<a class='neon-link' href='https://pagina2profe.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='section-chip'>Audio</div>", unsafe_allow_html=True)
    st.subheader("💚 Voz a Texto")
    st.image(Image.open("3.jpg"))
    st.write("Convierte voz en texto usando IA.")
    st.markdown("<a class='neon-link' href='https://pbeo6cxaxwky2mxj3cxj57.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =============================
# Fila 2
# =============================
col4, col5, col6 = st.columns(3)
with col4:
    st.markdown("<div class='section-chip'>Visión</div>", unsafe_allow_html=True)
    st.subheader("💚 Interfaz OCR")
    st.image(Image.open("4.jpg"))
    st.write("Reconocimiento óptico de caracteres.")
    st.markdown("<a class='neon-link' href='https://ocr-audio-sunwazxyy3htz7w8eqm7yn.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

with col5:
    st.markdown("<div class='section-chip'>NLP</div>", unsafe_allow_html=True)
    st.subheader("💚 Análisis de Sentimiento")
    st.image(Image.open("5.jpg"))
    st.write("Reconoce emociones de un texto.")
    st.markdown("<a class='neon-link' href='https://3uxhnpwvxuwdawcd85n3ee.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

with col6:
    st.markdown("<div class='section-chip'>NLP</div>", unsafe_allow_html=True)
    st.subheader("💚 Análisis de Texto (Inglés)")
    st.image(Image.open("6.jpg"))
    st.write("Explora la relación entre textos y una pregunta.")
    st.markdown("<a class='neon-link' href='https://aafml3fw2lsqviu7k6dyjm.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =============================
# Fila 3
# =============================
col7, col8, col9 = st.columns(3)
with col7:
    st.markdown("<div class='section-chip'>NLP</div>", unsafe_allow_html=True)
    st.subheader("💚 Análisis de Texto (Español)")
    st.image(Image.open("7.jpg"))
    st.write("Analiza el texto desde preguntas.")
    st.markdown("<a class='neon-link' href='https://uzvwnqkgpdvyafmupea9fu.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

with col8:
    st.markdown("<div class='section-chip'>Visión</div>", unsafe_allow_html=True)
    st.subheader("💚 Reconocimiento de Objetos")
    st.image(Image.open("8.jpg"))
    st.write("Reconoce los objetos de una imagen.")
    st.markdown("<a class='neon-link' href='https://7gfmxhghfykz3hqwd5rtgw.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

with col9:
    st.markdown("<div class='section-chip'>Visión</div>", unsafe_allow_html=True)
    st.subheader("💚 Reconocimiento de Gestos")
    st.image(Image.open("9.jpg"))
    st.write("Interpreta movimientos usando visión computacional.")
    st.markdown("<a class='neon-link' href='https://bzllgjxt9zzhxw72snvu7p.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =============================
# Fila 4
# =============================
col10, col11, col12 = st.columns(3)
with col10:
    st.markdown("<div class='section-chip'>Docs</div>", unsafe_allow_html=True)
    st.subheader("💚 Chat PDF")
    st.image(Image.open("10.jpg"))
    st.write("Analiza el contenido de un documento PDF.")
    st.markdown("<a class='neon-link' href='https://ajjmaezetnmmeds42r2ttl.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

with col11:
    st.markdown("<div class='section-chip'>Visión</div>", unsafe_allow_html=True)
    st.subheader("💚 Interpretación de Imagen")
    st.image(Image.open("11.jpg"))
    st.write("Análisis avanzado de imágenes con IA.")
    st.markdown("<a class='neon-link' href='https://yz2rgx5rxrqsnrjbegaw8d.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

with col12:
    st.markdown("<div class='section-chip'>UX</div>", unsafe_allow_html=True)
    st.subheader("💚 Interfaz Táctil")
    st.image(Image.open("12.jpg"))
    st.write("Dibuja en un tablero interactivo.")
    st.markdown("<a class='neon-link' href='https://tablero-6pbavfx8iqfyobyfffug4g.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =============================
# Fila 5
# =============================
col13, col14, col15 = st.columns(3)
with col13:
    st.markdown("<div class='section-chip'>Visión</div>", unsafe_allow_html=True)
    st.subheader("💚 Reconocimiento de Bocetos")
    st.image(Image.open("13.jpg"))
    st.write("Analiza los dibujos hechos en el tablero.")
    st.markdown("<a class='neon-link' href='https://drawrecog-htvmekqhjm2psqx3huthk9.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

with col14:
    st.markdown("<div class='section-chip'>IoT</div>", unsafe_allow_html=True)
    st.subheader("💚 Control MQTT (Botones)")
    st.image(Image.open("14.jpg"))
    st.write("Control de dispositivos mediante MQTT y botones.")
    st.markdown("<a class='neon-link' href='https://sendcmqtt-cvddr5bndohn3vf69tazjd.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

with col15:
    st.markdown("<div class='section-chip'>IoT</div>", unsafe_allow_html=True)
    st.subheader("💚 Control MQTT (Voz)")
    st.image(Image.open("15.jpg"))
    st.write("Control de dispositivos mediante comandos de voz.")
    st.markdown("<a class='neon-link' href='https://ctrlvoice-cwg7b2khfj2a7r2q4trjtu.streamlit.app/' target='_blank'>Ir a la aplicación</a>", unsafe_allow_html=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =============================
# Pie de página
# =============================
st.markdown("""
<p style='text-align:center; color:#1f2a22; font-weight:800;'>
  💚 Fin del portafolio — FEID Vibes para <span style='color:#0b0f0c;'>Felipe Osorno</span> 💚
</p>
""", unsafe_allow_html=True)
