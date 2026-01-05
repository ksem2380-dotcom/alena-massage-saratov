from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, jsonify
import json
import os
import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'super-secret-key-change-me-1234567890'  # ОБЯЗАТЕЛЬНО смените на свой длинный пароль!
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp4', 'webm', 'svg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

CONTENT_FILE = 'content.json'
VISITS_FILE = 'visits.json'

# Создание начальных файлов
if not os.path.exists(CONTENT_FILE):
    default_content = {
        "logo_image": "",
        "hero_title": "Позвольте мне заворожить вас нежностью...",
        "hero_video": "",
        "hero_image": "https://example.com/hero.jpg",
        "programs_title": "Мои соблазнительные программы",
        "programs": [
            {"title": "Классический эротический", "description": "Нежные прикосновения с маслом и лепестками роз", "price": "60 мин — 3000 ₽<br>90 мин — 4500 ₽", "image": "https://example.com/img1.jpg"},
            {"title": "VIP релакс", "description": "Страстные акценты на чувствительных зонах", "price": "90 мин — 5000 ₽", "image": "https://example.com/img2.jpg"},
            {"title": "Сенсорный", "description": "Игра света свечей и нежных касаний", "price": "60 мин — 3500 ₽", "image": "https://example.com/img3.jpg"},
            {"title": "Тайский эротический", "description": "Экзотические техники для глубокого блаженства", "price": "75 мин — 4000 ₽", "image": "https://example.com/img4.jpg"},
            {"title": "Персональная", "description": "Только для вас — по вашим желаниям", "price": "от 60 мин — от 4000 ₽", "image": "https://example.com/img5.jpg"}
        ],
        "about_title": "Познакомьтесь ближе...",
        "about_text": "Я Алена — мастер страстных и нежных прикосновений. В приватной обстановке с ароматом свечей и лепестками роз подарю вам незабываемые ощущения.",
        "about_image": "https://example.com/about.jpg",
        "contacts_title": "Готовы к встрече?",
        "telegram_link": "https://t.me/alena_massage_saratov",
        "contact_text": "Саратов, центр (адрес после записи)<br>Ежедневно по предварительной записи",
        "footer_text": "© 2026 Алена. Тайна и удовольствие..."
    }
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    with open(CONTENT_FILE, 'w', encoding='utf-8') as f:
        json.dump(default_content, f, ensure_ascii=False, indent=4)

if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, 'w', encoding='utf-8') as f:
        json.dump({"daily": {}, "ips_today": []}, f)

def log_visit():
    today = datetime.date.today().isoformat()
    ip = request.remote_addr
    with open(VISITS_FILE, 'r+') as f:
        data = json.load(f)
        if today not in data["daily"]:
            data["daily"][today] = 0
            data["ips_today"] = []
        if ip not in data["ips_today"]:
            data["daily"][today] += 1
            data["ips_today"].append(ip)
        f.seek(0)
        json.dump(data, f, ensure_ascii=False)
        f.truncate()

@app.route('/')
def index():
    log_visit()
    with open(CONTENT_FILE, 'r', encoding='utf-8') as f:
        content = json.load(f)
    schema = {"@context": "https://schema.org", "@type": "LocalBusiness", "name": "Эротический массаж Алены в Саратове", "address": {"@type": "PostalAddress", "addressLocality": "Саратов"}}
    return render_template('index.html', content=content, schema=json.dumps(schema))

# (остальные маршруты: uploaded_file, admin_login, admin_panel, logout — из предыдущих сообщений)

if __name__ == '__main__':
    app.run()