# 🩺 Diabetes Risk Predictor

An interactive **Shiny app** to predict the risk of diabetes using a trained machine learning model.  
Enter patient details, get instant predictions, and explore model insights!

---

## ✅ Steps to Run the Project

### 1️⃣ Run the Training Script  
Run `train_model.R` to train the model using the Pima Indians Diabetes dataset.  
It will save the trained model as `diabetes_model.rds`.

### 2️⃣ Check the Model File  
Ensure that `diabetes_model.rds` is created in your working directory.

### 3️⃣ Test the Model (Optional but Recommended)  
Before launching the app, test if the model works fine using this snippet:

```r
# Load the model
model <- readRDS("diabetes_model.rds")

# Create a sample input
sample_input <- data.frame(
  Pregnancies = 3,
  Glucose = 180,
  BloodPressure = 70,
  SkinThickness = 20,
  Insulin = 100,
  BMI = 35,
  DiabetesPedigreeFunction = 0.6,
  Age = 45
)

# Predict
predict(model, newdata = sample_input)
```
## ✅ Steps to Run the Project

```r
shiny::runApp()
```
You’ll be able to:

🧠 Enter user health data
⚠️ Predict diabetes risk
📈 View accuracy, confusion matrix, and feature importance

---
## ⚠️ Tips & Troubleshooting

- Make sure required R packages are installed:  
  `shiny`, `caret`, `ggplot2`, `shinythemes`
  
  ```r
  install.packages(c("shiny", "caret", "ggplot2", "shinythemes"))
  ```
- Validate input ranges carefully to avoid errors.  
- Keep both diabetes_model.rds and diabetes.csv in the same directory as app.R
- Results are based on the Pima Indians Diabetes dataset (UCI repository)
- If errors occur, try testing model prediction code independently outside the app.

---

## Summary

| Step          | Action                          |
| ------------- | -------------------------------|
| 1             | Train & save model (`diabetes_model.rds`)  |
| 2             | Verify model predictions        |
| 3             | Run Shiny app and predict risk  |
| 4             | Troubleshoot and validate inputs|

---

Happy predicting! 🎉  
Feel free to contribute or report issues.

---

*Made with 🧪 & ❤️ to simplify early diabetes risk screening.*
