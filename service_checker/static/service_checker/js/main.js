console.log('loaded js')


setInterval(() => {
    source = document.querySelector('.data-row p:nth-child(1)');
    target = document.querySelector('.data-row p:nth-child(2)');

    fetch('http://localhost:8000/service/status/' + source.textContent)
        .then(response => response.text())
        .then(data => {
            target.innerHTML = data;
        })


}, 10000)

