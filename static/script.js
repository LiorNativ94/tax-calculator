document.getElementById('tax-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const income = document.getElementById('income').value;
    
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ income: income })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Your tax is: $${data.tax}`;
    })
    .catch(error => console.error('Error:', error));
});
