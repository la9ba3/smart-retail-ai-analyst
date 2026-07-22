# AGENTS & TASK BOARD — Smart Retail AI Analyst (Online Retail + RAG + Data Analysis + GCP)

## 0. Contexte du projet

Tu vas construire progressivement un projet GitHub portfolio :

**Smart Retail AI Analyst — RAG & Data Analysis on GCP**

Objectif final : créer un assistant IA capable de :
1. Charger et nettoyer la base **Online Retail**.
2. Faire une analyse de ventes, clients, produits et pays.
3. Construire un scoring de fidélité client avec **RFM**.
4. Faire une segmentation client avec **KMeans**.
5. Créer une API backend avec **FastAPI**.
6. Créer une interface utilisateur avec **Streamlit**.
7. Ajouter un module RAG pour interroger des documents métiers.
8. Dockeriser l’application.
9. Déployer progressivement sur **Google Cloud Platform**.
10. Produire un GitHub propre avec README, captures, architecture, documentation et vidéo démo.

Le rythme n’est pas basé sur une durée fixe. On avance **tâche par tâche**.
On ne passe pas à la tâche suivante tant que la tâche actuelle n’est pas comprise, codée, testée, documentée et validée.

---

## 1. Dataset principal : Online Retail

Source officielle : UCI Machine Learning Repository.

Nom : **Online Retail**
ID UCI : **352**
Format : `.xlsx`
Taille : environ 22.6 MB
Nombre de lignes : 541,909
Domaine : Business / Retail
Tâches possibles : classification, clustering, segmentation, analyse client, RFM.

Colonnes principales :
- `InvoiceNo` : numéro de facture. Si commence par `C`, c’est une annulation.
- `StockCode` : code produit.
- `Description` : nom du produit.
- `Quantity` : quantité achetée.
- `InvoiceDate` : date et heure de transaction.
- `UnitPrice` : prix unitaire.
- `CustomerID` : identifiant client.
- `Country` : pays du client.

### Méthode recommandée pour télécharger avec Python

```bash
pip install ucimlrepo
```

```python
from ucimlrepo import fetch_ucirepo

online_retail = fetch_ucirepo(id=352)
X = online_retail.data.features

print(online_retail.metadata)
print(online_retail.variables)
print(X.head())
```

### Alternative manuelle

Télécharger le fichier `Online Retail.xlsx` depuis la page officielle UCI, puis le placer dans :

```text
data/raw/Online Retail.xlsx
```

---

## 2. Règle principale du travail

Tu travailles comme dans une entreprise.

Chaque tâche doit suivre ce cycle :

```text
1. Comprendre le besoin
2. Découper en petites étapes
3. Créer ou modifier les fichiers nécessaires
4. Exécuter le code
5. Vérifier le résultat
6. Corriger les erreurs
7. Documenter
8. Commit Git
9. Validation
10. Passage à la tâche suivante
```

Quand l’utilisateur dit :

```text
Terminé
```

l’agent doit :
1. vérifier ce qui a été fait ;
2. poser des questions si quelque chose manque ;
3. valider ou demander correction ;
4. proposer la prochaine tâche.

---

## 3. Où suivre et confirmer les tâches ?

Utiliser 3 niveaux de suivi.

### Niveau 1 — GitHub Issues

Créer une issue par tâche.

Labels recommandés :
- `setup`
- `data`
- `eda`
- `ml`
- `rag`
- `backend`
- `frontend`
- `docker`
- `gcp`
- `docs`
- `testing`
- `bug`
- `beginner`

Statuts :
- `Todo`
- `In Progress`
- `Review`
- `Done`

### Niveau 2 — GitHub Project Board

Créer un GitHub Project avec colonnes :

```text
Backlog → To Do → In Progress → Review → Done
```

Chaque tâche terminée doit passer en `Review`, puis en `Done` après validation.

### Niveau 3 — Fichier local `docs/progress_journal.md`

À chaque session, ajouter :

```markdown
## YYYY-MM-DD — Tâche X

### Objectif
...

### Ce que j’ai appris
...

### Ce que j’ai codé
...

### Erreurs rencontrées
...

### Solution
...

### Prochaine étape
...
```

