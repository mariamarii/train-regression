import joblib
import pandas as pd
import streamlit as st


# Load the trained model and input columns
try:
    Model = joblib.load("Model.pkl")
    Inputs = joblib.load("Inputs.pkl")
except FileNotFoundError:
    st.error("Model or input files not found. Ensure 'Model.pkl' and 'Inputs.pkl' are in the directory.")
    st.stop()


def prediction(data):
    return Model.predict(data)[0]

def Main():
    st.title("Flight Ticket Price Prediction")
    st.write("Provide the following details to predict the Ticket Price:")



   
    
    Airline = st.selectbox("Airline", ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet'])
    Source = st.selectbox("Source", ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination", ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])
    
    Duration = st.number_input("Duration", min_value=10, max_value=3000, value=60, step=60)

    Total_Stops = st.slider("Total Stops", min_value=0, max_value=4, value=1)
    Additional_Info = st.selectbox("Additional Info", ['No info', 'In-flight meal not included',
       'No check-in baggage included', '1 Short layover',
       '1 Long layover', 'Change airports', 'Business class',
       'Red-eye flight', '2 Long layover'])
    
    Month = st.slider("Month", min_value=1, max_value=12, value=1)
    Day = st.slider("Day", min_value=1, max_value=31, value=1)
    Time_Of_Day = st.selectbox("Time of Day", ['Night', 'Midnight', 'Morning', 'Evening', 'Afternoon'])
  


    

    # Create DataFrame with all features
    data = pd.DataFrame([{
        'Airline':  Airline,
        'Source' :Source,
        'Destination' : Destination,
        'Duration' : Duration,
        'Total_Stops': Total_Stops,
        'Additional_Info':Additional_Info,
        'Month' : Month,
        'Day':Day,
        'Time_of_Day':Time_Of_Day
        
        
    }])

    # Check if DataFrame matches model input
    if not all(col in Inputs for col in data.columns):
        st.error("Mismatch between input columns and model expected columns.")
        return

    if st.button("Predict"):
        try:
            result = prediction(data)
            st.success(f"Predicted Ticket Price Value: ${result:,.2f}")
        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")

if __name__ == "__main__":
    Main()
