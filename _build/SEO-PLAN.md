# Plan SEO automatisé : punaises-de-lit-toulouse.fr

Propriétaire : Maxime Gaillard (Tada House). Exécuté par Claude via une tâche planifiée (lundi et jeudi matin).
Dossier `_build/` : non publié (Jekyll ignore les dossiers commençant par `_`).

## Règles non négociables
- Français, aucun tiret cadratin (—) dans les textes.
- Contenu utile, unique, vérifié. Chaque chiffre vient d'une source publique consultée pendant la séance. Jamais d'avis, témoignages, notes ou partenaires inventés.
- Pas de pages villes copiées-collées : une page commune n'est créée que si elle contient des informations propres à la commune (parc de logements, étudiants, transports, sources locales).
- Ne jamais toucher aux DNS email (MX, SPF, DKIM) ni au formulaire sans nécessité.
- Pas de fiche Google Business Profile (interdit pour un service de mise en relation).
- Emails à des tiers (prospection d'artisans, demandes de liens, partenaires) : Claude les envoie lui-même depuis le webmail Zimbra OVH (expéditeur Tada House <contact@tadahouse.com>), jamais depuis le connecteur Gmail. Messages courts et professionnels, aucun engagement de prix ou de contrat sans Maxime (proposer un appel avec lui).
## Méthode d'une séance
1. `git clone --depth 1 https://github.com/maxime93130/punaises-de-lit-toulouse.git site && cd site`
2. Lire ce fichier et le journal en bas. Prendre la prochaine tâche « À faire » de la file.
3. Rechercher (WebSearch / WebFetch) : SERP du mot-clé visé, pages concurrentes, sources officielles.
4. Écrire la page avec `_build/gen_guides.py` (ajouter un appel `guide(...)` avec `date='AAAA-MM-JJ'` et l'entrée dans `GUIDES`), copier les scripts à la racine, lancer `python3 gen_guides.py` (gen_pages.py seulement si une page légale change : il réécrit merci, 404, mentions, confidentialité), mettre à jour `sitemap.xml`, et ajouter la carte dans la section `#guides` de index.html si c'est un guide majeur.
5. Vérifier : pas de « — », liens internes OK, rendu mobile (Playwright), JSON-LD valide.
6. Publier : Chrome > https://github.com/maxime93130/punaises-de-lit-toulouse/upload/main (sous-dossiers : /upload/main/<dossier>), file_upload des fichiers modifiés depuis le clone local, cliquer « Commit changes » par coordonnées (le clic par ref échoue parfois), vérifier le commit dans /commits/main. Retirer gen_*.py de la racine (ne pas les uploader à la racine).
7. Mettre à jour ce fichier (statut + journal) et l'uploader dans `/upload/main/_build`.
8. Contrôle : recherche `site:punaises-de-lit-toulouse.fr` et position sur les mots-clés suivis ; Search Console si accessible.
9. Résumé court envoyé à Maxime (3 à 5 lignes).

## File de tâches (dans l'ordre)
- [ ] PRIORITÉ tant qu'aucun partenaire n'est signé : à chaque séance, lire les réponses des artisans (Gmail libellé Tada House) et y répondre depuis Zimbra ; email uniquement, pas d'appels (choix de Maxime du 01/10). Relance n°2 le jeudi 8 octobre (NON ENVOYÉE le 08/10 : session Zimbra expirée ; à envoyer dès la reconnexion de Maxime) aux prospects sans réponse (Dardard, Cimex Protect, Eco-Flair, Artémis, Sniper Pest Control 3D, Nuisible France Solution, Fair Sans Tox, Cynolfaction), puis arrêt. Si une demande de particulier arrive sans partenaire : la transmettre gratuitement à 1 ou 2 entreprises certifiées (« lead d'essai offert ») et prévenir Maxime (décision du 01/10).
- [ ] Prospection : trouver une adresse email valide pour SOS Nuisible Toulouse 31 (contact@sosnuisible31.fr rejetée) et HL Nuisible (contact@hlnuisible.fr rejetée) ; élargir la liste à d'autres indépendants certifiés de la métropole.
  - Recherche faite le 2026-10-05, ENVOIS À FAIRE (Zimbra expiré ce jour) avec le 1er email « nouvelle version » (compliment précis, lien /partenaires.html, « répondez oui ») :
    - Nuisible Occitanie (Steve Charpentier, EI, 1 rue du Treich 31500 Toulouse, Certibiocide affiché) : nuisible.occitanie@gmail.com (source : nuisibleoccitanie.com/mentions-legales).
    - Access Prevention (45 chemin des Maraîchers 31400 Toulouse, Certibiocide + Certipunaise affichés, 7j/7) : contact@accessprevention.fr.
    - HL Nuisible + (Castelmaurou, 07 89 74 24 32) : aucun email publié, passer par le formulaire hlnuisible.fr/contact.
    - SOS Nuisible Toulouse 31 : seule adresse publiée = celle rejetée ; passer par le formulaire de devis du site (sosnuisible31.fr/devis-eradication-des-nuisibles-a-toulouse-et-dans-le-31/).
    - À vérifier avant envoi (certification non affichée) : Stop Nuisibles 31 (Bruno Granier, EI, Toulouse 31300), stopnuisibles31@gmail.com.
    - Écartés : Bortolin Antinuisible (pas de zone Toulouse), réseaux nationaux (Cleanolia, Adrep, AS DE PIC).
- [ ] Visuels : chaque email de prospection renvoie vers /partenaires.html (vidéo de 10 s faite à partir de vraies captures du site, aucune image générée). Mettre à jour la vidéo si le site change (méthode : captures Playwright avec polices de marque, montage HTML image par image, ffmpeg, voir _build/gen_partenaires.py).
- [x] Search Console : ajouter la propriété de domaine avec le compte Google de Chrome (maxime@musokastudio.com), vérification par enregistrement TXT dans la zone DNS OVH de punaises-de-lit-toulouse.fr (ajouter uniquement le TXT), envoyer sitemap.xml, demander l'indexation des 6 pages. Puis Bing Webmaster Tools par import depuis Search Console.
  - Fait le 2026-10-01 : propriété préfixe d'URL https://punaises-de-lit-toulouse.fr/ vérifiée par fichier HTML (google442049fc25e1276f.html à la racine, NE PAS SUPPRIMER), sitemap envoyé, indexation demandée pour les 6 pages. Propriété de domaine créée mais non vérifiée (session OVH expirée) : TXT à ajouter si Maxime se reconnecte : google-site-verification=oKil_8upzTKsjL2eH9qUKFsf9eKvbwNDBXjXi8Ijkpo
- [ ] (Maxime) Bing Webmaster Tools : se connecter avec le compte Google puis « Importer depuis Google Search Console » (création de compte et autorisation OAuth à faire par Maxime).
- [x] Guide : punaises de lit et étudiants à Toulouse (résidences, colocations, que faire, qui paie). Toulouse est une grande ville étudiante.
- [x] Guide : combien de temps pour se débarrasser des punaises de lit. (publié le 2026-10-05)
- [x] Guide : faut-il jeter son matelas ? (housse anti-punaises, traitement, dépôt en déchetterie) (publié le 2026-10-08)
- [ ] Guide : traitement à la vapeur sèche (principe, limites, prix).
- [ ] Guide : punaises de lit au retour de voyage ou d'hôtel (prévention, valises).
- [ ] Guide : piqûres de punaises de lit (reconnaître, soulager, quand consulter), prudence médicale, renvoyer vers médecin/pharmacien.
- [ ] Guide : terre de diatomée, insecticides, remèdes maison : ce qui marche et ce qui ne marche pas.
- [ ] Guide : punaises de lit en copropriété, rôle du syndic.
- [ ] Page communes : Blagnac (si données locales suffisantes).
- [ ] Page communes : Colomiers.
- [ ] Page communes : Tournefeuille.
- [ ] Page communes : Balma, L'Union, Ramonville (une page chacune si données).
- [ ] Liens entrants : liste de 15 à 20 annuaires et sites locaux pertinents (associations de locataires, blogs toulousains, annuaires de services) + envoi des demandes depuis Zimbra (contact@tadahouse.com).
- [ ] Mise à jour trimestrielle des prix (vérifier les sources, mettre à jour dates et chiffres).

## Mots-clés suivis
punaise de lit toulouse (320/mois, difficulté 11) ; punaises de lit étudiant toulouse / crous ; traitement punaise de lit toulouse ; prix traitement punaises de lit toulouse ; chien détecteur punaises de lit toulouse ; punaises de lit locataire propriétaire.

## Journal
- 2026-09-28 : mise en ligne du site + 5 guides (prix, détection canine, reconnaître, que faire, locataire/propriétaire). HTTPS en attente d'émission du certificat.
- 2026-10-01 : Search Console configurée (préfixe d'URL, vérif. fichier HTML car session OVH expirée), sitemap envoyé, indexation demandée (accueil + 5 guides). Guide « étudiants à Toulouse » publié (Crous, studio, colocation, ADIL 31 ; sources : règlement intérieur Crous Toulouse 2025-26, Université de Toulouse fév. 2025). Correctif CSS : marges latérales manquantes sur mobile pour toutes les pages guides. Gmail : aucune réponse d'artisan, aucune demande de particulier (2 rebonds d'emails du 28/09, dont contact@hlnuisible.fr invalide). Indexation : site non encore indexé (normal, 3 jours).
- 2026-10-01 (après-midi) : page /partenaires.html (noindex) + vidéo de présentation 10 s (media/). Relances envoyées depuis Zimbra à 6 prospects (CTA « répondez oui », plus de demande d'appel) ; SOS Nuisible rejeté (adresse inexistante, déjà le cas le 28/09). Premiers emails envoyés à Fair Sans Tox et Cynolfaction (détection canine seule).
- 2026-10-05 : guide « combien de temps pour se débarrasser des punaises de lit » publié (2 à 3 passages à 15 jours, surveillance 1 à 2 mois ; sources : rapport CNEV 2015 publié par l'Anses, stop-punaises.gouv.fr, Santé Canada, DGCCRF), carte ajoutée sur l'accueil, sitemap mis à jour. Gmail : aucune réponse d'artisan, aucune demande de particulier. Prospection : 2 nouveaux indépendants certifiés trouvés + voie formulaire pour HL Nuisible et SOS Nuisible, mais session Zimbra expirée : envois reportés (Maxime doit se reconnecter).
- 2026-10-08 : guide « faut-il jeter son matelas » publié (traiter plutôt que jeter, housse intégrale 1 an avec fermeture scotchée, méthode pour jeter : emballer, rendre inutilisable, déchèterie, encombrants Toulouse Métropole, reprise 1 pour 1 ; sources : stop-punaises.gouv.fr, ARS Île-de-France 2019, Ville et Eurométropole de Strasbourg / ARS Grand Est, Santé Canada, CNEV 2015, Que Choisir 2022), carte accueil + sitemap. Gmail : aucune réponse d'artisan, aucune demande de particulier. Session Zimbra expirée : relance n°2 et nouveaux envois de prospection bloqués (Maxime doit se reconnecter). Note : la page officielle encombrants de Toulouse Métropole bloque les robots, conditions non citées en détail.
