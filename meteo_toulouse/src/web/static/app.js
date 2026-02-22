document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("searchInput");
    const suggestionsBox = document.getElementById("suggestions");
    const weatherCard = document.getElementById("weatherCard");
    const loading = document.getElementById("loading");
    const mapDiv = document.getElementById("map");

    let stationsData = [];
    let map = null;

    // Coordonnées GPS approximatives des stations principales pour la démo
    const coordsGPS = {
        "Basso Cambo": [43.570, 1.392], "Jean Jaurès": [43.604, 1.448],
        "Capitole": [43.604, 1.443], "Esquirol": [43.600, 1.444],
        "Carmes": [43.597, 1.444], "Palais de Justice": [43.593, 1.444],
        "Saint Agne": [43.582, 1.444], "Paul Sabatier": [43.561, 1.463],
        "Argoulets": [43.623, 1.482], "Mirail-Université": [43.574, 1.401],
        "Compans-Caffarelli": [43.610, 1.432]
    };

    fetchData();

    async function fetchData() {
        loading.classList.remove("hidden");
        try {
            const response = await fetch("/api/metro_data");
            const data = await response.json();
            stationsData = data.stations;
            loading.classList.add("hidden");
            initMap(); // Lancer la carte une fois les données chargées
        } catch (error) {
            console.error("Erreur:", error);
            loading.innerHTML = "<p>❌ Erreur de connexion aux serveurs.</p>";
        }
    }

    function initMap() {
        mapDiv.classList.remove("hidden");
        // Initialiser centré sur Toulouse
        map = L.map('map').setView([43.604, 1.444], 13);

        L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);

        // Ajouter les marqueurs
        stationsData.forEach(station => {
            // Utiliser les coordonnées si connues, sinon le centre de Toulouse
            const latlng = coordsGPS[station.name] || [43.604 + (Math.random()*0.02 - 0.01), 1.444 + (Math.random()*0.02 - 0.01)];

            const markerColor = station.metro_line === "Ligne A" ? "red" : "gold";
            const circle = L.circleMarker(latlng, {
                color: markerColor, fillColor: markerColor, fillOpacity: 0.7, radius: 8
            }).addTo(map);

            circle.bindPopup(`<b>${station.name}</b><br>${station.metro_line}`);

            // Si on clique sur le marqueur sur la carte, afficher la météo !
            circle.on('click', () => {
                showWeather(station);
                map.setView(latlng, 15);
            });
        });
    }

    searchInput.addEventListener("input", (e) => {
        const query = e.target.value.toLowerCase();
        suggestionsBox.innerHTML = "";
        if (query.length < 1) { suggestionsBox.style.display = "none"; return; }

        const filtered = stationsData.filter(s => s.name.toLowerCase().includes(query));

        if (filtered.length > 0) {
            suggestionsBox.style.display = "block";
            filtered.forEach(station => {
                const div = document.createElement("div");
                div.className = "suggestion-item";
                div.innerHTML = `<strong>${station.name}</strong> <span class="badge" style="background:#eee;color:#333;font-size:0.75rem;">${station.metro_line}</span>`;
                div.onclick = () => {
                    showWeather(station);
                    if (coordsGPS[station.name]) {
                        map.setView(coordsGPS[station.name], 16);
                    }
                };
                suggestionsBox.appendChild(div);
            });
        }
    });

    function showWeather(station) {
        searchInput.value = station.name;
        suggestionsBox.style.display = "none";
        weatherCard.classList.remove("hidden");

        document.getElementById("metroName").innerText = station.name;
        const badge = document.getElementById("metroLine");
        badge.innerText = station.metro_line;
        badge.style.backgroundColor = station.metro_line === "Ligne A" ? "#ffeaea" : "#fff4cc";
        badge.style.color = station.metro_line === "Ligne A" ? "#e63030" : "#b28f00";

        const w = station.live_weather;
        if (w) {
            document.getElementById("tempValue").innerText = w.temperature || "--";
            document.getElementById("rainValue").innerText = w.pluie;
            document.getElementById("humValue").innerText = w.humidite || "--";
            document.getElementById("windValue").innerText = w.vent || "--";
        }
    }
});