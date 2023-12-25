import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


data = pd.read_csv("day.csv", index_col = "instant")
data["dteday"] = pd.to_datetime(data["dteday"])

min_date = data["dteday"].min()
max_date = data["dteday"].max()

with st.sidebar:
  st.image("https://en.wikipedia.org/wiki/File:Bike_icon.png")
  start_date, end_date = st.date_input(
      label = "Rentang Waktu",
      min_value = min_date,
      max_value = max_date,
      value = [min_date, max_date]
  )

main_df = data[(data["dteday"] >= str(start_date)) & (data["dteday"] <= str(end_date))]
month = main_df.groupby("mnth")["cnt"].sum()

st.header(":sparkles: Dashboard Bike Sharing - Day :sparkles:")
st.subheader("Musim dan Bulan")

fig, ax = plt.subplots(1,2, figsize=(35,15))

color_s = ["#D48A72", "#D3D3D3", "#72BCD4", "#D3D3D3"]
sns.barplot(x = "season", y = "cnt", data = main_df, palette = color_s, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Musim", fontsize=15)
ax[0].set_title('Jumlah Rental Sepeda Berdasarkan Musim', loc="center", fontsize=30)


color_b = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D48A72"]
month.sort_index(ascending = False).plot(kind="barh", color = color_b, ax=ax[1])
ax[1].set_xlabel(None)
ax[1].set_ylabel("Bulan", fontsize=15)
ax[1].set_title('Jumlah Rental Sepeda Berdasarkan Musim', loc="center", fontsize=30)

st.pyplot(fig)


st.subheader("Cuaca Buruk")

fig, ax = plt.subplots(figsize=(35,15))

color = ["#D3D3D3", "#D3D3D3", "#D48A72"]
sns.barplot(x = "weathersit", y = "cnt", data = main_df, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel("Musim", fontsize=15)
ax.set_title('Jumlah Rental Sepeda Berdasarkan Cuaca Buruk', loc="center", fontsize=30)

st.pyplot(fig)


st.subheader("Trend Data")

fig, ax = plt.subplots(figsize=(35,15))

plt.plot(main_df["dteday"], main_df[["casual","registered"]])
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title('Trend Rental Sepeda Tahun 2011-2012', loc="center", fontsize=30)

st.pyplot(fig)
