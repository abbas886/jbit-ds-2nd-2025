async function load_players() {
    const response = await fetch('http://localhost:8002/players');
    if (!response.ok) {
        throw new Error('Failed to fetch players');
    }   
    display_players(await response.json());
    //return await response.json();
}

function display_players(players) {
    const playersList = document.getElementById('players-list');
    players.forEach(player => {
        const listItem = document.createElement('li');
        listItem.textContent = `${player.name} - ${player.team} - ${player.role}`;
        playersList.appendChild(listItem);
    });
}
load_players()
