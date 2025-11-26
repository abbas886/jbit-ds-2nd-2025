// integrate with your fast api backend - using fetch api

async function getTeams() {
    const response = await fetch('http://localhost:8001/teams');
    if (!response.ok) {
        throw new Error('Failed to fetch teams');
    }
    displayTeams(await response.json());
   // return await response.json();
}

// display teams details in html - <ul id="teams-list"></ul>
function displayTeams(teams) {
    const teamsList = document.getElementById('teams-list');
    teams.forEach(team => {
        const listItem = document.createElement('li');
        listItem.textContent = `${team.name} - ${team.city}`;
        teamsList.appendChild(listItem);
    });
}


getTeams()