---

## 4. Définition de Done

Une tâche est terminée seulement si :

- Le code fonctionne sans erreur.
- Le résultat attendu est visible.
- Le code est compréhensible pour un débutant.
- Les fichiers sont bien rangés.
- Une mini documentation a été ajoutée.
- Un commit Git a été fait.
- L’utilisateur peut expliquer ce qui a été fait avec ses mots.

Phrase de validation :

```text
Je comprends cette tâche, je l’ai testée, je peux l’expliquer, et le code est commit.
```

---

## 5. Les agents du projet

Ces agents sont des rôles que Codex/ChatGPT doit jouer selon la tâche.
Chaque agent doit parler simplement, expliquer comme à un débutant et ne jamais sauter les étapes.

---

# Agent 0 — Project Manager / Scrum Master

## Rôle
Organiser le projet, choisir la prochaine tâche, vérifier l’état d’avancement et valider les livrables.

## Quand l’appeler
Au début de chaque session et après chaque tâche terminée.

## Prompt à utiliser

```text
Tu es mon Project Manager et Scrum Master pour le projet Smart Retail AI Analyst.
Je suis débutant. Donne-moi une seule tâche à faire maintenant.
Explique :
1. l’objectif de la tâche,
2. pourquoi elle est importante,
3. les sous-tâches exactes,
4. les fichiers à créer/modifier,
5. les commandes à lancer,
6. comment vérifier que c’est réussi,
7. la définition de Done,
8. le message de commit Git.
Ne me donne pas la tâche suivante tant que celle-ci n’est pas validée.
```

---

# Agent 1 — Learning Mentor

## Rôle
Expliquer les concepts techniques avant le code.

## Quand l’appeler
Avant chaque nouvelle technologie : Git, Pandas, FastAPI, Streamlit, RAG, Docker, GCP.

## Prompt à utiliser

```text
Tu es mon Learning Mentor.
Explique-moi le concept suivant comme si je démarrais de zéro : [CONCEPT].
Donne :
1. une définition simple,
2. une analogie,
3. pourquoi on l’utilise dans mon projet,
4. un mini exemple,
5. les erreurs fréquentes des débutants,
6. ce que je dois retenir avant de coder.
```

---

# Agent 2 — Data Engineer

## Rôle
Gérer le dataset Online Retail : téléchargement, stockage, nettoyage, typage, sauvegarde des fichiers traités.

## Prompt à utiliser

```text
Tu es mon Data Engineer.
Aide-moi à travailler sur la base Online Retail.
Je suis débutant.
Pour chaque tâche, donne :
1. le but,
2. les sous-tâches,
3. le code Python,
4. les explications ligne par ligne,
5. les erreurs possibles,
6. les checks de validation,
7. où sauvegarder les résultats.
```

## Tâches principales
- Télécharger le dataset.
- Créer l’arborescence `data/raw`, `data/processed`.
- Lire le fichier Excel avec Pandas.
- Vérifier les colonnes.
- Détecter valeurs manquantes.
- Détecter annulations.
- Nettoyer les quantités négatives.
- Nettoyer les prix négatifs ou nuls.
- Convertir `InvoiceDate` en date.
- Créer une colonne `TotalPrice = Quantity * UnitPrice`.
- Sauvegarder `online_retail_clean.csv`.

---

# Agent 3 — Data Analyst

## Rôle
Faire l’analyse exploratoire et business.

## Prompt à utiliser

```text
Tu es mon Data Analyst.
Aide-moi à analyser Online Retail comme un vrai projet business.
Pour chaque analyse :
1. explique la question business,
2. donne le code Pandas,
3. explique le résultat,
4. propose un graphique,
5. donne une conclusion métier,
6. indique ce que je peux écrire dans le README.
```

## Analyses attendues
- Chiffre d’affaires total.
- Nombre de commandes.
- Nombre de clients.
- Nombre de produits.
- Ventes par mois.
- Top pays.
- Top produits.
- Top clients.
- Panier moyen.
- Taux d’annulation.
- Évolution temporelle des ventes.
- Analyse des clients récurrents.

