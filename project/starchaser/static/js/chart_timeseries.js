
// Load the Visualization API and the corechart package.
google.charts.load('current', { 'packages': ['corechart'] });

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart2);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart2() {

    ////////////////////////////////////////////////
    // Create the data table.
    var data_2 = new google.visualization.DataTable();
    //data_2.addColumn('date', "mjd")
    data_2.addColumn('number', "mjd")
    data_2.addColumn('number', 'Passband 0');
    data_2.addColumn('number', '1');
    data_2.addColumn('number', '2');
    data_2.addColumn('number', '3');
    data_2.addColumn('number', '4');
    data_2.addColumn('number', '5');
 
    //console.log(window.temp5);
    data_2.addRows( window.temp5 );

    // Set chart options
    var options_2 = {
        'title': 'Flux by Passband vs Day',
        'width': 300,
        'height': 600,
        'interpolateNulls': true
    };

    // Instantiate and draw our chart, passing in some options.
    var chart_2 = new google.visualization.LineChart(document.getElementById('chart_div_2'));
    chart_2.draw(data_2, options_2);
}
