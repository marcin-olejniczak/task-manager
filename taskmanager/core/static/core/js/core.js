var homepage = (function(){
    function drawCalendarChart() {
        var dataTable = new google.visualization.DataTable();
        dataTable.addColumn({ type: 'date', id: 'Date' });
        dataTable.addColumn({ type: 'number', id: 'Won/Loss' });
        dataTable.addRows([
            [ new Date(2015, 9, 4), 1 ],
            [ new Date(2015, 9, 5), 3 ],
            [ new Date(2015, 9, 12), 5 ],
            [ new Date(2015, 9, 13), 10 ],
            [ new Date(2015, 9, 19), 2 ],
            [ new Date(2015, 9, 23), 5 ],
            [ new Date(2016, 0, 24), 1 ],
            [ new Date(2016, 0, 30), 6],
            [ new Date(2016, 0, 30), 9 ]
        ]);

       var chart = new google.visualization.Calendar(document.getElementById('activity_chart'));

        var options = {
            title: "Activity",
            height: 350,
            calendar: {
                cellSize: 15,
            }
        };

        chart.draw(dataTable, options);
    }

    var initActivityChart = function(){
        // make ajax call
        drawCalendarChart();
    };
    google.load('visualization', '1.0', {'packages':['calendar'], 'language': 'eng'});
    google.setOnLoadCallback(initActivityChart);
})();

var gui = (function(){
    window.onhashchange = function(){
        $(".nav-sidebar li").removeClass('active');
        var hash = window.location.hash;
        hash = ( hash == "")? '#' : hash;
        var active = ".nav-sidebar li a[href='"+ hash +"']";
        $(active).parents('li').addClass('active')
    };
})();