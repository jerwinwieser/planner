function create_chart_bar(){
    var ctx = document.getElementById('my_chart').getContext('2d');
    var my_chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'dev',
                data: default_data,
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