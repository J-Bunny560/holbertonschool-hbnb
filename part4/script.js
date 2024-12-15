/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    document.getElementById('price-filter').addEventListener('change', () => {
        filter = document.getElementById('price-filter').value;
        const placeCards = document.querySelectorAll('.place-card');
        placeCards.forEach((place) => {
            if (filter === 'all') {
                place.style.display = 'block';
            } else {
                const priceText = place.querySelector('p').textContent;
                parseFloat(priceText.slice(priceText.indexOf('$') + 1)) <= parseFloat(filter)
                    ? (place.style.display = 'block')
                    : (place.style.display = 'none');
            }
        });
        // Iterate over the places and show/hide them based on the selected price
    });

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            loginUser(loginForm.email, loginForm.password);
        });
    }
});

async function fetchPlaces() {
    const response = (await fetch('http://localhost:5000/api/v1/places/')).json();
    response.then((places) => {
        displayPlaces(places);
    });
}

async function displayPlaces(places) {
    const placesList = document.querySelector('#places-list');
    //placesList.childNodes.forEach((child) => removeChild(child));
    places.forEach(async (place) => {
        const placeCard = document.createElement('div');
        placeCard.className = 'place-card';
        const placeName = document.createElement('h1');
        placeName.textContent = place.title;
        placeCard.appendChild(placeName);
        const placePrice = document.createElement('p');
        placePrice.textContent = `Price per night: $${place.price}`;
        placeCard.appendChild(placePrice);
        const button = document.createElement('button');
        button.className = 'details-button';
        button.textContent = 'View Details';
        placeCard.appendChild(button);
        placesList.appendChild(placeCard);
    });
}

async function loginUser(email, password) {
    const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    });
    if (response.ok) {
        const data = await response.json();
        document.cookie = `token=${data.access_token}; path=/`;
        window.location.href = 'index.html';
    } else {
        alert('Login failed: ' + response.statusText);
    }
}

class AppHeader extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
<header>
        <nav>
            <div class="navigation-header">
                <a href="index.html"><img src="images/logo.png" alt="hbnb logo"></a>
                <a href="login.html" id="login-link">Login</a>
            </div>
        </nav>
    </header>
    
`;
    }
}

class AppFooter extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
    <footer>
    <p class="copyright">© HBnB Evolution. All rights reserved.</p>
    </footer>
    `;
    }
}

window.customElements.define('app-header', AppHeader);
window.customElements.define('app-footer', AppFooter);

window.onload = () => {
    fetchPlaces();
};
