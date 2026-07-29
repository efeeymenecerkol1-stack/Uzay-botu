import os
import google.generativeai as genai

# Gemini API yapılandırması
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def uzay_bilgisi_uret():
    # Güncel ve standart model adı
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = """
    Bugün uzayda yaşanan tarihi bir olayı özetle ve ardından uzayla ilgili aşırı şaşırtıcı 1 ilginç bilgi ver. 
    TikTok videosu için uygun, akıcı, dikkat çekici ve en fazla 45 saniyede okunabilecek bir Türkçe metin yaz.
    """
    response = model.generate_content(prompt)
    print("--- GÜNÜN UZAY ÖZETİ VE BİLGİSİ ---")
    print(response.text)

if __name__ == "__main__":
    uzay_bilgisi_uret()

