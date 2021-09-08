import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def app(car_df):
	st.header("Here is the Visualized Data: ")
	st.set_option("deprecation.showPyplotGlobalUse", False)
	st.subheader("Scatter Plot: ")
	features_list = st.multiselect("Select X-axis values", ("carwidth", "enginesize", "horsepower", "drivewheel_fwd", "car_company_buick"))
	for feature in features_list:
		st.subheader(f"Scatterplot between {feature} and price")
		plt.figure(figsize = (12, 6))
		sns.scatterplot(x = feature, y = "price", data = car_df)
		st.pyplot()
	st.subheader("Visualization Selector")
	plot_types = st.multiselect("select chars or plots", ("histogram", "boxplot", "heatmap"))
	if "histogram" in plot_types:
		st.subheader("Histogram")
		columns = st.selectbox("Select the Column to Create its Histogram", ("carwidth", "enginesize", "horsepower", "drivewheel_fwd", "car_company_buick"))
		plt.figure(figsize = (12, 6))
		plt.title(f"Histogram for {columns}")
		plt.hist(car_df[columns], bins = "sturges", edgecolor = "black")
		st.pyplot()
	if "boxplot" in plot_types:
		st.subheader("Boxplot")
		columns = st.selectbox("Select the Column to Create its Boxplot", ("carwidth", "enginesize", "horsepower", "drivewheel_fwd", "car_company_buick"))
		plt.figure(figsize = (12, 2))
		plt.title(f"Boxplot for {columns}")
		plt.boxplot(car_df[columns])
		st.pyplot()
	if "heatmap" in plot_types:
		st.subheader("Heatmap")
		columns = st.selectbox("Select the Column to Create its Heatmap", ("carwidth", "enginesize", "horsepower", "drivewheel_fwd", "car_company_buick"))
		plt.figure(figsize = (12, 6))
		plt.title(f"Heatmap for {columns}")
		ax = sns.heatmap(car_df.corr(), annot = True)
		bottom, top = ax.get_ylim()
		ax.set_ylim(bottom + 0.5, top - 0.5)
		st.pyplot()