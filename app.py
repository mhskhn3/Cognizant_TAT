from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
from datetime import datetime
from numpy import busday_count
import traceback
import random

app = Flask(__name__)

# Load model and data
try:
    model = joblib.load('onboarding_tat_predictor.joblib')
    df = pd.read_csv('Open Data.csv')
    
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Verify required columns exist
    required_columns = {'supplier_name', 'product_area', 'country', 'region',
                       'open_work_orders', 'pending_xws_activation',
                       'pending_idv_completion', 'pending_pw_reset_completion',
                       'st_created_date', 'access_type', 'hardware_type'}
    
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

except Exception as e:
    print(f"Error loading files: {str(e)}")
    print(traceback.format_exc())
    raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Mock prediction response (replace with actual model prediction)
        prediction = {
            'Onboarding TAT': random.randint(10, 20),
            'xWS Activation': random.randint(2, 5),
            'System Activation': random.randint(8, 15),
            'xws_activation_to_idv': random.randint(2, 4),
            'xws_idv_to_system_activation': random.randint(4, 8)
        }
        
        return jsonify(prediction)
    
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@app.route('/dashboard-data', methods=['POST'])
def dashboard_data():
    try:
        data = request.get_json()
        
        # Mock dashboard response (replace with actual data processing)
        response = {
            'open_work_orders': random.randint(1000, 4000),
            'pending_xws': random.randint(500, 2000),
            'pending_idv': random.randint(300, 1500),
            'pending_system': random.randint(200, 1000),
            'prediction_xws': random.randint(3, 7),
            'prediction_xws_to_idv': random.randint(2, 5),
            'prediction_idv_to_sys': random.randint(3, 6),
            'total_estimated': random.randint(8, 18),
            'estimated_insights': f"Based on current processing rates, all pending work orders for {data.get('supplier', 'your supplier')} in {data.get('country', 'your country')} ({data.get('region', 'your region')}) should be completed in approximately {random.randint(8, 18)} days. This includes {data.get('product', 'your product')} product area work orders."
        }
        
        return jsonify(response)
    
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@app.route('/get-options', methods=['GET'])
def get_options():
    try:
        # Get unique values for dropdowns
        suppliers = sorted(df['supplier_name'].dropna().astype(str).unique().tolist())
        product_areas = sorted(df['product_area'].dropna().astype(str).unique().tolist())
        countries = sorted(df['country'].dropna().astype(str).unique().tolist())
        regions = sorted(df['region'].dropna().astype(str).unique().tolist())
        
        return jsonify({
            'suppliers': suppliers,
            'product_areas': product_areas,
            'countries': countries,
            'regions': regions
        })
    
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)