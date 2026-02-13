import streamlit as st
import time

st.set_page_config(page_title="FitPlan AI Elite", page_icon="💎", layout="wide")

# ================== CSS ==================
st.markdown("""
<style>

/* ===== GOOGLE FONT ===== */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

/* ===== CINEMATIC BACKGROUND ===== */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(10,10,20,0.45), rgba(10,10,20,0.45)),
        url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* ===== TEXT COLORS ===== */
h1, h2, h3, h4, p, label {
    color: white !important;
}

/* ===== GLASS INPUT ===== */
div[data-baseweb="input"],
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 30px !important;
    border: 2px solid rgba(255,255,255,0.35) !important;
    backdrop-filter: blur(15px);
    transition: all 0.3s ease !important;
}

div[data-baseweb="input"] > div {
    background: transparent !important;
}

div[data-baseweb="input"] input {
    background: transparent !important;
    color: white !important;
    border: none !important;
}

div[data-baseweb="input"] button {
    background: transparent !important;
    color: white !important;
}

/* ===== HOVER GLOW ===== */
div[data-baseweb="input"]:hover,
.stSelectbox > div > div:hover,
.stMultiSelect > div > div:hover {
    border: 2px solid transparent !important;
    background: linear-gradient(rgba(20,20,40,0.8), rgba(20,20,40,0.8)) padding-box,
                linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff) border-box !important;
    box-shadow:
        0 0 15px #ff00cc,
        0 0 25px #7928ca,
        0 0 35px #00f0ff !important;
}

/* ===== NEON BUTTON ===== */
.stButton > button {
    background: rgba(255,255,255,0.12) !important;
    border-radius: 40px !important;
    padding: 14px 45px !important;
    border: 2px solid rgba(255,255,255,0.4) !important;
    color: white !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff) !important;
    background-size: 300% 300% !important;
    animation: neonMove 4s ease infinite !important;
    border: none !important;
    box-shadow:
        0 0 20px #ff00cc,
        0 0 40px #7928ca,
        0 0 60px #00f0ff !important;
    transform: translateY(-4px) scale(1.03) !important;
}

@keyframes neonMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

img {
    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# ================== HERO LAYOUT ==================

left, center, right = st.columns([1,2,1])

with left:
    st.image(
        "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
        use_column_width=True
    )

with center:
    st.markdown("<h1 style='text-align:center;'>💎 FitPlan AI Elite</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Train Smart. Perform Elite.</p>", unsafe_allow_html=True)

with right:
    st.image(
        "https://images.unsplash.com/photo-1558611848-73f7eb4001a1",
        use_column_width=True
    )

st.markdown("---")

# ================== FORM ==================

name = st.text_input("Full Name")

height_cm = st.number_input(
    "Height (cm)",
    min_value=1,
    value=170,
    step=1,
    format="%d"
)

weight_kg = st.number_input(
    "Weight (kg)",
    min_value=1,
    value=70,
    step=1,
    format="%d"
)

goal = st.selectbox(
    "Goal",
    ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
)

level = st.selectbox(
    "Level",
    ["Beginner", "Intermediate", "Advanced"]
)

equipment = st.multiselect(
    "Equipment",
    ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment",
     "Bench", "Treadmill", "Cycle", "Pullup Bar"]
)

generate = st.button("Generate Elite Plan 🚀")

# ================== BMI ==================

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

def generate_workout(goal, level):
    plans = {
        "Weight Loss": ["Jump Rope – 3x2 min", "Burpees – 3x12"],
        "Build Muscle": ["Bench Press – 4x10", "Pullups – 3x8"],
        "Strength Gain": ["Deadlifts – 5x5"],
        "Abs Building": ["Planks – 3x60 sec"],
        "Flexible": ["Yoga Flow – 20 min"]
    }
    workout = plans.get(goal, [])
    if level == "Intermediate":
        workout = [w + " 🔥" for w in workout]
    elif level == "Advanced":
        workout = [w + " 💪 ELITE" for w in workout]
    return workout

if generate:
    if name.strip() == "":
        st.error("Please enter your name.")
    else:
        bmi = calculate_bmi(height_cm, weight_kg)
        category = bmi_category(bmi)

        st.subheader(f"👤 {name}")
        st.markdown(f"### BMI: {bmi}")
        st.markdown(f"### Category: {category}")

        st.markdown("---")
        st.subheader("🏋️ Your Personalized Workout Plan")

        for exercise in generate_workout(goal, level):
            st.markdown(f"✅ {exercise}")