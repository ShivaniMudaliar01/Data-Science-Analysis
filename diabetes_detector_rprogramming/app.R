server <- function(input, output, session) {
  
  # ... your existing code ...
  
  output$prediction_ui <- renderUI({
    req(input$predict_btn)
    
    # Validate inputs (you can keep your existing validation logic)
    validate(
      need(input$Glucose >= 0 && input$Glucose <= 200, "Glucose must be between 0 and 200"),
      need(input$BloodPressure >= 0 && input$BloodPressure <= 150, "Blood Pressure must be between 0 and 150"),
      need(input$SkinThickness >= 0 && input$SkinThickness <= 100, "Skin Thickness must be between 0 and 100"),
      need(input$Insulin >= 0 && input$Insulin <= 900, "Insulin must be between 0 and 900"),
      need(input$BMI >= 0 && input$BMI <= 70, "BMI must be between 0 and 70"),
      need(input$DiabetesPedigreeFunction >= 0 && input$DiabetesPedigreeFunction <= 2, "Diabetes Pedigree Function must be between 0 and 2"),
      need(input$Age >= 1 && input$Age <= 120, "Age must be between 1 and 120")
    )
    
    input_data <- data.frame(
      Pregnancies = input$Pregnancies,
      Glucose = input$Glucose,
      BloodPressure = input$BloodPressure,
      SkinThickness = input$SkinThickness,
      Insulin = input$Insulin,
      BMI = input$BMI,
      DiabetesPedigreeFunction = input$DiabetesPedigreeFunction,
      Age = input$Age
    )
    
    prediction <- predict(model, newdata = input_data)
    
    if (prediction == 1) {
      tagList(
        tags$span(class = "high-risk", 
                  shiny::icon("exclamation-triangle", lib = "font-awesome"), 
                  " High Risk of Diabetes! Please consult a healthcare professional."
        )
      )
    } else {
      tagList(
        tags$span(class = "low-risk", 
                  shiny::icon("check-circle", lib = "font-awesome"), 
                  " Low Risk of Diabetes."
        )
      )
    }
  })
  
  # Keep your other outputs as they are (conf_matrix, accuracy, plot)
}
