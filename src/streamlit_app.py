import streamlit as st

st.set_page_config(page_title="AI Fitness Planner", page_icon="💪", layout="wide")

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.block-container {
    background: rgba(0, 0, 0, 0.65);
    backdrop-filter: blur(18px);
    border-radius: 20px;
    padding: 2rem;
}

h1, h2, h3, h4, label, p {
    color: white !important;
}

.stTextInput input,
.stNumberInput input,
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.15) !important;
    color: white !important;
    border-radius: 10px;
}

.stButton > button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    border-radius: 12px;
    padding: 12px 28px;
    border: none;
    font-weight: 600;
}

.card {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}

.bmi-bar {
    height: 18px;
    border-radius: 10px;
    background: linear-gradient(to right, 
        #00bfff 0%, 
        #00ff00 25%, 
        #ffff00 50%, 
        #ff8000 75%, 
        #ff0000 100%);
}

</style>
""", unsafe_allow_html=True)

st.title("💪 AI Fitness Planner")
st.markdown("### Build your personalized workout plan")
st.markdown("---")

left, right = st.columns([1,1])

with left:

    st.markdown("## 👤 Personal Information")

    name = st.text_input("Full Name *")
    height_cm = st.number_input("Height (cm) *", min_value=0.0)
    weight_kg = st.number_input("Weight (kg) *", min_value=0.0)

    st.markdown("## 🎯 Fitness Details")

    goal = st.selectbox(
        "Select Your Goal",
        ["Flexible", "Weight Loss", "Build Muscle", "Strength Gain", "Abs Building"]
    )

    level = st.selectbox(
        "Fitness Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    equipment = st.multiselect(
        "Available Equipment",
        ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment",
         "Inclined Bench", "Treadmill", "Cycle", "Skipping Rope",
         "Hand Gripper", "Pullups Bar", "Weight Plates",
         "Hula Hoop Ring", "Bosu Ball"]
    )

    generate = st.button("Generate Fitness Report 🚀")


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
        "Weight Loss": ["Jump Rope – 3x2 min","Treadmill – 15 min","Burpees – 3x12","Mountain Climbers – 3x20"],
        "Build Muscle": ["Dumbbell Squats – 4x12","Bench Press – 4x10","Pullups – 3x8","Shoulder Press – 3x12"],
        "Strength Gain": ["Deadlift – 5x5","Pullups – 4x6","Dumbbell Press – 4x6"],
        "Abs Building": ["Plank – 3x60 sec","Leg Raises – 3x15","Russian Twists – 3x20"],
        "Flexible": ["Yoga Flow – 15 min","Stretching – 10 min","Mobility – 10 min"]
    }

    workout = plans.get(goal, [])

    if level == "Intermediate":
        workout = [w + " 🔥" for w in workout]
    elif level == "Advanced":
        workout = [w + " 💪🔥" for w in workout]

    return workout


with right:

    if generate:

        if name.strip() == "":
            st.error("Name is required.")
        elif height_cm <= 0 or weight_kg <= 0:
            st.error("Height and Weight must be greater than zero.")
        else:

            bmi = calculate_bmi(height_cm, weight_kg)
            category = bmi_category(bmi)

            st.markdown("## 💪 Your BMI Result")

            st.markdown(f"""
            <div class="card">
                <h3>{name}</h3>
                <h2>BMI: {bmi}</h2>
                <h4>Category: {category}</h4>
                <div class="bmi-bar"></div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("## 🏆 Your Workout Plan")

            plan = generate_workout(goal, level)

            for exercise in plan:
                st.markdown(f"""
                <div class="card">✅ {exercise}</div>
                """, unsafe_allow_html=True)

            st.success("Stay consistent. Results will follow! 💯🔥")