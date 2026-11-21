#Logistic regression 20-11-2026

# Import required libraries
from sklearn.linear_model import LogisticRegression

# Dataset
X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Predict for a student who studied 4 hours
prediction = model.predict([[4]])
prediction

# Display result
if prediction[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")

#sigmoid function
import math

# Given values
b0 = -5
b1 = 1.2
x = 5

# Calculate z
z = b0 + (b1 * x)

# Apply sigmoid function
probability = 1 / (1 + math.exp(-z))

print("Z value:", z)
print("Probability:", probability)

# Classification
if probability >= 0.5:
    print("Student will Pass")
else:
    print("Student will Fail")