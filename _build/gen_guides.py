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
 ('punaises-de-lit-etudiants-toulouse.html','Étudiants : résidence, Crous, colocation'),
 ('combien-de-temps-se-debarrasser-punaises-de-lit.html','Combien de temps pour s\'en débarrasser ?'),
 ('faut-il-jeter-matelas-punaises-de-lit.html','Faut-il jeter son matelas ?'),
 ('vapeur-seche-punaises-de-lit.html','Traitement à la vapeur sèche'),
 ('punaises-de-lit-voyage-hotel.html','Voyage et hôtel : ne pas les ramener'),
 ('piqures-punaises-de-lit.html','Piqûres : reconnaître et soulager'),
 ('terre-de-diatomee-insecticides-remedes-punaises-de-lit.html','Diatomée, insecticides, remèdes maison'),
]
MOIS=['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
def fr_date(d):
    y,m,j=d.split('-'); return f"{int(j)} {MOIS[int(m)-1]} {y}"

def guide(fn,title,desc,h1,crumb,body,faq=None,date=None):
    date=date or DATE
    ld=[{"@context":"https://schema.org","@type":"Article","headline":h1,"description":desc,"datePublished":date,"dateModified":date,"inLanguage":"fr-FR","mainEntityOfPage":BASE+fn,"image":BASE+"og-image.png","author":{"@type":"Organization","name":"Tada House","url":BASE},"publisher":{"@type":"Organization","name":"Tada House","logo":{"@type":"ImageObject","url":BASE+"favicon.svg"}}},
        {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Punaises de lit Toulouse","item":BASE},{"@type":"ListItem","position":2,"name":crumb,"item":BASE+fn}]}]
    if faq:
        ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})
        body+='<h2>Questions fréquentes</h2>'+''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in faq)
    rel=''.join(f'<li><a href="/{f}">{t}</a></li>' for f,t in GUIDES if f!=fn)
    full=f'''<div class="wrap page"><article class="prose">
<nav class="crumbs" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › {crumb}</nav>
<h1>{h1}</h1>
<p class="updated">Mis à jour le {fr_date(date)}</p>
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

# 6. ETUDIANTS (2026-10-01)
guide('punaises-de-lit-etudiants-toulouse.html',
"Punaises de lit étudiant à Toulouse : résidence Crous, colocation",
"Étudiant à Toulouse avec des punaises de lit ? Que faire en résidence Crous, en studio ou en colocation, qui paie le traitement et à qui demander de l'aide gratuitement.",
"Punaises de lit et étudiants à Toulouse : que faire et qui paie ?",
"Étudiants à Toulouse",
'''<p class="intro">Toulouse compte plus de 110 000 étudiants inscrits dans les établissements du site universitaire toulousain, dont environ 90 % dans la métropole. À chaque rentrée, les déménagements, les meubles d'occasion et les retours de vacances favorisent le transport involontaire de punaises de lit. Voici quoi faire selon que vous logez en résidence Crous, en studio loué ou en colocation.</p>
<h2>Pourquoi les étudiants sont souvent concernés</h2>
<ul>
<li><strong>Les déménagements fréquents</strong> : cartons, matelas et valises passent d'un logement à l'autre.</li>
<li><strong>Le mobilier d'occasion</strong> : un sommier ou un canapé récupéré peut abriter des punaises et des œufs invisibles.</li>
<li><strong>Les logements collectifs</strong> : résidences et colocations multiplient les allers et venues, et une infestation peut passer d'une chambre à l'autre par les gaines et les plinthes.</li>
</ul>
<p>Avoir des punaises de lit n'a rien à voir avec l'hygiène : elles se nourrissent de sang, pas de saleté. Il n'y a aucune honte à le signaler, et plus vous le faites tôt, plus le traitement est simple.</p>
<h2>Vous logez en résidence Crous</h2>
<p>Le règlement intérieur des résidences universitaires du Crous de Toulouse (édition 2025-2026) est clair : si vous constatez la présence de nuisibles, notamment de punaises de lit, vous devez <strong>en informer la résidence sans délai</strong>. Le guide du résident demande de le signaler à l'accueil de la résidence et de <strong>ne pas utiliser d'insecticide</strong>, mais de suivre le protocole interne.</p>
<p><strong>Qui paie ?</strong> Selon ce même règlement, les frais sont engagés par le Crous. Ils ne peuvent être facturés au résident qu'en cas de non-signalement de l'infestation ou de non-respect du protocole de désinsectisation. Autrement dit : signaler vite et suivre les consignes vous protège.</p>
<ol>
<li>Prévenez l'accueil de votre résidence dès les premiers signes (piqûres, taches noires sur le matelas, insecte vu).</li>
<li>Gardez une trace écrite de votre signalement (email, photo datée).</li>
<li>Suivez le protocole qu'on vous remet : lavage du linge, sacs fermés, accès à la chambre pour l'entreprise.</li>
<li>Ne déménagez pas vos affaires chez un ami ou chez vos parents avant traitement : vous risquez d'y emmener les punaises.</li>
</ol>
<h2>Vous louez un studio ou une chambre (meublé ou vide)</h2>
<p>Les règles sont celles de toute location : le bailleur doit fournir un logement décent, <strong>exempt de toute infestation d'espèces nuisibles et parasites</strong> (article 6 de la loi du 6 juillet 1989, modifié par la loi ELAN de 2018). Le traitement est donc en principe à sa charge, que le logement soit meublé ou non. Il peut demander au locataire d'en supporter le coût s'il prouve que celui-ci est à l'origine de l'infestation, par exemple avec un meuble d'occasion infesté.</p>
<p>Prévenez votre propriétaire ou l'agence par écrit, avec photos et dates, et demandez une intervention rapide. Le détail des démarches figure dans notre guide <a href="/punaises-de-lit-locataire-proprietaire.html">locataire ou propriétaire : qui paie ?</a></p>
<h2>Vous êtes en colocation</h2>
<p>En colocation, les punaises ne restent jamais dans une seule chambre très longtemps. Quelques règles de bon sens :</p>
<ul>
<li><strong>Prévenez tout de suite vos colocataires</strong>, même si vous êtes le seul à être piqué : certaines personnes ne réagissent pas aux piqûres.</li>
<li><strong>Faites un signalement commun</strong> au propriétaire ou à l'agence, par écrit.</li>
<li><strong>Faites traiter tout le logement en même temps</strong> : traiter une seule chambre conduit presque toujours à une réinfestation.</li>
<li><strong>Appliquez tous le même protocole</strong> : linge lavé à 60 °C, affaires en sacs fermés, pas de déplacement d'affaires entre les chambres.</li>
</ul>
<p>Si un désaccord apparaît sur la prise en charge entre colocataires ou avec le bailleur, l'ADIL de Haute-Garonne peut vous informer gratuitement sur votre situation précise.</p>
<h2>Avant d'emménager : les réflexes qui évitent les ennuis</h2>
<ul>
<li><strong>À l'état des lieux d'entrée</strong>, inspectez le matelas, le sommier et les plinthes avec une lampe. Notez et photographiez toute tache suspecte.</li>
<li><strong>Meubles et vêtements d'occasion</strong> : examinez-les avant de les rentrer. Le site officiel stop-punaises.gouv.fr recommande de laver les textiles à 60 °C minimum ou de les passer au sèche-linge chaud au moins 30 minutes.</li>
<li><strong>Au retour de voyage</strong>, ne posez pas votre valise sur le lit, inspectez vos affaires et passez l'aspirateur dans la valise.</li>
</ul>
<h2>Les aides et contacts gratuits à Toulouse</h2>
<ul>
<li><strong>ADIL de Haute-Garonne (ADIL 31)</strong> : 4 rue Furgole, 31000 Toulouse, 05 61 22 46 22. Conseil juridique gratuit et neutre sur vos droits de locataire.</li>
<li><strong>Numéro national d'information</strong> : 0806 706 806 (prix d'un appel local), et le site <a href="https://stop-punaises.gouv.fr/" rel="noopener">stop-punaises.gouv.fr</a>.</li>
<li><strong>Votre résidence Crous</strong> : l'accueil de votre résidence pour tout signalement.</li>
<li><strong>Votre médecin ou votre pharmacien</strong> si les piqûres vous gênent beaucoup ou provoquent une réaction importante.</li>
</ul>
<p>Pour un premier tri, consultez aussi <a href="/reconnaitre-punaises-de-lit.html">comment reconnaître les punaises de lit</a> et <a href="/que-faire-punaises-de-lit.html">que faire en attendant le professionnel</a>.</p>
<p class="note">Sources consultées le 1er octobre 2026 : règlement intérieur des résidences et guide du résident du Crous de Toulouse, document de caractérisation du site universitaire de Toulouse (Université de Toulouse, février 2025, effectifs 2023-2024), stop-punaises.gouv.fr, ANIL. Cette page donne une information générale et ne remplace pas un conseil juridique personnalisé.</p>''',
faq=[("Je suis en résidence Crous à Toulouse : qui paie le traitement contre les punaises de lit ?","D'après le règlement intérieur des résidences du Crous de Toulouse, les frais de désinsectisation sont engagés par le Crous. Ils ne peuvent être facturés au résident qu'en cas de non-signalement de l'infestation ou de non-respect du protocole. Signalez donc le problème à l'accueil sans attendre."),
("Puis-je utiliser un insecticide dans ma chambre ?","Non, c'est déconseillé. Le Crous demande de ne pas utiliser d'insecticide et de suivre le protocole de la résidence. Les produits grand public sont peu efficaces sur les punaises de lit et peuvent les disperser."),
("En colocation, faut-il traiter tout l'appartement ?","Oui, c'est fortement recommandé. Les punaises se déplacent d'une pièce à l'autre et traiter une seule chambre mène presque toujours à une réinfestation. Signalez le problème ensemble au bailleur, par écrit."),
("Je loue un studio meublé : le propriétaire doit-il payer ?","En principe oui. Le bailleur doit fournir un logement exempt de nuisibles et de parasites, meublé ou non. Il ne peut vous faire payer que s'il prouve que vous êtes à l'origine de l'infestation.")],
date='2026-10-01')
# 7. DUREE (2026-10-05)
guide('combien-de-temps-se-debarrasser-punaises-de-lit.html',
"Combien de temps pour se débarrasser des punaises de lit ?",
"Combien de temps faut-il pour se débarrasser des punaises de lit ? Nombre de passages, intervalle de 15 jours, surveillance après traitement : le calendrier réaliste et ce qui le rallonge.",
"Combien de temps faut-il pour se débarrasser des punaises de lit ?",
"Durée d'un traitement",
'''<p class="intro">On aimerait que tout soit réglé en une journée. En pratique, venir à bout des punaises de lit prend plutôt quelques semaines, puis un ou deux mois de surveillance. La raison est simple : il faut atteindre les insectes qui sortent des œufs après le premier passage. Voici le calendrier réaliste, étape par étape, et ce qui peut le raccourcir ou le rallonger.</p>
<h2>La réponse courte</h2>
<ul>
<li><strong>Un traitement chimique se fait en au moins 2 passages, parfois 3</strong>, espacés d'environ 15 jours (recommandation du rapport national « Punaises de lit en France », CNEV, 2015).</li>
<li><strong>Il faut ensuite surveiller 1 à 2 mois</strong> : c'est l'absence durable de nouvelles piqûres et de nouvelles traces sur cette période qui permet de considérer l'infestation comme éliminée (même source).</li>
<li><strong>Au total, comptez donc en général entre un mois et demi et trois mois</strong> entre le premier passage et la fin de la surveillance, selon le nombre de passages et le niveau d'infestation.</li>
</ul>
<h2>Pourquoi un seul passage ne suffit presque jamais</h2>
<p>Une femelle pond plusieurs œufs par jour, environ 200 au cours de sa vie, et les œufs mettent <strong>entre 6 et 17 jours à éclore</strong> (Santé Canada). Or les œufs, collés dans les recoins, sont beaucoup plus difficiles à atteindre que les insectes. Le rapport du CNEV le résume ainsi : la désinsectisation chimique doit être pratiquée au moins deux fois, avec 15 jours d'intervalle, pour tuer les jeunes issus des œufs.</p>
<p>Le deuxième passage n'est donc pas un signe d'échec : il est prévu dès le départ. Méfiez-vous d'une offre qui promet de tout régler en une seule application d'insecticide sans visite de contrôle.</p>
<h2>Le calendrier type d'un traitement</h2>
<ol>
<li><strong>Avant l'intervention</strong> : le professionnel fait un premier échange, souvent par téléphone, et vous remet les consignes de préparation du logement (stop-punaises.gouv.fr). Un diagnostic, visuel ou avec un chien détecteur, permet de délimiter les pièces touchées.</li>
<li><strong>Jour 0, premier passage</strong> : traitement des zones infestées (literie, sommier, plinthes, meubles proches du lit).</li>
<li><strong>Environ 15 jours plus tard, deuxième passage</strong> : il vise les jeunes punaises sorties des œufs entre-temps.</li>
<li><strong>Si besoin, un troisième passage</strong> environ 15 jours après, quand l'infestation était importante ou que des signes persistent.</li>
<li><strong>Puis 1 à 2 mois de surveillance</strong> : vous vérifiez régulièrement le matelas et les coutures, et vous signalez à l'entreprise toute nouvelle piqûre ou trace.</li>
</ol>
<p>Les méthodes non chimiques (vapeur sèche, chaleur, froid) suivent des protocoles qui varient d'une entreprise à l'autre. Dans tous les cas, demandez que le devis précise <strong>le nombre de passages prévus, leur intervalle et la visite de contrôle</strong>.</p>
<h2>Ce qui rallonge la durée</h2>
<ul>
<li><strong>Attendre avant d'agir</strong> : chaque semaine compte, puisque de nouvelles générations apparaissent en continu.</li>
<li><strong>Une préparation incomplète</strong> : linge non lavé, affaires laissées en vrac au sol, pièces inaccessibles le jour du passage.</li>
<li><strong>Déplacer ses affaires</strong> dans une autre pièce ou chez des proches avant le traitement : on déplace aussi les punaises.</li>
<li><strong>Traiter une seule pièce</strong> ou un seul logement d'un immeuble touché : la réinfestation vient alors des pièces ou des voisins non traités.</li>
<li><strong>Les insecticides grand public</strong> utilisés en amont, qui sont peu efficaces sur les punaises et peuvent les disperser.</li>
</ul>
<h2>Partir quelques semaines ne règle rien</h2>
<p>Laisser le logement vide pour « affamer » les punaises ne fonctionne pas : elles peuvent survivre plusieurs mois sans se nourrir. Le rapport du CNEV cite jusqu'à 135 jours à 22 °C et 277 jours à 18 °C, et Santé Canada évoque jusqu'à 18 mois dans certaines conditions. À votre retour, elles seront toujours là.</p>
<h2>Ce que vous pouvez faire pour accélérer</h2>
<ul>
<li><strong>Linge et textiles</strong> : lavage en machine à 60 °C ou plus, ou au moins 30 minutes au sèche-linge à chaud (stop-punaises.gouv.fr).</li>
<li><strong>Petits objets non lavables</strong> : au congélateur dans un sac fermé pendant 72 heures (stop-punaises.gouv.fr).</li>
<li><strong>Recoins et tissus d'ameublement</strong> : appareil à vapeur sèche d'au moins 120 °C (DGCCRF), puis aspirateur, sac jeté dans un sac fermé.</li>
<li><strong>Respecter à la lettre les consignes</strong> de l'entreprise avant et après chaque passage.</li>
</ul>
<p>Les gestes à faire dès le premier jour sont détaillés dans notre guide <a href="/que-faire-punaises-de-lit.html">que faire en attendant le professionnel</a>.</p>
<h2>Comment savoir que c'est vraiment fini ?</h2>
<p>On considère l'infestation éliminée quand il n'y a plus de nouvelles piqûres ni de nouvelles traces pendant 1 à 2 mois après le dernier passage. Attention : certaines personnes ne réagissent pas aux piqûres. Inspectez donc aussi le matelas, les coutures et le sommier à la lampe. En cas de doute, une détection canine permet de contrôler le logement (voir notre guide sur la <a href="/detection-canine-punaises-de-lit-toulouse.html">détection canine à Toulouse</a>).</p>
<h2>Bien choisir l'entreprise pour ne pas perdre de temps</h2>
<p>Pour un traitement insecticide, vérifiez que l'entreprise dispose d'un certificat <strong>Certibiocide</strong> en cours de validité. Comparez au moins deux devis, et ne payez rien tant que la prestation n'a pas été réalisée (DGCCRF). Les fourchettes de prix pratiquées sont présentées dans notre guide <a href="/prix-traitement-punaises-de-lit-toulouse.html">prix d'un traitement à Toulouse</a>.</p>
<p class="note">Sources consultées le 5 octobre 2026 : rapport « Punaises de lit en France : état des lieux et recommandations » (Centre national d'expertise sur les vecteurs, septembre 2015, publié par l'Anses), stop-punaises.gouv.fr, Santé Canada (« Punaises de lit : à quoi ressemblent-elles ? »), DGCCRF (« Se débarrasser des punaises de lit : comparez les devis »). Durées indicatives : seul le diagnostic d'un professionnel permet d'établir le protocole adapté à votre logement.</p>''',
faq=[("Combien de passages faut-il pour éliminer les punaises de lit ?","Pour un traitement chimique, au moins deux passages, parfois trois, espacés d'environ 15 jours. Le deuxième passage sert à éliminer les jeunes punaises sorties des œufs après le premier."),
("Combien de temps après le traitement les punaises disparaissent-elles ?","Elles diminuent dès le premier passage, mais il faut attendre la fin des passages puis 1 à 2 mois sans nouvelle piqûre ni nouvelle trace pour considérer l'infestation comme éliminée."),
("Peut-on dormir dans son lit pendant le traitement ?","Suivez les consignes de l'entreprise, qui indique le délai avant de réoccuper les pièces traitées. Évitez surtout d'aller dormir dans une autre pièce ou chez des proches : vous risquez d'y transporter les punaises."),
("Si je pars en vacances un mois, les punaises vont-elles mourir de faim ?","Non. Les punaises de lit peuvent survivre plusieurs mois sans se nourrir, jusqu'à 135 jours à 22 °C d'après le rapport national de 2015, et parfois bien plus. Un traitement reste nécessaire.")],
date='2026-10-05')
# 8. MATELAS (2026-10-08)
guide('faut-il-jeter-matelas-punaises-de-lit.html',
"Punaises de lit : faut-il jeter son matelas ?",
"Punaises de lit : faut-il jeter son matelas ? Dans la plupart des cas, non. Traitement, housse intégrale, et si vous le jetez quand même : comment l'emballer et où le déposer à Toulouse.",
"Punaises de lit : faut-il jeter son matelas ?",
"Faut-il jeter son matelas ?",
'''<p class="intro">Quand on découvre des punaises de lit, le premier réflexe est souvent de sortir le matelas sur le trottoir. C'est rarement la bonne idée. Dans la plupart des cas, le matelas se traite et se protège. Le jeter ne règle pas l'infestation, et mal le jeter peut la propager dans tout l'immeuble. Voici comment décider, et comment faire proprement si vous devez vraiment vous en séparer.</p>
<h2>La réponse courte</h2>
<ul>
<li><strong>En général, non</strong> : les documents des autorités sanitaires (ARS Île-de-France, stop-punaises.gouv.fr) recommandent de traiter le matelas (aspiration, vapeur) plutôt que de le jeter.</li>
<li><strong>Jeter le matelas ne suffit pas</strong> : les punaises se cachent aussi dans le sommier, la tête de lit, les plinthes et les meubles proches. Un matelas neuf posé dans un logement non traité sera recolonisé.</li>
<li><strong>Si vous le jetez</strong>, faites-le après ou pendant le traitement, emballé hermétiquement, rendu inutilisable, et jamais déposé sur le palier ou dans la rue.</li>
</ul>
<h2>Pourquoi jeter le matelas n'est pas la solution</h2>
<p>Les punaises de lit ne vivent pas seulement dans le matelas. Elles se logent dans les coutures, mais aussi dans les fentes du sommier, les lattes, les cadres de lit, les prises et les plinthes. Retirer le matelas laisse donc en place une bonne partie de la population.</p>
<p>Elles peuvent en outre survivre longtemps sans se nourrir : jusqu'à 135 jours à 22 °C selon le rapport national « Punaises de lit en France » (CNEV, 2015). Un lit neuf acheté avant que le logement soit traité risque d'être infesté en quelques jours, et la dépense est perdue.</p>
<p>Enfin, transporter un matelas non emballé dans la cage d'escalier ou l'ascenseur peut semer des punaises chez les voisins. C'est l'une des raisons pour lesquelles les autorités demandent de <strong>ne pas abandonner d'objets potentiellement infestés dans la rue ou sur le palier</strong> (ARS Île-de-France).</p>
<h2>Comment traiter un matelas infesté</h2>
<ol>
<li><strong>Aspirer minutieusement les deux faces</strong>, en insistant sur les coutures, les passepoils et les poignées. L'ARS Île-de-France recommande de renouveler l'aspiration régulièrement pendant une dizaine de jours. Fermez ensuite le sac de l'aspirateur avec du ruban adhésif et jetez-le dans un sac poubelle fermé, à la poubelle extérieure (stop-punaises.gouv.fr).</li>
<li><strong>Passer le matelas à la vapeur sèche</strong> : la vapeur entre 120 °C et 180 °C tue immédiatement les œufs et les larves qu'elle atteint (protocole d'auto-traitement de stop-punaises.gouv.fr). Passez lentement, à quelques centimètres de la surface.</li>
<li><strong>Laver tout le linge de lit à 60 °C minimum</strong>, cycle long, puis au sèche-linge à chaud au moins 30 minutes si possible (stop-punaises.gouv.fr).</li>
<li><strong>Traiter aussi le sommier et le cadre de lit</strong>, et faire intervenir un professionnel si l'infestation est installée : un traitement chimique se fait en au moins deux passages espacés d'environ 15 jours (CNEV, 2015).</li>
</ol>
<p>Le détail du calendrier est expliqué dans notre guide <a href="/combien-de-temps-se-debarrasser-punaises-de-lit.html">combien de temps pour se débarrasser des punaises de lit</a>.</p>
<h2>La housse intégrale : utile, mais pas un traitement</h2>
<p>Une housse anti-punaises enveloppe le matelas sur ses six faces et se ferme par une glissière. Posée sur un matelas infesté, elle enferme les insectes présents et les coupe du dormeur. Posée sur un matelas sain, elle les empêche de s'installer dans les coutures.</p>
<ul>
<li><strong>Fermeture</strong> : Santé Canada conseille de recouvrir la fermeture éclair de ruban adhésif, car les punaises peuvent se faufiler à travers.</li>
<li><strong>Durée</strong> : gardez le matelas recouvert pendant un an (Santé Canada), sans ouvrir la housse pour la laver.</li>
<li><strong>Intégrité</strong> : la protection ne fonctionne que tant que la housse est intacte, sans trou ni déchirure.</li>
<li><strong>Limite</strong> : la housse ne protège ni le sommier, ni la tête de lit, ni le reste de la pièce. Elle complète le traitement, elle ne le remplace pas.</li>
</ul>
<h2>Quand jeter le matelas peut se justifier</h2>
<p>Un matelas très abîmé (déchiré, éventré, coutures ouvertes) ne peut plus être protégé correctement par une housse, et la vapeur n'atteint pas l'intérieur. Si le matelas était de toute façon en fin de vie, le remplacer peut être raisonnable. Demandez l'avis de l'entreprise qui intervient : c'est elle qui voit l'état réel de la literie.</p>
<h2>Si vous le jetez : la bonne méthode</h2>
<ol>
<li><strong>Emballer hermétiquement</strong> le matelas dans du film plastique ou une housse fermée <strong>avant</strong> de le sortir de la chambre (ARS Île-de-France, Ville et Eurométropole de Strasbourg).</li>
<li><strong>Le rendre inutilisable</strong>, par exemple en le lacérant ou en le marquant à la peinture, pour que personne ne le récupère (document de la Ville et de l'Eurométropole de Strasbourg soutenu par l'ARS Grand Est).</li>
<li><strong>Ne pas le déposer sur le palier ou dans la rue</strong>, ne pas le vendre, ne pas le donner.</li>
<li><strong>L'apporter directement en déchèterie</strong> et prévenir les agents de l'infestation, ou passer par la collecte des encombrants de votre commune (en cas de doute, la mairie indique la marche à suivre, rappelle l'ARS Île-de-France).</li>
</ol>
<h2>Où déposer un matelas à Toulouse</h2>
<p>Toulouse Métropole propose une <strong>collecte des encombrants sur rendez-vous</strong>, avec une démarche en ligne sur le site metropole.toulouse.fr, ainsi qu'un réseau de déchèteries. Vérifiez les conditions à jour sur le site de la Métropole avant de prendre rendez-vous, et signalez que le matelas est emballé à cause de punaises de lit.</p>
<p>Si vous achetez un matelas neuf, le vendeur est en principe tenu de reprendre gratuitement l'ancien depuis le 1er janvier 2022 (loi antigaspillage, rappel de Que Choisir, juin 2022), sauf petits vendeurs exonérés. Prévenez-le de l'infestation avant l'enlèvement et remettez-lui le matelas emballé.</p>
<h2>Et le sommier, le canapé, les meubles ?</h2>
<p>La même logique s'applique : on traite d'abord, on ne jette qu'en dernier recours, et toujours emballé. Pour les petits objets qui ne se lavent pas, le congélateur fonctionne : 5 jours à -18 °C dans une boîte fermée (stop-punaises.gouv.fr). Pour la suite des gestes à faire, consultez notre guide <a href="/que-faire-punaises-de-lit.html">que faire en attendant le professionnel</a>.</p>
<p class="note">Sources consultées le 8 octobre 2026 : protocole d'auto-traitement de stop-punaises.gouv.fr ; brochure « Punaises de lit » de l'ARS Île-de-France (2019) ; « Stop aux punaises de lit ! », Ville et Eurométropole de Strasbourg, contrat local de santé soutenu par l'ARS Grand Est ; Santé Canada (« Punaises de lit : comment s'assurer qu'elles ne reviendront pas ? ») ; rapport « Punaises de lit en France » (CNEV, 2015, publié par l'Anses) ; Que Choisir (5 juin 2022) ; Toulouse Métropole (collecte des encombrants). Seul le diagnostic d'un professionnel permet de juger l'état de votre literie.</p>''',
faq=[("Faut-il jeter son matelas quand on a des punaises de lit ?","Dans la plupart des cas, non. Le matelas se traite (aspiration, vapeur sèche entre 120 et 180 °C) puis se protège avec une housse intégrale fermée. Le jeter ne règle pas l'infestation, car les punaises se cachent aussi dans le sommier, le cadre de lit et la pièce."),
("Une housse anti-punaises suffit-elle ?","Non. Elle enferme les punaises présentes dans le matelas et empêche de nouvelles de s'y installer, mais elle ne protège pas le sommier, la tête de lit ni le reste de la pièce. Elle complète le traitement. Santé Canada conseille de la garder fermée pendant un an."),
("Comment jeter un matelas infesté sans contaminer l'immeuble ?","Emballez-le hermétiquement dans du film plastique avant de le sortir de la chambre, rendez-le inutilisable (lacéré ou marqué à la peinture), puis apportez-le en déchèterie en prévenant les agents, ou passez par la collecte des encombrants. Ne le laissez jamais sur le palier ou dans la rue."),
("Faut-il acheter un nouveau matelas tout de suite ?","Mieux vaut attendre que le logement soit traité. Un matelas neuf installé dans une pièce encore infestée peut être recolonisé en quelques jours, car les punaises survivent des mois sans se nourrir.")],
date='2026-10-08')
guide('vapeur-seche-punaises-de-lit.html',
"Vapeur sèche contre les punaises de lit : efficacité, limites, prix",
"Traitement des punaises de lit à la vapeur sèche : comment ça marche, ce que dit l'Anses, les limites de la méthode, la bonne technique et les prix d'un professionnel à Toulouse.",
"Vapeur sèche contre les punaises de lit : principe, limites et prix",
"Traitement à la vapeur sèche",
'''<p class="intro">La vapeur sèche est l'une des méthodes les plus utilisées contre les punaises de lit, par les professionnels comme par les particuliers. Elle ne laisse pas de résidu chimique et tue les insectes et les œufs qu'elle touche. Mais elle ne touche que ce qu'elle atteint : c'est sa force et sa limite. Voici ce qu'en disent les autorités sanitaires, comment bien l'utiliser et ce que coûte une intervention.</p>
<h2>La réponse courte</h2>
<ul>
<li><strong>Efficace au contact</strong> : l'Anses classe la vapeur parmi les méthodes à efficacité « élevée », avec un risque pour la santé jugé négligeable (avis de juillet 2023).</li>
<li><strong>Limitée à ce qu'elle touche</strong> : il est difficile d'atteindre toutes les cachettes d'une pièce, et une punaise que la vapeur n'atteint pas survit.</li>
<li><strong>Rarement suffisante seule</strong> : selon l'Anses, aucune méthode ne suffit à elle seule. La vapeur s'intègre dans un traitement complet (aspiration, lavage du linge, parfois insecticide, contrôle).</li>
<li><strong>Prix</strong> : comptez en général de 350 à 1 300 € pour un logement traité par un professionnel, selon la surface et l'infestation.</li>
</ul>
<h2>Comment agit la vapeur sèche</h2>
<p>Un appareil à vapeur sèche produit une vapeur très chaude et peu chargée en eau. Le protocole d'auto-traitement de stop-punaises.gouv.fr indique une température <strong>entre 120 °C et 180 °C</strong>, qui permet d'éliminer immédiatement les œufs et les larves touchés. Le guide de l'université du Tennessee (Extension, 2014) rappelle que tous les stades de la punaise meurent en moins d'une minute au-delà d'environ 49 °C (120 °F) : la vapeur agit donc par simple choc thermique.</p>
<p>Le mot « sèche » compte. Les appareils à vapeur sèche ou à faible humidité sont préférables parce qu'ils mouillent moins les matériaux et limitent le risque de moisissures (fiche HealthLinkBC n° 95, 2020). Un nettoyeur vapeur classique, qui détrempe le tissu, est moins adapté.</p>
<h2>Ce que dit l'Anses</h2>
<p>Dans son expertise « Les punaises de lit : impacts, prévention et lutte » (juillet 2023), l'Anses a évalué les différentes méthodes de lutte :</p>
<ul>
<li><strong>Vapeur</strong> : efficacité élevée, applicabilité moyenne, car il est difficile de cibler toutes les zones où les punaises se reposent. Le risque pour la santé est négligeable, avec une altération possible de l'objet traité.</li>
<li><strong>Chaleur sèche</strong> (traitement thermique de toute la pièce) : efficacité élevée également, mais réservée aux professionnels équipés.</li>
<li><strong>Insecticides</strong> : l'agence signale des résistances chez les punaises de lit et recommande de privilégier les méthodes non chimiques.</li>
</ul>
<p>Autrement dit, la vapeur est une bonne méthode à condition d'être appliquée méthodiquement, partout où les punaises peuvent se cacher.</p>
<h2>Les limites à connaître</h2>
<ul>
<li><strong>Pas d'effet rémanent</strong> : la vapeur tue sur le moment. Une punaise cachée ailleurs, ou qui éclot d'un œuf non atteint, n'est pas touchée après le passage. D'où l'intérêt de répéter le traitement et de surveiller.</li>
<li><strong>Profondeur limitée</strong> : selon l'université du Tennessee, la vapeur pénètre d'environ 2 cm dans un tissu et d'un peu plus de 5 cm dans une fente. Elle n'atteint pas le cœur d'un matelas épais ni l'intérieur des murs.</li>
<li><strong>Matériaux fragiles</strong> : bois vernis, cuir, certains tissus et revêtements peuvent être abîmés par la chaleur et l'humidité. Testez sur une zone cachée. N'approchez jamais la vapeur des prises électriques ou des appareils.</li>
<li><strong>Risque de brûlure</strong> : la vapeur dépasse 120 °C. Le protocole officiel le rappelle : attention aux brûlures, surtout en présence d'enfants ou d'animaux.</li>
</ul>
<h2>Bien utiliser la vapeur sèche</h2>
<ol>
<li><strong>Aspirer d'abord</strong> avec un aspirateur à sac, en insistant sur les coutures, plinthes et fissures. Fermez ensuite le sac avec du ruban adhésif et jetez-le dans un sac poubelle fermé, à la poubelle extérieure (stop-punaises.gouv.fr).</li>
<li><strong>Utiliser un appareil qui dépasse 120 °C</strong>, acheté ou loué (stop-punaises.gouv.fr).</li>
<li><strong>Passer lentement, à quelques centimètres de la surface</strong>. La fiche HealthLinkBC conseille d'aller aussi lentement que possible. L'université du Tennessee recommande un embout large (triangulaire) plutôt qu'une buse fine, dont le jet peut souffler les punaises avant de les tuer.</li>
<li><strong>Viser les cachettes</strong> : coutures et passepoils du matelas, sommier, cadre et tête de lit, canapé, plinthes, encadrements, intérieur des tiroirs et des armoires.</li>
<li><strong>Répéter</strong> : le protocole officiel prévoit de compter environ 15 jours pour une élimination complète et de refaire la vapeur si nécessaire. Si le logement reste infesté, faites appel à un professionnel.</li>
</ol>
<p>En complément, lavez le linge à 60 °C et séchez-le à chaud. Le calendrier complet est détaillé dans notre guide <a href="/combien-de-temps-se-debarrasser-punaises-de-lit.html">combien de temps pour se débarrasser des punaises de lit</a>, et les gestes du premier jour dans <a href="/que-faire-punaises-de-lit.html">que faire en attendant le professionnel</a>.</p>
<h2>Faire soi-même ou faire appel à un professionnel ?</h2>
<p>Pour quelques punaises repérées tôt dans un lit, une vapeur sèche bien menée, combinée à l'aspiration et au lavage, peut suffire. Dès que l'infestation touche plusieurs meubles ou plusieurs pièces, un professionnel est plus sûr : il dispose d'appareils puissants, connaît les cachettes et combine souvent la vapeur avec d'autres méthodes. S'il applique un insecticide, il doit détenir le certificat <strong>Certibiocide</strong>, une obligation rappelée par l'Anses.</p>
<h2>Combien coûte un traitement à la vapeur sèche ?</h2>
<p>Le prix dépend surtout de la surface et du nombre de passages. À titre indicatif, un comparatif mis à jour en avril 2026 (MesDépanneurs.fr) relève :</p>
<div class="table-scroll"><table>
<thead><tr><th>Surface traitée</th><th>Prix indicatif TTC</th></tr></thead>
<tbody>
<tr><td>Chambre d'environ 15 m²</td><td>180 à 240 €</td></tr>
<tr><td>Studio ou 2 petites pièces (30 m²)</td><td>360 à 480 €</td></tr>
<tr><td>T2 ou T3 (60 m²)</td><td>720 à 960 €</td></tr>
<tr><td>T4 ou maison (100 m²)</td><td>1 200 à 1 600 €</td></tr>
</tbody></table></div>
<p class="note">Fourchettes nationales indicatives. À Toulouse, la plupart des devis pour un logement se situent entre 350 et 1 300 €. Seul le devis établi après diagnostic fait foi : vérifiez qu'il précise le nombre de passages et la visite de contrôle.</p>
<p>Pour comparer avec les autres méthodes (chimique, détection canine, thermique), consultez notre guide <a href="/prix-traitement-punaises-de-lit-toulouse.html">prix d'un traitement à Toulouse</a>. Si vous êtes locataire, lisez aussi <a href="/punaises-de-lit-locataire-proprietaire.html">qui paie le traitement</a>.</p>
<p class="note">Sources consultées le 12 octobre 2026 : protocole d'auto-traitement de stop-punaises.gouv.fr ; Anses, avis et rapport « Les punaises de lit : impacts, prévention et lutte » (juillet 2023) ; University of Tennessee Extension, « Affordable Bed Bug Management? » (SP 761, 2014) ; HealthLinkBC, fiche « Les punaises de lit » n° 95 (juin 2020) ; MesDépanneurs.fr, prix d'un traitement contre les punaises de lit (mis à jour en avril 2026). Ce guide ne remplace pas le diagnostic d'un professionnel.</p>''',
faq=[("La vapeur sèche tue-t-elle les œufs de punaises de lit ?","Oui, au contact. Le protocole de stop-punaises.gouv.fr indique qu'une vapeur entre 120 et 180 °C élimine immédiatement les œufs et les larves touchés. Les œufs que la vapeur n'atteint pas survivent, d'où la nécessité de passer partout et de répéter le traitement."),
("La vapeur sèche suffit-elle à éliminer une infestation ?","Rarement seule. L'Anses juge la vapeur efficace, mais estime qu'aucune méthode ne suffit à elle seule. Elle se combine avec l'aspiration, le lavage du linge à 60 °C, la surveillance et, si besoin, l'intervention d'un professionnel."),
("Quelle température faut-il pour tuer les punaises de lit à la vapeur ?","Utilisez un appareil qui dépasse 120 °C, comme le recommande stop-punaises.gouv.fr. Passez lentement, à quelques centimètres de la surface, pour que la chaleur atteigne bien les insectes cachés dans les coutures et les fentes."),
("Combien coûte un traitement à la vapeur sèche à Toulouse ?","Comptez le plus souvent entre 350 et 1 300 € pour un logement, selon la surface et le niveau d'infestation. Pour une seule chambre d'environ 15 m², les fourchettes nationales relevées en 2026 vont de 180 à 240 €.")],
date='2026-10-12')
guide('punaises-de-lit-voyage-hotel.html',
"Punaises de lit à l'hôtel et au retour de voyage : que faire ?",
"Punaises de lit en voyage : inspecter la chambre d'hôtel, protéger sa valise, que faire si l'on en trouve, et les gestes au retour à Toulouse (lavage 60 °C, sèche-linge, congélation).",
"Punaises de lit en voyage et à l'hôtel : comment ne pas les ramener chez soi",
"Voyage et hôtel",
'''<p class="intro">Les punaises de lit ne volent pas et ne sautent pas : elles voyagent dans les bagages et les vêtements. Une nuit dans une chambre infestée suffit pour en ramener quelques-unes, et quelques-unes suffisent pour installer une infestation chez soi. Bonne nouvelle : des gestes simples, à l'hôtel puis au retour, réduisent fortement le risque. Voici ce que recommandent les autorités sanitaires.</p>
<h2>La réponse courte</h2>
<ul>
<li><strong>À l'arrivée</strong> : posez la valise dans la salle de bain ou sur un porte-bagages inspecté, jamais sur le lit, puis inspectez le matelas et la tête de lit.</li>
<li><strong>Pendant le séjour</strong> : gardez la valise fermée et le linge sale dans un sac fermé.</li>
<li><strong>Si vous en trouvez</strong> : photographiez, prévenez la réception et demandez une chambre éloignée, ou changez d'hôtel.</li>
<li><strong>Au retour</strong> : ouvrez la valise sur une surface dure, loin du lit, lavez tous les textiles à 60 °C ou passez-les au sèche-linge chaud au moins 30 minutes, puis aspirez la valise.</li>
</ul>
<h2>Avant de partir</h2>
<ul>
<li><strong>Prévoyez des grands sacs plastique refermables</strong> pour séparer vos affaires, et un sac fermé dédié au linge sale (Santé Canada).</li>
<li><strong>Préférez une valise rigide et claire</strong> : les punaises s'y voient mieux et s'y cachent moins que dans un sac en tissu foncé. À défaut, une valise en tissu peut être enveloppée dans un sac plastique blanc bien fermé (Santé Canada).</li>
<li><strong>N'emportez pas votre propre oreiller</strong>, qui peut servir de cachette (Santé Canada).</li>
<li><strong>Une petite lampe de poche</strong> (celle du téléphone suffit) aide à inspecter les coutures et les fentes.</li>
</ul>
<h2>En arrivant dans la chambre</h2>
<ol>
<li><strong>Laissez la valise dans la salle de bain</strong> (carrelage, baignoire) ou sur le porte-bagages après l'avoir examiné, y compris les sangles. L'ARS Nouvelle-Aquitaine conseille de ne poser les bagages ni par terre, ni sur le lit, ni dessous.</li>
<li><strong>Inspectez le lit</strong> : soulevez les coins du drap et du matelas, regardez les coutures et passepoils, le sommier, l'arrière de la tête de lit et le mur derrière. Cherchez des insectes bruns de 4 à 7 mm, des petits points noirs de 1 à 2 mm (déjections) ou des taches de sang sur les draps.</li>
<li><strong>Regardez aussi les fauteuils et le placard</strong>, en particulier les fentes et les recoins.</li>
</ol>
<p>Pour savoir à quoi ressemblent les insectes, les œufs et les traces, consultez notre guide <a href="/reconnaitre-punaises-de-lit.html">reconnaître les punaises de lit</a>.</p>
<h2>Pendant le séjour</h2>
<ul>
<li><strong>Gardez la valise fermée</strong> quand vous ne l'utilisez pas, et ne rangez pas vos vêtements dans l'armoire sans l'avoir examinée (ARS Nouvelle-Aquitaine).</li>
<li><strong>N'étalez pas vos affaires sur le lit</strong> et ne laissez ni chaussures ni sacs sous le lit (Santé Canada).</li>
<li><strong>Fermez le sac de linge sale.</strong> Une étude de l'université de Sheffield publiée dans <em>Scientific Reports</em> (2017) a montré qu'en l'absence de dormeur, les punaises de lit étaient deux fois plus nombreuses à se regrouper sur des sacs de linge porté que sur des sacs de linge propre. Les auteurs conseillent de garder le linge sale dans un sac fermé, surtout à l'hôtel.</li>
</ul>
<h2>Si vous trouvez des punaises de lit à l'hôtel</h2>
<ol>
<li><strong>Ne déballez rien de plus</strong> et sortez vos bagages du contact du lit et des tissus.</li>
<li><strong>Prenez des photos</strong> des insectes, des traces sur la literie et, le cas échéant, des piqûres. Gardez une trace écrite de vos échanges avec l'établissement.</li>
<li><strong>Prévenez la réception</strong> et demandez une autre chambre, éloignée de la chambre suspecte (Santé Canada), ou changez d'hôtel. Vous pouvez demander un geste commercial ou un remboursement ; en cas de litige, une association de consommateurs peut vous aider.</li>
<li><strong>Traitez vos affaires dès le retour</strong>, comme expliqué ci-dessous, même si vous n'avez pas été piqué.</li>
</ol>
<p>Les piqûres ne permettent pas à elles seules de conclure : tout le monde ne réagit pas, et les réactions peuvent apparaître plusieurs jours après. Selon l'ARS Auvergne-Rhône-Alpes, elles disparaissent en général d'elles-mêmes en une dizaine de jours. En cas de réaction importante ou de doute, demandez conseil à un pharmacien ou à un médecin.</p>
<h2>Au retour à la maison : les bons gestes</h2>
<ol>
<li><strong>Ouvrez la valise sur une surface dure</strong> (carrelage, baignoire, balcon, garage), loin du lit, du canapé et des tapis (Santé Canada, ARS Nouvelle-Aquitaine).</li>
<li><strong>Sortez tous les textiles directement dans un sac fermé</strong> jusqu'à la machine, qu'ils aient été portés ou non.</li>
<li><strong>Lavez à 60 °C</strong>, ou passez au sèche-linge en cycle chaud pendant au moins 30 minutes ce qui ne supporte pas ce lavage (ARS Nouvelle-Aquitaine, Santé Canada).</li>
<li><strong>Congelez ce qui ne se lave pas</strong> (petits objets, chaussures en tissu, peluches) : au moins 72 heures à -20 °C, dans un sac fermé (ARS Nouvelle-Aquitaine, ARS Auvergne-Rhône-Alpes). Un congélateur ménager qui n'atteint pas -20 °C ne garantit pas le résultat.</li>
<li><strong>Inspectez les trousses</strong> de toilette et de maquillage, la brosse à cheveux, les poches et les sacs à main.</li>
<li><strong>Aspirez la valise</strong>, coutures et poches comprises. Jetez aussitôt le sac de l'aspirateur dans un sac plastique bien fermé, à la poubelle extérieure, puis nettoyez le conduit. Pour un aspirateur sans sac, videz le réservoir de la même façon et lavez-le à l'eau chaude.</li>
<li><strong>Rangez la valise loin des chambres</strong> (cave, garage, placard d'entrée), idéalement dans un grand sac fermé.</li>
</ol>
<h2>Dans les semaines qui suivent</h2>
<p>Restez attentif pendant quelques semaines : piqûres alignées au réveil, petites taches noires ou de sang sur les draps, insectes dans les coutures du matelas. Au moindre signe, ne déplacez pas vos affaires dans d'autres pièces et suivez les étapes de notre guide <a href="/que-faire-punaises-de-lit.html">que faire en attendant le professionnel</a>. Plus le traitement commence tôt, plus il est court et moins il coûte : voir <a href="/combien-de-temps-se-debarrasser-punaises-de-lit.html">combien de temps pour s'en débarrasser</a> et <a href="/prix-traitement-punaises-de-lit-toulouse.html">les prix à Toulouse</a>. En cas de doute, une <a href="/detection-canine-punaises-de-lit-toulouse.html">détection canine</a> permet de confirmer ou d'écarter une infestation débutante.</p>
<p>Vous êtes étudiant et rentrez de vacances en résidence ou en colocation ? Les démarches propres aux logements étudiants sont détaillées dans notre guide <a href="/punaises-de-lit-etudiants-toulouse.html">étudiants à Toulouse</a>. Le numéro national d'information est le 0806 706 806 (prix d'un appel local), et le site officiel stop-punaises.gouv.fr.</p>
<p class="note">Sources consultées le 15 octobre 2026 : Santé Canada, « Punaises de lit : comment les éviter en voyage ? » ; ARS Nouvelle-Aquitaine, « Les punaises de lit, mieux se protéger et prévenir leur apparition » (août 2024) ; ARS Auvergne-Rhône-Alpes, dépliant « Punaises de lit » (mai 2024) ; W. Hentley et al., université de Sheffield, « Bed bug aggregation on dirty laundry: a mechanism for passive dispersal », <em>Scientific Reports</em> (septembre 2017). Ce guide ne remplace pas l'avis d'un professionnel de santé ou de la désinsectisation.</p>''',
faq=[("Comment savoir s'il y a des punaises de lit dans une chambre d'hôtel ?","Inspectez le lit avant de vous installer : soulevez les coins du drap et du matelas, regardez les coutures, le sommier et l'arrière de la tête de lit. Cherchez des insectes bruns de 4 à 7 mm, de petits points noirs (déjections) ou des taches de sang sur les draps. Vérifiez aussi les fauteuils et le placard."),
("Où poser sa valise à l'hôtel pour éviter les punaises de lit ?","Dans la salle de bain, sur le carrelage ou dans la baignoire, ou sur un porte-bagages que vous avez inspecté. Jamais sur le lit, sous le lit ou sur un fauteuil. Gardez-la fermée quand vous ne l'utilisez pas."),
("Que faire de ses vêtements au retour d'un voyage ?","Ouvrez la valise sur une surface dure, loin du lit, et mettez tous les textiles dans un sac fermé jusqu'à la machine, portés ou non. Lavez à 60 °C ou passez au sèche-linge chaud au moins 30 minutes. Ce qui ne se lave pas peut être congelé 72 heures à -20 °C."),
("Faut-il jeter sa valise après un séjour dans un hôtel infesté ?","Non, en général. Aspirez-la soigneusement, coutures et poches comprises, jetez le sac de l'aspirateur dans un sac fermé, et rangez la valise loin des chambres, idéalement dans un grand sac fermé. Surveillez ensuite votre logement quelques semaines.")],
date='2026-10-15')

