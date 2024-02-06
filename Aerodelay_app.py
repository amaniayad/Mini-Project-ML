# Import Flask and util module
from flask import Flask, request, jsonify, render_template
import util

# Create a Flask application
app = Flask(__name__, template_folder='templates')
app.static_folder = 'static'

# Route for the main page
@app.route('/')
def main_page():
    return render_template('app.html')

# Route to predict flight delay
@app.route('/predict_flight_delay', methods=['POST'])
def predict_flight_delay():
    try:
        # Extract input parameters from the request
        month = int(request.form['month'])
        day_of_month = int(request.form['day_of_month'])
        day_of_week = int(request.form['day_of_week'])
        dep_time = int(request.form['dep_time'])
        unique_carrier = request.form['unique_carrier']
        origin = request.form['origin']
        dest = request.form['dest']
        distance = float(request.form['distance'])

        # Make prediction using the util module
        delay_prediction = util.predict_delay(month, day_of_month, day_of_week, dep_time, unique_carrier, origin, dest, distance)

        # Check if prediction is successful
        if delay_prediction is not None:
            # Convert NumPy integer to native Python integer
            delay_prediction = int(delay_prediction)

            response = jsonify({
                'delay_prediction': delay_prediction
            })
        else:
            response = jsonify({
                'error': 'Error in prediction. Please check input parameters.'
            })

        response.headers.add('Access-Control-Allow-Origin', '*')
        print("Response Data:", response.get_data())
        return response

    except Exception as e:
        # Log the exception message directly into the server logs
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Internal server error: {str(e)}. Check logs for details.'})


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
