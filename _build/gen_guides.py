import json, re
exec(open('gen_pages.py',encoding='utf-8').read().split("page('merci.html'")[0])
BASE='https://punaises-de-lit-toulouse.fr/'
DATE='2026-09-28'
GUIDES=[
 ('prix-traitement-punaises-de-lit-toulouse.html',"Prix d'un traitement à Toulouse"),
 ('detection-canine-punaises-de-lit-toulouse.html','Détection canine'),
 ('reconnaitre-punaises-de-lit.html','Reconnaître les punaises de lit'),
 ('que-faire-punaises-de-lit.html','Que faire en attendant le pro'),
 ('punaises-de-lit-locataire-proprietaire.html','Locataire ou propriétaire : qui paie ?'),
]
def guide(fn,title,desc,h1,crumb,body,faq=None):
    ld=[{"@context":"https://schema.org","@type":"Article","headline":h1,"description":desc,"datePublished":DATE,"dateModified":DATE,"inLanguage":"fr-FR","mainEntityOfPage":BASE+fn,"image":BASE+"og-image.png","author":{"@type":"Organization","name":"Tada House","url":BASE},"publisher":{"@type":"Organization","name":"Tada House","logo":{"@type":"ImageObject","url":BASE+"favicon.svg"}}},
        {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Punaises de lit Toulouse","item":BASE},{"@type":"ListItem","position":2,"name":crumb,"item":BASE+fn}]}]
    if faq:
        ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})
        body+='<h2>Questions fréquentes</h2>'+''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in faq)
    rel=''.join(f'<li><a href="/{f}">{t}</a></li>' for f,t in GUIDES if f!=fn)
    full=f'''<div class="wrap page"><article class="prose">
<nav class="crumbs" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › {crumb}</nav>
<h1>{h1}</h1>
<p class="updated">Mis à jour le 28 septembre 2026</p>
{body}
<div class="cta-box"><h2>Un professionnel certifié vous rappelle</h2><p>Décrivez votre situation en une minute. Une entreprise locale vous rappelle pour un diagnostic et un devis gratuits, sans engagement.</p><a class="btn" href="/#devis">Demander mon devis gratuit <svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div>
<div class="related"><h2>À lire aussi</h2><ul>{rel}</ul></div>
</article></div>
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>'''
    page(fn,title,desc,full,robots="index, follow",canon=fn)
    # add OG tags
    h=open(fn,encoding='utf-8').read()
    og=f'''<meta property="og:type" content="article">
<meta property="og:title" content="{h1}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE+fn}">
<meta property="og:image" content="{BASE}og-image.png">
<meta property="og:locale" content="fr_FR">'''
    h=h.replace('<meta name="theme-color"',og+'\n<meta name="theme-color"',1)
    open(fn,'w',encoding='utf-8').write(h)

