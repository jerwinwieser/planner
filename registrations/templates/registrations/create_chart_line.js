function create_chart_line(){
    var ctx = document.getElementById('my_chart').getContext('2d');
    var my_chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: x,
            datasets: [{
                label: 'dev',
                data: y,
            }],
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}