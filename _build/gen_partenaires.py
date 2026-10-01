# Page partenaires (artisans) : noindex, liee depuis les emails de prospection.
exec(open('gen_pages.py',encoding='utf-8').read().split("page('merci.html'")[0])
page('partenaires.html','Devenir partenaire | Punaises de lit Toulouse',
"Entreprises de traitement des punaises de lit à Toulouse : recevez les demandes de particuliers, une seule entreprise par secteur.",
'''<div class="wrap page"><article class="prose">
<p class="kicker" style="color:var(--teal);font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:.8rem">Espace professionnels</p>
<h1>Recevez les demandes de particuliers à Toulouse</h1>
<p class="intro">punaises-de-lit-toulouse.fr aide les particuliers et les propriétaires de Toulouse et de la métropole à trouver une entreprise certifiée pour traiter les punaises de lit. Nous transmettons leurs demandes à une seule entreprise par secteur.</p>
<video controls playsinline muted preload="metadata" poster="/media/presentation-partenaires.jpg" style="width:100%;height:auto;border-radius:16px;margin:8px 0 24px;box-shadow:0 12px 30px rgba(16,33,46,.12)"><source src="/media/presentation-partenaires.mp4" type="video/mp4"></video>
<h2>Comment ça marche</h2>
<ol>
<li><strong>Le particulier décrit sa situation</strong> sur le site, en une minute : type de logement, pièces touchées, ce qu'il a constaté, urgence.</li>
<li><strong>Vous recevez la demande par email</strong>, avec son téléphone, pour le rappeler et établir votre devis.</li>
<li><strong>Vous fixez librement vos prix</strong> et vous réalisez l'intervention. Le client vous paie directement.</li>
</ol>
<h2>Ce que nous proposons</h2>
<ul>
<li><strong>Une seule entreprise par secteur</strong> : les demandes ne sont pas revendues à plusieurs concurrents.</li>
<li><strong>Les premières demandes sont offertes</strong>, sans engagement, pour que vous jugiez la qualité sur pièce.</li>
<li><strong>Des entreprises certifiées uniquement</strong> : le Certibiocide est requis pour l'usage de produits biocides.</li>
</ul>
<div class="cta-box"><h2>Intéressé ?</h2><p>Écrivez-nous en précisant les communes que vous couvrez. Nous vous répondons rapidement.</p><a class="btn" href="mailto:contact@tadahouse.com?subject=Partenariat%20punaises-de-lit-toulouse.fr">contact@tadahouse.com <svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div>
<p class="note">punaises-de-lit-toulouse.fr est édité par Tada House (Maxime Gaillard EI). Voir les <a href="/mentions-legales.html">mentions légales</a>.</p>
</article></div>''',robots="noindex, follow",canon='partenaires.html')
print('ok')
