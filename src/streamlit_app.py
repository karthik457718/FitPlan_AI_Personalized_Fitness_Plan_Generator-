import streamlit as st

st.set_page_config(page_title="AI Fitness Planner", page_icon="💪", layout="wide")

st.markdown("""
<style>

/* Import modern font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Transparent gym background */
[data-testid="stAppViewContainer"] {
    background: 
        linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
        url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Center container */
.block-container {
    max-width: 1100px;
    margin: auto;
    padding: 2rem;
}

/* Glass effect */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(18px);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}

/* White text */
h1, h2, h3, h4, label, p {
    color: white !important;
}

/* Inputs styling */
.stTextInput input,
.stNumberInput input,
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.12) !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
}

/* Rounded Gradient Button */
.stButton > button {
    background: linear-gradient(90deg, #ff7b00, #ff0066);
    color: white;
    border-radius: 30px;
    padding: 14px 35px;
    border: none;
    font-weight: 600;
    font-size: 16px;
    transition: 0.3s ease;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #ff0066, #ff7b00);
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>💪 AI Fitness Planner</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Build your personalized workout plan</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("👤 Personal Information")
    name = st.text_input("Full Name *")
    height_cm = st.number_input("Height (cm) *", min_value=0.0)
    weight_kg = st.number_input("Weight (kg) *", min_value=0.0)

    st.subheader("🎯 Fitness Details")
    goal = st.selectbox("Select Your Goal",
        ["Flexible", "Weight Loss", "Build Muscle", "Strength Gain", "Abs Building"]
    )

    level = st.selectbox("Fitness Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    equipment = st.multiselect("Available Equipment",
        ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment",
         "Inclined Bench", "Treadmill", "Cycle", "Skipping Rope",
         "Hand Gripper", "Pullups Bar", "Weight Plates",
         "Hula Hoop Ring", "Bosu Ball"]
    )

    generate = st.button("Generate Fitness Report 🚀")

    st.markdown('</div>', unsafe_allow_html=True)


def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def generate_workout(goal, level):
    plans = {
        "Weight Loss": ["Jump Rope – 3x2 min","Treadmill – 15 min","Burpees – 3x12"],
        "Build Muscle": ["Dumbbell Squats – 4x12","Bench Press – 4x10","Pullups – 3x8"],
        "Strength Gain": ["Deadlift – 5x5","Pullups – 4x6"],
        "Abs Building": ["Plank – 3x60 sec","Leg Raises – 3x15"],
        "Flexible": ["Yoga Flow – 15 min","Stretching – 10 min"]
    }

    workout = plans.get(goal, [])
    if level == "Intermediate":
        workout = [w + " 🔥" for w in workout]
    elif level == "Advanced":
        workout = [w + " 💪🔥" for w in workout]
    return workout


with col2:
    if generate:
        if name.strip() == "":
            st.error("Name is required.")
        elif height_cm <= 0 or weight_kg <= 0:
            st.error("Height and Weight must be greater than zero.")
        else:
            bmi = calculate_bmi(height_cm, weight_kg)
            category = bmi_category(bmi)

            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("💪 Your BMI Result")
            st.write(f"### {name}")
            st.write(f"## BMI: {bmi}")
            st.write(f"### Category: {category}")
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("🏆 Your Workout Plan")
            plan = generate_workout(goal, level)
            for ex in plan:
                st.write("✅", ex)
            st.markdown('</div>', unsafe_allow_html=True)

            st.success("Stay consistent. Results will follow! 💯🔥")