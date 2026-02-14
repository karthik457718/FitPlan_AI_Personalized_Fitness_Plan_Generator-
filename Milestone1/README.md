
⸻

FitPlan AI – Personalized Fitness Plan Generator

Milestone 1: Front-End Development (BMI Calculator)

⸻

1. Project Overview

This project represents the first milestone of the FitPlan AI system.

The goal of this milestone is to build a simple and user-friendly web application that:
	•	Collects basic fitness information from users
	•	Calculates Body Mass Index (BMI)
	•	Classifies users into health categories
	•	Displays the result clearly

This milestone lays the foundation for future AI-based personalized fitness recommendations.

⸻

2. Features Implemented 🧩

Fitness Profile Form

An interactive form was developed using Streamlit to collect the following details:

Personal Information 👤
	•	Name (Required)
	•	Height in centimeters (Required)
	•	Weight in kilograms (Required)

Fitness Details 🏋️
	•	Fitness Goal
(Build Muscle, Weight Loss, Strength Gain, Abs Building, Flexible)
	•	Available Equipment
(Multiple selection allowed – Dumbbells, Resistance Band, Yoga Mat, No Equipment, etc.)
	•	Fitness Level
(Beginner, Intermediate, Advanced)

⸻

3. BMI Calculation Logic 📊

Formula Used

BMI = Weight (kg) / (Height (m))²

Steps Followed
	1.	Convert height from centimeters to meters
	2.	Apply the BMI formula
	3.	Round the result to two decimal places
	4.	Display the user’s name along with BMI value and category

⸻

4. BMI Classification 📌

The application automatically classifies users into the following categories:

| BMI Range        | Category        |
|------------------|-----------------|
| 18.5 and below   | Underweight     |
| 18.5 – 24.9      | Normal          |
| 25 – 29.9        | Overweight      |
| 30 and above     | Obese           |

⸻

5. Input Validation ✅

Strict validation rules are implemented to ensure accurate calculations:
	•	All required fields must be filled
	•	Height and weight must be greater than zero
	•	Clear warning messages are displayed for invalid inputs
	•	Prevents calculation errors from incomplete data

⸻

6. Deployment 🚀

Successfully deployed the application on Hugging Face Spaces.

Live Link:

👉 [Hugging Face Space](https://huggingface.co/spaces/Karthik71212/fit_plan)

Verification:
	•	Verified that the application works correctly after deployment
	•	Ensured responsive UI and proper display of results

⸻

7. Technologies Used 🛠️

| Technology        | Purpose                                |
|-------------------|----------------------------------------|
| Python            | Core programming language              |
| Streamlit         | Web application framework              |
| Hugging Face Spaces | Deployment platform                    |
| Git & GitHub      | Version control and code hosting       |

⸻

8. Project Structure 📂

FitPlan-AI/
├── Milestone1/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   └── screenshots/

⸻

9. Milestone Completion Status ✔

✔ Created user-friendly form
✔ BMI calculation function implemented
✔ BMI classification added
✔ Input validation working
✔ Successful deployment

⸻

10. Internship Submission

This completes Milestone 1 of the FitPlan AI project.