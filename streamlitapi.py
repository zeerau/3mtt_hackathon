import streamlit as st
import pickle


model = pickle.load(open('crop_prediction_model.pkl','rb'))
def main():
    st.title('Crop Type Predictor')

    N = st.text_input('N')
    P = st.text_input('P')
    K = st.text_input('K')
    ph = st.text_input('ph')

    if st.button('Predict'):
        makeprediction = model.predict([[N,P,K,ph]])
        output = makeprediction[0]
        st.success('You can grow {} is your field'.format(output))
if __name__ == '__main__':
        main()