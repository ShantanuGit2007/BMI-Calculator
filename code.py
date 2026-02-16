import streamlit as st 

#Header section
col1,col2,col3=st.columns([2,1,2])
with col2:
    st.image("Bmi_image.png",caption=None,width=200)

st.markdown(
'''<fieldset>
<center><h2>Body Mass Index Calculator</h2></center>
<hr>
<marquee>⚠️ This BMI calculator is intended for adults (18 years and above) only. ⚠️</marquee>
</fieldset>
<br><br>''',
unsafe_allow_html=True
)


# Input Section
weight=st.number_input(
    "Weight in Kilogram (KG)",
    min_value=00.00
)
height=st.number_input(
    "Height in Centimeter (CM)",
    min_value=00.00
)


# Button Section
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    click=st.button("Submit")


# Calculation
if click:
    try:
        height_in_meter=height/100
        bmi=round(weight/(height_in_meter**2),2)
        st.success(f"BMI: {bmi}")


# Body Type section
        if bmi < 18.5:
            st.warning("Underweight")
        elif 18.5 <= bmi < 24.9:
            st.info("Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("Overweight")
        else:
            st.error("Obese")
    except ZeroDivisionError:
        st.error(f"Height & Weight Cannot be Zero")


# Footer Section
st.markdown('''
<br>
<center><p>© 2026 Shantanu Gupta. All rights reserved.</p></center>''',
unsafe_allow_html=True)
