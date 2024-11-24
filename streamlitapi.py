import streamlit as st
import pickle


model = pickle.load(open('crop_prediction_model.pkl','rb'))
def main():
    st.title('Crop Type Predictor')

    N = st.text_input('Nitrogen')
    P = st.text_input('Phosphorous')
    K = st.text_input('Potassium')
    ph = st.text_input('pH')

    if st.button('Predict'):
        makeprediction = model.predict([[N,P,K,ph]])
        output = makeprediction[0]
        st.success('You can grow {} in your field'.format(output))
if __name__ == '__main__':
        main()