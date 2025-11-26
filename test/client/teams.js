// teams.js
import { display_team_players } from './players.js';

const teams_base_url = "http://localhost:8001/teams";

// -----------------------------
// Load all teams
// -----------------------------
async function load_teams() {
    const response = await fetch(teams_base_url);

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
}

// -----------------------------
// Display list of teams in Side Navigation
// -----------------------------
async function display_teams() {
    try {
        const teams = await load_teams();
        const listElement = document.getElementById('teams');
        const loadingElement = document.getElementById('loading');

        listElement.innerHTML = ''; // clear loading placeholder

        teams.forEach(team => {
            const li = document.createElement('li');
            li.classList.add("team-item");

            const a = document.createElement('a');
            a.textContent = team.abbreviation;
            a.href = "#";

            // Click event → Load team details
            a.addEventListener("click", function (event) {
                event.preventDefault();
                display_team_details(team.id);
            });

            li.appendChild(a);
            listElement.appendChild(li);
        });

    } catch (error) {
        console.error('Error fetching teams:', error);
        const loadingElement = document.getElementById('loading');
        loadingElement.textContent = "Failed to load teams.";
        loadingElement.style.color = 'red';
    }
}

display_teams();

// -----------------------------
// Load team details by ID
// -----------------------------
async function load_team_details(id) {
    const url = `${teams_base_url}/${id}`;
    const response = await fetch(url);

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
}

// -----------------------------
// Show team details in Main Content Section
// -----------------------------
async function display_team_details(id) {
    const team_details = await load_team_details(id);

    document.getElementById("team_id").textContent = team_details.id;
    document.getElementById("team_name").textContent = team_details.name;
    document.getElementById("team_city").textContent = team_details.city;
    document.getElementById("team_abbreviation").textContent = team_details.abbreviation;
    document.getElementById("team_championshipsWon").textContent = team_details.championshipsWon;

    // Click event to load players section
    document.getElementById("team_name").onclick = function (e) {
        e.preventDefault();
        display_team_players(team_details.name);
    };
}
