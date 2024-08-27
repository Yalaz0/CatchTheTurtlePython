import turtle
import random
import time

# Ekranı oluştur ve yapılandır
ekran = turtle.Screen()
ekran.title("Tıklama Oyunu")
ekran.bgcolor("light blue")
ekran.setup(width=700, height=650)

# Skor ve sayaç için global değişkenler
skor = 0
sure = 30

# Skor tablosu oluştur
skor_tahtasi = turtle.Turtle()
skor_tahtasi.hideturtle()
skor_tahtasi.penup()
skor_tahtasi.goto(-250, 250)
skor_tahtasi.write(f"Skor: {skor}", align="left", font=("Arial", 16, "normal"))

# Sayaç oluştur
sayaç_tahtasi = turtle.Turtle()
sayaç_tahtasi.hideturtle()
sayaç_tahtasi.penup()
sayaç_tahtasi.goto(200, 250)
sayaç_tahtasi.write(f"Süre: {sure}", align="left", font=("Arial", 16, "normal"))

# Tıklanacak kaplumbağa nesnesini oluştur
tıklanacak_turtle = turtle.Turtle()
tıklanacak_turtle.shape("turtle")
tıklanacak_turtle.color("green")
tıklanacak_turtle.penup()
tıklanacak_turtle.speed(0)

# Skor güncelleme fonksiyonu
def skor_guncelle():
    global skor
    skor += 1
    skor_tahtasi.clear()
    skor_tahtasi.write(f"Skor: {skor}", align="left", font=("Arial", 16, "normal"))

# Sayaç güncelleme fonksiyonu
def sayaç_guncelle():
    global sure
    sure -= 1
    sayaç_tahtasi.clear()
    sayaç_tahtasi.write(f"Süre: {sure}", align="left", font=("Arial", 16, "normal"))

# Kaplumbağanın konumunu rastgele olarak güncelle
def konum_guncelle():
    x = random.randint(-250, 250)
    y = random.randint(-200, 200)
    tıklanacak_turtle.goto(x, y)

# Tıklama işlemi
def tıklama_islemi(x, y):
    if sure > 0:
        skor_guncelle()
        konum_guncelle()

# Tıklama olayını dinle
tıklanacak_turtle.onclick(tıklama_islemi)

while sure > 0:
    konum_guncelle()
    time.sleep(1)
    sayaç_guncelle()

# Oyun bitti
sayaç_tahtasi.clear()
sayaç_tahtasi.write("Oyun Bitti!", align="left", font=("Arial", 16, "normal"))
tıklanacak_turtle.hideturtle()

# Ekranı kapat
ekran.mainloop()
