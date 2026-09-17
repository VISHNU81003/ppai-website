# PPAI Website (starter)

Hello World Django project for the Plant Protection Association of India website.

This is a starting point. Build the full site locally, then push updates to GitHub and deploy them on the Hostinger VPS.

## Run locally (Windows)

In PowerShell or the VS Code terminal:

```powershell
cd C:\Users\LENOVO\Projects\ppai-website
.\venv\Scripts\Activate.ps1
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

If activation is blocked, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

## GitHub

Do **not** upload the `venv` folder. Use the zip that excludes it, or `git push` after creating a GitHub repository.
