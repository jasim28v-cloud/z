import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def run_celebrity_news():
    # المصدر الجديد: أخبار المشاهير (Laha Magazine كمثال)
    rss_url = "https://www.lahamag.com/rss/celebrities"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        # رابطك الربحي (يظل ثابتاً في بروتوكول الإنزال)
        my_direct_link = "Https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=20)
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        # شريط الأخبار العاجلة للمشاهير
        ticker_items = " • ".join([f"✨ {item.title.text}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:24]):
            title = item.title.text
            news_url = item.link.text
            
            # محاولة استخراج الصورة من enclosure أو الوصف
            img_element = item.find('enclosure')
            img_url = img_element.get('url') if img_element else "https://images.pexels.com/photos/2748239/pexels-photo-2748239.jpeg"
            
            news_html += f'''
            <article class="celeb-card">
                <div class="trend-tag">تريند الآن 🔥</div>
                <div class="card-thumb">
                    <a href="{my_direct_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="celeb news">
                    </a>
                </div>
                <div class="card-body">
                    <h2 class="card-title">{title}</h2>
                    <div class="celeb-info">
                        <span>📸 أضواء وشهرة</span>
                        <span>⏱️ {datetime.now().strftime("%I:%M")}</span>
                    </div>
                    <div class="button-group">
                        <a href="{my_direct_link}" target="_blank" class="btn-exclusive">شاهد التفاصيل الحصرية 💎</a>
                        <a href="{news_url}" target="_blank" class="btn-source">المصدر</a>
                    </div>
                </div>
            </article>'''

            # إعلان "أسرار النجوم"
            if (i + 1) % 5 == 0:
                news_html += f'''
                <div class="vip-ad-block">
                    <a href="{my_direct_link}" target="_blank">
                        <div class="ad-content">
                            <span class="ad-label">VIP</span>
                            <h3>كشف أسرار لم تنشر من قبل!</h3>
                            <p>اضغط هنا لمشاهدة الصور المسربة وفيديوهات المشاهير</p>
                            <div class="ad-button">دخول القسم السري 🕵️‍♀️</div>
                        </div>
                    </a>
                </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ستار كود | عالم الأضواء</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #0f0f0f; --gold: #d4af37; --text: #ffffff;
            --accent: #e91e63; --card-bg: #1a1a1a;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: var(--primary); font-family: 'Cairo', sans-serif; color: var(--text); padding-top: 140px; }}
        
        header {{ background: rgba(0, 0, 0, 0.98); padding: 15px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 2px solid var(--accent); display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 28px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--accent); }}

        .live-ticker {{ position: fixed; top: 78px; width: 100%; background: #333; color: var(--gold); overflow: hidden; height: 35px; display: flex; align-items: center; z-index: 999; border-bottom: 1px solid var(--gold); }}
        .ticker-label {{ background: var(--accent); color: #fff; padding: 0 15px; font-weight: 800; font-size: 13px; height: 100%; display: flex; align-items: center; }}
        .ticker-text {{ white-space: nowrap; animation: scroll 45s linear infinite; font-weight: 600; }}
        @keyframes scroll {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-200%); }} }}

        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 15px; display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 25px; }}
        
        .celeb-card {{ background: var(--card-bg); border-radius: 10px; overflow: hidden; transition: 0.4s; border: 1px solid #222; position: relative; }}
        .celeb-card:hover {{ transform: translateY(-10px); border-color: var(--accent); }}
        
        .trend-tag {{ position: absolute; top: 15px; left: 15px; background: var(--accent); color: #fff; padding: 4px 12px; font-size: 11px; font-weight: 900; border-radius: 4px; z-index: 10; }}

        .card-thumb {{ height: 250px; overflow: hidden; }}
        .card-thumb img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.6s; }}
        
        .card-body {{ padding: 20px; }}
        .card-title {{ font-size: 18px; font-weight: 700; line-height: 1.5; margin-bottom: 15px; height: 54px; overflow: hidden; color: #eee; }}
        .celeb-info {{ display: flex; justify-content: space-between; font-size: 12px; color: var(--gold); margin-bottom: 20px; }}
        
        .button-group {{ display: flex; gap: 10px; }}
        .btn-exclusive {{ flex: 2; background: linear-gradient(45deg, var(--accent), #ff5e95); color: #fff; text-decoration: none; text-align: center; padding: 12px; border-radius: 5px; font-weight: 700; }}
        .btn-source {{ flex: 1; background: transparent; color: #888; text-decoration: none; text-align: center; padding: 12px; border-radius: 5px; border: 1px solid #333; font-size: 12px; }}

        .vip-ad-block {{ grid-column: 1 / -1; background: #000; border: 1px dashed var(--gold); border-radius: 15px; padding: 30px; text-align: center; }}
        .ad-content h3 {{ color: var(--gold); font-size: 22px; }}
        .ad-button {{ background: var(--gold); color: #000; padding: 10px 30px; border-radius: 5px; font-weight: 900; display: inline-block; margin-top: 15px; }}
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">STAR<span>CODE</span></a>
        <div style="font-size: 12px; color: var(--accent);">✨ حصريات المشاهير</div>
    </header>
    <div class="live-ticker">
        <div class="ticker-label">عاجل</div>
        <div class="ticker-text">{ticker_items}</div>
    </div>
    <main class="container">{news_html}</main>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        print("Protocol Complete: Celebrity node deployed.")
            
    except Exception as e:
        print(f"Interference detected: {e}")

if __name__ == "__main__":
    run_celebrity_news()
