import streamlit as st

st.set_page_config(
    page_title="AI Fitness Planner",
    page_icon="💪",
    layout="wide"
)

# ===============================
# CUSTOM MODERN UI (Like Image)
# ===============================
st.markdown("""
<style>

/* Full Animated Gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, 
        #000000 0%, 
        #1a1a1a 25%, 
        #2c2c2c 50%, 
        #1a1a1a 75%, 
        #000000 100%);
    background-size: 300% 300%;
    animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Glass Container */
.block-container {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(18px);
    border-radius: 20px;
    padding: 2rem;
}

/* Remove header background */
[data-testid="stHeader"] {
    background: transparent;
}

/* White Text */
h1, h2, h3, label, p {
    color: white !important;
}

/* Inputs */
.stTextInput input,
.stNumberInput input,
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.15) !important;
    color: white !important;
    border-radius: 10px;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    border-radius: 12px;
    padding: 12px 28px;
    border: none;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# ===============================
# HEADER
# ===============================
col1, col2 = st.columns([2, 1])

with col1:
    st.title("💪 AI Fitness Planner")
    st.markdown("### Build your personalized workout plan")
    st.markdown("---")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2936/2936886.png", width=200)


# ===============================
# PERSONAL INFORMATION SECTION
# ===============================
st.subheader("👤 Personal Information")

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("Full Name *")

with col2:
    height_cm = st.number_input("Height (cm) *", min_value=0.0, step=0.1)

with col3:
    weight_kg = st.number_input("Weight (kg) *", min_value=0.0, step=0.1)

st.markdown("---")

# ===============================
# FITNESS DETAILS SECTION
# ===============================
st.subheader("🎯 Fitness Details")

col1, col2 = st.columns(2)

with col1:
    goal = st.selectbox(
        "Select Your Goal",
        ["Flexible", "Weight Loss", "Build Muscle", "Strength Gain", "Abs Building"]
    )

with col2:
    level = st.selectbox(
        "Fitness Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

equipment = st.multiselect(
    "🏋️ Select Available Equipment",
    [
        "Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment",
        "Inclined Bench", "Treadmill", "Cycle", "Skipping Rope",
        "Hand Gripper", "Pullups Bar", "Weight Plates",
        "Hula Hoop Ring", "Bosu Ball"
    ]
)

st.markdown("---")


# ===============================
# BMI CALCULATION FUNCTION
# ===============================
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


# ===============================
# WORKOUT PLAN FUNCTION (UNCHANGED)
# ===============================
def generate_workout(goal, level):

    plans = {
        "Weight Loss": [
            "Jump Rope – 3x2 min",
            "Treadmill Run – 15 min",
            "Burpees – 3x12",
            "Mountain Climbers – 3x20",
            "Cycling – 10 min"
        ],
        "Build Muscle": [
            "Dumbbell Squats – 4x12",
            "Incline Bench Press – 4x10",
            "Pullups – 3x8",
            "Dumbbell Shoulder Press – 3x12",
            "Resistance Band Rows – 3x15"
        ],
        "Strength Gain": [
            "Deadlift – 5x5",
            "Pullups – 4x6",
            "Dumbbell Press – 4x6",
            "Hand Gripper – 3xMax",
            "Bosu Ball Squats – 3x10"
        ],
        "Abs Building": [
            "Plank – 3x60 sec",
            "Leg Raises – 3x15",
            "Russian Twists – 3x20",
            "Mountain Climbers – 3x25",
            "Bosu Ball Crunches – 3x15"
        ],
        "Flexible": [
            "Yoga Flow – 15 min",
            "Hamstring Stretch – 3x30 sec",
            "Hip Mobility – 10 min",
            "Cat-Cow – 3x15",
            "Balance Hold – 3x30 sec"
        ]
    }

    workout = plans.get(goal, [])

    if level == "Intermediate":
        workout = [exercise + " 🔥" for exercise in workout]
    elif level == "Advanced":
        workout = [exercise + " 💪🔥 (Increase weight/intensity)" for exercise in workout]

    return workout


# ===============================
# MAIN BUTTON
# ===============================
if st.button("Generate Fitness Report 🚀"):

    # ===== INPUT VALIDATION =====
    if name.strip() == "":
        st.error("⚠ Name is required.")
    elif height_cm <= 0 or weight_kg <= 0:
        st.error("⚠ Height and Weight must be greater than zero.")
    else:

        bmi = calculate_bmi(height_cm, weight_kg)
        category = bmi_category(bmi)

        st.subheader("📊 Your BMI Result")

        st.markdown(f"""
        <div style="
            padding:20px;
            background:rgba(255,255,255,0.12);
            border-radius:15px;
            margin-bottom:20px;">
            <h3>👤 {name}</h3>
            <h2>BMI: {bmi}</h2>
            <h3>Category: {category}</h3>
        </div>
        """, unsafe_allow_html=True)

        # ===== Workout Plan =====
        st.subheader("🏆 Your Personalized Workout Plan")

        plan = generate_workout(goal, level)

        for exercise in plan:
            st.markdown(f"""
            <div style="
                padding:15px;
                margin-bottom:10px;
                background:rgba(255,255,255,0.15);
                border-radius:12px;">
                ✅ {exercise}
            </div>
            """, unsafe_allow_html=True)

        st.success("Stay consistent. Results will follow! 💯🔥")