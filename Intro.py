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
# Estilos FEID (ultra neón) + layout con header y botones
# =============================
page_bg = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Urbanist:wght@300;400;700;900&family=Chakra+Petch:wght@400;700&display=swap');

:root{
  --neon:#00FF4D;           /* Verde ULTRA neón */
  --neon-2:#39FF14;         /* Segundo tono neón */
  --bg-1:#caffbf;           /* Base fondo clara */
  --bg-2:#b7ffb0;           /* Degradado */
  --ink:#041004;            /* Texto principal */
  --ink-soft:#163b16;       /* Suave */
}

/* Fondo hero radiante */
[data-testid="stAppViewContainer"]{
  background: radial-gradient(1000px 700px at 15% 10%, var(--bg-1), #e9ffe9 45%, #f4fff4 85%);
  color: var(--ink);
  font-family:'Urbanist', system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
  position:relative; overflow:hidden;
}
[data-testid="stHeader"]{ background: transparent; }

/* Header pegajoso con blur */
.header{
  position: sticky; top: 0; z-index: 5; margin-bottom: 8px;
  backdrop-filter: blur(6px);
  background: linear-gradient(90deg, rgba(202,255,191,.85), rgba(244,255,244,.85));
  border-bottom:1px solid rgba(0,255,77,.35);
  box-shadow: 0 6px 24px rgba(0,0,0,.06);
}
.header-inner{ max-width:1200px; margin:auto; padding:10px 20px; display:flex; align-items:center; justify-content:space-between; }
.brand{ display:flex; align-items:center; gap:.75rem; }
.brand .dot{ width:14px; height:14px; border-radius:50%; background:var(--neon); box-shadow:0 0 16px var(--neon); }
.brand h1{ font-family:'Bebas Neue', sans-serif; letter-spacing:1px; font-size:36px; margin:0; text-shadow:0 0 18px rgba(0,255,77,.6); }
.brand small{ display:block; font-weight:800; color:var(--ink-soft); margin-top:-6px; letter-spacing:.6px; text-transform:uppercase; }

.nav{ display:flex; gap:.5rem; }
.nav a{ text-decoration:none; font-weight:800; padding:.45rem .75rem; border-radius:999px; border:1.5px solid var(--neon); color:var(--ink); background: rgba(0,255,77,.12); box-shadow:0 0 10px rgba(0,255,77,.35); }
.nav a:hover{ background: var(--neon); color:#041004; box-shadow:0 0 16px rgba(0,255,77,.7); }

/* Partículas neon */
.neon-particles{ position:fixed; inset:0; pointer-events:none; z-index:0; }
.neon-particles span{ position:absolute; display:block; width:8px; height:8px; background:var(--neon); border-radius:50%; opacity:.45; filter:blur(2px) brightness(1.4); animation:floatMove linear infinite; box-shadow: 0 0 14px var(--neon), 0 0 28px var(--neon-2); }
@keyframes floatMove{ 0%{ transform: translateY(100vh) translateX(0) scale(1); opacity:.2;} 50%{ transform: translateY(50vh) translateX(28px) scale(1.6); opacity:.7;} 100%{ transform: translateY(-10vh) translateX(-28px) scale(1); opacity:.35;} }

/* Hero */
.hero{ max-width:1100px; margin: 24px auto 6px; text-align:center; position:relative; z-index:1; }
.hero-title{ font-family:'Bebas Neue', sans-serif; font-size: clamp(48px, 7vw, 110px); line-height:.9; margin:.25rem 0; text-shadow:0 0 28px rgba(0,255,77,.75), 0 0 48px rgba(0,255,120,.5); }
.hero-sub{ font-weight:900; letter-spacing:.8px; color:var(--ink-soft); text-transform:uppercase; margin-top:-6px; }
.hero-cta{ margin-top:10px; display:flex; gap:.75rem; justify-content:center; flex-wrap:wrap; }

/* Botón de enlace neón */
.neo-btn{ display:inline-flex; align-items:center; gap:.45rem; padding:.55rem 1rem; border-radius:12px; border:2px solid var(--neon); text-decoration:none; font-weight:900; letter-spacing:.4px; background:#071e07; color:var(--neon); box-shadow:0 0 18px rgba(0,255,77,.5); transition: transform .2s ease, box-shadow .2s ease, filter .2s ease; }
.neo-btn:hover{ transform:translateY(-2px) scale(1.03); filter:brightness(1.25); box-shadow:0 0 28px rgba(0,255,77,.8); }
.neo-btn.small{ padding:.45rem .8rem; font-weight:800; border-radius:999px; }

/* Tarjetas / grid */
.grid{ max-width:1200px; margin: 6px auto; position:relative; z-index:1; }
.row{ display:grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap:18px; }
@media (max-width: 980px){ .row{ grid-template-columns: repeat(2, minmax(0,1fr)); } }
@media (max-width: 640px){ .row{ grid-template-columns: 1fr; } }

.app-card{ background: linear-gradient(180deg, rgba(255,255,255,.92), rgba(234,255,234,.88)); border:1px solid rgba(0,255,77,.35); border-radius:22px; padding:14px; box-shadow: 0 10px 22px rgba(0,0,0,.06), 0 0 0 2px rgba(0,255,77,.2); display:flex; flex-direction:column; gap:.4rem; align-items:center; }
.app-card h3{ font-family:'Chakra Petch', sans-serif; margin:.15rem 0 .15rem; letter-spacing:.4px; }
.app-card p{ margin:0 0 .2rem; color:var(--ink); text-align:center; }
.app-card .chip{ display:inline-block; padding:.2rem .55rem; border:1.5px solid var(--neon); border-radius:999px; font-size:.75rem; font-weight:900; letter-spacing:.4px; text-transform:uppercase; color:var(--ink-soft); background:rgba(0,255,77,.12); }
.app-card img{ width:100%; height:320px !important; object-fit:cover !important; border-radius:14px; box-shadow:0 0 14px rgba(0,255,77,.45); }

.hr{ height:1px; background: linear-gradient(90deg, transparent, rgba(0,255,77,.85), transparent); margin: 22px 0; }

/* Enlace subrayado neón (si lo usas en texto) */
.neon-link{ color:var(--ink); font-weight:700; text-decoration:none; position:relative; }
.neon-link:after{ content:""; position:absolute; left:0; right:0; bottom:-2px; height:2px; background: var(--neon); box-shadow:0 0 14px rgba(0,255,77,.85); }
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Partículas neon (muchas)
particle_html = "<div class='neon-particles'>" + ''.join([
    f"<span style='left:{(i*2)%100}%;animation-duration:{7 + (i%6)}s;animation-delay:{i*.12}s;'></span>" for i in range(100)
]) + "</div>"
st.markdown(particle_html, unsafe_allow_html=True)

# =============================
# HEADER + NAV
# =============================
header_html = """
<div class='header'>
  <div class='header-inner'>
    <div class='brand'>
      <div class='dot'></div>
      <div>
        <h1>FEID Vibes · AI Apps</h1>
        <small>Portafolio para Felipe Osorno</small>
      </div>
    </div>
    <nav class='nav'>
      <a href='#apps'>Apps</a>
      <a href='#sobre'>Sobre</a>
    </nav>
  </div>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# =============================
# HERO
# =============================
st.markdown("""
<div class='hero'>
  <div class='hero-title'>
    FERXXO <span style='color:var(--neon); text-shadow:0 0 20px var(--neon);'>NEÓN</span> EXPERIENCE
  </div>
  <div class='hero-sub'>Aplicaciones con Inteligencia Artificial · Estética FEID</div>
  <div class='hero-cta'>
    <a class='neo-btn' href='#apps'>🟢 Ver todas las apps</a>
    <a class='neo-btn small' href='#sobre'>ℹ️ Sobre el portafolio</a>
  </div>
</div>
<div class='hr'></div>
""", unsafe_allow_html=True)

# =============================
# DATA
# =============================
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

# =============================
# GRID DE APPS
# =============================
st.markdown("<div id='apps'></div>", unsafe_allow_html=True)
st.markdown("<div class='grid'>", unsafe_allow_html=True)

for i in range(0, 15, 3):
    row_cards = []
    for j in range(3):
        idx = i + j
        if idx >= len(apps):
            break
        cat, title, desc, link = apps[idx]
        img = imagenes[idx]
        card_html = f"""
        <div class='app-card'>
          <span class='chip'>{cat}</span>
          <h3>{title}</h3>
          <img src='{img}' alt='{title}' />
          <p>{desc}</p>
          <a class='neo-btn' href='{link}' target='_blank'>🚀 Ir a la aplicación</a>
        </div>
        """
        row_cards.append(card_html)
    st.markdown("<div class='row'>" + "".join(row_cards) + "</div>", unsafe_allow_html=True)
    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =============================
# SOBRE (breve)
# =============================
st.markdown("""
<div id='sobre' class='grid' style='max-width:1000px;'>
  <h2 style='text-align:center; font-family: \"Bebas Neue\", sans-serif; font-size: clamp(28px, 5vw, 60px); margin-bottom:4px;'>Sobre este portafolio</h2>
  <p style='text-align:center; color:var(--ink-soft); font-weight:700;'>
    Estilo FEID con tipografías combinadas (Bebas Neue + Chakra Petch + Urbanist),
    botones neón, y fondo con partículas animadas.
  </p>
</div>
<div class='hr'></div>
""", unsafe_allow_html=True)

# =============================
# FOOTER
# =============================
st.markdown("""
<p style='text-align:center; color:var(--ink); font-weight:900;'>
  ⚡ Hecho con cariño para <span style='color:var(--neon); text-shadow:0 0 12px var(--neon);'>Felipe Osorno</span>. Estética FEID, verde ultra neón.
</p>
""", unsafe_allow_html=True)
