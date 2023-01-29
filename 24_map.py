import pandas as pd
import numpy as np
import streamlit as st

df = pd.DataFrame(np.random.randn(500, 2) / [20, 10] + [49.89, -97.14], columns=['lat', 'lon'])
st.map(df)
