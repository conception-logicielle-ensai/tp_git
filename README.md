# TP – Git Avancé  Ca neige et il y a plus de bus, ca va dormir dehors


## Lancement de l’application

### Prérequis

Avant de lancer l’application, assurez-vous de disposer des éléments suivants :

* **Python 3.11 ou supérieur**
* **uv** installé et accessible depuis le terminal

---

### Création de l’environnement et installation des dépendances

Depuis la racine du projet, exécutez les commandes suivantes :

```bash
uv venv
uv sync
```

Ces commandes permettent :

* de créer l’environnement virtuel du projet ;
* d’installer l’ensemble des dépendances définies dans `pyproject.toml` et verrouillées dans `uv.lock`.

---

### Démarrage de l’application

Une fois l’environnement configuré, lancez l’API avec la commande suivante :

```bash
uv run uvicorn app.main:app --reload
```

L’option `--reload` active le rechargement automatique du serveur lors des modifications du code.

---

### Accès à la documentation de l’API

La documentation interactive de l’API (Swagger / OpenAPI) est accessible à l’adresse suivante :

```
http://127.0.0.1:8000/docs
```

Cette interface permet de consulter et tester les différents endpoints exposés par l’application.
