import numpy as np
import plotly.express as px
import streamlit as st

# Load the data
params = np.load('ParamsWNF.npy')

# Streamlit app
st.title("3D Scatter Plot Visualization")

# Dropdown inputs
varied_variable = st.selectbox("Select Variable:", ['xHI', 'MSE', 'R^2'])
model_specifics = st.selectbox("Select Model:", ['UiT', 'ViT', 'UNet'])

# Load the appropriate variable based on user input
if varied_variable == 'R^2':
    variable = np.load(f'R2_{model_specifics}.npy')
    variable[variable < 0.0] = 0.0
elif varied_variable == 'MSE':
    variable = np.load(f'MSE_{model_specifics}.npy')
else:
    variable = params[:, 3]

# 3 Spatial variables
Mh_min = params[:, 0]
Nion = params[:, 1]
Rmfp = params[:, 2]

custom_color_scale = [
    (np.min(variable), "black"),
    (np.mean(variable),  "#8c2981"),
    (np.max(variable), "white"),
]

# Create 3D scatter plot with xHI as color using the Magma color scale
fig = px.scatter_3d(
    x=Mh_min, 
    y=Nion, 
    z=Rmfp, 
    color=variable,
    title=f"Variation of {varied_variable} with M<sub>h,min</sub>, N<sub>ion</sub>, and R<sub>mfp</sub>",
    labels={
        'x': 'M<sub>h,min</sub>',  # Subscript for M_h,min
        'y': 'N<sub>ion</sub>',     # Subscript for N_ion
        'z': 'R<sub>mfp</sub>',     # Subscript for R_mfp
        'color': f'{varied_variable}'   # Subscript for x_HI
    },
    color_continuous_scale=custom_color_scale   # Use the Magma color scale
)

# Display the plot in Streamlit
st.plotly_chart(fig)
