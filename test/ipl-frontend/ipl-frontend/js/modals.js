// js/modals.js - global modal system (plain script)
(function(){
  const API = { team: "http://localhost:8001/teams", player: "http://localhost:8002/players", match: "http://localhost:8003/matches" };
  function entityModal(){ return document.getElementById('entityModal'); }
  function deleteModal(){ return document.getElementById('deleteModal'); }
  function openModal(m){ if (m) m.setAttribute('aria-hidden','false'); }
  function closeModal(m){ if (m) m.setAttribute('aria-hidden','true'); }
  function wireCloseButtons(){
    const eClose = document.getElementById('entityModalClose');
    const eCancel = document.getElementById('entityCancel');
    if(eClose) eClose.onclick = ()=>closeModal(entityModal());
    if(eCancel) eCancel.onclick = ()=>closeModal(entityModal());
    const dClose = document.getElementById('deleteModalClose');
    const dCancel = document.getElementById('deleteCancel');
    if(dClose) dClose.onclick = ()=>closeModal(deleteModal());
    if(dCancel) dCancel.onclick = ()=>closeModal(deleteModal());
  }
  function capitalize(s){ return s? s[0].toUpperCase()+s.slice(1):''; }

  async function fetchJson(url, opts){ const r = await fetch(url, opts); if(!r.ok) throw new Error('HTTP '+r.status); return r.json(); }

  // build form fields
  function buildFormFields(entityType, data={}){
    const body = document.getElementById('entityFormBody');
    body.innerHTML = '';
    const input = (id,label,val='',opts={})=>{
      const wrap = document.createElement('div');
      if(opts.full) wrap.classList.add('full');
      const lab = document.createElement('label'); lab.htmlFor=id; lab.textContent=label;
      let field;
      if(opts.textarea) field = document.createElement('textarea');
      else if(opts.type === 'select') field = document.createElement('select');
      else field = document.createElement('input');
      field.id = id; field.name = id;
      if(opts.type && !opts.textarea && opts.type!=='select') field.type = opts.type;
      field.value = val ?? '';
      wrap.appendChild(lab); wrap.appendChild(field); return wrap;
    };

    if(entityType==='team'){
      body.appendChild(input('name','Name',data.name||''));
      body.appendChild(input('abbreviation','Abbreviation',data.abbreviation||''));
      body.appendChild(input('city','City',data.city||''));
      body.appendChild(input('championshipsWon','Championships Won',data.championshipsWon||0,{type:'number'}));
    } else if(entityType==='player'){
      body.appendChild(input('name','Name',data.name||''));
      body.appendChild(input('role','Role',data.role||''));
      const teamDiv = input('team_id','Team',data.team_id||'',{type:'select'});
      teamDiv.classList.add('full');
      body.appendChild(teamDiv);
      // populate teams
      fetchJson(API.team).then(teams=>{
        const sel = teamDiv.querySelector('select');
        sel.innerHTML='';
        teams.forEach(t=>{
          const o = document.createElement('option'); o.value = t.id; o.text = t.abbreviation+' - '+t.name;
          if(String(t.id)===String(data.team_id)) o.selected = true;
          sel.add(o);
        });
      }).catch(()=>{});
    } else if(entityType==='match'){
      body.appendChild(input('team1','Team 1',data.team1||'',{full:true}));
      body.appendChild(input('team2','Team 2',data.team2||'',{full:true}));
      body.appendChild(input('venue','Venue',data.venue||''));
      body.appendChild(input('date','Date',data.date||'',{type:'date'}));
      body.appendChild(input('winner','Winner',data.winner||''));
    }
  }

  function openEntityModal(action, type, data={}){
    const modal = entityModal(); if(!modal) return console.warn('entityModal missing');
    document.getElementById('entity_action').value = action;
    document.getElementById('entity_type').value = type;
    document.getElementById('entity_id').value = data.id || '';
    document.getElementById('entityModalTitle').textContent = (action==='add'?'Add ':'Edit ')+capitalize(type);
    document.getElementById('entitySubmit').textContent = action==='add'?'Create':'Save';
    buildFormFields(type, data);
    openModal(modal);
  }

  let pendingDelete = null;
  function openDelete(type,id,label){
    const modal = deleteModal(); if(!modal) return;
    pendingDelete = {type,id};
    document.getElementById('deleteMessage').textContent = `Delete ${capitalize(type)} "${label || id}"?`;
    openModal(modal);
  }

  async function onSubmit(e){
    e.preventDefault();
    const action = document.getElementById('entity_action').value;
    const type = document.getElementById('entity_type').value;
    const id = document.getElementById('entity_id').value;
    const bodyEl = document.getElementById('entityFormBody');
    const inputs = bodyEl.querySelectorAll('input,textarea,select');
    const payload = {};
    inputs.forEach(inp=>{
      if(!inp.id) return;
      payload[inp.id] = inp.type==='number' ? Number(inp.value) : inp.value;
    });
    try {
      let res;
      if(action==='add'){
        res = await fetch(API[type], {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(payload)});
      } else {
        res = await fetch(API[type]+'/'+id, {method:'PUT', headers:{'Content-Type':'application/json'}, body:JSON.stringify(payload)});
      }
      if(!res.ok) throw new Error('Server '+res.status);
      closeModal(entityModal());
      if(window['refresh'+capitalize(type)+'s']) window['refresh'+capitalize(type)+'s']();
      if(type==='team' && typeof window.refreshPlayers==='function') window.refreshPlayers();
    } catch(err){
      alert('Save failed: '+err.message);
    }
  }

  async function onDeleteConfirm(){
    if(!pendingDelete) return;
    const {type,id} = pendingDelete;
    try{
      const res = await fetch(API[type]+'/'+id, {method:'DELETE'});
      if(!res.ok) throw new Error('Delete failed '+res.status);
      closeModal(deleteModal());
      pendingDelete = null;
      if(window['refresh'+capitalize(type)+'s']) window['refresh'+capitalize(type)+'s']();
      if(type==='team' && typeof window.refreshPlayers==='function') window.refreshPlayers();
    }catch(err){
      alert('Delete failed: '+err.message);
    }
  }

  // expose
  window.openAddEntity = (t)=>openEntityModal('add',t,{});
  window.openEditEntity = (t,data)=>openEntityModal('edit',t,data||{});
  window.openDeleteEntity = (t,id,label)=>openDelete(t,id,label);

  // wire handlers
  function wire(){
    const form = document.getElementById('entityForm');
    if(form) form.addEventListener('submit', onSubmit);
    const delBtn = document.getElementById('deleteConfirm');
    if(delBtn) delBtn.addEventListener('click', onDeleteConfirm);
    wireClose();
  }
  function wireClose(){
    const eClose = document.getElementById('entityModalClose');
    const eCancel = document.getElementById('entityCancel');
    if(eClose) eClose.onclick = ()=>closeModal(entityModal());
    if(eCancel) eCancel.onclick = ()=>closeModal(entityModal());
    const dClose = document.getElementById('deleteModalClose');
    const dCancel = document.getElementById('deleteCancel');
    if(dClose) dClose.onclick = ()=>closeModal(deleteModal());
    if(dCancel) dCancel.onclick = ()=>closeModal(deleteModal());
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',wire);
  else wire();

})();