guide('piqures-punaises-de-lit.html',
"Piqûres de punaises de lit : reconnaître, soulager, quand consulter",
"Piqûres de punaises de lit : à quoi elles ressemblent, combien de temps elles durent, comment soulager les démangeaisons et quand consulter un médecin ou un pharmacien. Sources officielles.",
"Piqûres de punaises de lit : comment les reconnaître et les soulager",
"Piqûres",
'''<p class="intro">Des boutons rouges qui grattent au réveil, parfois alignés sur le bras ou la jambe : c'est souvent ce qui met la puce à l'oreille. Mais une piqûre ne suffit pas à prouver la présence de punaises de lit, et l'inverse est vrai aussi. Voici ce que disent les autorités sanitaires pour reconnaître ces piqûres, les soulager et savoir quand demander un avis médical. Ce guide donne des informations générales : il ne remplace pas l'avis d'un médecin ou d'un pharmacien.</p>
<h2>La réponse courte</h2>
<ul>
<li><strong>À quoi elles ressemblent</strong> : de petits boutons rouges qui démangent, proches de piqûres de moustique, souvent groupés ou alignés par trois à cinq, sur les zones découvertes pendant la nuit (ARS Île-de-France).</li>
<li><strong>Quand elles apparaissent</strong> : souvent au réveil, mais la réaction peut survenir de quelques heures à 10 jours après la piqûre (Manuel MSD).</li>
<li><strong>Combien de temps elles durent</strong> : en général quelques jours, environ une semaine (gouvernement du Québec, Manuel MSD).</li>
<li><strong>Sont-elles dangereuses ?</strong> Les punaises de lit ne transmettent pas de maladie (Anses, ARS Île-de-France). Le risque principal vient du grattage, qui peut infecter la peau.</li>
<li><strong>Que faire</strong> : laver à l'eau et au savon, ne pas gratter, demander conseil à un pharmacien. Consulter si la réaction est forte ou étendue.</li>
</ul>
<h2>Reconnaître une piqûre de punaise de lit</h2>
<p>Les piqûres prennent le plus souvent la forme de <strong>papules rouges</strong> (petits reliefs) qui démangent, parfois avec un minuscule point au centre. Selon le Manuel MSD, elles peuvent aussi se limiter à de petits points, à des taches violacées ou, plus rarement, former des cloques.</p>
<ul>
<li><strong>Où ?</strong> Sur la peau exposée pendant le sommeil : bras, jambes, épaules, dos, cou ou visage (ARS Île-de-France, gouvernement du Québec).</li>
<li><strong>Comment ?</strong> Souvent plusieurs piqûres groupées ou alignées, par trois ou quatre selon l'Anses, par trois à cinq selon l'ARS Île-de-France. Cette disposition en ligne est l'indice le plus caractéristique.</li>
<li><strong>Quand ?</strong> Elles sont souvent découvertes au réveil. Les démangeaisons sont généralement plus fortes tôt le matin et diminuent dans la journée (gouvernement du Québec).</li>
</ul>
<h2>Pourquoi une piqûre ne suffit pas à conclure</h2>
<ul>
<li><strong>Elles ressemblent à d'autres piqûres.</strong> L'Anses rappelle qu'elles ressemblent à celles d'autres insectes, et le Manuel MSD indique que même un médecin peut avoir du mal à poser le diagnostic sur le seul aspect de la peau.</li>
<li><strong>Tout le monde ne réagit pas.</strong> Environ 30 % des personnes n'ont aucune réaction cutanée visible, ce qui peut laisser une infestation passer inaperçue pendant des semaines (ARS Île-de-France). Dans un même lit, une seule personne peut présenter des boutons (gouvernement du Québec).</li>
<li><strong>La réaction peut être tardive.</strong> Elle peut apparaître jusqu'à 10 jours après la piqûre (Manuel MSD) : des boutons au retour de voyage peuvent donc venir de l'hôtel.</li>
</ul>
<p>Pour confirmer, il faut trouver d'autres indices dans le logement : insectes bruns de 4 à 7 mm, petits points noirs (déjections) ou taches de sang sur les draps, mues dans les coutures du matelas. Notre guide <a href="/reconnaitre-punaises-de-lit.html">reconnaître les punaises de lit</a> détaille ces signes. En cas de doute persistant, une <a href="/detection-canine-punaises-de-lit-toulouse.html">détection canine</a> permet de trancher.</p>
<h2>Soulager les démangeaisons</h2>
<ol>
<li><strong>Lavez la peau</strong> à l'eau fraîche avec un savon doux non parfumé (gouvernement du Québec, ARS Île-de-France).</li>
<li><strong>Évitez de vous gratter</strong>, pour limiter le risque d'infection. Garder les ongles courts aide, surtout chez les enfants.</li>
<li><strong>Demandez conseil à votre pharmacien</strong> : il peut vous orienter vers une crème apaisante adaptée. Selon le Manuel MSD, un médecin peut prescrire une crème à base de corticoïdes et des antihistaminiques par voie orale si les démangeaisons sont importantes.</li>
<li><strong>Traitez le logement</strong> : soigner la peau ne règle rien si les punaises restent. Comme le rappelle l'ARS Île-de-France, seule leur élimination évite que les piqûres reviennent.</li>
</ol>
<p>Les marques disparaissent généralement seules en quelques jours si la peau n'est pas piquée à nouveau (gouvernement du Québec). L'ARS Auvergne-Rhône-Alpes parle d'une dizaine de jours.</p>
<h2>Quand consulter un médecin ou un pharmacien</h2>
<p>Le gouvernement du Québec et l'ARS Île-de-France recommandent de consulter dans les cas suivants :</p>
<ul>
<li>réaction allergique importante ou urticaire ;</li>
<li>lésions étendues ou très nombreuses ;</li>
<li>apparition de cloques ;</li>
<li>peau qui gonfle, devient très rouge, chaude ou douloureuse (signes possibles d'infection) ;</li>
<li>démangeaisons qui persistent ou gênent beaucoup, notamment le sommeil.</li>
</ul>
<p>En cas de gêne respiratoire, de gonflement du visage ou des lèvres, ou de malaise, appelez immédiatement le 15 ou le 112. Pour un bébé, une femme enceinte ou une personne fragile, demandez un avis médical sans attendre.</p>
<h2>Sommeil, stress, anxiété : un impact à ne pas négliger</h2>
<p>L'ARS Île-de-France souligne que les effets psychologiques constituent souvent l'impact sanitaire le plus important d'une infestation : troubles du sommeil, fatigue, anxiété, isolement. L'Anses note aussi que la peur d'être stigmatisé pousse certaines personnes à ne pas en parler, ce qui retarde le traitement. Avoir des punaises de lit n'est pas lié à un manque d'hygiène. Si le sommeil ou le moral sont durablement affectés, parlez-en à votre médecin.</p>
<h2>Et ensuite ?</h2>
<p>Si les piqûres s'accompagnent d'autres indices, agissez vite : ne déplacez pas vos affaires dans d'autres pièces, ne dormez pas ailleurs dans le logement et suivez notre guide <a href="/que-faire-punaises-de-lit.html">que faire en attendant le professionnel</a>. Pour la suite : <a href="/prix-traitement-punaises-de-lit-toulouse.html">les prix d'un traitement à Toulouse</a>, <a href="/combien-de-temps-se-debarrasser-punaises-de-lit.html">combien de temps pour s'en débarrasser</a> et, si vous êtes locataire, <a href="/punaises-de-lit-locataire-proprietaire.html">qui paie le traitement</a>. Le numéro national d'information est le 0806 706 806 (prix d'un appel local), et le site officiel stop-punaises.gouv.fr.</p>
<p class="note">Sources consultées le 19 octobre 2026 : ARS Île-de-France, « Punaises de lit en Île-de-France : prévention, piqûres et traitements » (mise à jour août 2026) ; Gouvernement du Québec, « Piqûres de punaises de lit » (juin 2023) ; Manuel MSD grand public, « Infestation de punaises de lit » (J. Dinulos, révision novembre 2025) ; Anses, « Bed bugs in 13 questions » (octobre 2023) ; ARS Auvergne-Rhône-Alpes, dépliant « Punaises de lit » (mai 2024). Ce guide ne remplace pas l'avis d'un professionnel de santé.</p>''',
faq=[("Comment reconnaître une piqûre de punaise de lit ?","Ce sont de petits boutons rouges qui démangent, proches de piqûres de moustique, souvent groupés ou alignés par trois à cinq sur les zones découvertes la nuit (bras, jambes, épaules, cou). Ils sont souvent découverts au réveil. Seuls, ils ne prouvent pas la présence de punaises : cherchez aussi des insectes, des points noirs ou des taches de sang sur la literie."),
("Combien de temps durent les piqûres de punaises de lit ?","En général quelques jours, environ une semaine, si la peau n'est pas piquée à nouveau. La réaction peut toutefois apparaître de quelques heures à 10 jours après la piqûre."),
("Les punaises de lit transmettent-elles des maladies ?","Non. L'Anses et les agences régionales de santé indiquent que les punaises de lit ne transmettent pas de maladie. Le risque vient surtout du grattage, qui peut provoquer une infection de la peau, et de l'impact sur le sommeil et le moral."),
("Que mettre sur une piqûre de punaise de lit ?","Lavez la peau à l'eau fraîche et au savon doux, évitez de gratter et demandez conseil à un pharmacien pour une crème apaisante. Si les démangeaisons sont fortes, un médecin peut prescrire un traitement adapté."),
("Quand faut-il consulter pour des piqûres de punaises de lit ?","En cas de réaction allergique, de lésions étendues, de cloques, de peau gonflée, chaude ou douloureuse, ou de démangeaisons qui empêchent de dormir. En cas de gêne respiratoire ou de gonflement du visage, appelez le 15 ou le 112.")],
date='2026-10-19')

