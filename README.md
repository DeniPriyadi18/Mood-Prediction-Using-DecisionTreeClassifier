#  **Prediction Mood by Morning Routine Using DecisionTreeClassifier**

![image-alt](https://github.com/DeniPriyadi18/Mood-Prediction-Using-DecisionTreeClassifier/blob/main/Foto/preview_web_app.png?raw=true)
## Project Overview
This project focuses on predicting daily mood based on morning routine activities. The system analyzes various morning habits and activities to predict an individual's mood for the day, helping users understand the correlation between their morning practices and emotional well-being.
### Key Features
- **Wake-Up Time** : Time when user wake-up
- **Sleep Duration(hrs)** : Total hours a person sleeps
- **Meditation (mins)** : Minutes spent on meditation/mindfulness
- **Exercise (mins)** : Duration of physical exercise
- **Breakfast Type** : Categories: Skipped, Light, Protein-rich, Carb-rich, Heavy
- **Journaling** :  Whether journaling activity was performed (Yes/No)
- **Prep Time** : Time between wake-up and work start.

### Technical Implemetation
- **Algorithm** : DecisionTreeClassifier
- **Target Class** : Sad and Happy
- **Interface** : Interactive web application built with streamlit
- **Data Preprocessing** : Feature engineering and scaling using MinMaxScaling for optimal model performance

### Resource
Download dataset in here [tautan berikut](https://www.kaggle.com/datasets/jayeshx19/morning-routine-dataset)


## Instalation and Setup
### Prerequisites
- Python 3.10.17 or higher
- pip package manager

### Clone Repository
```
git clone https://github.com/DeniPriyadi18/Mood-Prediction-Using-DecisionTreeClassifier.git
cd mood-prediction-morning-routine
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Run Web Application
```
streamlit run app.py
```
## Usage
### Web Interface
1. Launch the web Application using streamlit run app.py
2. Input your morning details :
    - Sleep duration
    - Meditation and exercise minutes
    - Wake-up time and work start time
    - Breakfast type and journaling status
3. Click button "Predict" to get you prediction mood
4. View the predicted result

## Author
Deni Priyadi
- **Linkedin** : https://www.linkedin.com/in/denipriyadi18/
- **Email** : denipriyadi90@gmail.com

## Acknowledgements
- Dataset provided by kaggle
- Built with streamlit
- Machine learning powered by scikit-learn
