import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_sports():
    rss_url = "https://arabic.rt.com/rss/sport/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        # الرابط الربحي الخاص بك
        my_direct_link = "Https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=25)
        response.encoding = 'utf-8'
        
        # استخدام html.parser الافتراضي لضمان العمل على أي بيئة
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('item')
        
        ticker_items = " • ".join([f"⚽ {item.title.text}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:24]):
            title = item.title.text
            news_url = item.link.text
            img_element = item.find('enclosure')
            img_url = img_element.get('url') if img_element else "https://images.pexels.com/photos/46798/the-ball-stadion-football-the-pitch-46798.jpeg"
            
            news_html += f'''
            <article class="sport-card">
                <div class="live-tag">بث مباشر</div>
                <div class="card-thumb">
                    <a href="{my_direct_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="sport news">
                    </a>
                </div>
                <div class="card-body">
                    <h2 class="card-title">{title}</h2>
                    <div class="match-info">
                        <span>🏟️ الدوري العالمي</span>
                        <span>⏱️ {datetime.now().strftime("%I:%M")}</span>
                    </div>
                    <div class="button-group">
                        <a href="{my_direct_link}" target="_blank" class="btn-live">شاهد المباراة الآن ⚡</a>
                        <a href="{news_url}" target="_blank" class="btn-source">التفاصيل</a>
                    </div>
                </div>
            </article>'''

            if (i + 1) % 5 == 0:
                news_html += f'''
                <div class="premium-ad-block">
                    <a href="{my_direct_link}" target="_blank">
                        <div class="ad-content">
                            <span class="ad-label">حصري</span>
                            <h3>جدول مباريات والقنوات الناقلة اليوم</h3>
                            <p>اضغط هنا لمتابعة النتائج والتشكيلات فوراً</p>
                            <div class="ad-button">دخول الاستوديو التحليلي 🏟️</div>
                        </div>
                    </a>
                </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ستاديوم 24 | عالم الرياضة</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary: #1a1a1a; --gold: #f2cc60; --text: #ffffff; --accent: #ff3e3e; --card-bg: #242424; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: var(--primary); font-family: 'Cairo', sans-serif; color: var(--text); padding-top: 140px; }}
        header {{ background: rgba(0, 0, 0, 0.95); padding: 15px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 3px solid var(--gold); display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 28px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--gold); }}
        .live-ticker {{ position: fixed; top: 78px; width: 100%; background: var(--accent); color: #fff; overflow: hidden; height: 35px; display: flex; align-items: center; z-index: 999; }}
        .ticker-text {{ white-space: nowrap; animation: scroll 40s linear infinite; font-weight: 600; padding-right: 100%; }}
        @keyframes scroll {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 15px; display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 25px; }}
        .sport-card {{ background: var(--card-bg); border-radius: 15px; overflow: hidden; border: 1px solid #333; position: relative; }}
        .live-tag {{ position: absolute; top: 15px; right: 15px; background: var(--accent); color: #fff; padding: 4px 15px; font-size: 12px; font-weight: 900; border-radius: 50px; z-index: 10; }}
        .card-thumb img {{ width: 100%; height: 200px; object-fit: cover; }}
        .card-body {{ padding: 20px; }}
        .card-title {{ font-size: 19px; font-weight: 800; margin-bottom: 15px; height: 54px; overflow: hidden; }}
        .btn-live {{ display: block; background: var(--gold); color: #000; text-decoration: none; text-align: center; padding: 12px; border-radius: 8px; font-weight: 900; margin-bottom: 10px; }}
        .btn-source {{ display: block; color: #fff; text-decoration: none; text-align: center; padding: 5px; font-size: 12px; }}
        .premium-ad-block {{ grid-column: 1 / -1; background: #333; border: 2px solid var(--gold); border-radius: 20px; padding: 30px; text-align: center; }}
    </style>
</head>
<body>
    <header><a href="#" class="logo">ستاديوم <span>24</span></a></header>
    <div class="live-ticker"><div class="ticker-text">{ticker_items}</div></div>
    <main class="container">{news_html}</main>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        print("Done!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_sports()
