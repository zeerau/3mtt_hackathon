import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open('crop_prediction_model.pkl', 'rb'))

def main():
    st.title('Crop Type Predictor')

    N = st.text_input('Nitrogen')
    P = st.text_input('Phosphorous')
    K = st.text_input('Potassium')
    ph = st.text_input('pH')

    if st.button('Predict'):
        # Convert input values to numerical type
        try:
            N = float(N)
            P = float(P)
            K = float(K)
            ph = float(ph)
        except ValueError:
            st.error("Please enter valid numeric values for all inputs.")
            return
        
        makeprediction = model.predict([[N, P, K, ph]])
        output = makeprediction[0]  # Extract the prediction from the array
        st.success('You can grow {} in your field'.format(output))

if __name__ == '__main__':
    main()
