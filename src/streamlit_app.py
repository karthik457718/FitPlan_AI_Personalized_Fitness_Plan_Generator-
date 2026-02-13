import streamlit as st

st.set_page_config(page_title="FitPlan AI", page_icon="💪", layout="wide")

st.markdown("""
<style>

/* ===== Modern Font ===== */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

/* ===== Gym Background with Dark Transparent Overlay ===== */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(10,10,20,0.75), rgba(10,10,20,0.75)),
        url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* ===== Centered Container ===== */
.block-container {
    max-width: 1150px;
    margin: auto;
    padding-top: 60px;
}

/* ===== Glass Card ===== */
.glass {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(25px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 28px;
    padding: 40px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.5);
    margin-bottom: 35px;
}

/* ===== Result Premium Glow ===== */
.result-glass {
    background: linear-gradient(135deg, rgba(255,0,150,0.15), rgba(110,0,255,0.15));
    backdrop-filter: blur(30px);
    border-radius: 28px;
    padding: 40px;
    box-shadow: 0 0 60px rgba(255,0,200,0.25);
}

/* ===== Typography ===== */
h1 {
    font-size: 48px !important;
    font-weight: 700 !important;
    color: white !important;
    text-align: center;
}

h2, h3, h4, p, label {
    color: rgba(255,255,255,0.95) !important;
}

/* ===== Inputs ===== */
.stTextInput input,
.stNumberInput input,
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.1) !important;
    color: white !important;
    border-radius: 16px !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    padding: 10px !important;
}

/* ===== Premium Button ===== */
.stButton > button {
    background: linear-gradient(135deg, #ff0080, #7928ca);
    border-radius: 50px;
    padding: 14px 45px;
    border: none;
    font-size: 16px;
    font-weight: 600;
    color: white;
    box-shadow: 0 15px 35px rgba(255,0,200,0.4);
    transition: 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 45px rgba(255,0,200,0.6);
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1>💪 FitPlan AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Train Smart. Look Sharp. Perform Better.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1,1], gap="large")

with col1:
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

    generate = st.button("Generate Elite Plan 🚀")

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
        "Weight Loss": ["HIIT Circuit", "Sprint Intervals", "Burpees"],
        "Strength Gain": ["Deadlifts", "Weighted Pullups"],
        "Abs Building": ["Plank Series", "Hanging Leg Raises"],
        "Flexible": ["Yoga Flow", "Mobility Routine"]
    }
    workout = plans.get(goal, [])
    if level == "Intermediate":
        workout = [w + " 🔥" for w in workout]
    elif level == "Advanced":
        workout = [w + " 💎 Elite" for w in workout]
    return workout


with col2:
    if generate:
        if name.strip() == "" or height_cm <= 0 or weight_kg <= 0:
            st.error("Please complete all fields properly.")
        else:
            bmi = calculate_bmi(height_cm, weight_kg)
            category = bmi_category(bmi)

            st.markdown('<div class="result-glass">', unsafe_allow_html=True)

            st.markdown(f"### {name}")
            st.markdown(f"## BMI: {bmi}")
            st.markdown(f"### Category: {category}")

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 🏆 Recommended Plan")

            for ex in generate_workout(goal, level):
                st.markdown(f"- {ex}")

            st.markdown('</div>', unsafe_allow_html=True)

            st.success("Elite consistency builds elite results. 💎")