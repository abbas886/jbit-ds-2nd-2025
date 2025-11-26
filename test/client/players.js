const players_base_url = "http://localhost:8002/players";

export async function display_team_players(team_id) {
    // players.html is already included via includeHTML() in index.html
    
    const players = await load_team_players(team_id);

    const listElement = document.getElementById('players_list');
    listElement.innerHTML = '';

    players.forEach(player => {
        const li = document.createElement('li');
        li.textContent = player.name;
        listElement.appendChild(li);
    });
}

async function load_team_players(team_id) {
    const url = `${players_base_url}?team_id=${team_id}`;
    const response = await fetch(url);
    return await response.json();
}
