import turtle
import math

# --- Ayarlar ---
ekran = turtle.Screen()
ekran.setup(width=800, height=500)
ekran.bgcolor("#E30A17")
ekran.title("Türk Bayrağı - Ortalanmış Hilal ve Yıldız")

kalem = turtle.Turtle()
kalem.speed(0)
kalem.hideturtle()

# --- Orijinal (geliştirme sırasında kullandığımız) konumlar ve boyutlar ---
# (Bu değerleri dilediğiniz gibi değiştirin; program otomatik olarak ortalar.)
outer_center = (-100, -120); R_outer = 120   # beyaz dış daire (hilal için)
inner_center = (-70, -96);   R_inner = 96    # kırmızı iç daire (oyma)
star_center = (70, 40);      star_r = 40     # yıldızın merkezi ve dış yarıçapı

shapes = [
    ("circle", outer_center[0], outer_center[1], R_outer),
    ("circle", inner_center[0], inner_center[1], R_inner),
    ("circle", star_center[0], star_center[1], star_r)  # yıldız için de kabaca kutu alıyoruz
]

# --- Bounding box hesapla ---
min_x = min(cx - r for (_t, cx, cy, r) in shapes)
max_x = max(cx + r for (_t, cx, cy, r) in shapes)
min_y = min(cy - r for (_t, cx, cy, r) in shapes)
max_y = max(cy + r for (_t, cx, cy, r) in shapes)

bbox_center_x = (min_x + max_x) / 2
bbox_center_y = (min_y + max_y) / 2

# ekran merkezi (turtle koordinat sistemi 0,0 ortadadır) -> hedef merkez (0,0)
# o halde gerekli kaydırma:
tx = -bbox_center_x
ty = -bbox_center_y

# --- Yardımcı fonksiyonlar ---
def draw_filled_circle_center(cx, cy, r, color):
    kalem.penup()
    kalem.goto(cx, cy - r)   # turtle.circle çizerken başlangıç noktası bu şekilde merkezli olur
    kalem.setheading(0)
    kalem.color(color)
    kalem.pendown()
    kalem.begin_fill()
    kalem.circle(r)
    kalem.end_fill()
    kalem.penup()

def draw_filled_star(cx, cy, outer_r):
    # 10 noktalı yıldız poligonu (dolu)
    kalem.color("white")
    points = []
    for i in range(10):
        angle = math.radians(i * 36 - 90)  # -90 ile bir uç yukarı baksın; istersen ayarla
        radius = outer_r if i % 2 == 0 else outer_r * 0.382
        px = cx + radius * math.cos(angle)
        py = cy + radius * math.sin(angle)
        points.append((px, py))

    kalem.penup()
    kalem.goto(points[0])
    kalem.pendown()
    kalem.begin_fill()
    for p in points[1:]:
        kalem.goto(p)
    kalem.goto(points[0])
    kalem.end_fill()
    kalem.penup()

# --- Çizimleri yap (kaydırma uygulanmış koordinatlarla) ---
# Beyaz dış daire
draw_filled_circle_center(outer_center[0] + tx, outer_center[1] + ty, R_outer, "white")

# İç kırmızı daire (arka plan rengi ile aynı)
draw_filled_circle_center(inner_center[0] + tx, inner_center[1] + ty, R_inner, "#E30A17")

# Yıldız (dolu)
draw_filled_star(star_center[0] + tx, star_center[1] + ty, star_r)

turtle.done()