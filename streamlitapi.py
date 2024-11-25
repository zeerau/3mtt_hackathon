import streamlit as st
import pickle

model = pickle.load(open('crop_prediction_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
def predict_crop(N, P, K, ph):
    try:
        input_values = [[float(N), float(P), float(K), float(ph)]]
        scaled_input = scaler.transform(input_values)  
        prediction = model.predict(scaled_input)[0] 
        return prediction
    except ValueError:
        return "Invalid input. Please enter numeric values."

def main():
    st.title('Crop Type Predictor')

    N = st.number_input('Nitrogen', value=0.0)  # Use number_input for numeric input
    P = st.number_input('Phosphorous', value=0.0)
    K = st.number_input('Potassium', value=0.0)
    ph = st.number_input('pH', value=0.0)

    if st.button('Predict'):
        result = predict_crop(N, P, K, ph)
        if isinstance(result, str):  # Check if result is an error message
            st.error(result)
        else:
            st.success('You can grow {} in your field'.format(result))

if __name__ == '__main__':
    main()
