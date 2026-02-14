# 🏋️ FitPlan AI – Personalized Fitness Plan Generator  
## 📌 Milestone 1: Front-End Development (BMI Calculator)

---

## 🎯 Objective of the Milestone

The objective of Milestone 1 is to design and develop a user-friendly web application that collects essential fitness details from users and accurately calculates their Body Mass Index (BMI).

This milestone builds the foundation of the FitPlan AI project before integrating AI-based personalized fitness recommendations.

### Key Objectives:
- Create an interactive and structured fitness profile form  
- Collect essential health and fitness information  
- Implement accurate BMI calculation logic  
- Classify BMI into standard health categories  
- Apply proper input validation  
- Deploy the application on Hugging Face Spaces  

---

## 📐 BMI Formula Explanation

Body Mass Index (BMI) is a standard measurement used to determine whether a person has a healthy body weight relative to their height.

### ✅ Formula Used:

```
BMI = Weight (kg) / (Height (m))²
```

### 🔎 Steps Implemented in the Application:

1. Convert height from centimeters to meters  
   ```
   height_in_meters = height_in_cm / 100
   ```

2. Apply the BMI formula  
   ```
   BMI = weight / (height_in_meters ** 2)
   ```

3. Round the result to two decimal places  
   ```
   BMI = round(BMI, 2)
   ```

---

## 📊 BMI Classification Categories

| BMI Range        | Category      |
|------------------|--------------|
| Less than 18.5   | Underweight  |
| 18.5 – 24.9      | Normal       |
| 25 – 29.9        | Overweight   |
| 30 and above     | Obese        |

The application automatically classifies the user based on the calculated BMI.

---

## 🛠 Steps Performed

### 1️⃣ Form Creation

Developed an interactive fitness profile form using Streamlit.

### 📌 Personal Information Collected:
- Name (Required)  
- Height in centimeters (Required)  
- Weight in kilograms (Required)  

### 📌 Fitness Details Collected:
- Fitness Goal  
  (Build Muscle, Weight Loss, Strength Gain, Abs Building, Flexible)  
- Available Equipment  
  (Multiple selection allowed – Dumbbells, Resistance Band, Yoga Mat, No Equipment, etc.)  
- Fitness Level  
  (Beginner, Intermediate, Advanced)  

---

### 2️⃣ Input Validation

Implemented validation to ensure:

- Required fields are not left empty  
- Height and weight values are greater than zero  
- Clear warning messages are displayed for invalid inputs  

This ensures accuracy and prevents incorrect BMI calculations.

---

### 3️⃣ BMI Logic Implementation

- Converted height from centimeters to meters  
- Applied the BMI formula correctly  
- Rounded BMI to two decimal places  
- Classified users into the appropriate BMI category  
- Displayed the user’s name along with calculated BMI and category  

---

### 4️⃣ Deployment

- Successfully deployed the application on Hugging Face Spaces  
- Verified functionality after deployment  
- Ensured proper UI responsiveness and result display  

---

## 🚀 Technologies Used

- Python  
- Streamlit  
- Hugging Face Spaces  
- Git & GitHub  

---

## 🌐 Live Deployment Link

👉 **Hugging Face Space:**  
(Add your live Hugging Face Space link here)
https://huggingface.co/spaces/Karthik71212/fit_plan


## 📸 Application Screenshots

### 🔹 User Input Form

![User Form](screenshots/form.png)

---

### 🔹 BMI Result Output

![BMI Result](screenshots/bmi_result.png)

---

## 📂 Project Structure

```
FitPlan-AI/
└── Milestone1/
    ├── app.py
    ├── requirements.txt
    ├── README.md
    └── screenshots/
```

---

## ✅ Milestone Completion Status

✔ User-Friendly Form Created  
✔ BMI Calculation Implemented  
✔ BMI Classification Added  
✔ Input Validation Applied  
✔ Successfully Deployed  

---

## 👨‍💻 Internship Submission  
**FitPlan AI – Milestone 1**