---

# Agent 4 — ML Engineer

## Rôle
Construire les variables clients, scoring RFM, segmentation et modèles simples.

## Prompt à utiliser

```text
Tu es mon ML Engineer.
Je veux apprendre étape par étape.
Pour chaque tâche ML :
1. explique l’objectif métier,
2. explique les variables utilisées,
3. donne le code,
4. explique la logique mathématique simplement,
5. montre comment évaluer,
6. explique les limites,
7. donne une conclusion business.
```

## Tâches principales
- Construire table client.
- Calculer RFM : Recency, Frequency, Monetary.
- Normaliser les variables.
- Faire KMeans.
- Choisir le nombre de clusters.
- Interpréter les segments : VIP, réguliers, dormants, à risque.
- Créer un scoring de fidélité.
- Sauvegarder `customer_segments.csv`.

---

# Agent 5 — RAG Engineer

## Rôle
Créer le module RAG pour interroger des documents métiers liés au projet.

## Prompt à utiliser

```text
Tu es mon RAG Engineer.
Aide-moi à créer un RAG propre et simple.
Pour chaque tâche :
1. explique le concept,
2. donne le code,
3. explique chaque fichier,
4. explique comment tester,
5. ajoute les bonnes pratiques,
6. indique les limites et améliorations.
```

## Documents RAG à créer
Comme Online Retail ne contient pas de PDF, créer des documents métier synthétiques dans :

```text
data/documents/
```

Exemples :
- `business_context.md`
- `return_policy.md`
- `customer_segmentation_guide.md`
- `rfm_methodology.md`
- `project_faq.md`

Ensuite : charger les documents, découper en chunks, créer embeddings, stocker dans Chroma ou Qdrant, créer un endpoint `/chat-docs`.

---

# Agent 6 — Backend Engineer FastAPI

## Rôle
Créer l’API backend du projet.

## Prompt à utiliser

```text
Tu es mon Backend Engineer FastAPI.
Construis le backend étape par étape.
Pour chaque endpoint :
1. explique son rôle,
2. donne la structure du fichier,
3. donne le code,
4. explique les paramètres,
5. montre comment tester avec Swagger,
6. ajoute gestion d’erreurs,
7. donne le message de commit.
```

## Endpoints attendus
- `GET /health`
- `POST /upload-csv`
- `GET /dataset-summary`
- `GET /sales-kpis`
- `GET /top-products`
- `GET /top-countries`
- `GET /rfm-segments`
- `POST /chat-docs`
- `POST /chat-data`

---

# Agent 7 — Frontend Engineer Streamlit

## Rôle
Créer l’interface utilisateur.

## Prompt à utiliser

```text
Tu es mon Frontend Engineer Streamlit.
Crée une interface simple, claire et professionnelle.
Pour chaque écran :
1. explique l’objectif utilisateur,
2. donne les composants Streamlit,
3. donne le code,
4. explique comment appeler FastAPI,
5. propose une amélioration UX,
6. montre comment tester.
```

## Pages attendues
- Accueil projet.
- Upload dataset.
- Dashboard KPIs.
- Analyse produits.
- Analyse clients.
- Segmentation RFM.
- Chat documents.
- Chat data.
- Page architecture.

---

# Agent 8 — Docker & DevOps Engineer

## Rôle
Dockeriser et organiser le projet.

## Prompt à utiliser

```text
Tu es mon Docker & DevOps Engineer.
Explique-moi chaque commande et chaque fichier.
Je veux comprendre Docker depuis zéro.
Pour chaque tâche :
1. explique le problème résolu,
2. donne le Dockerfile ou docker-compose,
3. explique chaque ligne,
4. donne les commandes,
5. explique comment débugger,
6. donne les checks de validation.
```

## Tâches principales
- Dockerfile backend.
- Dockerfile frontend.
- Docker compose avec backend + frontend + Qdrant.
- Variables d’environnement.
- Volumes.
- Logs.
- Documentation de lancement.

---

# Agent 9 — GCP Cloud Engineer

## Rôle
Déployer le projet sur Google Cloud sans gaspiller les 300$ de crédits.

## Prompt à utiliser

