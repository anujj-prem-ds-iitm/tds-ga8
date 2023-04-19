import streamlit as st

def largest_of_three_numbers(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

st.title("Find the Largest of Three Numbers")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find the Largest"):
    result = largest_of_three_numbers(num1, num2, num3)
    st.write(f"The largest number is {result}")
