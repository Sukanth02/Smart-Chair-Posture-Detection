import streamlit as st
import pickle
pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

def check_status(left_thigh1,left_thigh2,left_thigh3,right_thigh1,right_thigh2,right_thigh3,spine1,spine2,spine3,spine4,spine5,spine6):
    prediction = classifier.predict([[left_thigh1,left_thigh2,left_thigh3,right_thigh1,right_thigh2,right_thigh3,spine1,spine2,spine3,spine4,spine5,spine6]])
    if prediction == 2:
        return "SITTING IN A HEALTHY MANNER"
    elif prediction == 3:
        return "SITTING IN AN UHEALTHY MANNER"
    elif prediction == 1:
        return "PLEASE LEAN BACK AND SIT" 
    else:
        return "NOT SITTING"  


def main():
    html_temp = """
    <div style="background-color:tomato; padding:10px">
    <h2 style="color:white;text-align:center;">SMART CHAIR READINGS</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    left_thigh1 = st.text_input("LEFT THIGH READING 1" , "")
    left_thigh2 = st.text_input("LEFT THIGH READING 2" , "")
    left_thigh3 = st.text_input("LEFT THIGH READING 3" , "")
    right_thigh1 = st.text_input("RIGHT THIGH READING 1" , "")
    right_thigh2 = st.text_input("RIGHT THIGH READING 2" , "")
    right_thigh3 = st.text_input("RIGHT THIGH READING 3" , "")
    spine1 = st.text_input("SPINE READING 1" , "")
    spine2 = st.text_input("SPINE READING 2" , "")
    spine3 = st.text_input("SPINE READING 3" , "")
    spine4 = st.text_input("SPINE READING 4" , "")
    spine5 = st.text_input("SPINE READING 5" , "")
    spine6 = st.text_input("SPINE READING 6" , "")
    result=""
    if st.button("CHECK STATUS"):
        result = check_status(left_thigh1,left_thigh2,left_thigh3,right_thigh1,right_thigh2,right_thigh3,spine1,spine2,spine3,spine4,spine5,spine6)
    st.success("STATUS: {}".format(result))
    if st.button("About"):
        st.text("PROJECT BY SUKANTH A(20MIC0098)")  

if __name__ == '__main__':
    main()