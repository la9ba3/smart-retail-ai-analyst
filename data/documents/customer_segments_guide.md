# Guide Des Segments Clients

## Objectif

Ce document explique les principaux segments clients utilisés dans le projet Smart Retail AI Analyst.

Les segments sont basés sur le scoring RFM et sur la segmentation KMeans.

## Champions

Les clients Champions sont les meilleurs clients.

Ils ont généralement :
- une récence faible ;
- une fréquence élevée ;
- un montant dépensé élevé.

Interprétation :
- ils ont acheté récemment ;
- ils achètent souvent ;
- ils génèrent beaucoup de chiffre d'affaires.

Actions recommandées :
- avantages VIP ;
- offres exclusives ;
- service prioritaire ;
- accès anticipé à certains produits ;
- communication personnalisée.

## Loyal Customers

Les clients fidèles achètent régulièrement.

Ils ont souvent :
- une bonne récence ;
- une bonne fréquence ;
- un montant moyen ou élevé.

Actions recommandées :
- programme de fidélité ;
- recommandations personnalisées ;
- offres de montée en gamme ;
- campagnes de réachat.

## Potential Customers

Les clients potentiels ont un comportement intéressant mais pas encore totalement fidèle.

Ils peuvent être :
- récents mais peu fréquents ;
- nouveaux clients ;
- clients avec montant moyen mais fréquence faible.

Actions recommandées :
- offres de bienvenue ;
- recommandations produits ;
- bundles ;
- incitations au deuxième achat.

## At Risk

Les clients à risque ont déjà montré de l'intérêt, mais ils ne sont plus très récents.

Ils peuvent avoir :
- une fréquence correcte ;
- un historique d'achat intéressant ;
- une récence faible en score, donc un dernier achat ancien.

Actions recommandées :
- campagne de réactivation ;
- email personnalisé ;
- offre limitée dans le temps ;
- enquête de satisfaction.

## Lost Customers

Les clients perdus sont peu actifs ou inactifs depuis longtemps.

Ils ont souvent :
- une récence élevée ;
- une fréquence faible ;
- un montant faible.

Actions recommandées :
- campagne de retour à faible coût ;
- coupon de réactivation ;
- message simple ;
- éviter de dépenser trop de budget marketing sur ce segment.

## Segments KMeans

KMeans crée des groupes automatiquement à partir des variables :
- `recency` ;
- `frequency` ;
- `monetary`.

Les numéros de clusters n'ont pas de signification directe.

Il faut les interpréter avec :
- la récence moyenne ;
- la fréquence moyenne ;
- le montant moyen ;
- le nombre de clients.

## Priorité Marketing

Une stratégie simple peut être :
1. protéger les clients Champions ;
2. développer les clients fidèles ;
3. convertir les clients potentiels ;
4. réactiver les clients à risque ;
5. traiter les clients perdus avec prudence.