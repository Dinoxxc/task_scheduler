# quotes.py
import random

def get_random_quote(lang='id'):
    """
    Mengembalikan kutipan motivasi secara acak.
    Tersedia untuk dua bahasa: English (en) dan Indonesia (id).
    """
    quotes_id = [
        "Tetap semangat, setiap tugas yang kamu selesaikan mendekatkanmu pada kesuksesan!",
        "Teruslah berusaha, karena kegigihan adalah kunci utama keberhasilan.",
        "Perjalanan seribu mil dimulai dari satu langkah kecil.",
        "Kegagalan adalah jalan memutar, bukan jalan buntu.",
        "Satu-satunya cara untuk melakukan pekerjaan yang hebat adalah mencintai apa yang kamu lakukan."
    ]
    quotes_en = [
        "Keep your spirits up! Every task you finish brings you closer to success!",
        "Never give up, persistence is the key to achieving your goals.",
        "A journey of a thousand miles begins with a single step.",
        "Failure is a detour, not a dead-end street.",
        "The only way to do great work is to love what you do."
    ]

    if lang == 'en':
        return random.choice(quotes_en)
    return random.choice(quotes_id)
