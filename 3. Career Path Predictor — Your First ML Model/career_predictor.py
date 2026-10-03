import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
data = pd.read_csv("career_dataset.csv")

# Separate the features and target
X = data[["skills"]]
y = data["career"]

# Convert the skills into numbers
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X)

# Create the Decision Tree model
model = DecisionTreeClassifier()

# Train the model
model.fit(X_encoded, y)

# Get input from the user
user_skill = input("Enter one of your main skills or interests: ").strip().lower()

# Check if the skill exists in the dataset
known_skills = data["skills"].str.lower().tolist()

if user_skill not in known_skills:
    print("Sorry, that skill is not in our training dataset.")
    print("Try a skill such as coding, painting, trading, or journalism.")
else:
    # Put the new skill into the same format as the training data
    new_skill = pd.DataFrame(
        [[user_skill]],
        columns=["skills"]
    )

    # Convert the new skill into numbers
    new_skill_encoded = encoder.transform(new_skill)

    # Predict the career category
    prediction = model.predict(new_skill_encoded)

    # Display the result
    print("Predicted career category:", prediction[0])