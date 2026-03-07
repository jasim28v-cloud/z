import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_shadow_entertainment():
    rss_url = "https://www.sayidaty.net/rss.xml"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        my_link = "Https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=25)
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        ticker_items = " • ".join([f"✨ {item.title.text}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:32]):
            title = item.title.text
            link = item.link.text
            
            img_tag = item.find('media:content') or item.find('enclosure')
            img_url = img_tag.get('url') if img_tag else "https://images.pexels.com/photos/175658/pexels-photo-175658.jpeg"

            news_html += f'''
            <article class="celeb-card">
                <div class="trend-tag">تريند اليوم</div>
                <div class="card-thumb">
                    <a href="{my_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="celeb news">
                    </a>
                </div>
                <div class="card-body">
                    <h2 class="card-title">{title}</h2>
                    <div class="meta-info">
                        <span>🎬 مشاهير العرب</span>
                        <span>📅 {datetime.now().strftime("%d مارس")}</span>
                    </div>
                    <div class="action-buttons">
                        <a href="{my_link}" target="_blank" class="btn-main">التفاصيل الكاملة 👁️‍🗨️</a>
                        <a href="{link}" target="_blank" class="btn-sub">المصدر</a>
                    </div>
                </div>
            </article>'''

            if (i + 1) % 6 == 0:
                news_html += f'''
                <div class="premium-ad-block">
                    <a href="{my_link}" target="_blank">
                        <div class="ad-wrap">
                            <span class="exclusive">حصري</span>
                            <h3>كواليس وأسرار النجوم المسربة اليوم</h3>
                            <p>اضغط هنا لمشاهدة الصور والفيديوهات الحصرية</p>
                            <div class="ad-button">دخول الأرشيف السري 💎</div>
                        </div>
                    </a>
                </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>سيدتي لايت | عالم النجوم والمشاهير</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --main: #8e44ad; --gold: #f1c40f; --dark: #121212; --card: #1e1e1e; --text: #ffffff; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: var(--dark); font-family: 'Cairo', sans-serif; color: var(--text); padding-top: 140px; }}
        header {{ background: rgba(0,0,0,0.9); padding: 15px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 3px solid var(--main); display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 28px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--main); }}
        .ticker-bar {{ position: fixed; top: 78px; width: 100%; background: #fff; color: #000; overflow: hidden; height: 35px; display: flex; align-items: center; z-index: 999; border-bottom: 2px solid var(--gold); }}
        .ticker-label {{ background: var(--main); color: #fff; padding: 0 15px; font-weight: 800; font-size: 13px; height: 100%; display: flex; align-items: center; }}
        .ticker-text {{ white-space: nowrap; animation: scroll 45s linear infinite; font-weight: 700; }}
        @keyframes scroll {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-250%); }} }}
        .grid-container {{ max-width: 1200px; margin: 0 auto; padding: 0 15px; display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 25px; }}
        .celeb-card {{ background: var(--card); border-radius: 20px; overflow: hidden; transition: 0.3s; border: 1px solid #333; position: relative; }}
        .celeb-card:hover {{ transform: translateY(-10px); border-color: var(--main); }}
        .trend-tag {{ position: absolute; top: 15px; right: 15px; background: var(--main); color: #fff; padding: 4px 15px; font-size: 11px; font-weight: 900; border-radius: 50px; z-index: 10; }}
        .card-thumb {{ height: 230px; overflow: hidden; }}
        .card-thumb img {{ width: 100%; height: 100%; object-fit: cover; }}
        .card-body {{ padding: 20px; }}
        .card-title {{ font-size: 18px; font-weight: 800; line-height: 1.5; margin-bottom: 15px; height: 54px; overflow: hidden; color: #eee; }}
        .meta-info {{ display: flex; justify-content: space-between; font-size: 11px; color: var(--gold); margin-bottom: 20px; }}
        .action-buttons {{ display: flex; gap: 10px; }}
        .btn-main {{ flex: 2; background: var(--main); color: #fff; text-decoration: none; text-align: center; padding: 12px; border-radius: 12px; font-weight: 900; }}
        .btn-sub {{ flex: 1; border: 1px solid #444; color: #ccc; text-decoration: none; text-align: center; padding: 12px; border-radius: 12px; font-size: 11px; }}
        .premium-ad-block {{ grid-column: 1 / -1; background: linear-gradient(45deg, #2c3e50, #000); border: 1px solid var(--gold); border-radius: 20px; padding: 40px; text-align: center; }}
        .ad-button {{ background: var(--gold); color: #000; display: inline-block; padding: 12px 40px; border-radius: 50px; font-weight: 900; margin-top: 20px; text-decoration: none; }}
        @media (max-width: 600px) {{ .grid-container {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">سيدتي <span>LIGHT</span></a>
        <div style="font-size: 12px; font-weight: bold; color: var(--gold);">✨ أخبار النجوم</div>
    </header>
    <div class="ticker-bar">
        <div class="ticker-label">عاجل</div>
        <div class="ticker-text">{ticker_items}</div>
    </div>
    <main class="grid-container">{news_html}</main>
    <footer style="text-align:center; padding: 50px; color: #555; font-size: 12px;">
        <p>SAYIDATY LIGHT &copy; 2026 | ENTERTAINMENT PORTAL</p>
    </footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_shadow_entertainment()
