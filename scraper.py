import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import os

class ShadowSportsEngine:
    def __init__(self):
        self.target_rss = "https://arabic.rt.com/rss/sport/"
        self.monetization_link = "Https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

    def clean_title(self, title):
        # تنظيف العناوين من الزوائد لجعلها تبدو احترافية
        removals = ["شاهد..", "بالفيديو..", "مباشر:"]
        for word in removals:
            title = title.replace(word, "")
        return title.strip()

    def fetch_data(self):
        try:
            print("[+] الإطلاق: جاري سحب البيانات من المدار الرياضي...")
            response = requests.get(self.target_rss, headers=self.headers, timeout=15)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.content, 'xml')
            return soup.find_all('item')
        except Exception as e:
            print(f"[-] خطأ في الاتصال: {e}")
            return []

    def build_interface(self, items):
        print(f"[+] معالجة {len(items)} هدفاً... جاري بناء الهيكل الرقمي.")
        
        ticker_text = " • ".join([f"🔥 {self.clean_title(i.title.text)}" for i in items[:10]])
        articles_html = ""

        for index, item in enumerate(items[:30]):  # زيادة العدد لـ 30 خبر
            title = self.clean_title(item.title.text)
            news_url = item.link.text
            img_element = item.find('enclosure')
            img_url = img_element.get('url') if img_element else "https://images.pexels.com/photos/1884574/pexels-photo-1884574.jpeg"
            
            # هندسة الكروت الرياضية
            articles_html += f'''
            <div class="shadow-card">
                <div class="badge-live">LIVE • مباشر</div>
                <div class="img-container">
                    <img src="{img_url}" alt="News">
                    <div class="overlay"></div>
                </div>
                <div class="content">
                    <span class="category">🏆 دوري أبطال الظل</span>
                    <h2>{title}</h2>
                    <div class="stats">
                        <span>👁️ {1200 + index * 45} مشاهدة</span>
                        <span>⏱️ {datetime.now().strftime("%H:%M")}</span>
                    </div>
                    <div class="actions">
                        <a href="{self.monetization_link}" class="btn-main">دخول البث المباشر ⚡</a>
                        <a href="{news_url}" class="btn-sub">المصدر</a>
                    </div>
                </div>
            </div>'''

            # حقن إعلاني ذكي كل 4 أخبار
            if (index + 1) % 4 == 0:
                articles_html += f'''
                <div class="mega-promo">
                    <div class="promo-inner">
                        <div class="text">
                            <h3>🎁 مفاجأة اليوم: سحب جوائز المشجعين</h3>
                            <p>اضغط لتسجيل اسمك في السحب المباشر الآن</p>
                        </div>
                        <a href="{self.monetization_link}" class="btn-promo">سجل الآن</a>
                    </div>
                </div>'''

        return self.get_full_template(ticker_text, articles_html)

    def get_full_template(self, ticker, content):
        return f'''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHADOW SPORTS | الرادار الرياضي</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #050505; --surface: #121212; --primary: #00ff88;
            --accent: #ff0055; --text: #e0e0e0;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: var(--bg); font-family: 'Cairo', sans-serif; color: var(--text); line-height: 1.6; }}
        
        header {{ background: rgba(0,0,0,0.9); border-bottom: 2px solid var(--primary); padding: 20px; text-align: center; position: sticky; top: 0; z-index: 100; backdrop-filter: blur(10px); }}
        .logo {{ font-family: 'Orbitron', sans-serif; font-size: 32px; color: var(--primary); text-shadow: 0 0 15px var(--primary); }}
        
        .ticker-wrap {{ background: var(--accent); color: white; padding: 10px 0; overflow: hidden; font-weight: bold; }}
        .ticker-move {{ display: inline-block; white-space: nowrap; animation: move 50s linear infinite; }}
        @keyframes move {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}

        .main-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; padding: 40px 5%; }}
        
        .shadow-card {{ background: var(--surface); border-radius: 20px; overflow: hidden; border: 1px solid #222; transition: 0.3s; position: relative; }}
        .shadow-card:hover {{ transform: translateY(-10px); border-color: var(--primary); box-shadow: 0 10px 30px rgba(0,255,136,0.2); }}
        
        .badge-live {{ position: absolute; top: 15px; left: 15px; background: var(--accent); padding: 5px 15px; border-radius: 50px; font-size: 12px; z-index: 5; animation: blink 1s infinite; font-weight: 900; }}
        @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}

        .img-container {{ height: 220px; position: relative; }}
        .img-container img {{ width: 100%; height: 100%; object-fit: cover; }}
        .overlay {{ position: absolute; bottom: 0; width: 100%; height: 50%; background: linear-gradient(transparent, var(--surface)); }}
        
        .content {{ padding: 25px; }}
        .category {{ color: var(--primary); font-size: 12px; font-weight: bold; text-transform: uppercase; }}
        h2 {{ font-size: 20px; margin: 10px 0; height: 60px; overflow: hidden; color: #fff; }}
        
        .stats {{ display: flex; justify-content: space-between; font-size: 13px; color: #888; margin-bottom: 20px; border-top: 1px solid #222; pt: 10px; }}
        
        .actions {{ display: flex; gap: 10px; }}
        .btn-main {{ flex: 2; background: var(--primary); color: #000; text-decoration: none; text-align: center; padding: 12px; border-radius: 12px; font-weight: 900; transition: 0.3s; }}
        .btn-main:hover {{ background: #fff; transform: scale(1.05); }}
        .btn-sub {{ flex: 1; border: 1px solid #444; color: #fff; text-decoration: none; text-align: center; padding: 12px; border-radius: 12px; font-size: 13px; }}

        .mega-promo {{ grid-column: 1 / -1; background: linear-gradient(90deg, #1a1a1a, #004422); border-radius: 20px; padding: 40px; border: 1px dashed var(--primary); }}
        .promo-inner {{ display: flex; justify-content: space-between; align-items: center; }}
        .btn-promo {{ background: white; color: black; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: 900; box-shadow: 0 0 20px rgba(255,255,255,0.4); }}

        @media (max-width: 768px) {{ .main-grid {{ grid-template-columns: 1fr; }} .promo-inner {{ flex-direction: column; gap: 20px; text-align: center; }} }}
    </style>
</head>
<body>
    <header><div class="logo">SHΔDØW SPORTS</div></header>
    <div class="ticker-wrap"><div class="ticker-move">{ticker}</div></div>
    <main class="main-grid">{content}</main>
    <footer style="padding: 50px; text-align: center; color: #444;">
        <p>TERMINAL V99 // DATA EXPLOIT // 2026</p>
    </footer>
</body>
</html>'''

    def execute(self):
        items = self.fetch_data()
        if items:
            html_output = self.build_interface(items)
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(html_output)
            print(f"[+] المهمة اكتملت. تم توليد الترسانة في index.html")
        else:
            print("[-] فشل المهمة: لم يتم العثور على بيانات.")

if __name__ == "__main__":
    mission = ShadowSportsEngine()
    mission.execute()
