# ==============================================================================
# FICHIER : app.py
# ROLE    : Page d'accueil orientée client — marketing + accès interne discret
# ==============================================================================

import streamlit as st

st.set_page_config(
    page_title="Desjardins Assurances",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #f0fdf4 !important;
}
section[data-testid="stSidebar"] { display: none !important; }
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }

.stButton button {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    width: 100% !important;
}
.stButton button:hover { background: transparent !important; }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# BARRE INTERNE DISCRÈTE (haut de page)
# ==============================================================================
col_bar1, col_bar2, col_bar3 = st.columns([6, 1, 1])
with col_bar2:
    if st.button("👔 Employé", use_container_width=True):
        st.switch_page("pages/2_Employe.py")
with col_bar3:
    if st.button("⚙️ Dev", use_container_width=True):
        st.switch_page("pages/3_Developpeur.py")

st.markdown("""
<div style="border-bottom:1px solid #d1fae5;margin-bottom:0;"></div>
""", unsafe_allow_html=True)

# ==============================================================================
# EN-TÊTE HERO
# ==============================================================================
st.markdown("""
<div style="background:linear-gradient(135deg, #006B3C, #00874A, #34d399);
            padding:4rem 2rem 3.5rem;
            text-align:center;
            border-radius:0 0 40px 40px;
            margin-bottom:3rem;
            box-shadow:0 8px 40px rgba(0,107,60,0.20)">
  <div style="font-size:3.5rem;margin-bottom:0.8rem">🚗</div>
  <div style="font-family:'Playfair Display',Georgia,serif;
              font-size:2.8rem;font-weight:700;color:#fff;
              letter-spacing:-0.5px;margin-bottom:0.6rem">
    Desjardins Assurances
  </div>
  <div style="font-size:1.1rem;color:rgba(255,255,255,0.85);
              font-weight:400;margin-bottom:2rem">
    Protégez ce qui compte le plus — simple, rapide, fiable.
  </div>
  <div style="display:inline-block;background:#fff;color:#006B3C;
              font-size:14px;font-weight:700;padding:12px 32px;
              border-radius:99px;cursor:pointer;
              box-shadow:0 4px 16px rgba(0,0,0,0.12)">
    Obtenir une soumission gratuite ↓
  </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# AVANTAGES
# ==============================================================================
st.markdown("""
<div style="text-align:center;margin-bottom:2.5rem">
  <div style="font-size:11px;font-weight:700;text-transform:uppercase;
              letter-spacing:2px;color:#16a34a;margin-bottom:8px">
    Pourquoi nous choisir
  </div>
  <div style="font-size:1.5rem;font-weight:700;color:#064e3b">
    Une assurance qui vous ressemble
  </div>
</div>
""", unsafe_allow_html=True)

AVANTAGE = """
<div style="background:#fff;border:1.5px solid {border};border-radius:16px;
            padding:1.8rem 1.5rem;text-align:center;
            box-shadow:0 2px 12px rgba(0,107,60,0.07);height:100%">
  <div style="font-size:2.4rem;margin-bottom:0.8rem">{icon}</div>
  <div style="font-size:1rem;font-weight:700;color:#065f46;margin-bottom:0.5rem">
    {titre}
  </div>
  <div style="font-size:13px;color:#475569;line-height:1.7">{desc}</div>
</div>
"""

c1, c2, c3, c4 = st.columns(4, gap="medium")
with c1:
    st.markdown(AVANTAGE.format(
        icon="⚡", titre="Réponse instantanée",
        desc="Obtenez une évaluation de votre demande en moins de 2 minutes grâce à notre système intelligent.",
        border="#bbf7d0"
    ), unsafe_allow_html=True)
with c2:
    st.markdown(AVANTAGE.format(
        icon="🔒", titre="100% sécurisé",
        desc="Vos données personnelles sont protégées et chiffrées. Votre vie privée est notre priorité.",
        border="#bbf7d0"
    ), unsafe_allow_html=True)
with c3:
    st.markdown(AVANTAGE.format(
        icon="💰", titre="Meilleur prix",
        desc="Notre tarification VMR garantit un prix juste basé sur votre profil réel de conducteur.",
        border="#bbf7d0"
    ), unsafe_allow_html=True)
with c4:
    st.markdown(AVANTAGE.format(
        icon="🤝", titre="Support humain",
        desc="Un employé qualifié révise chaque dossier pour vous assurer un service personnalisé.",
        border="#bbf7d0"
    ), unsafe_allow_html=True)

st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)

# ==============================================================================
# APPEL À L'ACTION PRINCIPAL
# ==============================================================================
st.markdown("""
<div style="text-align:center;margin-bottom:2rem">
  <div style="font-size:1.5rem;font-weight:700;color:#064e3b;margin-bottom:0.5rem">
    Prêt à assurer votre véhicule ?
  </div>
  <div style="font-size:13.5px;color:#475569">
    Connectez-vous à votre espace client pour soumettre une demande.
  </div>
</div>
""", unsafe_allow_html=True)

col_cta = st.columns([2, 2, 2])[1]
with col_cta:
    if st.button("👤 Accéder à mon espace client", use_container_width=True):
        st.switch_page("pages/1_Client.py")

    st.markdown("""
    <div style="text-align:center;margin-top:10px;font-size:12px;color:#6b7280">
      Nouveau client ? Votre conseiller créera votre compte.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)

