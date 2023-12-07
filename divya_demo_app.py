import streamlit as st
st.title("Divya's tds demo app 1")
st.header("Subtraction between 2 numbers")
def subtraction(a,b):
  return a-b

a = st.number_input("Enter first number:")
b =st.number_input("Enter second number:")
st.write("First Number is : ",a)
st.write("Second Number is : ",b)
st.write("Difference:", subtraction(a,b))
