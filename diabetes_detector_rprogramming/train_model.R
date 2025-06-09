setwd("D:/Shivani/MAHE/rdir/disease_risk_predictor")
# train_model.R
library(tidyverse)
library(caret)

# Step 3.1: Load and clean data
data <- read.csv("diabetes.csv")
data$Outcome <- as.factor(data$Outcome)

# Step 3.2: Train-Test split
set.seed(123)
split <- createDataPartition(data$Outcome, p = 0.8, list = FALSE)
train_data <- data[split, ]
test_data <- data[-split, ]

# Step 3.3: Train the model
model <- train(Outcome ~ ., data = train_data, method = "rf")

# Save the model to use in app.R
saveRDS(model, "diabetes_model.rds")

# (Optional) Evaluate
pred <- predict(model, newdata = test_data)
confusionMatrix(pred, test_data$Outcome)
