# Logistic Regression – Hands-on Implementation

## 1. Introduction

This notebook demonstrates the implementation of Logistic Regression, a supervised Machine Learning algorithm used for binary classification problems.

In this practical example, Logistic Regression is used to predict whether a student will pass or fail based on the number of hours studied.

The notebook also demonstrates the mathematical working of the Sigmoid Function, which converts a linear combination of input features into a probability between 0 and 1.

## 2. Objectives

- Understand the fundamentals of Logistic Regression.
- Implement Logistic Regression using Python and Scikit-learn.
- Predict binary outcomes using a trained model.
- Understand the Sigmoid Function.
- Calculate probabilities using the Logistic Regression equation.
- Classify predictions using a probability threshold of 0.5.

## 3. Dataset Description

A simple sample dataset is used to demonstrate student performance prediction.

| Study Hours | Result |
|---|---|
| 1 | Fail (0) |
| 2 | Fail (0) |
| 3 | Fail (0) |
| 4 | Pass (1) |
| 5 | Pass (1) |
| 6 | Pass (1) |

**Input Feature (X):** Number of hours studied.

**Target Variable (y):** Student result (0 = Fail, 1 = Pass).

## 4. Tools and Libraries

- Python
- Google Colab / Jupyter Notebook
- Scikit-learn
- Math (Python standard library)

## 5. Implementation

### Part A: Logistic Regression using Scikit-learn

The LogisticRegression class from Scikit-learn is used to create and train the classification model.

Steps involved:

1. Import the Logistic Regression library.
2. Define the dataset.
3. Create the Logistic Regression model.
4. Train the model using `fit()`.
5. Predict the result for a student who studied 4 hours using `predict()`.
6. Display the predicted result as Pass or Fail.

### Part B: Understanding the Sigmoid Function

The Sigmoid Function is used to convert a calculated linear value into a probability between 0 and 1.

The mathematical formula is:

**Sigmoid Function:**

\[
P = \frac{1}{1+e^{-z}}
\]

Where:

- z = b₀ + b₁x
- b₀ = Intercept
- b₁ = Coefficient
- x = Input value
- e = Euler's number

In this example:

- b₀ = -5
- b₁ = 1.2
- x = 5

The calculated probability is compared with a threshold of 0.5 to classify the student result.

- If probability ≥ 0.5: Student will Pass.
- If probability < 0.5: Student will Fail.

## 6. Key Concepts Demonstrated

- Binary Classification
- Logistic Regression Model
- Model Training and Prediction
- Sigmoid Activation Function
- Probability Estimation
- Classification Threshold

## 7. Expected Learning Outcomes

After completing this practical session, participants will be able to:

- Explain the concept of Logistic Regression.
- Differentiate between Linear Regression and Logistic Regression.
- Implement a Logistic Regression model using Scikit-learn.
- Understand how the Sigmoid Function works.
- Calculate and interpret predicted probabilities.
- Perform binary classification using a threshold.

## 8. Applications of Logistic Regression

- Student Pass/Fail Prediction
- Email Spam Detection
- Customer Churn Prediction
- Disease Classification
- Loan Default Prediction

## 9. Conclusion

This practical exercise provides an introduction to Logistic Regression through a simple student performance prediction problem. It demonstrates how a classification model can be trained using Scikit-learn and how the Sigmoid Function converts linear values into probabilities for making binary classification decisions.

The notebook helps participants gain hands-on experience with one of the fundamental classification algorithms in Machine Learning.

---

**Programme:** Faculty Development Programme (FDP)  
**Practical Topic:** Logistic Regression  
**Date:** 20 November 2026
