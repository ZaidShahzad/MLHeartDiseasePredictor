import Model
import gradio as gr

# Prediction function that takes in patient data and returns a prediction about heart disease.
def predict_heart_disease(age, sex, cp, thalach, exang, oldpeak, slope, ca, thal):
    # Check if any of the fields are left blank
    if None in [age, sex, cp, thalach, exang, oldpeak, slope, ca, thal]:
        return "Please fill in all fields before predicting."

    # Convert categorical inputs to numerical values based on predefined mappings
    sex = 1 if sex == "Male" else 0
    cp_mapping = {"Asymptomatic": 0, "Typical Angina": 1, "Atypical Angina": 2, "Non-Anginal Pain": 3}
    cp = cp_mapping[cp]
    slope_mapping = {"Downsloping": 0, "Flat": 1, "Upsloping": 2}
    slope = slope_mapping[slope]
    thal_mapping = {"Normal": 1, "Fixed Defect": 2, "Reversible Defect": 3}
    thal = thal_mapping[thal]

    # Use the Model module to predict and return the result
    prediction = Model.predict(age, sex, cp, thalach, exang, oldpeak, slope, ca, thal)
    return "You are likely to have heart disease." if prediction == 'Heart Disease' else "You are unlikely to have heart disease."


# Set up the Gradio interface
demo = gr.Blocks(theme=gr.themes.Monochrome(), css="#border {box-shadow: 0 4px 8px 0;}")

with demo:
    # Display titles and descriptions
    gr.Markdown("<h1 style='text-align: center; font-family: Arial, Helvetica, sans-serif; font-weight: bold;'>Heart Disease Predictor</h1>")
    gr.Markdown("<h2 style='text-align: center; font-weight: font-family: Times New Roman, Times, serif; bold;'>Predicts the likelihood of heart disease based on patient data.</h2>")

    # Organize the input fields and result display in a two-column layout
    with gr.Row():
        # Column for input fields (Patient Information)
        with gr.Column(elem_id="border"):
            gr.Markdown("<h3 style='padding-left: 13px; font-family: Arial, Helvetica, sans-serif; font-weight: bold;'>Patient Information<h3/>")
            age = gr.Number(label="Age of the patient", precision=0, step=1)
            sex = gr.Radio(choices=["Female", "Male"], label="Birth Gender", value="Female")
            cp = gr.Dropdown(elem_id="blacktext", choices=["Asymptomatic", "Typical Angina", "Atypical Angina", "Non-Anginal Pain"], label="Type of Chest Pain")
            thalach = gr.Slider(minimum=60, maximum=200, label="Maximum Heart Rate during Exercise")
            exang = gr.Checkbox(label="Angina during Exercise")
            oldpeak = gr.Number(label="Heart Activity Decrease during Exercise", precision=2)
            slope = gr.Radio(choices=["Downsloping", "Flat", "Upsloping"], label="Slope of Peak Exercise ST Segment")
            ca = gr.Slider(minimum=0, maximum=3, step=1, label="Major Vessels Colored by Fluoroscopy")
            thal = gr.Dropdown(choices=["Normal", "Fixed Defect", "Reversible Defect"], label="Thalassemia")

        # Column for displaying output (Result)
        with gr.Column(elem_id="border"):
            gr.Markdown("<h3 style='padding-left: 13px; font-family: Arial, Helvetica, sans-serif; font-weight: bold;'>Result<h3/>")
            output = gr.Textbox(label="Prediction")
            btn = gr.Button("Predict")
            btn.click(predict_heart_disease, inputs=[age, sex, cp, thalach, exang, oldpeak, slope, ca, thal],
                      outputs=output)

# Launch the Gradio interface
if __name__ == "__main__":
    demo.launch()
