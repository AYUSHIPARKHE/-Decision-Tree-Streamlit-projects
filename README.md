# 🌳 Decision Tree Classifier Web App using Streamlit  

### 👩‍💻 Developed by: **Ayushi Parkhe**  
*Data Science & Machine Learning Enthusiast*  

---

## 📌 Overview  
This project is a **Streamlit-based Machine Learning web application** that predicts whether a customer will purchase a product based on their **Age**, **Gender**, and **Estimated Salary**.  

The model is trained using a **Decision Tree Classifier** on the `Social_Network_Ads.csv` dataset.  
It showcases an end-to-end ML pipeline — from **data preprocessing, model training, evaluation**, to **interactive web deployment**.

---

## ⚙️ Project Workflow  
1. Data Cleaning and Feature Encoding  
2. Normalization of Age and Salary columns  
3. Model training using `DecisionTreeClassifier`  
4. Model evaluation using accuracy score and confusion matrix  
5. Building a **Streamlit web app** for real-time predictions  

---

## 💡 Key Features  
- 📊 User-friendly web interface using Streamlit  
- 🧩 Encodes gender feature (Male/Female)  
- 🌿 Visualizes Decision Tree predictions  
- ⚖️ Data normalization for better model performance  
- 🎯 Displays model accuracy dynamically  
- 💬 Real-time prediction based on custom input  

---

## 🧠 Tech Stack  
| Category | Tools / Libraries |
|-----------|------------------|
| Language | Python |
| Web Framework | Streamlit |
| Machine Learning | Scikit-learn |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| IDE | Jupyter Notebook |

---

## 📁 Dataset Information  
**File:** `Social_Network_Ads.csv`  

| Feature | Description |
|----------|-------------|
| Gender | Male/Female (Categorical Feature) |
| Age | Customer Age |
| EstimatedSalary | Annual Salary Estimate |
| Purchased | Target Variable (1 = Yes, 0 = No) |

---

## 📂 File Structure  
| File | Description |
|------|--------------|
| `decisiontreeclassi.ipynb` | Jupyter Notebook used for EDA, preprocessing, and model training |
| `de.py` | Streamlit web app file for prediction |
| `Social_Network_Ads.csv` | Dataset used for model training |
| `requirements.txt` | Python libraries required to run the app |
| `.gitignore` | Files and folders excluded from Git tracking |

---

## 🚀 How to Run the Project  

### 🔹 Clone the Repository  
```bash
git clone https://github.com/AYUSHIPARKHE/Decision-Tree-Streamlit-Project.git
cd Decision-Tree-Streamlit-Project
