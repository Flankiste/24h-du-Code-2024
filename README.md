# Participations aux 24h du code 2024
## Présentation
Ce dépôt contient notre participations aux 24h du code en Avril 2024. Nous avons choisi de paticiper au sujet de l'association HAUM où nous devions réaliser plusieurs tâches :
- Créer un système de navigation dans un espace 3D avec des contraintes paticulières
- Créer ces espaces 3D à partir d'exemple de carte déjà générées. 


## Membres
Notre groupe est composé de 5 membres, principalement des étudiants en informatique dans l'école d'ingénieur CESI ainsi que d'un élève en BUT GEII à l'IUT de Nantes.s
- [Samuel Deschamps](https://github.com/Sunslihgt) - Étudiant au CESI, campus de Saint-Nazaire
- [Adélie Castel](https://github.com/casteladelie) - Étudiante au CESI, campus de Saint-Nazaire
- [Raphaël Maestri](https://github.com/Flankiste) - Étudiant au CESI, campus du Mans
- [Killian Hubault](https://github.com/Eclipes2) - Étudiant au CESI, campus de Saint-Nazaire
- [Arthur Nogues](https://github.com/ArkeoNo) - Étudiant à l'IUT de Nantes, département GEII.

## Déroulement du concours 
Le concours a eu lieu du 6 Avril 2024 à 10h au 7 Avril 2024 à 10h. Nous étions dans la chambre de commerce du Mans avec le reste des équipes participantes. Après une rapide présentation des sujets, nous avons choisi de participer au sujet de l'association HAUM.
Durant l'épreuve, notre travail à été évalué à plusieurs reprises via le moyen de session où chaque équipe publiait des cartes à résoudre sur un serveur dédié. Chacune des équipes devait ensuite soummettre une solution pour chaque carte. 
Au total il y a eu 3 sessions d'évaluation, leur poids dans le résultat final augmentant à chaque fois.

## Réalisation 

### Système de navigation
Sources : `mouvement.py` `map.py` `mouvements.py` `chemin_bfs.py`

La majeure partie du projet porte sur la création d'un système de navigation dans un espace 3D avec les contraintes particulière citée plus haut.
Les premières carte fournies étant relativement vide, nous avons commencé par créer un système de navigation simple en implémentant un algorithme de recherche de chemin basé sur le parcours en largeur (BFS). Toutes les zones avec un effet particulier étaient considérées comme des obstacles.
Au fur et à mesure des sessions, nous avons ajouté des fonctionnalités supplémentaires comme la prise en compte des effets des zones, le passage de portes, etc.
Avec plus de temps, nous aurions pu finir d'ajouter la navigation en diagonale. Les essais que nous avons pu faire n'étaient pas concluants et nous avons préféré ne pas les intégrer à notre solution.

### Génération de carte
Sources : `map_creation.py`

Des exemples de cartes nous étant fournis, la première étape a été de comprendre comment elles étaient générées. Nous avons donc analysé les fichiers de carte pour comprendre leur structure et les données qu'ils contenaient.

Nous avons ensuite créé un programme python permettant de générer des cartes aléatoires. Ce programme permet de générer des cartes de différentes tailles, avec des obstacles et des zones de départ et d'arrivée aléatoires. Il est possible de spécifier le nombre d'obstacle, la taille de la carte, etc.

## Résultats

Malgré une première session d'évaluation difficile, nous avons réussi à nous améliorer et à obtenir des résultats satisfaisants lors des sessions suivantes
Au bout de 24h éprouvantes, nous avons réussi à créer un système de navigation fonctionnel et à générer des cartes aléatoires.
Nous avons terminé 1er sur la dizaine d'équipe particpantes (équipe étudiante et professionnelle confondue).


## Remerciements
Nous remercions l'association HAUM pour la proposition de sujet ainsi que les organisateurs des 24h du code. Nous remercions également les autres équipes participantes pour leur fair-play et leur bonne humeur tout au long de l'épreuve.

## Liens
- [Site des 24h du code](https://les24hducode.fr/)
- [Site de l'association HAUM](https://haum.org/)
- [Article du CESI sur la compétition](https://le-mans.cesi.fr/fr/actualites/24h-du-code-2024/#:~:text=Les%2024%20heures%20du%20code,projets%20individuels%20ou%20en%20%C3%A9quipe.)