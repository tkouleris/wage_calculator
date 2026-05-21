import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv("data.csv")

# Remove duplicate columns if needed
df = df.loc[:, ~df.columns.duplicated()]

# Target column
target = "Yearly Income"

# Features and labels
X = df.drop(columns=[target])
y = df[target]

# Handle missing values
imputer = SimpleImputer(strategy="median")
X = imputer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error:", mae)
print("R² Score:", r2)
print("****************************************************")
# print(X_test[1])

# Example prediction
sample_prediction = model.predict([X_test[0]])
print("Predicted income:", sample_prediction[0] / 14)
print("Actual income:", y_test.iloc[0] / 14)
print("===================================================")
sample_prediction = model.predict([X_test[1]])
print("Predicted income:", sample_prediction[0] / 14)
print("Actual income:", y_test.iloc[1] / 14)
print("===================================================")
sample_prediction = model.predict([X_test[2]])
print("Predicted income:", sample_prediction[0] / 14)
print("Actual income:", y_test.iloc[2] / 14)
print("===================================================")
sample_prediction = model.predict([X_test[3]])
print("Predicted income:", sample_prediction[0] / 14)
print("Actual income:", y_test.iloc[3] / 14)
print("===================================================")
sample_prediction = model.predict([X_test[4]])
print("Predicted income:", sample_prediction[0] / 14)
print("Actual income:", y_test.iloc[4] / 14)
print("===================================================")
sample_prediction = model.predict([X_test[5]])
print("Predicted income:", sample_prediction[0] / 14)
print("Actual income:", y_test.iloc[5] / 14)

import joblib

joblib.dump(model, "income_model.pkl")
joblib.dump(imputer, "imputer.pkl")