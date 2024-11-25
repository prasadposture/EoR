import numpy as np
import plotly.express as px
import streamlit as st

# Load the data
params = np.load('ParamsWNF.npy')

# Streamlit app
st.title("3D Scatter Plot Visualization")

# Dropdown input for varied_variable
varied_variable = st.selectbox("Select Variable:", ['xHI', 'MSE', 'R^2'])

# 3 Spatial variables
Mh_min = params[:, 0]
Nion = params[:, 1]
Rmfp = params[:, 2]

# Function to load and process data for the chosen variable
def load_variable(model_specific):
    if varied_variable == 'R^2':
        variable = np.load(f'R2_{model_specific}.npy')
        variable[variable < 0.0] = 0.0
    elif varied_variable == 'MSE':
        variable = np.load(f'MSE_{model_specific}.npy')
    else:  # For 'xHI'
        variable = params[:, 3]
    return variable

# UiT Model
st.subheader("UiT Model")
variable_uiT = load_variable('UiT')
fig_uiT = px.scatter_3d(
    x=Mh_min, 
    y=Nion, 
    z=Rmfp, 
    color=variable_uiT,
    title=f"Variation of {varied_variable} with M<sub>h,min</sub>, N<sub>ion</sub>, and R<sub>mfp</sub> (UiT)",
    labels={
        'x': 'M<sub>h,min</sub>',
        'y': 'N<sub>ion</sub>',
        'z': 'R<sub>mfp</sub>',
        'color': f'{varied_variable}'
    },
    color_continuous_scale=[
        (np.min(variable_uiT), "black"),
        (np.mean(variable_uiT), "#8c2981"),
        (np.max(variable_uiT), "white")
    ]
)
st.plotly_chart(fig_uiT)

# ViT Model
st.subheader("ViT Model")
variable_viT = load_variable('ViT')
fig_viT = px.scatter_3d(
    x=Mh_min, 
    y=Nion, 
    z=Rmfp, 
    color=variable_viT,
    title=f"Variation of {varied_variable} with M<sub>h,min</sub>, N<sub>ion</sub>, and R<sub>mfp</sub> (ViT)",
    labels={
        'x': 'M<sub>h,min</sub>',
        'y': 'N<sub>ion</sub>',
        'z': 'R<sub>mfp</sub>',
        'color': f'{varied_variable}'
    },
    color_continuous_scale=[
        (np.min(variable_viT), "black"),
        (np.mean(variable_viT), "#8c2981"),
        (np.max(variable_viT), "white")
    ]
)
st.plotly_chart(fig_viT)

# UNet Model
st.subheader("UNet Model")
variable_unet = load_variable('UNet')
fig_unet = px.scatter_3d(
    x=Mh_min, 
    y=Nion, 
    z=Rmfp, 
    color=variable_unet,
    title=f"Variation of {varied_variable} with M<sub>h,min</sub>, N<sub>ion</sub>, and R<sub>mfp</sub> (UNet)",
    labels={
        'x': 'M<sub>h,min</sub>',
        'y': 'N<sub>ion</sub>',
        'z': 'R<sub>mfp</sub>',
        'color': f'{varied_variable}'
    },
    color_continuous_scale=[
        (np.min(variable_unet), "black"),
        (np.mean(variable_unet), "#8c2981"),
        (np.max(variable_unet), "white")
    ]
)
st.plotly_chart(fig_unet)
