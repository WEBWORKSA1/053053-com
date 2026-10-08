#!/usr/bin/env python3
"""Generates assets/img/og.png (1200x630 social card). Needs Pillow; run by the build workflow."""
import os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1200, 630
im = Image.new("RGB", (W, H), "#070d1a"); d = ImageDraw.Draw(im)
for i in range(H): d.line([(0, i), (W, i)], fill=(7 + i // 40, 13 + i // 30, 26 + i // 20))
def f(sz, b=True):
    for p in (["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"] if b else ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]):
        try: return ImageFont.truetype(p, sz)
        except OSError: pass
    return ImageFont.load_default()
d.rounded_rectangle([80, 90, 230, 240], radius=36, fill="#2ee6c5"); d.text((155, 165), "053", font=f(52), fill="#04121e", anchor="mm")
d.text((270, 110), "053053", font=f(96), fill="#e8eefb")
d.text((272, 225), "Number Intelligence & Scam Shield", font=f(40, False), fill="#2ee6c5")
d.text((80, 330), "Who called you from 053?", font=f(64), fill="#e8eefb")
d.text((80, 420), "TR Turkcell · IL Hot Mobile · KR Daegu · JP Hamamatsu · NL Enschede · UTC+05:30", font=f(30, False), fill="#a7b4cf")
d.text((80, 520), "Free lookup · scam red flags · report · get protected", font=f(32, False), fill="#ffb547")
im.save(os.path.join(ROOT, "assets/img/og.png"), optimize=True)
print("og.png written")
