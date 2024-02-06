function onClickedPredictDelay() {
    console.log("Predict delay button clicked");

    var month = parseInt(document.getElementById("uiMonth").value);
    var dayOfMonth = parseInt(document.getElementById("uiDayOfMonth").value);
    var dayOfWeek = parseInt(document.getElementById("uiDayOfWeek").value);
    var depTime = parseInt(document.getElementById("uiDepTime").value);
    var uniqueCarrier = document.getElementById("uiUniqueCarrier").value;
    var origin = document.getElementById("uiOrigin").value;
    var dest = document.getElementById("uiDest").value;
    var distance = parseFloat(document.getElementById("uiDistance").value);
    
    var url = "/predict_flight_delay";

    $.post(url, {
        month: month,
        day_of_month: dayOfMonth,
        day_of_week: dayOfWeek,
        dep_time: depTime,
        unique_carrier: uniqueCarrier,
        origin: origin,
        dest: dest,
        distance: distance
    }, function (data, status) {
        console.log(data);

        // Check if there's an error
        if (data.error) {
            console.log("Error in prediction. Please check input parameters.");
            console.log("Server Error Message:", data.error); // Log the server error message
        } else {
            // Update the HTML content with the prediction result
            var predictionResultElement = document.getElementById('predictionResult');

if (predictionResultElement) {
    if (data.delay_prediction === 1) {
        predictionResultElement.textContent = "There will be a delay.";
        predictionResultElement.classList.add('result_box');
    } else if (data.delay_prediction === 0) {
        predictionResultElement.textContent = "There won't be a delay.";
        predictionResultElement.classList.add('result_box');
    } else {
        predictionResultElement.textContent = "Unexpected response. Please check the server.";
    }
} else {
    console.log("Error: Element with id 'predictionResult' not found.");
}

        }
    }).fail(function (xhr, textStatus, errorThrown) {
        console.log("POST request failed:", textStatus);
        console.log("Error thrown:", errorThrown);
    });
}

function onClearResult() {
    var predictionResultElement = document.getElementById('predictionResult');
    if (predictionResultElement) {
        predictionResultElement.textContent = "";
    } else {
        console.log("Error: Element with id 'predictionResult' not found.");
    }
}

