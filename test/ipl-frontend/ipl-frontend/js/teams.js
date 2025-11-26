// js/teams.js
import { display_team_players } from './players.js';
const TEAMS_API = "http://localhost:8001/teams";

async function fetchJson(url,opts={}){ const r = await fetch(url,opts); if(!r.ok) throw new Error('HTTP '+r.status); return r.json(); }

export async function display_teams(){
  try{
    const teams = await fetchJson(TEAMS_API);
    const list = document.getElementById('teams');
    if(!list) return;
    list.innerHTML = '';
    teams.forEach(team=>{
      const li = document.createElement('li');
      li.className = 'team-item';
      const txt = document.createElement('a');
      txt.href='#'; txt.textContent = team.abbreviation + ' — ' + team.name;
      txt.addEventListener('click',(e)=>{ e.preventDefault(); display_team_details(team.id); document.querySelectorAll('#teams li').forEach(n=>n.classList.remove('selected')); li.classList.add('selected'); });
      const tools = document.createElement('div'); tools.className='team-tools';
      const edit = document.createElement('button'); edit.className='icon-btn'; edit.textContent='✏️'; edit.title='Edit'; edit.addEventListener('click',(ev)=>{ev.stopPropagation(); openEditEntity('team',team);});
      const del = document.createElement('button'); del.className='icon-btn'; del.textContent='🗑️'; del.title='Delete'; del.addEventListener('click',(ev)=>{ev.stopPropagation(); openDeleteEntity('team',team.id,team.name);});
      tools.appendChild(edit); tools.appendChild(del);
      li.appendChild(txt); li.appendChild(tools); list.appendChild(li);
    });
    const addLi = document.createElement('li'); addLi.className='team-add'; const addBtn = document.createElement('button'); addBtn.className='btn btn-primary'; addBtn.textContent='+ Add Team'; addBtn.addEventListener('click',()=>openAddEntity('team')); addLi.appendChild(addBtn); list.appendChild(addLi);
  }catch(err){
    console.error(err);
    const loading = document.getElementById('loading'); if(loading){ loading.textContent='Failed to load teams'; loading.style.color='red'; }
  }
}

export async function display_team_details(id){
  try{
    const team = await fetchJson(TEAMS_API+'/'+id);
    const set = (s,v)=>{ const el=document.getElementById(s); if(el) el.textContent = v ?? ''; };
    set('team_id',team.id); set('team_name',team.name); set('team_city',team.city); set('team_abbreviation',team.abbreviation); set('team_championshipsWon',team.championshipsWon);
    window.currentTeamId = team.id; window.currentTeamName = team.name;
    const tools = document.getElementById('team_tools') || (function(){ const d=document.createElement('div'); d.id='team_tools'; document.querySelector('.card').appendChild(d); return d; })();
    tools.innerHTML=''; const edit=document.createElement('button'); edit.className='btn btn-primary'; edit.textContent='Edit Team'; edit.addEventListener('click',()=>openEditEntity('team',team));
    const del=document.createElement('button'); del.className='btn btn-danger'; del.textContent='Delete Team'; del.addEventListener('click',()=>openDeleteEntity('team',team.id,team.name));
    const addP=document.createElement('button'); addP.className='btn btn-secondary'; addP.textContent='Add Player'; addP.addEventListener('click',()=>{ openAddEntity('player'); setTimeout(()=>{ const sel=document.getElementById('team_id'); if(sel) sel.value = team.id; },150); });
    tools.appendChild(edit); tools.appendChild(del); tools.appendChild(addP);
    const teamNameEl = document.getElementById('team_abbreviation'); if(teamNameEl) teamNameEl.onclick = (e)=>{ e.preventDefault(); (async()=>{ if(!document.getElementById('players_list')) await includeHTML(); display_team_players(team.abbreviation); })(); };
  }catch(err){ console.error(err); alert('Cannot load team details'); }
}

window.refreshTeams = display_teams;
display_teams();
