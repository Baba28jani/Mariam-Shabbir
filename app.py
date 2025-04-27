import streamlit as st

# Title
st.title("Unit Converter ⚡")

# Conversion Types
conversion_types = ["Length", "Weight", "Temperature"]

# User selects conversion type
conversion_choice = st.selectbox("Choose conversion type:", conversion_types)

# Length Conversion
if conversion_choice == "Length":
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Centimeters"]
    input_value = st.number_input("Enter length value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit:", length_units)
    to_unit = st.selectbox("To unit:", length_units)

    # Dictionary for conversion
    length_conversions = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Centimeters": 0.01
    }

    if st.button("Convert", key="convert_length"):
        result = input_value * (length_conversions[from_unit] / length_conversions[to_unit])
        st.success(f'{input_value:.2f} {from_unit} is equal to {result:.2f} {to_unit}')

# Weight Conversion
elif conversion_choice == "Weight":
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    input_value = st.number_input("Enter weight value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit:", weight_units)
    to_unit = st.selectbox("To unit:", weight_units)

    # Dictionary for conversion
    weight_conversions = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }

    if st.button("Convert", key="convert_weight"):
        result = input_value * (weight_conversions[from_unit] / weight_conversions[to_unit])
        st.success(f'{input_value:.2f} {from_unit} is equal to {result:.2f} {to_unit}')

# Temperature Conversion
elif conversion_choice == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("Enter temperature value:", format="%.2f")
    from_unit = st.selectbox("From unit:", temperature_units)
    to_unit = st.selectbox("To unit:", temperature_units)

    # Function to convert temperature
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
            else:
                return value
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
            else:
                return value
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
            else:
                return value

    if st.button("Convert", key="convert_temperature"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f'{input_value:.2f} {from_unit} is equal to {result:.2f} {to_unit}')