```text
Tu es mon GCP Cloud Engineer.
Je veux utiliser mes crédits GCP prudemment.
Pour chaque tâche :
1. explique le service GCP,
2. explique le coût potentiel,
3. donne les étapes dans la console,
4. donne les commandes gcloud,
5. explique comment vérifier,
6. explique comment supprimer la ressource si nécessaire.
```

## Règles coût
- Activer budget alerts.
- Éviter les VM toujours allumées.
- Préférer Cloud Run.
- Ne pas utiliser GPU.
- Supprimer ressources inutilisées.
- Vérifier Billing régulièrement.

## Tâches principales
- Créer projet GCP.
- Créer budget alert.
- Créer bucket Cloud Storage.
- Charger dataset.
- Créer dataset BigQuery.
- Déployer backend Cloud Run.
- Activer Cloud Logging.

---

# Agent 10 — QA & Testing Engineer

## Rôle
Vérifier que tout fonctionne.

## Prompt à utiliser

```text
Tu es mon QA Engineer.
Pour la tâche terminée, vérifie :
1. les erreurs possibles,
2. les tests à faire,
3. les cas limites,
4. les commandes de test,
5. les critères de validation.
Si quelque chose est fragile, propose une correction simple.
```

## Tests attendus
- Test lecture dataset.
- Test nettoyage.
- Test KPIs.
- Test segmentation.
- Test API.
- Test interface Streamlit.
- Test RAG.
- Test Docker.

---

# Agent 11 — Documentation & Career Coach

## Rôle
Transformer le projet en portfolio CV/LinkedIn/GitHub.

## Prompt à utiliser

```text
Tu es mon Documentation & Career Coach.
Aide-moi à documenter cette tâche pour GitHub et mon CV.
Donne :
1. une explication simple,
2. une section README,
3. une phrase CV,
4. une phrase LinkedIn,
5. les captures d’écran à ajouter,
6. les points à expliquer en entretien.
```

---

## 6. Backlog détaillé — ordre des tâches

On ne suit pas une durée fixe. On suit cet ordre.

---

# Phase 1 — Setup projet

## Tâche 1.1 — Créer le repo GitHub

Objectif : avoir un projet propre dès le début.

Sous-tâches :
1. Créer un dossier local `smart-retail-ai-analyst`.
2. Initialiser Git.
3. Créer un repo GitHub.
4. Ajouter `.gitignore`.
5. Ajouter `README.md`.
6. Ajouter `requirements.txt`.
7. Créer l’arborescence.

Arborescence cible :

