import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

st.title("🎯 Social Network Ads Data Processor")

# Step 1: Load CSV file directly
data = pd.read_csv("Social_Network_Ads.csv")
st.success("✅ CSV File Loaded Successfully!")

# Step 2: Show Data
st.subheader("📋 Original Data")
st.dataframe(data.head())

# Step 3: Clean & Encode Gender
data['Gender'] = data['Gender'].str.strip().str.capitalize()

# Step 4: Gender Picker
gender_option = st.selectbox("Select Gender 👇", options=data['Gender'].unique())
st.write(f"You selected: **{gender_option}**")

# Step 5: Filter Data
filtered_data = data[data['Gender'] == gender_option].copy()

# Step 6: Normalize Age
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
filtered_data['Normalized_Age'] = scaler.fit_transform(filtered_data[['Age']])

# Step 7: Encode Gender (Human-readable)
filtered_data['Gender_Encoded'] = filtered_data['Gender'].apply(lambda x: 'Male' if x == 'Male' else 'Female')

# Step 8: Display
st.subheader("📊 Processed Data")
st.dataframe(filtered_data[['Gender', 'Age', 'Normalized_Age', 'Gender_Encoded']])

# Step 9: Download Button
csv = filtered_data.to_csv(index=False).encode('utf-8')

#st.download_button("Download Processed CSV", csv, "proces_

# Step 8: Display
st.subheader("📊 Processed Data")
st.dataframe(filtered_data[['Gender', 'Age', 'Normalized_Age', 'Gender_Encoded']])

# Step 9: Download Button
csv = filtered_data.to_csv(index=False).encode('utf-8')
st.download_button(" Download Processed CSV", csv, "processed_data.csv", "text/csv")


