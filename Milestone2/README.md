FitPlan AI – Personalized Fitness Plan Generator

Milestone 2: Core AI Model Integration (LLM-Based Workout Generator)

⸻

1. Project Overview

This milestone enhances the FitPlan AI system by integrating a Large Language Model (LLM) to generate dynamic and personalized 5-day workout plans.

The objective of this milestone is to:

• Integrate a pre-trained Large Language Model from Hugging Face
• Construct structured prompts using user fitness inputs
• Generate personalized 5-day workout plans dynamically
• Deploy the AI-powered application on Hugging Face Spaces

This milestone transforms the application from a static BMI calculator into an intelligent AI-driven fitness assistant.

⸻

2. Features Implemented 🤖

AI Workout Plan Generator

The application now:

• Collects user fitness data from Milestone 1
• Constructs a structured AI prompt
• Sends the prompt to a pre-trained Hugging Face LLM
• Generates a complete 5-day personalized workout plan
• Displays the formatted workout plan in a styled interface

⸻

Multi-Page Application Structure

The system now uses a multi-page architecture:

Page 1:
• User profile form
• Age input added
• Fitness goal selection
• Equipment selection
• Fitness level selection

Page 2:
• AI-generated 5-day workout plan
• Displays BMI and BMI category
• Styled output card
• Back navigation button

⸻

3. Model Integration 🧠

Model Used

Qwen/Qwen2.5-7B-Instruct
(Pre-trained instruction-tuned LLM from Hugging Face)

Model Integration Steps
	1.	Imported InferenceClient from huggingface_hub
	2.	Used secure authentication via HF_TOKEN
	3.	Constructed chat-style messages
	4.	Generated structured text output
	5.	Handled inference errors using try-except blocks

Example Model Initialization:
client = InferenceClient(
    model="Qwen/Qwen2.5-7B-Instruct",
    token=HF_TOKEN
)

4. Prompt Engineering Strategy 📝

The prompt dynamically includes:

• Name
• Age
• Height & Weight
• Calculated BMI
• BMI Category
• Fitness Goal
• Fitness Level
• Available Equipment

The system instruction ensures:

• 5 clearly divided workout days
• Exercise names
• Sets and reps
• Rest periods
• Intensity adjusted to BMI category
• Beginner safety considerations

This structured prompt ensures high-quality, organized AI responses.

⸻

5. Error Handling & Validation ⚙️

The application includes:

• HF_TOKEN validation
• Model inference error handling
• Graceful fallback messages
• Required field validation
• Session state management for multi-page flow

⸻

6. Testing Scenarios 🧪

The model was tested using multiple user profiles:

Scenario 1:
• Beginner
• Weight loss goal
• No equipment

Scenario 2:
• Intermediate
• Muscle building
• Dumbbells & Bench

Scenario 3:
• Advanced
• Strength gain
• Full equipment

Each scenario successfully generated structured 5-day workout plans.

⸻

7. Deployment 🚀

The updated AI-powered application is deployed on Hugging Face Spaces.

Live Link:

👉 https://huggingface.co/spaces/Karthik71212/fit_plan

Deployment Verification:

• Model loads successfully
• HF_TOKEN authentication verified
• Multi-page navigation working
• Workout plan generation functioning
• Clean UI rendering

⸻

8. Technologies Used 🛠️
Technology	Purpose
Python	Core programming language
Streamlit	Web application framework
Hugging Face Spaces	Deployment platform
Git & GitHub	Version control and code hosting
9. Updated Project Structure 📂

FitPlan-AI/
├── Milestone2/
│   ├── app.py
│   ├── model_api.py
│   ├── prompt_builder.py
│   ├── requirements.txt
│   ├── README.md
│   ├── pages/
│   │   └── 1_Workout_Plan.py
│   └── screenshots/

⸻

10. Milestone Completion Status ✔

✔ Large Language Model integrated
✔ Secure token authentication implemented
✔ Structured prompt design completed
✔ AI-generated 5-day workout plan working
✔ Multi-page architecture implemented
✔ Deployed successfully on Hugging Face
✔ Error handling and validation added

⸻

11. Internship Submission

This completes Milestone 2 of the FitPlan AI project, transforming the system into an AI-powered personalized fitness planner.
