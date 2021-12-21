import streamlit as st

import pandas as pd

from PIL import Image



# from sklearn import datasets

# from sklearn.ensemble import RandomForestClassifier

hour_List=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]


st.write("""

# WATER ANALYSIS""")

rad = st.sidebar.radio("Navigator",["Home","About us"])
if rad == "Home":

        


#INPUT FILE

 name = "csv_file"

if st.button("input") :
    st.write("Name: {}" . format (name.upper()))


# status = st.radio (" What is your status", ("Active" , "Inactive"))
# if status == 'Active' :
#     st.success("You are active")
# elif status == "Inactive" :
#     st.warning("Inactive")




#Comments 

#'RESULT'



st.sidebar.header('User Input Values')



def user_input_features():

    


    
    Int_Rate = st.sidebar.slider('Interest Rate in %', 0.0, 100.0)

    	##st.sidebar.add_rows

    Principal = st.sidebar.text_input('Please input',00)

    	##st.sidebar.add_rows

    No_Of_Years = st.sidebar.selectbox('Select No Of hour',hour_List, 0)


df = user_input_features()


#if rad == "About us":


#copy image address 

message = st.text_area("Enter Message",height=200)
st.write(message)


















