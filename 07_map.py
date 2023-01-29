import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 10] + [49.89, -97.14],
    columns=['lat', 'lon'])

st.map(map_data)
