import streamlit as st
import pickle



rfc_model=pickle.load(open('rfc_model.pkl','rb'))




def main():
    st.title("Failure load prediction - all input values in mm")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Iris Classification</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
  
e1=st.number_input('Enter end distance', min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

e2=st.number_input('Enter edge distance', min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

p1=st.number_input('Enter longitudinal pitch', min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

p2=st.number_input('Enter transverse pitch', min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

d0=st.number_input('Enter bolt hole diameter', min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

d=st.number_input('Enter bolt diameter', min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

t=st.number_input('Enter plate thickness', min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

n=st.number_input('Enter number of bolts', min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

fy=st.number_input('Enter material yield strength', min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

   
  
    inputs=[[e1,e2,p1,p2,d0,d,t,n,fy]]
    if st.button('Enter'):
       
           st.success(rfc_model.predict(inputs))
         


if __name__=='__main__':
    main()
