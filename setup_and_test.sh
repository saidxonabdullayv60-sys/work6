#!/usr/bin/env bash
# Git Bash (Windows) uchun: bir martada o'rnatish + test + server
set -e

# 1) Virtual muhit (eski .venv bo'lsa ham, yangisini yaratamiz)
python -m venv .venv

# Windows: .venv/Scripts, Linux/Mac: .venv/bin
if [ -f ".venv/Scripts/activate" ]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

# 2) Kutubxonalar
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3) Baza
python manage.py migrate

# 4) Testlar
python manage.py test -v 2

echo ""
echo "=== HAMMASI TAYYOR. Server ishga tushyapti: http://127.0.0.1:8000/api/products/ ==="
python manage.py runserver
