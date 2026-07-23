\## 2026-07-23 - Tâche 2.1



\### Objectif



Télécharger le dataset Online Retail depuis UCI et le sauvegarder localement.



\### Ce que j'ai appris



J'ai appris à utiliser `ucimlrepo` pour récupérer un dataset depuis le UCI Machine Learning Repository. J'ai aussi appris qu'un dataset brut doit être sauvegardé dans `data/raw/`.



\### Ce que j'ai codé



J'ai créé le script `src/data/download\_online\_retail.py`. Ce script télécharge le dataset Online Retail avec `fetch\_ucirepo(id=352)` puis le sauvegarde dans `data/raw/online\_retail\_raw.csv`.



\### Erreurs rencontrées



Aucune erreur bloquante pour l'instant.



\### Solution



Le fichier CSV est ignoré par Git grâce à `.gitignore`, car les datasets volumineux ne doivent pas forcément être versionnés.



\### Prochaine étape



Valider la tâche 2.1 avant de passer à la tâche 2.2.

