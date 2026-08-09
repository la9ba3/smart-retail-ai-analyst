# Méthodologie RFM

## Définition

La méthode RFM est une méthode de segmentation client basée sur trois dimensions :

- `Recency` : depuis combien de temps le client n'a pas acheté ;
- `Frequency` : combien de commandes le client a passées ;
- `Monetary` : combien le client a dépensé au total.

## Recency

La récence mesure le nombre de jours depuis le dernier achat du client.

Une récence faible signifie que le client a acheté récemment.

Exemple :
- 5 jours depuis le dernier achat : client récent ;
- 250 jours depuis le dernier achat : client inactif ou à risque.

## Frequency

La fréquence mesure le nombre de factures différentes associées au client.

Une fréquence élevée signifie que le client commande souvent.

Exemple :
- 1 commande : client occasionnel ;
- 20 commandes : client fidèle.

## Monetary

Le montant mesure la somme totale dépensée par le client.

Un montant élevé indique un client à forte valeur.

Exemple :
- 50 euros dépensés : faible valeur ;
- 5 000 euros dépensés : forte valeur.

## Scoring

Dans ce projet, chaque dimension RFM reçoit un score de 1 à 5.

Pour `Frequency` et `Monetary` :
- 1 signifie faible ;
- 5 signifie fort.

Pour `Recency`, le score est inversé :
- un client très récent reçoit un score élevé ;
- un client ancien reçoit un score faible.

## Interprétation

Un client avec de bons scores sur les trois dimensions est généralement un client très important.

Exemple :
- `R=5`, `F=5`, `M=5` : client champion ;
- `R=1`, `F=1`, `M=1` : client perdu ou très peu actif.

## Utilisation Métier

Le scoring RFM permet de :
- identifier les clients fidèles ;
- repérer les clients à risque ;
- prioriser les campagnes marketing ;
- personnaliser les offres ;
- améliorer la fidélisation client.

## Limites

Le RFM ne prend pas en compte :
- les préférences produits ;
- les marges ;
- les retours détaillés ;
- les canaux d'achat ;
- les données démographiques.

Il doit donc être vu comme une base simple, explicable et utile, mais pas comme une segmentation complète à lui seul.