guide('terre-de-diatomee-insecticides-remedes-punaises-de-lit.html',
"Terre de diatomée, insecticides, remèdes maison : ce qui marche contre les punaises de lit",
"Terre de diatomée, bombes insecticides, huiles essentielles, produits interdits : ce que disent l'Anses et les études sur l'efficacité et les risques des remèdes contre les punaises de lit.",
"Terre de diatomée, insecticides, remèdes maison : ce qui marche et ce qui ne marche pas",
"Diatomée, insecticides, remèdes maison",
'''<p class="intro">Face aux punaises de lit, le premier réflexe est souvent d'acheter une bombe insecticide, un sachet de terre de diatomée ou un spray « naturel ». Certains de ces produits ont un intérêt limité, d'autres ne servent à rien, et quelques-uns sont dangereux. Voici ce que disent l'Anses, les centres antipoison et les études scientifiques, pour éviter de perdre du temps et de l'argent, ou de mettre sa santé en jeu.</p>
<h2>La réponse courte</h2>
<ul>
<li><strong>Ce qui marche</strong> : les méthodes mécaniques et thermiques (aspiration, lavage à 60 °C, sèche-linge chaud, vapeur sèche, congélation), que l'Anses recommande en premier.</li>
<li><strong>Terre de diatomée</strong> : une efficacité reconnue par l'Anses, mais lente, partielle et seulement en complément. À utiliser uniquement sous forme de produit autorisé, en respectant le mode d'emploi, car la poussière irrite les voies respiratoires.</li>
<li><strong>Bombes et fumigènes</strong> : peu ou pas d'effet dans les études, car le produit n'atteint pas les cachettes et beaucoup de punaises sont résistantes.</li>
<li><strong>Huiles essentielles et remèdes « verts »</strong> : résultats faibles ou très variables selon les produits, aucun ne remplace un traitement complet.</li>
<li><strong>À ne jamais utiliser</strong> : les produits interdits achetés sur un marché, à l'étranger ou en ligne, comme le Sniper 1000 (dichlorvos), responsable d'intoxications graves et de décès en France.</li>
</ul>
<h2>Pourquoi les insecticides marchent de moins en moins</h2>
<p>L'Anses cite la <strong>résistance croissante des punaises aux insecticides</strong> parmi les causes de la hausse des infestations. Utiliser des produits chimiques sans méthode accentue encore cette résistance, réduit leur efficacité, pollue le logement et expose à des intoxications. L'agence recommande donc les méthodes non chimiques en premier, que l'on traite soi-même ou que l'on fasse appel à un professionnel. Le traitement chimique reste un dernier recours, confié à une entreprise dont les techniciens détiennent le certificat <strong>Certibiocide</strong>.</p>
<h2>Les bombes et fumigènes insecticides</h2>
<p>Les diffuseurs automatiques (« foggers ») vendus en magasin ont été testés par des chercheurs de l'université d'État de l'Ohio (S. C. Jones et J. L. Bryant, <em>Journal of Economic Entomology</em>, 2012) : trois marques du commerce, cinq populations de punaises de lit. Résultat : <strong>peu ou pas d'effet</strong> sur les insectes. Le brouillard se dépose sur les surfaces visibles, alors que les punaises passent l'essentiel de leur temps cachées dans les coutures, les fentes, sous le matelas ou au fond des moquettes. Plusieurs populations étaient en plus résistantes au produit.</p>
<p>Les auteurs concluent que ces produits ne devraient pas être recommandés : ils coûtent de l'argent, retardent un traitement efficace et peuvent renforcer la résistance.</p>
<h2>Les intoxications : un risque réel</h2>
<p>Les centres antipoison ont enregistré <strong>1 056 appels</strong> liés à l'usage d'insecticides contre les punaises de lit entre 2007 et 2021 (Anses, février 2023). Dans 76 % des cas, les personnes exposées ont eu des symptômes : irritation respiratoire ou ORL, irritation de la peau, maux de tête, douleurs abdominales, vertiges. Douze cas étaient graves, dont cinq chez des enfants, et un enfant est décédé. Dans 11 % des cas, le produit avait été utilisé à une dose supérieure à celle indiquée sur l'étiquette.</p>
<p>Si vous utilisez malgré tout un insecticide vendu en magasin, respectez strictement la dose, aérez, tenez les enfants et les animaux à l'écart et respectez le délai avant de réoccuper la pièce indiqué sur l'emballage. En cas de malaise, appelez un centre antipoison ou le 15.</p>
<h2>Sniper 1000 et produits interdits : danger</h2>
<p>Le <strong>Sniper 1000 EC DDVP</strong> contient du dichlorvos, une substance interdite en France depuis 2013. Il circule pourtant encore, vendu sur des marchés, dans des bazars ou rapporté de l'étranger. Dans un rapport d'octobre 2023, l'Anses a analysé les cas enregistrés par les centres antipoison entre janvier 2018 et juin 2023 : <strong>170 événements, 206 personnes exposées</strong>, un nombre en hausse constante, et trois décès. Ces expositions avaient lieu au domicile, surtout lors de la lutte contre les punaises de lit et les cafards. L'agence estime que le nombre réel de cas est sous-estimé.</p>
<p>Notre conseil est simple : <strong>n'achetez jamais d'insecticide hors des circuits de vente classiques</strong>, et ne gardez pas chez vous un produit sans étiquette en français. Si vous en avez un, ne l'utilisez pas et demandez à votre déchèterie comment vous en débarrasser.</p>
<h2>La terre de diatomée : utile, mais pas miracle</h2>
<p>La terre de diatomée est une poudre minérale faite de micro-algues fossilisées. Elle agit physiquement : elle abîme la couche protectrice de l'insecte, qui se dessèche. Les punaises ne peuvent donc pas y devenir résistantes comme aux insecticides chimiques.</p>
<ul>
<li><strong>Ce qu'en dit l'Anses</strong> : les insecticides à base de terre de diatomée (kieselguhr) ou de dioxyde de silicium ont « une bonne efficacité ». Mais à l'intérieur d'un logement, ils peuvent irriter les voies respiratoires. L'agence recommande de n'utiliser que des produits disposant d'une <strong>autorisation de mise sur le marché</strong> (numéro de la forme FR-20AA-XXXX sur l'emballage) et de respecter strictement leurs conditions d'emploi.</li>
<li><strong>C'est lent</strong> : la poudre peut mettre plusieurs jours à tuer une punaise, qui continue de piquer entre-temps.</li>
<li><strong>Les résultats varient selon le produit</strong> : dans une étude en double aveugle de l'université d'État du Mississippi (J. Goddard, <em>Insects</em>, 2014), une terre de diatomée pure n'a tué que 11 % des punaises ou moins, une poudre de diatomée additionnée d'insecticide 27 % au mieux, et un gel de silice jusqu'à environ 50 %, après six mois de vieillissement du dépôt. Les insecticides de synthèse de référence faisaient beaucoup mieux sur les punaises sensibles, mais aucun produit ne dépassait 50 % sur une souche résistante.</li>
<li><strong>Attention à la poussière</strong> : la terre de diatomée naturelle contient un peu de silice cristalline (0,1 à 4 %), et la terre calcinée beaucoup plus (20 à 60 %), selon l'INRS. Inhalée, la silice cristalline est classée cancérogène et peut provoquer une silicose. N'utilisez pas de terre de diatomée « pour piscine » ou de filtration, qui est souvent calcinée, et n'en répandez jamais de grandes quantités dans une chambre.</li>
</ul>
<p>Si vous en utilisez, déposez une <strong>fine couche</strong>, presque invisible, dans les fentes, derrière les plinthes et sous le sommier, là où les punaises passent, jamais sur le lit ni en tas. Elle ne fait que compléter l'aspiration, le lavage et la vapeur.</p>
<h2>Huiles essentielles et sprays « naturels »</h2>
<p>Des chercheurs de l'université Rutgers (N. Singh, C. Wang et R. Cooper, <em>Journal of Economic Entomology</em>, 2014) ont testé neuf produits du commerce à base d'huiles essentielles. Pulvérisés directement sur les punaises, la plupart n'en tuaient que <strong>0 à 30 %</strong> en dix jours. Deux produits faisaient beaucoup mieux au contact direct, mais restaient lents et peu efficaces quand les punaises pouvaient choisir où se poser (10 % de mortalité ou moins dans ce test). Aucun effet répulsif n'a été mesuré. Les auteurs demandent des essais en conditions réelles avant toute recommandation.</p>
<p>En pratique, une huile essentielle ne tue que les punaises qu'elle touche directement, comme la vapeur, et elle ne les fait pas fuir durablement. Les huiles essentielles peuvent en outre irriter la peau et les voies respiratoires et sont déconseillées sans avis médical pour les jeunes enfants, les femmes enceintes et les animaux.</p>
<h2>Vinaigre, alcool, bicarbonate, lavande</h2>
<p>Ces remèdes circulent beaucoup en ligne. Aucun des organismes consultés pour ce guide (Anses, stop-punaises.gouv.fr, agences régionales de santé) ne les recommande, et nous n'avons trouvé aucune étude sérieuse montrant qu'ils peuvent éliminer une infestation. Au mieux, ils tuent quelques insectes au contact ; au pire, ils font perdre des semaines pendant lesquelles les punaises se multiplient et se dispersent. L'alcool à brûler est en plus inflammable : ne le pulvérisez jamais sur une literie.</p>
<h2>Ce qui marche vraiment</h2>
<p>L'Anses recommande de combiner des méthodes mécaniques et thermiques, ciblées et proportionnées à l'infestation :</p>
<ol>
<li><strong>Désencombrer et aspirer</strong> soigneusement toutes les surfaces, coutures du matelas et plinthes comprises, puis fermer le sac et le jeter dans un sac poubelle fermé à l'extérieur.</li>
<li><strong>Laver le linge à plus de 55 °C</strong> (60 °C en pratique) ou le passer au sèche-linge chaud.</li>
<li><strong>Congeler</strong> ce qui ne se lave pas : au moins 72 heures à -18 °C ou moins, dans un sac fermé.</li>
<li><strong>Passer la vapeur sèche</strong> à 120 °C ou plus sur le matelas, le sommier, le canapé et les fentes. Notre guide <a href="/vapeur-seche-punaises-de-lit.html">vapeur sèche</a> explique la bonne technique.</li>
<li><strong>Faire appel à un professionnel</strong> si l'infestation persiste malgré ces gestes, plutôt que d'enchaîner les produits du commerce.</li>
</ol>
<p>Selon l'Anses, environ deux tiers des personnes infestées se débarrassent des punaises en moins de deux mois. Pour le calendrier détaillé, voir <a href="/combien-de-temps-se-debarrasser-punaises-de-lit.html">combien de temps pour s'en débarrasser</a> ; pour les premiers gestes, <a href="/que-faire-punaises-de-lit.html">que faire en attendant le professionnel</a> ; et pour le budget, <a href="/prix-traitement-punaises-de-lit-toulouse.html">les prix d'un traitement à Toulouse</a>.</p>
<p class="note">Sources consultées le 23 octobre 2026 : Anses, « Les punaises de lit en 13 questions » (octobre 2023) ; Anses, communiqué sur les intoxications liées aux insecticides contre les punaises de lit, repris par VIDAL (février 2023) ; Anses, rapport de toxicovigilance « Expositions au produit SNIPER 1000 EC DDVP » (octobre 2023) ; S. C. Jones et J. L. Bryant, « Ineffectiveness of Over-the-Counter Total-Release Foggers Against the Bed Bug », <em>Journal of Economic Entomology</em> (2012) ; J. Goddard, « Long-Term Efficacy of Various Natural or Green Insecticides against Bed Bugs: A Double-Blind Study », <em>Insects</em> (2014) ; N. Singh, C. Wang et R. Cooper, « Potential of Essential Oil-Based Pesticides and Detergents for Bed Bug Control », <em>Journal of Economic Entomology</em> (2014) ; INRS, « Silice cristalline ». Ce guide ne remplace pas l'avis d'un professionnel de la désinsectisation ou de santé.</p>''',
faq=[("La terre de diatomée tue-t-elle les punaises de lit ?","Oui, mais lentement et partiellement. L'Anses reconnaît une bonne efficacité aux produits autorisés à base de terre de diatomée, qui dessèchent l'insecte. Il faut souvent plusieurs jours, et les résultats varient beaucoup selon les produits. Elle ne s'utilise qu'en fine couche, en complément de l'aspiration, du lavage et de la vapeur."),
("La terre de diatomée est-elle dangereuse ?","Sa poussière irrite les voies respiratoires. L'Anses recommande de n'utiliser que des produits disposant d'une autorisation de mise sur le marché et de suivre leur mode d'emploi. Évitez la terre de diatomée calcinée, vendue notamment pour les piscines, qui peut contenir beaucoup de silice cristalline."),
("Les bombes insecticides sont-elles efficaces contre les punaises de lit ?","Non, en général. Une étude de l'université d'État de l'Ohio (2012) a montré que trois diffuseurs du commerce n'avaient que peu ou pas d'effet : le produit n'atteint pas les cachettes et beaucoup de punaises sont résistantes. Ces produits exposent en plus à des intoxications."),
("Les huiles essentielles font-elles fuir les punaises de lit ?","Non. Dans une étude de l'université Rutgers (2014), la plupart des produits à base d'huiles essentielles ne tuaient que 0 à 30 % des punaises pulvérisées directement, et aucun effet répulsif n'a été mesuré."),
("Le Sniper 1000 est-il autorisé en France ?","Non. Le Sniper 1000 contient du dichlorvos, interdit en France depuis 2013. L'Anses a recensé 206 personnes exposées et trois décès entre 2018 et mi-2023. N'utilisez jamais ce type de produit acheté sur un marché, à l'étranger ou en ligne.")],
date='2026-10-23')

print('ok')
