FitPlan AI – Personalized Fitness Plan Generator 

Milestone 1: Front-End Development (BMI Calculator) 

Objective of the Milestone 

The Milestone 1’s aim is to design and develop a web application that is easy to use and that gathers necessary fitness-related information from users and computes their BMI body mass index accurately. The milestone thus lays the groundwork of the FitPlan AI project before further integrating and utilising AI-based personalising fitness recommendation services. 

Key Objectives: 

Fitness profile form (Interactive) – create a structured form. Collect basic information related to the user’s health and fitness. Write logic for BMI calculation. Determine the health categories based on BMI results. Perform input validation. Successfully host the app on Huggingface space”. 

BMI Formula Explanation 

Body Mass Index (BMI) is a standard measurement that is used to ascertain whether or not an individual has a healthy body weight for their height. 

Formula Used: 

BMI = Weight (kg) / (height (m))2 

Steps Implemented in the Application: 

Convert height in centimeters to meters. Use the BMI formula. Evaluate the result to two decimal places. 

BMI Classification Categories 

Based on the calculated BMI, the user is automatically classified by the application. 

| BMI Range        | Category     | | | 18.5 and below  | Underweight | | 18.5 – 24.9      | Normal       | | 25 – 29.9        | Overweight   | | 30 and above     | Obese        | 

Steps Performed 

Form creation Form Creation: Created an interactive fitness profile form using Streamlit. 

Personal Information Collected: 

Name (required) Height in centimeters (compulsory) Weight in kilograms (required) 

Fitness Details Collected: 

Fitness Goal (Build Muscle, Weight Loss, Strength Gain, Abs Building, Flexible). Equipment at One’s Disposal (Multiple choices allowed- Dumbbells, Resistance Band, Yoga Mat, No Equipment, and more). Fitness Level (Beginner, Intermediate and Advanced). 

Input Validation 

Validation wise: The required fields are not left blank. Height and weight values should be greater than zero. Warning messages are clearly shown for invalid inputs. 

This ensures that a wrong BMI calculation is not performed on the data. 

BMI Logic Implementation 

Converted height from centimeters to meters. Used the BMI formula correctly. Calculated BMI and rounded it to the nearest two decimals. Classified users into BMI categories. The user’s name is also displayed with his calculated BMI and category. 

Deployment 

Deployed the application on Hugging Face Spaces successfully; Verified functionality after deployment; Made sure the UI was responsive and the results were displayed properly. 

Technologies Used 

Python Streamlit Hugging Face Spaces Git & GitHub 

Live Deployment Link 

👉 Hugging Face Space: https://huggingface.co/spaces/Karthik71212/fit_plan 

Project Structure 

FitPlan-AI/ Milestone1/     ├── app.py     ├── requirements.txt     ├── README.md     └── screenshots/ 

Milestone Completion Status 

✔ Created User-Friendly Form ✔ BMI Calculation Function; ✔ BMI Classification Added; ✔ Validation of the Inputs ✔ Made a Successful Deployment 

Internship Submission 

FitPlan AI – Milestone 1 