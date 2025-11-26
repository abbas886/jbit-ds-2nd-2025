// js/match.js
const MATCH_API = "http://localhost:8003/matches";
const TEAM_API = "http://localhost:8001/teams";
async function fetchJson(url,opts={}){ const r=await fetch(url,opts); if(!r.ok) throw new Error('HTTP '+r.status); return r.json(); }

export async function load_matches(){ return await fetchJson(MATCH_API); }
export async function load_match_by_id(id){ return await fetchJson(MATCH_API+'/'+id); }
export async function load_matches_by_team(team){ return await fetchJson(MATCH_API+'/team/'+encodeURIComponent(team)); }

export async function display_matches(){
  try{
    const list = document.getElementById('match_list');
    if(!list) return;
    const matches = await load_matches();
    list.innerHTML='';
    matches.forEach(m=>{
      const li=document.createElement('li');
      const a=document.createElement('a'); a.href='#'; a.textContent = (m.team1||'') + ' vs ' + (m.team2||'') + (m.date ? ' — '+m.date : '');
      a.addEventListener('click',(e)=>{ e.preventDefault(); display_match_details(m.id); });
      const edit=document.createElement('button'); edit.className='icon-btn'; edit.textContent='✏️'; edit.addEventListener('click',(ev)=>{ ev.stopPropagation(); openEditEntity('match', m); });
      const del=document.createElement('button'); del.className='icon-btn'; del.textContent='🗑️'; del.addEventListener('click',(ev)=>{ ev.stopPropagation(); openDeleteEntity('match', m.id, m.team1+' vs '+m.team2); });
      li.appendChild(a); li.appendChild(edit); li.appendChild(del); list.appendChild(li);
    });
    const addLi=document.createElement('li'); const addBtn=document.createElement('button'); addBtn.className='btn btn-primary'; addBtn.textContent='+ Add Match'; addBtn.addEventListener('click',()=>openAddEntity('match')); addLi.appendChild(addBtn); list.appendChild(addLi);
  }catch(err){ console.error(err); const list=document.getElementById('match_list'); if(list) list.innerHTML='<li style="color:red">Failed to load matches</li>'; }
}

export async function display_match_details(id){
  try{
    const m = await load_match_by_id(id);
    const set=(s,v)=>{ const el=document.getElementById(s); if(el) el.textContent = v ?? ''; };
    set('match_id',m.id); set('team1',m.team1); set('team2',m.team2); set('venue',m.venue); set('date',m.date); set('winner',m.winner);
    let tools = document.getElementById('match_tools') || (function(){ const d=document.createElement('div'); d.id='match_tools'; document.querySelector('.card').appendChild(d); return d; })();
    tools.innerHTML=''; const edit=document.createElement('button'); edit.className='btn btn-primary'; edit.textContent='Edit Match'; edit.addEventListener('click',()=>openEditEntity('match',m));
    const del=document.createElement('button'); del.className='btn btn-danger'; del.textContent='Delete Match'; del.addEventListener('click',()=>openDeleteEntity('match',m.id,m.team1+' vs '+m.team2));
    tools.appendChild(edit); tools.appendChild(del);
  }catch(err){ console.error(err); alert('Cannot load match details'); }
}

window.refreshMatches = display_matches;
display_matches();