# 1. PRIX
guide('prix-traitement-punaises-de-lit-toulouse.html',
"Prix traitement punaises de lit Toulouse : tarifs 2026 par méthode",
"Combien coûte un traitement contre les punaises de lit à Toulouse ? Fourchettes de prix 2026 par méthode, facteurs qui font varier le devis et pièges à éviter.",
"Prix d'un traitement contre les punaises de lit à Toulouse",
"Prix d'un traitement",
'''<p class="intro">À Toulouse comme ailleurs, le prix d'un traitement contre les punaises de lit va d'environ 150 € pour une détection à plusieurs milliers d'euros pour un traitement thermique complet. L'écart s'explique par la méthode, la surface à traiter et le niveau d'infestation. Voici les repères utiles pour lire un devis.</p>
<h2>Les fourchettes de prix par méthode</h2>
<div class="table-scroll"><table>
<thead><tr><th>Méthode</th><th>Prix indicatif TTC</th><th>Pour quel cas</th></tr></thead>
<tbody>
<tr><td>Détection canine</td><td>150 à 300 €</td><td>Confirmer une infestation, localiser les foyers, contrôler après traitement</td></tr>
<tr><td>Traitement chimique (biocide)</td><td>170 à 450 €</td><td>Infestation légère à moyenne, en général 2 passages espacés de 2 à 3 semaines</td></tr>
<tr><td>Vapeur sèche</td><td>350 à 1 300 €</td><td>Literie, textiles, logements avec enfants ou animaux, souvent combinée au chimique</td></tr>
<tr><td>Thermique ou cryogénie</td><td>1 000 à 4 000 €</td><td>Infestation importante, grands volumes, lieux sensibles</td></tr>
</tbody></table></div>
<p class="note">Fourchettes indicatives relevées sur des sources publiques en 2026. Seul le devis établi après diagnostic fait foi.</p>
<h2>Ce qui fait varier le prix</h2>
<ul>
<li><strong>La surface et le nombre de pièces touchées.</strong> Un studio avec une seule chambre infestée coûte beaucoup moins cher qu'une maison entière.</li>
<li><strong>Le niveau d'infestation.</strong> Quelques insectes dans un matelas se traitent vite ; des punaises dans les plinthes, les prises et les meubles demandent plus de temps et parfois plusieurs méthodes.</li>
<li><strong>Le nombre de passages.</strong> Les produits biocides n'agissent pas sur les œufs : un second passage, 2 à 3 semaines plus tard, est presque toujours nécessaire. Vérifiez qu'il est inclus dans le prix.</li>
<li><strong>L'encombrement du logement.</strong> Plus il y a d'objets et de recoins, plus la préparation et le traitement sont longs.</li>
<li><strong>Le contrôle final.</strong> Certaines entreprises incluent une détection canine de fin de traitement, d'autres la facturent en plus.</li>
</ul>
<h2>Comment lire un devis</h2>
<p>Un devis sérieux précise la méthode employée, le nombre de passages, les pièces traitées, les produits utilisés, la préparation demandée avant l'intervention et la garantie éventuelle en cas de réapparition. L'entreprise qui applique des produits biocides doit détenir le certificat <strong>Certibiocide</strong> : demandez-le, c'est la première garantie de sérieux.</p>
<h2>Les pièges à éviter</h2>
<ul>
<li>Un prix très bas annoncé au téléphone sans diagnostic : il cache souvent un seul passage ou des suppléments.</li>
<li>Une pression pour intervenir le soir même avec un paiement immédiat en espèces.</li>
<li>Un devis sans mention du nombre de passages ni de garantie.</li>
</ul>
<p>Si vous êtes locataire, le coût du traitement est en principe à la charge du propriétaire. Consultez notre guide <a href="/punaises-de-lit-locataire-proprietaire.html">locataire ou propriétaire : qui paie ?</a></p>''',
faq=[("Combien coûte un traitement contre les punaises de lit pour un appartement à Toulouse ?","Pour un appartement avec une infestation légère à moyenne, comptez le plus souvent entre 170 et 450 € pour un traitement chimique en deux passages, et entre 350 et 1 300 € pour un traitement à la vapeur sèche. Le devis dépend de la surface et du niveau d'infestation."),
("Pourquoi faut-il souvent deux passages ?","Les produits biocides tuent les punaises adultes et les larves mais pas les œufs. Un second passage 2 à 3 semaines plus tard élimine les punaises nées entre-temps, avant qu'elles puissent pondre."),
("Le diagnostic est-il payant ?","Beaucoup d'entreprises toulousaines proposent un diagnostic gratuit avant devis. La détection canine, plus précise, est généralement facturée entre 150 et 300 €.")])