```text
smart-retail-ai-analyst/
├── backend/
├── frontend/
├── notebooks/
├── src/
│   ├── data/
│   ├── analysis/
│   ├── ml/
│   └── rag/
├── data/
│   ├── raw/
│   ├── processed/
│   └── documents/
├── docs/
├── tests/
├── docker/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

Validation : le repo existe, le premier commit est fait, l’arborescence est visible sur GitHub.

Commit :
```bash
git commit -m "chore: initialize project structure"
```

---

## Tâche 1.2 — Créer environnement Python

Sous-tâches :
1. Créer un environnement virtuel.
2. Installer dépendances minimales.
3. Vérifier version Python.
4. Créer un notebook de test.

Packages initiaux :
```text
pandas
numpy
matplotlib
openpyxl
jupyter
python-dotenv
ucimlrepo
```

Validation : `python --version` fonctionne, `pip freeze` montre les packages, un notebook lit un petit DataFrame test.

Commit :
```bash
git commit -m "chore: setup python environment"
```

---

# Phase 2 — Dataset Online Retail

## Tâche 2.1 — Télécharger Online Retail

Sous-tâches :
1. Installer `ucimlrepo`.
2. Télécharger dataset avec `fetch_ucirepo(id=352)`.
3. Sauvegarder localement en CSV dans `data/raw/online_retail_raw.csv`.
4. Vérifier nombre de lignes et colonnes.

Validation : fichier brut présent, colonnes visibles, nombre de lignes cohérent.

Commit :
```bash
git commit -m "data: add online retail raw dataset loader"
```

---

## Tâche 2.2 — Comprendre les colonnes

Sous-tâches :
1. Afficher `.head()`.
2. Afficher `.info()`.
3. Afficher `.describe()`.
4. Créer `docs/data_dictionary.md`.
5. Expliquer chaque colonne en français.

Validation : le data dictionary existe et tu peux expliquer chaque colonne.

Commit :
```bash
git commit -m "docs: add data dictionary"
```

---

## Tâche 2.3 — Nettoyage initial

Sous-tâches :
1. Identifier les lignes avec `CustomerID` manquant.
2. Identifier `Quantity <= 0`.
3. Identifier `UnitPrice <= 0`.
4. Identifier factures annulées `InvoiceNo` commence par `C`.
5. Décider stratégie de nettoyage.
6. Créer `src/data/clean_online_retail.py`.
7. Sauvegarder `data/processed/online_retail_clean.csv`.

Validation : dataset nettoyé sauvegardé, nombre de lignes avant/après documenté, script reproductible.

Commit :
```bash
git commit -m "data: clean online retail transactions"
```

---

# Phase 3 — EDA business

## Tâche 3.1 — KPIs globaux

Calculer : CA total, nombre de factures, nombre de clients, nombre de produits, nombre de pays, panier moyen.

Fichiers :
- `notebooks/02_eda_kpis.ipynb`
- `src/analysis/kpis.py`

Commit :
```bash
git commit -m "feat: add global sales kpis"
```

---

## Tâche 3.2 — Analyse temporelle

Sous-tâches : extraire année/mois/jour/heure, CA par mois, nombre de commandes par mois, graphique ventes mensuelles, conclusion business.

Commit :
```bash
git commit -m "feat: add monthly sales analysis"
```

---

## Tâche 3.3 — Top produits et pays

Sous-tâches : top 10 produits par CA, top 10 produits par quantité, top 10 pays par CA, visualisations, conclusion business.

Commit :
```bash
git commit -m "feat: add product and country analysis"
```

---

# Phase 4 — RFM & segmentation

## Tâche 4.1 — Construire table client

Sous-tâches : regrouper par `CustomerID`, calculer dernière date d’achat, fréquence, montant total, créer `customer_features.csv`.

Commit :
```bash
git commit -m "feat: build customer feature table"
```

---

## Tâche 4.2 — Scoring RFM

Sous-tâches : calculer Recency, Frequency, Monetary, créer scores 1 à 5, créer segments : Champions, Loyal, Potential, At risk, Lost.

Commit :
```bash
git commit -m "feat: add rfm customer scoring"
```

---

## Tâche 4.3 — Clustering KMeans

Sous-tâches : choisir variables RFM, standardiser, tester plusieurs K, elbow method, entraîner KMeans, interpréter clusters, sauvegarder segments.

Commit :
```bash
git commit -m "feat: add customer segmentation with kmeans"
```

---

# Phase 5 — FastAPI backend

## Tâche 5.1 — API minimale
Créer `backend/main.py` et endpoint `/health`.

Commit :
```bash
git commit -m "feat: add FastAPI health endpoint"
```

## Tâche 5.2 — Endpoints data
Créer `/dataset-summary`, `/sales-kpis`, `/top-products`, `/top-countries`, `/rfm-segments`.

Commit :
```bash
git commit -m "feat: expose analytics endpoints"
```

---

# Phase 6 — Streamlit frontend

## Tâche 6.1 — Interface de base
Créer `frontend/app.py`, page accueil, menu latéral.

Commit :
```bash
git commit -m "feat: add Streamlit frontend shell"
```

## Tâche 6.2 — Dashboard analytics
Afficher KPIs, graphiques, top produits, segments clients.

Commit :
```bash
git commit -m "feat: add analytics dashboard"
```

---

# Phase 7 — RAG documents

## Tâche 7.1 — Créer documents métier
Créer dans `data/documents/` : `business_context.md`, `rfm_methodology.md`, `customer_segments_guide.md`, `project_faq.md`.

Commit :
```bash
git commit -m "docs: add business documents for rag"
```

## Tâche 7.2 — Pipeline RAG local
Créer loader, splitter, embeddings, vector store, retriever, fonction `answer_question`.

Commit :
```bash
git commit -m "feat: add local rag pipeline"
```

---

# Phase 8 — Chat data + Chat docs

## Tâche 8.1 — Chat documents
Créer endpoint `POST /chat-docs`.

Commit :
```bash
git commit -m "feat: add document chat endpoint"
```

## Tâche 8.2 — Chat data simple
Créer un module qui répond aux questions data prédéfinies : CA total, top produits, top pays, nombre clients, segments.

Commit :
```bash
git commit -m "feat: add simple data chat module"
```

---

# Phase 9 — Docker

## Tâche 9.1 — Docker backend
Créer Dockerfile backend.

Commit :
```bash
git commit -m "build: dockerize backend"
```

## Tâche 9.2 — Docker compose
Créer backend, frontend, qdrant si utilisé.

Commit :
```bash
git commit -m "build: add docker compose stack"
```

---

# Phase 10 — GCP

## Tâche 10.1 — Préparer GCP
Créer projet, activer billing, créer budget alerts, installer `gcloud`, authentifier.

Commit :
```bash
git commit -m "docs: add gcp setup guide"
```

## Tâche 10.2 — Cloud Storage + BigQuery
Créer bucket, upload dataset nettoyé, créer dataset BigQuery, charger table, tester requête SQL.

Commit :
```bash
git commit -m "feat: add bigquery loading guide"
```

## Tâche 10.3 — Cloud Run
Déployer backend FastAPI sur Cloud Run.

Commit :
```bash
git commit -m "deploy: add cloud run deployment"
```

---

# Phase 11 — Tests & qualité

## Tâche 11.1 — Tests unitaires
Tester nettoyage dataset, KPIs, RFM, endpoints API.

Commit :
```bash
git commit -m "test: add core unit tests"
```

## Tâche 11.2 — Logs et erreurs
Ajouter logging, try/except, messages d’erreurs propres.

Commit :
```bash
git commit -m "chore: improve logging and error handling"
```

---

# Phase 12 — Portfolio

## Tâche 12.1 — README professionnel
Inclure contexte, dataset, architecture, captures, installation, résultats, limites, prochaines étapes.

Commit :
```bash
git commit -m "docs: write professional README"
```

## Tâche 12.2 — Démo et CV
Créer vidéo 2 min, phrase CV, post LinkedIn, schéma architecture.

Commit :
```bash
git commit -m "docs: add portfolio assets"
```

---

## 7. Commandes Git quotidiennes

À chaque tâche :

```bash
git status
git add .
git commit -m "type: message clair"
git push
```

Types de commits : `chore:`, `data:`, `feat:`, `fix:`, `docs:`, `test:`, `build:`, `deploy:`.

---

## 8. Prompt quotidien à utiliser

```text
Je travaille sur le projet Smart Retail AI Analyst avec la base Online Retail.
Agis comme mon Project Manager + Mentor débutant.
Voici mon état actuel : [décrire ce qui est fait].
Donne-moi la prochaine tâche unique à faire.
Explique-la dans les détails des détails :
- objectif,
- pourquoi,
- sous-tâches,
- fichiers,
- code ou commandes,
- vérifications,
- erreurs possibles,
- définition de Done,
- commit Git.
Ne me donne pas la suite tant que je n’ai pas validé cette tâche.
```

---

## 9. Prompt de validation après une tâche

```text
J’ai terminé la tâche.
Voici ce que j’ai fait : [résumé].
Voici les fichiers modifiés : [liste].
Voici le résultat obtenu : [copier logs/captures].
Agis comme QA Engineer + Project Manager.
Vérifie si la tâche est vraiment Done.
Si oui, valide et donne la prochaine tâche.
Sinon, donne-moi exactement les corrections à faire.
```

---

## 10. Principe final

La durée n’est pas importante. Le but est de construire une compétence solide.

```text
Comprendre → Coder → Tester → Documenter → Commit → Review → Next task
```

Une tâche finie mais non comprise n’est pas terminée.
Un code qui marche mais non documenté n’est pas terminé.
Un projet sans commit propre n’est pas terminé.
