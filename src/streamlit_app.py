import streamlit as st
import time

st.set_page_config(page_title="FitPlan AI Ultra", page_icon="💎", layout="wide")

st.markdown("""
<style>

/* ===== FONT ===== */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
}

/* ===== CINEMATIC BACKGROUND ===== */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(5,5,20,0.85), rgba(5,5,20,0.85)),
        url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* ===== FLOATING PARTICLES ===== */
body::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,0,200,0.1) 2px, transparent 2px);
    background-size: 70px 70px;
    animation: moveParticles 100s linear infinite;
    z-index: 0;
}

@keyframes moveParticles {
    from { transform: translate(0,0); }
    to { transform: translate(-400px,-400px); }
}

/* ===== CENTER LAYOUT ===== */
.block-container {
    max-width: 850px;
    margin: auto;
    padding-top: 70px;
    position: relative;
    z-index: 1;
}

/* ===== TEXT ===== */
h1, h2, h3, h4, p, label {
    color: white !important;
}

h1 {
    text-align: center;
    font-size: 44px !important;
    letter-spacing: 2px;
}

/* ===== GLASS INPUTS ===== */
div[data-baseweb="input"] {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 40px !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    backdrop-filter: blur(15px);
}

div[data-baseweb="input"] input {
    background: transparent !important;
    color: white !important;
    border: none !important;
}

/* ===== GLASS SELECT ===== */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 40px !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    backdrop-filter: blur(15px);
    color: white !important;
}

/* ===== NEON HOVER BUTTON ===== */
.stButton > button {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 50px !important;
    padding: 14px 50px !important;
    border: 2px solid rgba(255,255,255,0.4) !important;
    color: white !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

/* HOVER EFFECT (WORKING VERSION) */
.stButton > button:hover {
    background: linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff) !important;
    background-size: 300% 300% !important;
    animation: neonMove 4s ease infinite !important;
    border: none !important;
    box-shadow:
        0 0 20px #ff00cc,
        0 0 40px #7928ca,
        0 0 60px #00f0ff !important;
    transform: translateY(-4px) !important;
}

@keyframes neonMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

</style>
""", unsafe_allow_html=True)

# ===== HERO =====
st.markdown("<h1>💎 FITPLAN AI ULTRA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>FUTURISTIC FITNESS INTELLIGENCE</p>", unsafe_allow_html=True)

# ===== FORM =====
name = st.text_input("Full Name")
height_cm = st.number_input("Height (cm)", min_value=0.0)
weight_kg = st.number_input("Weight (kg)", min_value=0.0)

goal = st.selectbox("Goal",
    ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
)

level = st.selectbox("Level",
    ["Beginner", "Intermediate", "Advanced"]
)

equipment = st.multiselect("Equipment",
    ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment",
     "Bench", "Treadmill", "Cycle", "Pullup Bar"]
)

generate = st.button("Generate Ultra Plan 🚀")

# ===== BMI FUNCTIONS =====
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# ===== WORKOUT GENERATOR =====
def generate_workout(goal, level):
    plans = {
        "Weight Loss": ["HIIT Sprint", "Burpees", "Mountain Climbers"],
        "Build Muscle": ["Bench Press", "Squats", "Pullups"],
        "Strength Gain": ["Deadlifts", "Heavy Pullups"],
        "Abs Building": ["Planks", "Leg Raises"],
        "Flexible": ["Yoga Flow", "Mobility Training"]
    }

    workout = plans.get(goal, [])

    if level == "Intermediate":
        workout = [w + " 🔥" for w in workout]
    elif level == "Advanced":
        workout = [w + " 💎 ELITE" for w in workout]

    return workout

# ===== RESULTS =====
if generate:
    if name.strip() == "" or height_cm <= 0 or weight_kg <= 0:
        st.error("Please complete all fields properly.")
    else:
        bmi = calculate_bmi(height_cm, weight_kg)
        category = bmi_category(bmi)

        st.subheader(f"👤 {name}")
        st.markdown(f"### BMI: {bmi}")
        st.markdown(f"### Category: {category}")

        st.markdown("---")
        st.subheader("🏋️ ULTRA WORKOUT PLAN")

        for exercise in generate_workout(goal, level):
            st.markdown(f"⚡ {exercise}")