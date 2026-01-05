from flask import Flask, render_template
import json

app = Flask(__name__)

# Всё контент здесь — меняйте прямо в коде
content = {
    "logo_image": "",
    "hero_title": "Позвольте мне заворожить вас нежностью...",
    "hero_video": "",
    "hero_image": "https://i.imgur.com/example.jpg",  # Замените на свою ссылку
    "programs_title": "Мои соблазнительные программы",
    "programs": [
        {"title": "Классический эротический", "description": "Нежные прикосновения с маслом", "price": "60 мин — 3000 ₽", "image": "https://i.imgur.com/img1.jpg"},
        # Добавьте остальные с ссылками на фото
    ],
    "about_title": "Познакомьтесь ближе...",
    "about_text": "Я Алена — частный мастер в Саратове...",
    "about_image": "https://i.imgur.com/about.jpg",
    "contacts_title": "Готовы к встрече?",
    "telegram_link": "https://t.me/alena_massage_saratov",
    "contact_text": "Саратов, центр<br>Запись заранее",
    "footer_text": "© 2026 Алена"
}

schema = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Эротический массаж Алены в Саратове",
    "address": {"@type": "PostalAddress", "addressLocality": "Саратов"}
}

@app.route('/')
def index():
    return render_template('index.html', content=content, schema=json.dumps(schema))

if __name__ == '__main__':
    app.run()