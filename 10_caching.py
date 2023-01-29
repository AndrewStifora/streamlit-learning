import streamlit as st
import time


@st.cache  # 👈 This function will be cached
def my_slow_function(arg1, arg2):
    # Do something really slow in here!
    add_args = arg1 + arg2
    time.sleep(1)
    print(f"{arg1} + {arg2} = {add_args}")
    return
