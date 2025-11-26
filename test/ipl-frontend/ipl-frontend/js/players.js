// js/players.js
const PLAYERS_API = "http://localhost:8002/players";
const TEAMS_API = "http://localhost:8001/teams";

async function fetchJson(url,opts={}){ const r = await fetch(url,opts); if(!r.ok) throw new Error('HTTP '+r.status); return r.json(); }

export async function load_team_players(team_name){
  const q = team_name ? '?team_name='+team_name : '';
  return await fetchJson(PLAYERS_API + q);
}

export async function display_team_players(team_name){
  if(!document.getElementById('players_list')) await includeHTML();
  try{
    const players = await load_team_players(team_name);
    const list = document.getElementById('players_list');
    if(!list) return;
    list.innerHTML='';
    players.forEach(p=>{
      const li=document.createElement('li'); li.className='player-item';
      const span=document.createElement('span'); span.textContent = p.name + ' — ' + p.role;
      const tools = document.createElement('div'); tools.className='player-tools';
      const edit = document.createElement('button'); edit.className='icon-btn'; edit.textContent='✏️'; edit.addEventListener('click',(e)=>{ e.stopPropagation(); openEditEntity('player', p); });
      const del = document.createElement('button'); del.className='icon-btn'; del.textContent='🗑️'; del.addEventListener('click',(e)=>{ e.stopPropagation(); openDeleteEntity('player', p.id, p.name); });
      tools.appendChild(edit); tools.appendChild(del);
      li.appendChild(span); li.appendChild(tools); list.appendChild(li);
    });
    const addLi=document.createElement('li'); const addBtn=document.createElement('button'); addBtn.className='btn btn-primary'; addBtn.textContent='+ Add Player'; addBtn.addEventListener('click',()=>{ openAddEntity('player'); setTimeout(()=>{ const sel=document.getElementById('team_id'); if(sel && window.currentTeamId) sel.value = window.currentTeamId; },150); });
    addLi.appendChild(addBtn); list.appendChild(addLi);
  }catch(err){ console.error(err); const list=document.getElementById('players_list'); if(list) list.innerHTML='<li style="color:red">Failed to load players</li>'; }
}

window.refreshPlayers = async function(){ if(window.currentTeamId) await display_team_players(window.currentTeamId); else { const list=document.getElementById('players_list'); if(list) list.innerHTML='<li>Select a team to view players</li>'; } };
