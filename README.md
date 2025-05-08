# Generador interactivo de micro-relatos de terror 🩸

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](
https://render.com/deploy?repo=https://github.com/nicolaefrancis/microrelatos-terror)

git clone https://github.com/nicolaefrancis/microrelatos-terror.git

Pequeña aplicación web hecha en **Python 3 + Flask + Markovify** que permite generar micro-relatos de terror en un clic.  
El usuario elige escenario, época y monstruo ; la app mezcla una plantilla literaria con un modelo de cadenas de Markov entrenado en mis propios textos y devuelve un relato de ≤ 280 caracteres, listo para compartir en redes.

---

## Demo

🔗 <https://👉TU_URL_RENDER👈>

*(Plan gratuito de Render; tarda 1-2 s en “despertar” tras inactividad.)*

---

## Características

- **Plantillas personalizables** para combinar con el texto generado.  
- **Modelo Markovify** cacheado en `data/model.json` para minimizar tiempos de arranque.  
- **Compartir en X/Twitter** con un enlace `intent/tweet` pre-armado.  
- Código formateado automáticamente con **Ruff** y cubierto por **pytest**.

---

## Cómo correr en local

```bash
git clone https://github.com/👉TU_USUARIO👈/microrelatos-terror.git
cd microrelatos-terror
python -m venv .venv
source .venv/bin/activate      # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
set FLASK_APP=app              # en bash: export FLASK_APP=app
flask run
