import Model
import gradio as gr

def predict_heart_disease(age, sex, cp, thalach, exang, oldpeak, slope, ca, thal):
    prediction = Model.predict(age, sex, cp, thalach, exang, oldpeak, slope, ca, thal)
    return "You are likely to have heart disease." if prediction[0] == 'Heart Disease' else "You are unlikely to have heart disease."

questions = [
    "Please enter the age of the patient:",
    "What is the patient's birth gender? (Enter 0 for female, 1 for male):",
    "What type of chest pain did the patient receive? (0: asymptomatic, 1: typical angina, 2: atypical angina, 3: non-anginal pain):",
    "What is the patient's maximum heart rate during exercise?",
    "Does the patient receive angina (chest pain) during exercise? (Enter 1 for Yes, 0 for No):",
    "How much does the patient's heart activity decrease during exercise compared to rest? Please provide a numerical value.:",
    "What is the patient's slope of the peak exercise ST segment? (0: downsloping, 1: flat, 2: upsloping):",
    "How many of the patient's major vessels are colored by fluoroscopy? (Enter a number from 0 to 3):",
    "Please enter the patient's thalassemia value. (1: normal, 2: fixed defect, 3: reversible defect):"
]

demo = gr.Interface(
    fn=predict_heart_disease,
    inputs=[gr.Text(label=q) for q in questions],
    outputs="text"
)

if __name__ == "__main__":
    demo.launch()
