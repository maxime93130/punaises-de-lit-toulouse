import re
idx=open('index.html',encoding='utf-8').read()
head_fonts='''<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@1,9..144,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">'''
sprite=re.search(r'<svg width="0".*?</svg>\n',idx,re.S).group(0)
header=re.search(r'<header.*?</header>',idx,re.S).group(0).replace('href="#','href="/#')
footer=re.search(r'<footer>.*?</footer>',idx,re.S).group(0).replace('href="#top"','href="#main"').replace('href="#','href="/#')
def page(fn,title,desc,body,robots="noindex, follow",canon=None):
    c=f'<link rel="canonical" href="https://punaises-de-lit-toulouse.fr/{canon}">' if canon else ''
    html=f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
{c}
<meta name="theme-color" content="#10212E">
{head_fonts}
</head>
<body>
<a class="skip" href="#main">Aller au contenu</a>
{sprite}{header}
<main id="main">
{body}
</main>
{footer}
</body>
</html>
'''
    open(fn,'w',encoding='utf-8').write(html)

page('merci.html','Demande envoyée | Punaises de lit Toulouse','Votre demande a bien été transmise.','''<div class="wrap center-page"><div>
<div class="big-ico"><svg viewBox="0 0 24 24" class="check-anim" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
<h1>Demande bien reçue, merci</h1>
<p class="sub" style="max-width:32em;margin:0 auto 12px">Un professionnel partenaire va vous rappeler rapidement, en général le jour même en semaine. Gardez votre téléphone à portée de main.</p>
<p style="max-width:32em;margin:0 auto 28px;color:var(--ink-2)">En attendant : ne déplacez pas votre literie, lavez le linge à 60 °C et n'utilisez pas d'insecticide grand public.</p>
<a class="btn btn-ghost" href="/">Retour à l'accueil</a>
</div></div>''')

page('404.html','Page introuvable | Punaises de lit Toulouse','Cette page n\'existe pas.','''<div class="wrap center-page"><div>
<div class="big-ico"><svg aria-hidden="true"><use href="#i-nose"/></svg></div>
<h1>Cette page est introuvable</h1>
<p class="sub" style="margin-bottom:28px">Elle a peut-être été déplacée. Votre demande de devis reste à un clic.</p>
<a class="btn" href="/#devis">Demander un devis gratuit <svg aria-hidden="true"><use href="#i-arrow"/></svg></a>
</div></div>''')

T='<span class="todo">[À COMPLÉTER]</span>'
page('mentions-legales.html','Mentions légales | Punaises de lit Toulouse','Mentions légales du site punaises-de-lit-toulouse.fr.',f'''<div class="wrap page"><div class="prose">
<h1>Mentions légales</h1>
<h2>Éditeur du site</h2>
<p>Le site punaises-de-lit-toulouse.fr est édité par Maxime Gaillard EI, entrepreneur individuel exerçant sous le nom commercial Tada House, SIRET 892 358 953 00016, domicilié 48 rue du Fond d'Orval, 93130 Noisy-le-Sec, France.<br>Directeur de la publication : Maxime Gaillard<br>Contact : <a href="mailto:contact@tadahouse.com">contact@tadahouse.com</a></p>
<h2>Hébergeur</h2>
<p>GitHub, Inc. (service GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis. <a href="https://github.com" rel="noopener">github.com</a></p><p>Nom de domaine enregistré auprès d'OVH SAS, 2 rue Kellermann, 59100 Roubaix, France.</p>
<h2>Nature du service</h2>
<p>punaises-de-lit-toulouse.fr est un service de mise en relation entre des particuliers ou professionnels et des entreprises spécialisées dans le traitement des nuisibles. L'éditeur ne réalise aucune intervention. Les entreprises partenaires établissent leurs propres devis, fixent librement leurs prix et sont seules responsables des prestations réalisées. Le service est gratuit pour l'utilisateur ; l'éditeur est rémunéré par les entreprises partenaires.</p>
<h2>Informations sur les prix</h2>
<p>Les prix affichés sur le site sont des fourchettes indicatives établies à partir de sources publiques. Ils n'ont pas de valeur contractuelle.</p>
<h2>Propriété intellectuelle</h2>
<p>Les textes, illustrations et éléments graphiques du site sont la propriété de l'éditeur, sauf mention contraire. Toute reproduction sans autorisation est interdite.</p>
<h2>Données personnelles</h2>
<p>Voir notre page <a href="/confidentialite.html">Données personnelles</a>.</p>
</div></div>''',robots="index, follow",canon="mentions-legales.html")

page('confidentialite.html','Données personnelles | Punaises de lit Toulouse','Comment sont utilisées les données transmises via le formulaire de devis.',f'''<div class="wrap page"><div class="prose">
<h1>Données personnelles</h1>
<h2>Responsable du traitement</h2>
<p>Maxime Gaillard EI (Tada House), SIRET 892 358 953 00016, 48 rue du Fond d'Orval, 93130 Noisy-le-Sec. Contact : <a href="mailto:contact@tadahouse.com">contact@tadahouse.com</a></p>
<h2>Données collectées</h2>
<p>Via le formulaire de demande de devis : prénom, code postal, téléphone, email (facultatif) et les informations que vous donnez sur votre situation (type de logement, pièces touchées, constats, délai, précisions).</p>
<h2>Finalité et base légale</h2>
<p>Ces données servent uniquement à transmettre votre demande à une entreprise partenaire de traitement des nuisibles, qui vous contactera pour établir un devis, et à vérifier la bonne prise en charge de votre demande. Le traitement repose sur votre consentement, donné en cochant la case du formulaire.</p>
<h2>Destinataires</h2>
<p>Votre demande est transmise à une seule entreprise partenaire intervenant dans votre secteur. Elle n'est ni vendue ni cédée à d'autres entreprises. Les données transitent par notre prestataire d'envoi de formulaires (Web3Forms, service d'envoi de formulaires).</p>
<h2>Durée de conservation</h2>
<p>Les données sont conservées 12 mois à compter de la demande, puis supprimées.</p>
<h2>Vos droits</h2>
<p>Vous pouvez accéder à vos données, les rectifier, les effacer, retirer votre consentement ou vous opposer à leur traitement en écrivant à <a href="mailto:contact@tadahouse.com">contact@tadahouse.com</a>. Vous pouvez aussi saisir la CNIL (<a href="https://www.cnil.fr" rel="noopener">cnil.fr</a>).</p>
<h2>Cookies</h2>
<p>Ce site ne dépose aucun cookie publicitaire ni cookie de mesure d'audience nécessitant votre accord. La mesure de fréquentation utilise un outil sans cookie.</p>
</div></div>''',robots="index, follow",canon="confidentialite.html")
