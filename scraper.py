import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def run_celeb_scraper():
    # المصدر الجديد: ليالينا
    rss_url = "https://www.layalina.com/rss/all"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    try:
        # الرابط الربحي الخاص بك
        my_link = "Https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=30)
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        ticker_items = " • ".join([f"💎 {item.title.text}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:35]):
            title = item.title.text
            link = item.link.text
            
            # محرك استخراج الصور الذكي لموقع ليالينا
            img_url = ""
            media_content = item.find('media:content') or item.find('enclosure')
            if media_content:
                img_url = media_content.get('url')
            
            if not img_url and item.description:
                img_match = re.search(r'<img src="(.*?)"', item.description.text)
                if img_match:
                    img_url = img_match.group(1)
            
            # صورة افتراضية راقية في حال عدم وجود صورة
            if not img_url:
                img_url = "https://www.layalina.com/assets/images/layalina-logo-social.png"

            news_html += f'''
            <article class="layalina-card">
                <div class="category-tag">مشاهير</div>
                <div class="card-thumb">
                    <a href="{my_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="Layalina News">
                    </a>
                </div>
                <div class="card-body">
                    <h2 class="card-title">{title}</h2>
                    <div class="meta-data">
                        <span>✨ ليالينا VIP</span>
                        <span>🗓️ {datetime.now().strftime("%d %B")}</span>
                    </div>
                    <a href="{my_link}" target="_blank" class="btn-view">عرض التفاصيل ⚡</a>
                </div>
            </article>'''

            # حقن إعلاني كل 6 أخبار
            if (i + 1) % 6 == 0:
                news_html += f'''
                <div class="dark-ad-section">
                    <a href="{my_link}" target="_blank">
                        <div class="ad-container">
                            <span class="pulse-red"></span>
                            <h3>تسريبات حصرية: ما لا تعرفه عن نجمك المفضل!</h3>
                            <p>اضغط هنا لمشاهدة الصور التي منعت من النشر</p>
                            <div class="ad-action-btn">كشف المستور الآن 🔓</div>
                        </div>
                    </a>
                </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ليالينا نيوز | بوابة النجوم</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary: #000000; --gold: #c5a059; --pink: #e91e63; --text: #ffffff; --card-bg: #121212; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: var(--primary); font-family: 'Cairo', sans-serif; color: var(--text); padding-top: 140px; }}
        
        header {{ background: rgba(0,0,0,0.98); padding: 15px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 2px solid var(--gold); display: flex; justify-content: space-between; align-items: center; backdrop-filter: blur(10px); }}
        .logo {{ font-size: 28px; font-weight: 900; color: #fff; text-decoration: none; letter-spacing: 1px; }}
        .logo span {{ color: var(--gold); }}

        .news-ticker {{ position: fixed; top: 76px; width: 100%; background: var(--gold); color: #000; height: 35px; display: flex; align-items: center; z-index: 999; overflow: hidden; }}
        .ticker-head {{ background: #000; color: #fff; padding: 0 15px; font-weight: 900; height: 100%; display: flex; align-items: center; font-size: 12px; }}
        .ticker-scroll {{ white-space: nowrap; animation: move 45s linear infinite; font-weight: 700; }}
        @keyframes move {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-350%); }} }}

        .main-grid {{ max-width: 1300px; margin: 0 auto; padding: 0 15px; display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 30px; }}
        
        .layalina-card {{ background: var(--card-bg); border-radius: 0; overflow: hidden; border: 1px solid #222; transition: 0.4s; position: relative; }}
        .layalina-card:hover {{ border-color: var(--gold); transform: translateY(-5px); }}
        
        .category-tag {{ position: absolute; top: 15px; right: 15px; background: var(--gold); color: #000; padding: 2px 15px; font-size: 11px; font-weight: 900; z-index: 5; }}

        .card-thumb {{ height: 260px; overflow: hidden; position: relative; }}
        .card-thumb::after {{ content: ''; position: absolute; bottom: 0; width: 100%; height: 50%; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent); }}
        .card-thumb img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.7s; }}
        .layalina-card:hover .card-thumb img {{ scale: 1.1; }}
        
        .card-body {{ padding: 20px; }}
        .card-title {{ font-size: 19px; font-weight: 700; height: 56px; overflow: hidden; line-height: 1.5; margin-bottom: 20px; color: #f0f0f0; }}
        .meta-data {{ display: flex; justify-content: space-between; font-size: 11px; color: var(--gold); margin-bottom: 20px; border-top: 1px solid #222; padding-top: 15px; }}
        
        .btn-view {{ display: block; background: transparent; color: var(--gold); text-decoration: none; text-align: center; padding: 12px; border: 1px solid var(--gold); font-weight: 900; transition: 0.3s; }}
        .btn-view:hover {{ background: var(--gold); color: #000; }}

        .dark-ad-section {{ grid-column: 1 / -1; background: #1a1a1a; border: 1px dashed var(--gold); padding: 50px; text-align: center; }}
        .ad-action-btn {{ background: var(--gold); color: #000; display: inline-block; padding: 15px 45px; margin-top: 25px; font-weight: 900; text-decoration: none; border-radius: 4px; }}
        
        .pulse-red {{ display: inline-block; width: 10px; height: 10px; background: red; border-radius: 50%; margin-left: 10px; animation: blink 1s infinite; }}
        @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0; }} 100% {{ opacity: 1; }} }}

        @media (max-width: 600px) {{ .main-grid {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">LAYALINA<span>.PRO</span></a>
        <div style="font-size: 11px; color: var(--gold); border: 1px solid; padding: 2px 8px;">PREMIUM ACCESS</div>
    </header>
    <div class="news-ticker">
        <div class="ticker-head">آخر التطورات</div>
        <div class="ticker-scroll">{ticker_items}</div>
    </div>
    <main class="main-grid">{news_html}</main>
    <footer style="text-align:center; padding: 60px; color: #333; font-size: 12px; letter-spacing: 2px;">
        <p>LAYALINA PRO ENGINE &copy; 2026</p>
    </footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_celeb_scraper()
