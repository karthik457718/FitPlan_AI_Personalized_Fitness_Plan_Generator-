import streamlit as st

st.set_page_config(page_title="FitPlan AI", page_icon="💪", layout="wide")

st.markdown("""
<style>

/* ===== Google Font ===== */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

/* ===== Premium Gradient Background ===== */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 20% 30%, #1f1f3a 0%, transparent 40%),
                radial-gradient(circle at 80% 70%, #3a1f2f 0%, transparent 40%),
                linear-gradient(135deg, #0f0f1c, #1a1a2e);
    background-attachment: fixed;
}

/* ===== Center Layout ===== */
.block-container {
    max-width: 1150px;
    margin: auto;
    padding-top: 60px;
}

/* ===== Glass Card ===== */
.glass {
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(25px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 24px;
    padding: 35px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    margin-bottom: 30px;
}

/* ===== Headings ===== */
h1 {
    font-size: 42px !important;
    font-weight: 700 !important;
    color: white !important;
}

h2, h3, h4, p, label {
    color: rgba(255,255,255,0.9) !important;
}

/* ===== Inputs ===== */
.stTextInput input,
.stNumberInput input,
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    padding: 10px !important;
}

/* ===== Premium Button ===== */
.stButton > button {
    background: linear-gradient(135deg, #6e00ff, #ff00cc);
    border-radius: 50px;
    padding: 14px 40px;
    border: none;
    font-size: 16px;
    font-weight: 600;
    color: white;
    box-shadow: 0 10px 30px rgba(255,0,200,0.4);
    transition: 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 40px rgba(255,0,200,0.6);
}

/* ===== Result Glow Card ===== */
.result-card {
    background: linear-gradient(135deg, rgba(110,0,255,0.15), rgba(255,0,200,0.15));
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 0 50px rgba(255,0,200,0.2);
    backdrop-filter: blur(25px);
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>💪 FitPlan AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Design. Perform. Transform.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns([1,1], gap="large")

with left:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("👤 Personal Profile")

    name = st.text_input("Full Name")
    height_cm = st.number_input("Height (cm)", min_value=0.0)
    weight_kg = st.number_input("Weight (kg)", min_value=0.0)

    st.subheader("🎯 Fitness Preferences")

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

    generate = st.button("Generate Plan")

    st.markdown('</div>', unsafe_allow_html=True)


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
        "Build Muscle": ["Barbell Squats", "Bench Press", "Pull-ups"],
        "Weight Loss": ["HIIT Circuit", "Treadmill Run", "Burpees"],
        "Strength Gain": ["Deadlifts", "Weighted Pullups"],
        "Abs Building": ["Plank Variations", "Hanging Leg Raises"],
        "Flexible": ["Yoga Flow", "Mobility Routine"]
    }
    workout = plans.get(goal, [])
    if level == "Intermediate":
        workout = [w + " 🔥" for w in workout]
    elif level == "Advanced":
        workout = [w + " 💎" for w in workout]
    return workout


with right:
    if generate:
        if name.strip() == "" or height_cm <= 0 or weight_kg <= 0:
            st.error("Please fill all required fields properly.")
        else:
            bmi = calculate_bmi(height_cm, weight_kg)
            category = bmi_category(bmi)

            st.markdown('<div class="result-card">', unsafe_allow_html=True)

            st.markdown(f"### {name}")
            st.markdown(f"## BMI: {bmi}")
            st.markdown(f"### Category: {category}")

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("### 🏆 Workout Plan")

            for ex in generate_workout(goal, level):
                st.markdown(f"- {ex}")

            st.markdown('</div>', unsafe_allow_html=True)

            st.success("Consistency beats motivation. 🚀")