

// Load the Visualization API and the corechart package.
google.charts.load('current', { 'packages': ['corechart'] });


// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart1);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart1() {

    // Create the data table.
    var data1 = new google.visualization.DataTable();
    data1.addColumn('string', 'Topping');
    data1.addColumn('number', 'Slices');
    data1.addRows([
        ['Mushrooms', 3],
        ['Onions', 1],
        ['Olives', 1],
        ['Zucchini', 1],
        ['Pepperoni', 2]
    ]);

    // Set chart options
    var options1 = {
        'title': 'How Much Pizza I Ate Last Night',
        'width': 400,
        'height': 300
    };

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('chart_div_1'));
    chart.draw(data1, options1);
}






// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart2);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.



function drawChart2() {
    console.log("hello1")
    console.log(data_from_django)
    //{% if user.is_authenticated %}
    //console.log("here 5")
    //{% else %}
    //console.log("here 5")
    //{% endif %}



    //window.alert("hello2")
    //var has_paid_plan = {{ user.has_paid_plan }}

    ////////////////////////////////////////////////
    // Create the data table.
    var data_2 = new google.visualization.DataTable();
    //data_2.addColumn('date', "mjd")
    data_2.addColumn('number', "mjd")
    data_2.addColumn('number', '0');
    data_2.addColumn('number', '1');
    data_2.addColumn('number', '2');
    data_2.addColumn('number', '3');
    data_2.addColumn('number', '4');
    data_2.addColumn('number', '5');




   // data_from_django = {{ timeseries_data | safe }};
//widget.init(data_from_django);
// data_2.addRows( data_from_django );

// Set chart options
var options_2 = {
    'title': 'Fl3 by Passband vs Day',
    'width': 300,
    'height': 600,
    'interpolateNulls': true
};

// Instantiate and draw our chart, passing in some options.
var chart_2 = new google.visualization.LineChart(document.getElementById('chart_div_2'));
chart_2.draw(data_2, options_2);
}
