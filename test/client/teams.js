base_url = "http://localhost:8000/teams"

async function load_teams() {
    
        // Await the fetch request
    const response = await fetch(base_url );
     // Check if the request was successful
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
    const teams = await response.json();
    return teams
}

 async function display_teams() {

    try{

    teams =  await load_teams()
    const listElement = document.getElementById('teams');
    const loadingElement = document.getElementById('loading');

     
    console.log(teams);
    // Clear the loading message
    listElement.innerHTML = ''; 
    teams.forEach(team => {
            const li = document.createElement('li');
            const a  = document.createElement('a');
            // set link text and href
            a.textContent =`${team.name}`;
            const url = `${base_url}?id=${team.id}`;
            a.href = 'url | #';
            // Pass parameter using event listener
            a.addEventListener("click", function (event) {
            event.preventDefault();      // stops page reload
            display_team_details(team.id);            // call your function with parameter
            });
            //li.textContent = `${team.name}`;
            li.appendChild(a)
            listElement.appendChild(li);
        });    

       }   catch (error) {
        // Handle any errors that occurred during the fetch operation
        console.error('Error fetching data:', error);
        loadingElement.textContent = 'Failed to load users. Please try again later.';
        loadingElement.style.color = 'red';
    }
}

display_teams();



async function display_team_details(id){
    
    team_details = await load_team_details(id)
    document.getElementById("team_id").textContent = team_details.id
}
async function load_team_details(id) {
    const url = `${base_url}?id=${id}`;

    const response = await fetch(url)
    const team_details = await response.json();
    return team_details
    
}

