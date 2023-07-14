import streamlit as st

page_title = "Health Index GUI 1"
layout = 'centered'

st.set_page_config(page_title=page_title, layout=layout)
st.title(page_title)

# @st.cache_data 
def fitness_index_MT_model2(glucose, poor_health_threshold=0.7, average_health_threshold=0.5):
    global in_range, high_range, less_range
    parameter_limits = {
        "Cholesterol": {"value": cholesterol,"lower": 0, "upper": 200},
        "Glucose": {"value": glucose, "lower": 70, "upper": 100},
        "Hemoglobin": {"value":Hemoglobin, "lower": 13, "upper": 17},
        "Systolic": {"value": systolic, "lower": 80, "upper": 90},
        "Diastolic": {"value":diastolic,"lower": 120, "upper": 130},
        "BMI": {"value":bmi,"lower": 18.5, "upper": 24.9},
        "a": {"value":a,"lower": 18.5, "upper": 25.9},
        "b": {"value":b,"lower": 19.5, "upper": 24.9},
        "c": {"value":c,"lower": 16.5, "upper": 23.9},
        "d": {"value":d,"lower": 17.5, "upper": 22.9}
    }
    st.dataframe(parameter_limits)
    x = 0
    y = 0
    total_params = len(parameter_limits)
    in_range = []
    less_range = []
    high_range = []

    for param, limits in parameter_limits.items():
        value = limits['value']
        # st.write(value)
        if value == 0.0:
            y += 1
            less_range.append(param)
        elif value <= limits["lower"]:
            # print("less than the admissible range")
            less_range.append(param)
            x += 1

        elif value >= limits["upper"]:
            # print('more than the admissible range')
            high_range.append(param)
            x +=1
    
        else:
            # print("In range")
            in_range.append(param)


    out_of_range_ratio = x / total_params
    if out_of_range_ratio == 1:
        st.write(f'Extremely poor health {x} out of {total_params} vitals out of range and {y} vitals not provided')        
    elif out_of_range_ratio >= poor_health_threshold:
        st.write(f'Poor health {x} out of {total_params} vitals out of range and {y} vitals not provided')
    elif out_of_range_ratio >= average_health_threshold:
        st.write(f'Average health {x} out of {total_params} vitals out of range and {y} vitals not provided')
    elif out_of_range_ratio < average_health_threshold:
        st.write(f'Good health {x} out of {total_params} vitals out of range and {y} vitals not provided')        
    elif y <= 3 and out_of_range_ratio == 0:
        st.write('Extremely Good health')

    if y >= 3:
        st.write('Insufficient data provided')


with st.form('entry_form'):
    col1, col2 = st.columns(2)

    cholesterol = col1.number_input('Cholesterol')
    if cholesterol == 0.0:
        pass
    elif cholesterol < 0:
        col1.warning('less than the admissible range')
    elif cholesterol > 200:
        col1.warning("more than the admissible range")

    glucose = col2.number_input('Glucose')
    if glucose == 0.0:
        pass
    elif glucose < 70:
        col2.warning('less than the admissible range')
    elif glucose > 100:
        col2.warning("more than the admissible range")


    Hemoglobin  = col1.number_input('Hemoglobin')
    if Hemoglobin == 0.0:
        pass
    elif Hemoglobin < 13:
        col1.warning('less than the admissible range')
    elif Hemoglobin > 17:
        col1.warning("more than the admissible range")

    bmi = col2.number_input('BMI')
    if bmi == 0.0:
        pass
    elif bmi < 18.5:
        col2.warning('less than the admissible range')
    elif bmi > 24.9:
        col2.warning("more than the admissible range")

    systolic = col2.number_input('Systolic')
    if systolic == 0.0:
        pass
    elif systolic < 80:
        col2.warning('less than the admissible range')
    elif systolic > 90:
        col2.warning("more than the admissible range")

    diastolic = col1.number_input('Diastolic')
    if diastolic == 0.0:
        pass
    elif diastolic < 120:
        col1.warning('less than the admissible range')
    elif diastolic > 130:
        col1.warning("more than the admissible range")

    a = col1.number_input('a')
    if a == 0.0:
        pass
    elif a < 18.5:
        col1.warning('less than the admissible range')
    elif a > 25.9:
        col1.warning("more than the admissible range")

    b = col2.number_input('b')
    if b == 0.0:
        pass
    elif b < 19.5:    
        col2.warning('less than the admissible range')
    elif b > 24.9:
        col2.warning("more than the admissible range")

    c = col1.number_input('c')
    if c == 0.0:
        pass
    elif c < 16.5:
        col1.warning('less than the admissible range')
    elif c > 23.9:
        col1.warning("more than the admissible range")

    d = col2.number_input('d')
    if d == 0.0:
        pass
    elif d < 17.5:
        col2.warning('less than the admissible range')
    elif d > 22.9:
        col2.warning("more than the admissible range")

    col1.form_submit_button("Submit", on_click=fitness_index_MT_model2(glucose))
    col2.form_submit_button("Refresh")

st.write("In Range:", in_range)
st.write("Less Range:", less_range)
st.write("Out Range:", high_range)

