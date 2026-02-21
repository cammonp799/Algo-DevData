document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("searchInput");
    const suggestionsBox = document.getElementById("suggestions");
    const weatherCard = document.getElementById("weatherCard");
    const loading = document.getElementById("loading");

    let stationsData = [];

    // Charger les données au démarrage
    fetchData();

    async function fetchData() {
        loading.classList.remove("hidden");
        try {
            const response = await fetch("/api/metro_data");
            const data = await response.json();
            stationsData = data.stations;
            loading.classList.add("hidden");
        } catch (error) {
            console.error("Erreur:", error);
            loading.innerHTML = "<p>❌ Erreur de connexion aux serveurs.</p>";
        }
    }

    // Gestion de la recherche
    searchInput.addEventListener("input", (e) => {
        const query = e.target.value.toLowerCase();
        suggestionsBox.innerHTML = "";

        if (query.length < 1) {
            suggestionsBox.style.display = "none";
            return;
        }

        const filtered = stationsData.filter(station =>
            station.name.toLowerCase().includes(query)
        );

        if (filtered.length > 0) {
            suggestionsBox.style.display = "block";
            filtered.forEach(station => {
                const div = document.createElement("div");
                div.className = "suggestion-item";

                // Style dynamique du badge dans la liste de recherche
                const badgeBg = station.metro_line === "Ligne A" ? "#ffeaea" : "#fff4cc";
                const badgeColor = station.metro_line === "Ligne A" ? "#e63030" : "#b28f00";

                div.innerHTML = `
                    <strong>${station.name}</strong> 
                    <span class="badge" style="background-color: ${badgeBg}; color: ${badgeColor}; font-size: 0.75rem;">${station.metro_line}</span>
                `;
                div.onclick = () => showWeather(station);
                suggestionsBox.appendChild(div);
            });
        } else {
            suggestionsBox.style.display = "none";
        }
    });

    // Afficher la météo
    function showWeather(station) {
        searchInput.value = station.name;
        suggestionsBox.style.display = "none";
        weatherCard.classList.remove("hidden");

        // Remplir les infos métro
        document.getElementById("metroName").innerText = station.name;
        document.getElementById("metroLine").innerText = station.metro_line;

        // Couleur dynamique du badge sur la carte principale
        const badge = document.getElementById("metroLine");
        badge.style.backgroundColor = station.metro_line === "Ligne A" ? "#ffeaea" : "#fff4cc";
        badge.style.color = station.metro_line === "Ligne A" ? "#e63030" : "#b28f00";

        // Remplir les infos météo
        const w = station.live_weather;
        if (w) {
            document.getElementById("tempValue").innerText = w.temperature || "--";
            document.getElementById("rainValue").innerText = w.pluie;
            document.getElementById("humValue").innerText = w.humidite || "--";
            document.getElementById("windValue").innerText = w.vent || "--";
        } else {
            alert("Données météo indisponibles pour cette station.");
        }
    }

    // Fermer les suggestions si on clique ailleurs
    document.addEventListener('click', function(e) {
        if (e.target !== searchInput) {
            suggestionsBox.style.display = 'none';
        }
    });
});