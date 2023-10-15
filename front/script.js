function getWeather() {
  const apiKey = '3cf54aa3315ab17be061f59b12cd8ca4';
  const city = document.getElementById('cityInput').value;
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`;

  fetch(url)
      .then(response => response.json())
      .then(data => {
          document.getElementById('city').textContent = data.name;
          document.getElementById('temperature').textContent = data.main.temp;
          document.getElementById('windspeed').textContent = data.wind.speed;
      })
      .catch(error => console.log(error));
}

let chart; // Déclarez une variable pour stocker le graphique

function createChart(data) {
    if (chart) {
        chart.destroy(); 
    }

    const ctx = document.getElementById("tempChart").getContext("2d");

    chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: Array.from({ length: data["temp-cable"].length }, (_, i) => i + 1),
            datasets: [{
                label: "Température du câble",
                data: data["temp-cable"],
                borderColor: "blue",
                fill: false,
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: "Temps"
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: "Température (°C)"
                    }
                }
            }
        }
    });
}


function getTempCable() {
    const temperature = document.getElementById('temperature').textContent;
    const windspeed = document.getElementById('windspeed').textContent;
    const intensity = document.getElementById('intensity').value;
    
    const url = `http://127.0.0.1:8000/temp?ws=${windspeed}&ta=${temperature}&i=${intensity}`;
  
    fetch(url)
        .then(response => response.json())
        .then(data => {
            createChart(data); 
        })
        .catch(error => console.log(error));
}
