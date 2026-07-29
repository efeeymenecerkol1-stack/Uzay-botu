import os
from google import genai

# Yeni Google GenAI istemcisini başlat
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def uzay_bilgisi_uret():
    prompt = """
    Bugün uzayda yaşanan tarihi bir olayı özetle ve ardından uzayla ilgili aşırı şaşırtıcı 1 ilginç bilgi ver. 
    TikTok videosu için uygun, akıcı, dikkat çekici ve en fazla 45 saniyede okunabilecek bir Türkçe metin yaz.
    """
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    print("--- GÜNÜN UZAY ÖZETİ VE BİLGİSİ ---")
    print(response.text)

if __name__ == "__main__":
    uzay_bilgisi_uret()
    