# 2. DETECTION CANINE
guide('detection-canine-punaises-de-lit-toulouse.html',
"Détection canine punaises de lit Toulouse : prix et fonctionnement",
"Chien détecteur de punaises de lit à Toulouse : comment se déroule une inspection, quand la demander, combien elle coûte et comment choisir une équipe sérieuse.",
"Détection canine des punaises de lit à Toulouse",
"Détection canine",
'''<p class="intro">Un chien spécialement dressé repère l'odeur des punaises de lit vivantes et de leurs œufs, même cachés dans une plinthe ou un sommier. En quelques minutes par pièce, il indique les zones infestées. C'est la méthode la plus fiable pour confirmer un doute ou vérifier qu'un traitement a fonctionné.</p>
<h2>Comment se déroule une inspection</h2>
<ol>
<li>Le maître-chien vous interroge sur les signes observés et les pièces concernées.</li>
<li>Le chien inspecte chaque pièce : lits, canapés, meubles, plinthes, rideaux. Il marque l'arrêt (en général en s'asseyant) devant une zone suspecte.</li>
<li>Le technicien vérifie visuellement les zones marquées et vous remet un compte rendu, souvent avec un plan des foyers.</li>
</ol>
<p>Comptez de 30 minutes à une heure pour un appartement. Aérez sans parfumer le logement avant la visite et évitez d'utiliser un insecticide dans les jours qui précèdent, qui pourrait gêner le chien.</p>
<h2>Quand faire appel à un chien détecteur</h2>
<ul>
<li><strong>En cas de doute</strong> : piqûres sans insecte visible, qui peuvent venir d'autres causes.</li>
<li><strong>Avant un traitement</strong> : pour traiter seulement les pièces touchées et réduire la facture.</li>
<li><strong>Après un traitement</strong> : pour contrôler qu'il ne reste aucun foyer actif.</li>
<li><strong>Avant d'emménager ou d'acheter</strong> un meuble ou un logement, et pour les hôtels et locations saisonnières.</li>
</ul>
<h2>Combien coûte une détection canine à Toulouse</h2>
<p>Les prix observés à Toulouse se situent en général entre <strong>150 et 300 € TTC</strong> pour un logement, selon la surface. À titre d'exemple, une entreprise toulousaine affiche en 2026 175 € pour un studio ou un T2, 200 € pour un T3, 225 € pour un T4 et 275 € pour un T5. Certaines entreprises déduisent le prix de la détection du traitement si vous le leur confiez.</p>
<h2>Bien choisir son équipe cynophile</h2>
<p>Demandez si le chien est certifié pour la détection des punaises de lit et à quelle fréquence il est réévalué, si le compte rendu est écrit, et si l'entreprise peut aussi réaliser le traitement. Un chien fatigue vite : pour un grand logement, une équipe sérieuse prévoit des pauses.</p>''')

