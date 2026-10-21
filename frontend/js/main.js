document.addEventListener('DOMContentLoaded', () => {
    const visitsElement = document.getElementById('visits');

    fetch('/api/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            visitsElement.innerText = data.visits;
        })
        .catch(error => {
            visitsElement.innerText = 'Error';
            console.error('Error fetching visits:', error);
        });
});
