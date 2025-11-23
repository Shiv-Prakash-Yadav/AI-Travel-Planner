/* project/static/main.js */
document.getElementById('travel-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const city = document.getElementById('city').value;
    const days = document.getElementById('days').value;

    try {
        const response = await fetch('/plan', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ city, days })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `<h3>Your Personalized Itinerary:</h3><p>${data.itinerary}</p>`;

    } catch (error) {
        document.getElementById('result').innerHTML = `<p>Error: ${error.message}</p>`;
    }
});