# 3. RECONNAITRE
guide('reconnaitre-punaises-de-lit.html',
"Reconnaître les punaises de lit : insecte, piqûres, signes (guide)",
"Comment savoir si vous avez des punaises de lit ? Taille et aspect de l'insecte, piqûres typiques, taches, mues et confusions fréquentes avec d'autres nuisibles.",
"Comment reconnaître les punaises de lit",
"Reconnaître les punaises de lit",
'''<p class="intro">Les punaises de lit se cachent le jour et sortent la nuit pour piquer. On les découvre souvent par leurs piqûres ou leurs traces avant de voir l'insecte. Voici les signes fiables pour savoir si vous êtes concerné.</p>
<h2>À quoi ressemble une punaise de lit</h2>
<ul>
<li><strong>Taille</strong> : celle d'un pépin de pomme, 5 à 7 mm pour un adulte. Les larves sont plus petites et plus claires.</li>
<li><strong>Forme</strong> : ovale et très plate, ce qui lui permet de se glisser dans les coutures et les fentes.</li>
<li><strong>Couleur</strong> : brun à brun-rouge, plus rouge et plus gonflée après un repas de sang.</li>
<li><strong>Comportement</strong> : elle ne saute pas et ne vole pas. Elle marche et se déplace d'un logement à l'autre par les bagages, les meubles et les vêtements.</li>
</ul>
<h2>Les signes d'une infestation</h2>
<ul>
<li><strong>Des piqûres au réveil</strong>, souvent groupées par 3 ou 4 ou alignées, sur les parties du corps découvertes la nuit. Elles ressemblent à des piqûres de moustique et démangent. Certaines personnes ne réagissent pas du tout.</li>
<li><strong>Des petits points noirs</strong> sur le matelas, les coutures, le sommier ou le mur derrière la tête de lit : ce sont les déjections.</li>
<li><strong>Des traces de sang</strong> sur les draps.</li>
<li><strong>Des œufs blancs</strong> d'environ 1 mm et des <strong>mues</strong> translucides dans les recoins.</li>
<li><strong>Une odeur</strong> douceâtre dans les cas d'infestation importante.</li>
</ul>
<h2>Où regarder</h2>
<p>Commencez par le lit : coutures et étiquettes du matelas, sommier, lattes, tête de lit. Élargissez ensuite aux plinthes, aux prises électriques, aux cadres, aux rideaux, au canapé et aux meubles proches. Une lampe torche et une carte de crédit glissée dans les fentes aident à les faire sortir.</p>
<h2>Les confusions fréquentes</h2>
<ul>
<li><strong>Les puces</strong> sautent et piquent surtout les chevilles, souvent en présence d'un animal.</li>
<li><strong>Les moustiques</strong> laissent des piqûres isolées et on les entend la nuit.</li>
<li><strong>Les acariens</strong> sont invisibles à l'œil nu et ne piquent pas.</li>
<li><strong>Les réactions cutanées</strong> (allergie, urticaire) peuvent imiter des piqûres : en l'absence de tout autre signe, une détection canine lève le doute.</li>
</ul>
<p>Les punaises de lit ne transmettent pas de maladie, mais les démangeaisons et le manque de sommeil peuvent être pénibles : parlez-en à votre médecin ou à votre pharmacien si besoin. Ensuite, suivez <a href="/que-faire-punaises-de-lit.html">les bons gestes en attendant le professionnel</a>.</p>''')

# 4. QUE FAIRE
guide('que-faire-punaises-de-lit.html',
"Punaises de lit : que faire en attendant le professionnel ?",
"Vous avez des punaises de lit ? Les bons gestes dès le premier jour (lavage à 60 °C, congélation, aspirateur) et les erreurs qui aggravent l'infestation.",
"Punaises de lit : que faire en attendant le professionnel",
"Que faire en attendant le pro",
'''<p class="intro">Les bons gestes des premiers jours limitent la propagation et rendent le traitement plus efficace. Les mauvais réflexes, eux, dispersent les punaises dans tout le logement.</p>
<h2>Les bons gestes</h2>
<ol>
<li><strong>Laver à 60 °C minimum</strong> les draps, housses, pyjamas et vêtements proches du lit.</li>
<li><strong>Passer au sèche-linge</strong> au moins 30 minutes en position chaude ce qui ne se lave pas à 60 °C.</li>
<li><strong>Congeler</strong> les petits objets et textiles fragiles pendant 72 heures dans un sac fermé.</li>
<li><strong>Aspirer</strong> le matelas, le sommier, les plinthes et le sol, puis jeter le sac immédiatement dans un sac plastique fermé, à l'extérieur.</li>
<li><strong>Isoler le linge propre</strong> dans des sacs fermés jusqu'à la fin du traitement.</li>
<li><strong>Prévenir</strong> votre propriétaire ou votre syndic si vous êtes en immeuble, par écrit et avec photos.</li>
<li><strong>Faire établir un diagnostic</strong> par un professionnel certifié.</li>
</ol>
<h2>Les erreurs à éviter</h2>
<ul>
<li><strong>Dormir dans une autre pièce</strong> : les punaises vous suivent et colonisent la nouvelle pièce.</li>
<li><strong>Utiliser des insecticides grand public</strong> (bombes, fumigènes) : ils sont peu efficaces sur les punaises et les poussent à se disperser.</li>
<li><strong>Jeter son matelas ou ses meubles dans la rue</strong> sans les emballer : vous risquez de contaminer d'autres logements, et le traitement permet souvent de les garder.</li>
<li><strong>Déplacer des affaires</strong> chez des proches sans les avoir lavées ou congelées.</li>
</ul>
<h2>Préparer le passage du professionnel</h2>
<p>L'entreprise vous donnera une liste précise. En général : dégager le tour des lits et les plinthes, laver le linge, vider les tables de nuit, et ne pas faire le ménage à fond juste avant, pour laisser les traces visibles au diagnostic.</p>
<h2>Les ressources officielles</h2>
<p>Le site du gouvernement <a href="https://stop-punaises.gouv.fr/" rel="noopener">stop-punaises.gouv.fr</a> et le numéro national d'information <strong>0806 706 806</strong> (prix d'un appel local) donnent des conseils gratuits. Pour le traitement lui-même, faites appel à une entreprise titulaire du certificat Certibiocide.</p>''')

