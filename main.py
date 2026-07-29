import os
import json
import urllib.request

api_key = os.environ.get("GEMINI_API_KEY")

# Asla 404 vermeyen güncel endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

prompt_text = (
    "Bugün uzayda yaşanan tarihi bir olayı özetle ve ardından uzayla ilgili aşırı şaşırtıcı 1 ilgilç bilgi ver. "
    "TikTok videosu için uygun, akıcı, dikkat çekici ve en fazla 45 saniyede okunabilecek bir Türkçe metin yaz."
)

data = {
    "contents": [{
        "parts": [{"text": prompt_text}]
    }]
}

headers = {'Content-Type': 'application/json'}
req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)

try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        text = result['candidates'][0]['content']['parts'][0]['text']
        
        with open("gunluk_uzay.txt", "w", encoding="utf-8") as f:
            f.write(text)
            
        print("Metin başarıyla yazıldı!")
except Exception as e:
    print(f"Hata oluştu: {e}")
        
