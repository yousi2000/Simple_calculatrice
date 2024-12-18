function append(value) {
    const expression = document.getElementById('expression');
    expression.value += value;
}

function clearExpression() {
    document.getElementById('expression').value = '';
    document.getElementById('result').innerText = '';
}

async function calculate() {
    const expression = document.getElementById('expression').value;
    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression }),
        });
        const data = await response.json();
        if (response.ok) {
            document.getElementById('result').innerText = `Résultat : ${data.result}`;
        } else {
            document.getElementById('result').innerText = `Erreur : ${data.error}`;
        }
    } catch (error) {
        document.getElementById('result').innerText = 'Erreur réseau!';
    }
}