# 5. LOCATAIRE
guide('punaises-de-lit-locataire-proprietaire.html',
"Punaises de lit : locataire ou propriétaire, qui paie le traitement ?",
"Punaises de lit en location à Toulouse : ce que dit la loi (loi de 1989, loi ELAN), qui paie le traitement, les exceptions et les démarches pour le locataire.",
"Punaises de lit en location : qui paie le traitement ?",
"Locataire ou propriétaire",
'''<p class="intro">En location, le traitement contre les punaises de lit est en principe à la charge du propriétaire. La loi prévoit toutefois des exceptions. Voici les règles et les démarches à connaître.</p>
<h2>Ce que dit la loi</h2>
<p>Depuis la loi ELAN de 2018, l'article 6 de la loi du 6 juillet 1989 impose au bailleur de remettre au locataire un logement décent <strong>exempt de toute infestation d'espèces nuisibles et parasites</strong>. Les punaises de lit en font partie. Le propriétaire doit donc, en règle générale, faire traiter le logement et en supporter le coût.</p>
<h2>Les cas où le locataire peut devoir payer</h2>
<p>Le propriétaire peut demander au locataire de prendre en charge le traitement s'il prouve que celui-ci est responsable de l'infestation : par exemple des punaises rapportées dans des meubles achetés d'occasion, un signalement très tardif qui a laissé l'infestation s'étendre, ou le refus de laisser intervenir l'entreprise. C'est au propriétaire d'apporter cette preuve.</p>
<h2>En copropriété</h2>
<p>Si l'infestation touche plusieurs logements ou vient des parties communes, le syndic doit être prévenu pour organiser un traitement coordonné. Traiter un seul appartement quand les voisins sont infestés conduit presque toujours à une réinfestation.</p>
<h2>Les démarches pour le locataire</h2>
<ol>
<li>Prévenir le propriétaire ou l'agence <strong>par écrit</strong> (email puis lettre recommandée), avec photos et date des premiers signes.</li>
<li>Faire constater l'infestation par un professionnel, idéalement avec un diagnostic écrit.</li>
<li>Demander au propriétaire de faire intervenir une entreprise dans un délai raisonnable.</li>
<li>Conserver toutes les factures et échanges.</li>
<li>Faciliter l'accès et suivre les consignes de préparation.</li>
</ol>
<p>En cas de blocage, l'ADIL de Haute-Garonne informe gratuitement locataires et propriétaires sur leurs droits.</p>
<h2>Vous êtes propriétaire</h2>
<p>Agissez vite : une infestation traitée tôt coûte beaucoup moins cher. Faites intervenir une entreprise certifiée, informez le syndic si besoin, et conservez les justificatifs. Un traitement réalisé dans les règles protège aussi vos relations avec le locataire.</p>
<p class="note">Cette page donne une information générale et ne remplace pas un conseil juridique personnalisé.</p>''')
print('ok')
