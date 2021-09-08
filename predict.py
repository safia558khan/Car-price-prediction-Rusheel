import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression  
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, mean_squared_log_error

@st.cache()
def prediction(car_df, car_width, engine_size, horse_power, drive_wheel_fwd, car_comp_buick):
	X = car_df.iloc[:, :-1]
	y = car_df["price"]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
	lin_reg = LinearRegression()
	lin_reg.fit(X_train, y_train)
	score = lin_reg.score(X_train, y_train)
	price = lin_reg.predict([[car_width, engine_size, horse_power, drive_wheel_fwd, car_comp_buick]])
	price = price[0]
	y_test_pred = lin_reg.predict(X_test)
	test_r2_score = r2_score(y_test, y_test_pred)
	test_mae = mean_absolute_error(y_test, y_test_pred)
	test_msle = mean_squared_log_error(y_test, y_test_pred)
	test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
	return(price, score, test_r2_score, test_mae, test_msle, test_rmse)
def app(car_df):
	st.subheader("Select Values")
	car_width = st.slider("Car Width", float(car_df["carwidth"].min()), float(car_df["carwidth"].max()))
	engine_size = st.slider("Engine Size", float(car_df["enginesize"].min()), float(car_df["enginesize"].max()))
	horse_power = st.slider("Horse Power", float(car_df["horsepower"].min()), float(car_df["horsepower"].max()))
	d_fwd = st.radio("Is it a Forward Drive Wheel Car?", ("Yes", "No"))
	if d_fwd == "No":
		d_fwd = 0
	else:
		d_fwd = 1
	com_bui = st.radio("Is the car manufactured by Buick", ("Yes", "No"))
	if com_bui == "No" :
		com_bui = 0
	else:
		com_bui = 1
	if st.button("Predict"):
		st.subheader("Prediction Results")
		price, score, car_r2, car_mae, car_msle, car_rmse = prediction(car_df, car_width, engine_size, horse_power, d_fwd, com_bui)
		st.success(f"The predicted price of the car: {int(price)}")
		st.info(f"Accuracy score of the model: {score}")
		st.info(f"R2 Score: {car_r2}")
		st.info(f"Mean Absolute Error: {car_mae}")
		st.info(f"Root Mean Squared Error: {car_rmse}")
		st.info(f"Mean Squared Log Error: {car_msle}")