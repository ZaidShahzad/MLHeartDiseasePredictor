import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Load the dataset and preprocess it
dataset = pd.read_csv("./dataset/Heart_disease_cleveland_new.csv")

# Drop columns that are not used in the model
dataset = dataset.drop({"trestbps", "chol", "fbs", "restecg"}, axis=1)

# Convert target variable to categorical labels
dataset['target'] = dataset['target'].replace({0: 'Normal', 1: 'Heart Disease'})

# Split the dataset into training and testing sets
X = dataset.drop(['target'], axis=1)
Y = dataset['target']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.7, test_size=0.3, random_state=2)

# Define and train an SVM model
svm_model = SVC(kernel='linear', C=0.1, gamma='scale')
svm_model.fit(X_train, Y_train)

# Function to make predictions using the trained model
def predict(age, sex, cp, thalach, exang, oldpeak, slope, ca, thal):
    # Convert inputs to the required data types and structure them as a single sample
    try:
        input_data = [
            [
                float(age),
                int(sex),
                int(cp),
                float(thalach),
                int(exang),
                float(oldpeak),
                int(slope),
                int(ca),
                int(thal)
            ]
        ]
        prediction = svm_model.predict(input_data)
        return prediction[0]
    except ValueError as e:
        # Return error message if there is a value error in the input data
        return str(e)
