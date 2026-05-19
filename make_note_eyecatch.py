from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "assets" / "ai-starter-note-thumbnail.png"
OUT = ROOT / "assets" / "note-eyecatch-ai-starter.png"

img = Image.open(SRC).convert("RGB")
width, height = 1280, 670

bg = img.resize((width, height), Image.Resampling.LANCZOS).filter(ImageFilter.GaussianBlur(14))
canvas = Image.alpha_composite(
    bg.convert("RGBA"),
    Image.new("RGBA", (width, height), (255, 248, 232, 180)),
)

# Crop out the AI-generated text from the original vertical image and keep papa/laptop.
crop = img.crop((55, 355, 1010, 1260))
right_h = 700
right_w = int(crop.width * right_h / crop.height)
right = crop.resize((right_w, right_h), Image.Resampling.LANCZOS)
canvas.alpha_composite(right.convert("RGBA"), (width - right_w + 70, -8))

# Readability wash on the left.
canvas.alpha_composite(Image.new("RGBA", (720, height), (255, 250, 238, 224)), (0, 0))

draw = ImageDraw.Draw(canvas)
font_bold = r"C:\Windows\Fonts\NotoSansJP-VF.ttf"
font_serif = r"C:\Windows\Fonts\NotoSerifJP-VF.ttf"
font_main = ImageFont.truetype(font_bold, 58)
font_main2 = ImageFont.truetype(font_bold, 54)
font_sub = ImageFont.truetype(font_bold, 31)
font_small = ImageFont.truetype(font_bold, 24)
font_note = ImageFont.truetype(font_serif, 22)

ink = (22, 55, 61)
green = (15, 118, 110)
muted = (83, 98, 96)
line = (213, 199, 164)
yellow = (246, 196, 83)

label = "30〜60代のAI初心者へ"
draw.rounded_rectangle((58, 54, 360, 98), radius=20, fill=(227, 244, 239), outline=(170, 213, 204), width=2)
draw.text((78, 59), label, font=font_small, fill=green)

x = 58
y = 140
draw.text((x, y), "AIに乗り遅れた", font=font_main, fill=ink)
draw.text((x, y + 76), "かも、と思った人へ", font=font_main2, fill=ink)

for offset in range(3):
    draw.line((x + 4, y + 158 + offset, x + 492, y + 150 + offset), fill=yellow, width=3)

sub_lines = ["ゼロ知識から試した", "無料スターターキットを配布中"]
sy = y + 196
for i, line_text in enumerate(sub_lines):
    draw.text((x, sy + i * 44), line_text, font=font_sub, fill=green if i == 1 else muted)

bullet_y = 520
items = ["無料", "クレカ不要", "スマホOK", "全文コピーで使える"]
bx = x
for item in items:
    tw = draw.textlength(item, font=font_small)
    draw.rounded_rectangle((bx, bullet_y, bx + tw + 32, bullet_y + 42), radius=18, fill=(255, 255, 255, 228), outline=line, width=2)
    draw.text((bx + 16, bullet_y + 4), item, font=font_small, fill=ink)
    bx += int(tw) + 48

draw.text((x, 592), "ChatGPT / Claudeに貼って、まず1つ試せます", font=font_note, fill=muted)

OUT.parent.mkdir(parents=True, exist_ok=True)
canvas.convert("RGB").save(OUT, quality=95)
print(OUT)
