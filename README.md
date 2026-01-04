# TP du cours Git Avancé


## LAncer l'application 

Pour lancer l'application il est nécessaire d'avoir déjà installer python > 3.11 et uv.

lancer ka commande 

```
uv venv
uv run uvicorn app.main:app --reload
```

LE swagger de l'API sera disponible à l'URL
 `http://127.0.0.1:8000/docs`