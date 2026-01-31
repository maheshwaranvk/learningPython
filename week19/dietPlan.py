import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# ---------------------------------
# 1. Create enriched diet dataset
# ---------------------------------
data = {
    "Current_Weight": [85, 78, 92, 80, 95, 88, 75, 82, 90, 77],
    "Calories": [2500, 2200, 1800, 2000, 2700, 1900, 2100, 2300, 1700, 2400],
    "Exercise_days": [2, 3, 5, 4, 1, 5, 4, 2, 6, 3],
    "Sleep_hours": [6, 7, 8, 7, 5, 8, 7, 6, 8, 6],
    "Protein_grams": [60, 80, 110, 95, 55, 120, 100, 70, 130, 85],
    "Sugar_grams": [90, 70, 40, 50, 110, 35, 55, 80, 30, 75],
    "Water_liters": [2.0, 2.5, 3.0, 2.7, 1.8, 3.2, 2.6, 2.2, 3.5, 2.4],
    "Steps_per_day": [4000, 6000, 9000, 8000, 3000, 10000, 7500, 5000, 11000, 6500],
    "Weight_Loss": [1.2, 2.5, 4.5, 3.2, 0.8, 4.8, 3.0, 2.0, 5.2, 1.8]
}

df = pd.DataFrame(data)

# ---------------------------------
# 2. Split features & target
# ---------------------------------
X = df.drop("Weight_Loss", axis=1)
y = df["Weight_Loss"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# ---------------------------------
# 3. Train Decision Tree Regressor
# ---------------------------------
model = DecisionTreeRegressor(
    max_depth=4,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------------------------
# 4. Predictions
# ---------------------------------
predictions = model.predict(X_test)

# ---------------------------------
# 5. Evaluate
# ---------------------------------
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", round(mse, 3))

# ---------------------------------
# 6. Predict for a new person
# ---------------------------------
new_person = [[
    80,     # Current weight (kg)
    2000,   # Calories
    4,      # Exercise days
    7,      # Sleep hours
    100,    # Protein grams
    45,     # Sugar grams
    3.0,    # Water liters
    8000    # Steps per day
]]

predicted_loss = model.predict(new_person)
print("Predicted weight loss (kg):", round(predicted_loss[0], 2))

# ---------------------------------
# 7. Visualize Decision Tree
# ---------------------------------
plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=X.columns, filled=True, rounded=True, fontsize=10)
plt.title("Decision Tree Regressor - Weight Loss Prediction")
plt.tight_layout()
plt.show()

# ---------------------------------
# 8. Feature Importance
# ---------------------------------
importances = model.feature_importances_
feature_importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'], color='steelblue')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importance for Weight Loss Prediction')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
