(function(){
  var header=document.querySelector('.site-header');
  var onScroll=function(){header&&header.classList.toggle('scrolled',window.scrollY>8)};
  onScroll();window.addEventListener('scroll',onScroll,{passive:true});

  // Apparition au défilement
  var els=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}});
    },{rootMargin:'0px 0px -8% 0px',threshold:.08});
    els.forEach(function(el){io.observe(el)});
  }else{els.forEach(function(el){el.classList.add('in')})}

  // Bouton flottant mobile : visible hors du formulaire
  var sticky=document.getElementById('sticky'),card=document.getElementById('devis');
  if(sticky&&card&&'IntersectionObserver' in window){
    var seen=false;
    new IntersectionObserver(function(en){
      var vis=en[0].isIntersecting;if(vis)seen=true;
      sticky.classList.toggle('show',!vis&&(seen||window.scrollY>300));
    },{threshold:.15}).observe(card);
  }

  // Formulaire en 3 étapes
  var form=document.getElementById('lead-form');if(!form)return;
  var steps=[].slice.call(form.querySelectorAll('.step'));
  var bar=document.getElementById('bar'),num=document.getElementById('step-n'),err=document.getElementById('form-error');
  var cur=0;
  function show(i){
    steps[cur].classList.remove('active');cur=i;steps[cur].classList.add('active');
    bar.style.width=((cur+1)/steps.length*100)+'%';num.textContent=cur+1;hideErr();
    var first=steps[cur].querySelector('input:not([type=hidden]),textarea');
    if(first&&window.innerWidth>760)first.focus({preventScroll:true});
    if(window.innerWidth<=760)card.scrollIntoView({behavior:'smooth',block:'start'});
  }
  function showErr(m){err.textContent=m;err.classList.remove('show');void err.offsetWidth;err.classList.add('show')}
  function hideErr(){err.classList.remove('show')}
  function valid(step){
    var groups={};
    step.querySelectorAll('input[type=radio][required]').forEach(function(r){groups[r.name]=true});
    for(var g in groups){if(!step.querySelector('input[name="'+g+'"]:checked')){
      var lg=step.querySelector('input[name="'+g+'"]').closest('fieldset').querySelector('legend').textContent;
      showErr('Merci de choisir : '+lg.toLowerCase()+'.');return false}}
    var fields=step.querySelectorAll('input[required]:not([type=radio]):not([type=checkbox])');
    for(var i=0;i<fields.length;i++){var f=fields[i];
      if(!f.value.trim()){showErr('Merci de renseigner : '+f.labels[0].textContent.toLowerCase()+'.');f.focus();return false}
      if(f.id==='tel'&&f.value.replace(/\D/g,'').length<10){showErr('Ce numéro de téléphone semble incomplet.');f.focus();return false}
      if(f.id==='cp'&&!/^\d{5}$/.test(f.value.trim())){showErr('Le code postal doit contenir 5 chiffres.');f.focus();return false}
    }
    var em=step.querySelector('#email');
    if(em&&em.value&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em.value)){showErr('Cette adresse email semble incorrecte.');em.focus();return false}
    var c=step.querySelector('input[name=consentement]');
    if(c&&!c.checked){showErr('Merci de cocher la case d\'accord pour que nous puissions transmettre votre demande.');return false}
    return true;
  }
  form.querySelectorAll('.next').forEach(function(b){b.addEventListener('click',function(){if(valid(steps[cur]))show(cur+1)})});
  form.querySelectorAll('.back').forEach(function(b){b.addEventListener('click',function(){show(cur-1)})});
  // Passage automatique quand tous les choix d'une étape sont faits
  form.addEventListener('change',function(e){
    if(e.target.type!=='radio'||cur>=steps.length-1)return;
    var s=steps[cur],names={},done=true;
    s.querySelectorAll('input[type=radio][required]').forEach(function(r){names[r.name]=1});
    for(var n in names){if(!s.querySelector('input[name="'+n+'"]:checked'))done=false}
    hideErr();
    if(done&&!s.querySelector('textarea'))setTimeout(function(){show(cur+1)},260);
  });
  form.addEventListener('submit',function(e){
    e.preventDefault();
    if(!valid(steps[cur]))return;
    var key=form.querySelector('[name=access_key]').value;
    if(!key||key.indexOf('VOTRE_')===0){showErr('Formulaire en cours de configuration. Écrivez-nous à contact@tadahouse.com en attendant.');return}
    var btn=document.getElementById('submit');btn.disabled=true;btn.firstChild.textContent='Envoi en cours... ';
    var data=Object.fromEntries(new FormData(form).entries());
    fetch(form.action,{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify(data)})
      .then(function(r){return r.json()})
      .then(function(j){if(j.success){window.location.href='/merci.html'}else{throw new Error()}})
      .catch(function(){btn.disabled=false;btn.firstChild.textContent='Envoyer ma demande ';showErr('L\'envoi a échoué. Réessayez dans un instant ou écrivez à contact@tadahouse.com.')});
  });
})();
