import requests
from bs4 import BeautifulSoup
from datetime import datetime
import random
import time

def shadow_fetch(url):
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ]
    headers = {
        'User-Agent': random.choice(agents),
        'Referer': 'https://www.google.com/',
        'Cache-Control': 'no-cache'
    }
    # ثغرة تجاوز الكاش
    bypass_url = f"{url}{'&' if '?' in url else '?'}shd={random.randint(1000, 9999)}"
    try:
        response = requests.get(bypass_url, headers=headers, timeout=25)
        response.encoding = 'utf-8'
        return response.content if response.status_code == 200 else None
    except:
        return None

def run_stadium_stars_premium():
    sources = {
        "stars": "https://www.sayidaty.net/taxonomy/term/31/rss.xml",
        "sports": "https://arabic.rt.com/rss/sport/"
    }
    
    my_link = "https://data527.click/21330bf1d025d41336e6/4ba0cfe12d/?placementName=default"
    news_grid_html = ""

    # معالجة قسم المشاهير (Sayidaty)
    stars_content = shadow_fetch(sources["stars"])
    if stars_content:
        soup = BeautifulSoup(stars_content, 'xml')
        for item in soup.find_all('item')[:10]:
            title = item.title.text
            img = item.find('enclosure').get('url') if item.find('enclosure') else "https://via.placeholder.com/500x350"
            news_grid_html += f'''
            <div class="card stars">
                <a href="{my_link}" target="_blank">
                    <div class="card-img">
                        <img src="{img}" alt="news">
                        <div class="badge">TRENDING</div>
                    </div>
                    <div class="card-body">
                        <span class="category">✨ مشاهير</span>
                        <h3>{title}</h3>
                        <div class="card-footer"><span>⏱️ {datetime.now().strftime('%H:%M')}</span><span class="read-more">التفاصيل ←</span></div>
                    </div>
                </a>
            </div>'''

    # معالجة قسم الرياضة (RT)
    sports_content = shadow_fetch(sources["sports"])
    if sports_content:
        soup = BeautifulSoup(sports_content, 'xml')
        for item in soup.find_all('item')[:10]:
            title = item.title.text
            img = item.find('enclosure').get('url') if item.find('enclosure') else "https://via.placeholder.com/500x350"
            news_grid_html += f'''
            <div class="card sports">
                <a href="{my_link}" target="_blank">
                    <div class="card-img">
                        <img src="{img}" alt="news">
                        <div class="badge" style="background:#00ff88; color:#000;">GOAL</div>
                    </div>
                    <div class="card-body">
                        <span class="category" style="color:#00ff88;">⚽ رياضة</span>
                        <h3>{title}</h3>
                        <div class="card-footer"><span>⏱️ {datetime.now().strftime('%H:%M')}</span><span class="read-more">التفاصيل ←</span></div>
                    </div>
                </a>
            </div>'''

    full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>STADIUM STARS | Premium Feed</title>
    <script src="https://data527.click/pfe/current/tag.min.js?z=8345712" data-cfasync="false" async></script>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary: #ff0055; --dark: #08090b; --card-bg: #12141a; --text: #ffffff; }}
        body {{ background: var(--dark); color: var(--text); font-family: 'Cairo', sans-serif; margin: 0; }}
        header {{ background: #000; padding: 15px 5%; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--primary); position: sticky; top: 0; z-index: 1000; }}
        .logo {{ font-size: 24px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--primary); }}
        .container {{ max-width: 1200px; margin: 20px auto; padding: 10px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }}
        .card {{ background: var(--card-bg); border-radius: 12px; overflow: hidden; transition: 0.3s; border: 1px solid #1f2229; }}
        .card:hover {{ transform: scale(1.02); border-color: var(--primary); }}
        .card a {{ text-decoration: none; color: inherit; }}
        .card-img {{ height: 180px; position: relative; }}
        .card-img img {{ width: 100%; height: 100%; object-fit: cover; }}
        .badge {{ position: absolute; top: 10px; right: 10px; background: var(--primary); font-size: 10px; padding: 3px 8px; border-radius: 4px; font-weight: bold; }}
        .card-body {{ padding: 15px; }}
        .card-body h3 {{ font-size: 16px; margin: 10px 0; line-height: 1.4; height: 45px; overflow: hidden; }}
        .category {{ font-size: 11px; font-weight: bold; }}
        .card-footer {{ display: flex; justify-content: space-between; border-top: 1px solid #1f2229; margin-top: 10px; padding-top: 10px; font-size: 12px; color: #888; }}
        footer {{ background: #000; padding: 30px; text-align: center; border-top: 2px solid var(--primary); margin-top: 40px; }}
    </style>
</head>
<body onclick="void(0)">
    <header><a href="#" class="logo">Stadium<span>Stars</span></a><div style="color: #ff0055;">V99 CORE</div></header>
    <div class="container"><div class="grid">{news_grid_html}</div></div>
    <footer><div class="logo">Stadium<span>Stars</span></div></footer>
</body></html>'''

    with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)

if __name__ == "__main__":
    run_stadium_stars_premium()
