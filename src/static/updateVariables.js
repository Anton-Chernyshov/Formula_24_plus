// JavaScript source code
function updateNumber() {
            fetch('/update')
            .then(response => response.json())
            .then(data => {
                document.getElementById('motorTemp').innerText = data.motorTemp;
                document.getElementById('voltage').innerText = data.voltage;
                document.getElementById('amperage').innerText = data.amperage;
                document.getElementById('rpm').innerText = data.rpm;
                
            })
            .catch(error => console.log('Error:', error));
        }

        setInterval(updateNumber, 500);