# ==============================================================================
# ÉTAPES DU PROCESSUS
# ==============================================================================
st.markdown("""
<div style="text-align:center;margin-bottom:2rem">
  <div style="font-size:11px;font-weight:700;text-transform:uppercase;
              letter-spacing:2px;color:#16a34a;margin-bottom:8px">
    Comment ça marche
  </div>
  <div style="font-size:1.4rem;font-weight:700;color:#064e3b">
    En 3 étapes simples
  </div>
</div>
""", unsafe_allow_html=True)

ETAPE = """
<div style="background:#fff;border:1.5px solid #bbf7d0;border-radius:16px;
            padding:1.8rem 1.5rem;text-align:center;
            box-shadow:0 2px 12px rgba(0,107,60,0.07)">
  <div style="width:44px;height:44px;background:#006B3C;border-radius:50%;
              color:#fff;font-size:1.1rem;font-weight:700;
              display:flex;align-items:center;justify-content:center;
              margin:0 auto 1rem">{num}</div>
  <div style="font-size:1rem;font-weight:700;color:#065f46;margin-bottom:0.5rem">
    {titre}
  </div>
  <div style="font-size:13px;color:#475569;line-height:1.7">{desc}</div>
</div>
"""

e1, e2, e3 = st.columns(3, gap="large")
with e1:
    st.markdown(ETAPE.format(
        num="1", titre="Connectez-vous",
        desc="Accédez à votre espace client avec votre numéro de client et votre code postal."
    ), unsafe_allow_html=True)
with e2:
    st.markdown(ETAPE.format(
        num="2", titre="Soumettez votre demande",
        desc="Sélectionnez votre véhicule et soumettez votre demande. Notre système l'évalue en temps réel."
    ), unsafe_allow_html=True)
with e3:
    st.markdown(ETAPE.format(
        num="3", titre="Recevez votre confirmation",
        desc="Téléchargez votre confirmation PDF une fois votre dossier approuvé par notre équipe."
    ), unsafe_allow_html=True)

# ==============================================================================
# FOOTER
# ==============================================================================
st.markdown("""
<div style="text-align:center;margin-top:4rem;padding:2rem;
            border-top:1px solid #d1fae5;
            background:#ecfdf5;border-radius:16px">
  <div style="font-size:1rem;font-weight:700;color:#065f46;margin-bottom:0.5rem">
    🚗 Desjardins Assurances
  </div>
  <div style="font-size:12px;color:#6b7280;margin-bottom:0.5rem">
    Cadys Operators · Système de gestion des demandes d'assurance automobile
  </div>
  <div style="font-size:11px;color:#9ca3af">
    © 2026 Desjardins Assurances · Tous droits réservés
  </div>
</div>
""", unsafe_allow_html=True)
