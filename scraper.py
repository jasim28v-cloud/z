import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def run_celebs_final():
    # مصدر متخصص في أخبار الفن والمشاهير (Vetogate Arts)
    rss_url = "https://www.vetogate.com/rss.aspx?id=31" 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    try:
        # الرابط الربحي الخاص بك
        my_direct_link = "Https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=25)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            return

        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        # شريط الأخبار العلوي
        ticker_items = " • ".join([f"✨ {item.title.text.strip()}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:24]):
            title = item.title.text.strip()
            news_url = item.link.text.strip()
            
            # استخراج الصورة
            img_url = "https://images.pexels.com/photos/2747449/pexels-photo-2747449.jpeg"
            enclosure = item.find('enclosure')
            if enclosure:
                img_url = enclosure.get('url')
            else:
                description = item.find('description').text if item.find('description') else ""
                img_match = re.search(r'<img src="(.*?)"', description)
                if img_match:
                    img_url = img_match.group(1)
            
            # بناء كرت الخبر
            news_html += f'''
            <article class="celeb-card">
                <div class="trend-tag">TREND | تريند</div>
                <div class="card-thumb">
                    <a href="{my_direct_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="celebrity news">
                    </a>
                </div>
                <div class="card-body">
                    <h2 class="card-title">{title}</h2>
                    <div class="meta-info">
                        <span>🎬 حصريات الفن</span>
                        <span>⏱️ {datetime.now().strftime("%H:%M")}</span>
                    </div>
                    <div class="button-group">
                        <a href="{my_direct_link}" target="_blank" class="btn-main">شاهد الان 💎</a>
                        <a href="{news_url}" target="_blank" class="btn-sub">المصدر</a>
                    </div>
                </div>
            </article>'''

            if (i + 1) % 6 == 0:
                news_html += f'''
                <div class="ad-section">
                    <a href="{my_direct_link}" target="_blank">
                        <div class="ad-box">
                            <span class="ad-badge">VIP ONLY</span>
                            <h3>أسرار لم تنشر من قبل عن نجومك المفضلين</h3>
                            <p>انقر هنا لمشاهدة الصور المسربة وحقائق لأول مرة</p>
                            <div class="ad-btn">اكتشف الآن 🔓</div>
                        </div>
                    </a>
                </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ستار جلام | عالم المشاهير والتريند</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #050505; --accent: #e91e63; --gold: #ffd700; --card: #121212;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Cairo', sans-serif; }}
        body {{ background: var(--bg); color: #fff; padding-top: 140px; }}
        header {{ background: #000; padding: 15px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 3px solid var(--accent); display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 26px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--accent); }}
        .ticker {{ position: fixed; top: 75px; width: 100%; background: var(--accent); color: #fff; height: 35px; overflow: hidden; display: flex; align-items: center; z-index: 999; font-size: 13px; font-weight: bold; }}
        .ticker-label {{ background: #000; padding: 0 15px; z-index: 2; }}
        .ticker-text {{ white-space: nowrap; animation: move 40s linear infinite; }}
        @keyframes move {{ 0% {{ transform: translateX(-100%); }} 100% {{ transform: translateX(100%); }} }}
        .main-grid {{ max-width: 1200px; margin: 0 auto; padding: 20px; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 25px; }}
        .celeb-card {{ background: var(--card); border-radius: 15px; overflow: hidden; border: 1px solid #222; position: relative; transition: 0.3s; }}
        .celeb-card:hover {{ border-color: var(--accent); transform: translateY(-5px); }}
        .trend-tag {{ position: absolute; top: 12px; right: 12px; background: var(--accent); padding: 3px 10px; font-size: 11px; font-weight: bold; border-radius: 3px; z-index: 5; }}
        .card-thumb {{ height: 210px; }}
        .card-thumb img {{ width: 100%; height: 100%; object-fit: cover; }}
        .card-body {{ padding: 20px; }}
        .card-title {{ font-size: 17px; height: 50px; overflow: hidden; margin-bottom: 15px; color: #f0f0f0; }}
        .meta-info {{ display: flex; justify-content: space-between; font-size: 11px; color: var(--gold); margin-bottom: 20px; }}
        .button-group {{ display: flex; gap: 10px; }}
        .btn-main {{ flex: 2; background: var(--accent); color: #fff; text-decoration: none; text-align: center; padding: 12px; border-radius: 8px; font-weight: bold; }}
        .btn-sub {{ flex: 1; background: #222; color: #aaa; text-decoration: none; text-align: center; padding: 12px; border-radius: 8px; font-size: 11px; }}
        .ad-section {{ grid-column: 1 / -1; margin: 20px 0; }}
        .ad-box {{ background: linear-gradient(45deg, #121212, #250a14); border: 2px dashed var(--accent); padding: 40px; text-align: center; border-radius: 15px; }}
        .ad-btn {{ background: var(--gold); color: #000; display: inline-block; padding: 10px 35px; border-radius: 20px; font-weight: 900; margin-top: 15px; }}
        @media (max-width: 600px) {{ .main-grid {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">STAR<span>GLAM</span></a>
        <div style="font-size: 12px; color: var(--gold);">✨ تريند اليوم</div>
    </header>
    <div class="ticker">
        <div class="ticker-label">عاجل</div>
        <div class="ticker-text">{ticker_items}</div>
    </div>
    <main class="main-grid">{news_html}</main>
    <footer style="text-align:center; padding: 40px; color: #444;">
        <p>STAR GLAM &copy; 2026 | Exclusive Trends</p>
    </footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        print("Done: index.html has been generated with Celebrity Content.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_celebs_final()
