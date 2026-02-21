// Application Météo Toulouse - Frontend JavaScript

document.addEventListener('DOMContentLoaded', () => {
    loadWeatherData();

    // Bouton actualiser
    document.getElementById('refresh-btn').addEventListener('click', () => {
        loadWeatherData();
    });

    // Auto-refresh toutes les 5 minutes
    setInterval(loadWeatherData, 5 * 60 * 1000);
});

async function loadWeatherData() {
    const loading = document.getElementById('loading');
    const error = document.getElementById('error');
    const container = document.getElementById('stations-container');

    // Afficher le loading
    loading.classList.remove('hidden');
    error.classList.add('hidden');
    container.innerHTML = '';

    try {
        const response = await fetch('/api/weather');
        const data = await response.json();

        loading.classList.add('hidden');

        if (data.success && data.stations) {
            renderStations(data.stations);
            updateLastUpdate();
        } else {
            throw new Error(data.error || 'Erreur inconnue');
        }
    } catch (err) {
        console.error('Erreur:', err);
        loading.classList.add('hidden');
        error.classList.remove('hidden');
    }
}

function renderStations(stations) {
    const container = document.getElementById('stations-container');

    stations.forEach(station => {
        const card = createStationCard(station);
        container.appendChild(card);
    });
}

function createStationCard(station) {
    const card = document.createElement('div');
    card.className = 'station-card';

    const temp = station.temperature !== null ? `${station.temperature}°C` : 'N/A';
    const humidity = station.humidite !== null ? `${station.humidite}%` : 'N/A';
    const pressure = station.pression !== null ? `${station.pression} hPa` : 'N/A';
    const rain = station.pluie !== null ? `${station.pluie} mm` : '0 mm';
    const wind = station.vent !== null ? `${station.vent} km/h` : 'N/A';
    const windDir = station.direction_vent !== null ? getWindDirection(station.direction_vent) : '';

    const time = station.heure ? formatTime(station.heure) : '--:--';

    card.innerHTML = `
        <div class="station-header">
            <span class="station-name">📍 ${station.name}</span>
            <span class="station-time">🕐 ${time}</span>
        </div>

        <div class="temperature-main">
            <div class="temperature-value">${temp}</div>
            <div class="temperature-label">Température actuelle</div>
        </div>

        <div class="weather-data">
            <div class="data-item">
                <span class="data-icon">💧</span>
                <div class="data-info">
                    <span class="data-value">${humidity}</span>
                    <span class="data-label">Humidité</span>
                </div>
            </div>

            <div class="data-item">
                <span class="data-icon">⬇️</span>
                <div class="data-info">
                    <span class="data-value">${pressure}</span>
                    <span class="data-label">Pression</span>
                </div>
            </div>

            <div class="data-item">
                <span class="data-icon">🌧️</span>
                <div class="data-info">
                    <span class="data-value">${rain}</span>
                    <span class="data-label">Précipitations</span>
                </div>
            </div>

            <div class="data-item">
                <span class="data-icon">💨</span>
                <div class="data-info">
                    <span class="data-value">${wind} ${windDir}</span>
                    <span class="data-label">Vent</span>
                </div>
            </div>
        </div>
    `;

    return card;
}

function getWindDirection(degrees) {
    if (degrees === null) return '';
    const directions = ['N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO'];
    const index = Math.round(degrees / 45) % 8;
    return directions[index];
}

function formatTime(timeStr) {
    try {
        const date = new Date(timeStr);
        return date.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
    } catch {
        return timeStr;
    }
}

function updateLastUpdate() {
    const now = new Date();
    const timeStr = now.toLocaleString('fr-FR');
    document.getElementById('last-update').textContent = `Dernière mise à jour: ${timeStr}`;
}