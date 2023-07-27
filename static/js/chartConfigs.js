
// Past Seven Days Index Price at 4 pm HKT Graphs
//*********************************************************************************************************/

var timestamps = compiled_prices.timestamp
.slice(0, 7)
.map(ts => moment(ts, 'YYYY-MM-DD HH:mm:ss').toISOString());
var btc_prices = compiled_prices.btc.slice(0, 7);
var eth_prices = compiled_prices.eth.slice(0, 7);
var sol_prices = compiled_prices.sol.slice(0, 7);

// Chart.js config for Bitcoin past 7 days index price at 4pm HKT chart
var ctx = document.getElementById('btc_priceChart').getContext('2d');
var btc_priceChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: timestamps,
        datasets: [{
            label: 'BTC Index Price (USD)',
            data: btc_prices,
            borderColor: 'rgb(38, 165, 165)',
            fill: false
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Bitcoin Index Price at 4 pm HKT'
            },
            legend: {
                display: true,
                position: 'top'
            }
        },
        responsive: true,
        scales: {
            x: {
                type: 'time',
                ticks: {
                    autoSkip: false,
                    maxRotation: 30,
                    minRotation: 30
                },
                time: {
                    unit: 'day',
                    tooltipFormat: 'MMM d, yyyy HH:mm',
                    displayFormats: {
                        day: 'MMM d, yyyy',
                        hour: 'HH:mm'
                    },
                    offset: -480
                },
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Timestamp'
                }
            },
            y: {
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Price'
                }
            }
        }
    }
});

// Chart.js config for Ethereum past 7 days index price at 4pm HKT chart
var ctx = document.getElementById('eth_priceChart').getContext('2d');
var eth_priceChart = new Chart(ctx, {   
    type: 'line',
    data: {
        labels: timestamps,
        datasets: [{
            label: 'ETH Index Price (USD)',
            data: eth_prices,
            borderColor: 'rgb(38, 165, 165)',
            fill: false
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Ethereum Index Price at 4 pm HKT'
            },
            legend: {
                display: true,
                position: 'top'
            }
        },
        responsive: true,
        scales: {
            x: {
                type: 'time',
                ticks: {
                    autoSkip: false,
                    maxRotation: 30,
                    minRotation: 30
                },
                time: {
                    unit: 'day',
                    tooltipFormat: 'MMM d, yyyy HH:mm',
                    displayFormats: {
                        day: 'MMM d, yyyy',
                        hour: 'HH:mm'
                    },
                    offset: -480
                },
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Timestamp'
                }
            },
            y: {
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Price'
                }
            }
        }
    }
});

// Chart.js config for Solana past 7 days index price at 4pm HKT chart
var ctx = document.getElementById('sol_priceChart').getContext('2d');
var sol_priceChart = new Chart(ctx, {   
    type: 'line',
    data: {
        labels: timestamps,
        datasets: [{
            label: 'SOL Index Price (USD)',
            data: sol_prices,
            borderColor: 'rgb(38, 165, 165)',
            fill: false
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Solana Index Price at 4 pm HKT'
            },
            legend: {
                display: true,
                position: 'top'
            }
        },
        responsive: true,
        scales: {
            x: {
                type: 'time',
                ticks: {
                    autoSkip: false,
                    maxRotation: 30,
                    minRotation: 30
                },
                time: {
                    unit: 'day',
                    tooltipFormat: 'MMM d, yyyy HH:mm',
                    displayFormats: {
                        day: 'MMM d, yyyy',
                        hour: 'HH:mm'
                    },
                    offset: -480
                },
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Timestamp'
                }
            },
            y: {
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Price'
                }
            }
        }
    }
});


// DVOL Graphs
//*********************************************************************************************************/

var DVOL_timestamps = DVOL_data.timestamp.map(ts => moment(ts, 'YYYY-MM-DD HH:mm:ss').toISOString());

// Chart.js config for Bitcoin past 7 days DVOL
var ctx = document.getElementById('btc_DVOLChart').getContext('2d');
var btc_DVOLChart = new Chart(ctx, {   
    type: 'line',
    data: {
        labels: DVOL_timestamps,
        datasets: [{
            label: 'BTC DVOL',
            data: DVOL_data.btc,
            borderColor: 'rgb(38, 165, 165)',
            fill: false
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Deribit Implied Volatility Index (DVOL) for Bitcoin, HKT'
            },
            legend: {
                display: true,
                position: 'top'
            }
        },
        responsive: true,
        scales: {
            x: {
                type: 'time',
                ticks: {
                    autoSkip: false,
                    maxRotation: 30,
                    minRotation: 30
                },
                time: {
                    unit: 'day',
                    tooltipFormat: 'MMM d, yyyy HH:mm',
                    displayFormats: {
                        day: 'MMM d, yyyy',
                        hour: 'HH:mm'
                    },
                    offset: -480
                },
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Date and Time (HKT)'
                }
            },
            y: {
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'DVOL'
                }
            }
        }
    }
});


// Chart.js config for Ethereum past 7 days DVOL
var ctx = document.getElementById('eth_DVOLChart').getContext('2d');
var btc_DVOLChart = new Chart(ctx, {   
    type: 'line',
    data: {
        labels: DVOL_timestamps,
        datasets: [{
            label: 'ETH DVOL',
            data: DVOL_data.eth,
            borderColor: 'rgb(38, 165, 165)',
            fill: false
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Deribit Implied Volatility Index (DVOL) for Ethereum, HKT'
            },
            legend: {
                display: true,
                position: 'top'
            }
        },
        responsive: true,
        scales: {
            x: {
                type: 'time',
                ticks: {
                    autoSkip: false,
                    maxRotation: 30,
                    minRotation: 30
                },
                time: {
                    unit: 'day',
                    tooltipFormat: 'MMM d, yyyy HH:mm',
                    displayFormats: {
                        day: 'MMM d, yyyy',
                        hour: 'HH:mm'
                    },
                    offset: -480
                },
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Date and Time (HKT)'
                }
            },
            y: {
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'DVOL'
                }
            }
        }
    }
});