#!/usr/bin/env python3
"""
Generate tasteful gradient placeholder images (pure stdlib, no PIL).

These are temporary stand-ins so the site looks polished before the real
photographs are added. Replace any file in assets/images/ with your own
photo of the same name (browsers display JPEG/PNG/WebP regardless of the
.png extension, so you can simply overwrite the file).
"""
import zlib
import struct
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
os.makedirs(OUT, exist_ok=True)


def write_png(path, width, height, top, bottom, accent=None):
    """Write a smooth vertical-gradient PNG with an optional soft accent glow."""
    tr, tg, tb = top
    br, bg, bb = bottom
    raw = bytearray()
    for y in range(height):
        t = y / max(1, height - 1)
        # ease the gradient a little for a softer look
        te = t * t * (3 - 2 * t)
        r = int(tr + (br - tr) * te)
        g = int(tg + (bg - tg) * te)
        b = int(tb + (bb - tb) * te)
        row = bytearray()
        row.append(0)  # filter type 0 (None)
        if accent:
            # subtle diagonal lightening band for a touch of depth
            ar, ag, ab = accent
            for x in range(width):
                d = ((x / width) * 0.5 + (1 - t) * 0.5)
                glow = max(0.0, 0.35 - abs(d - 0.62)) * 1.1
                row.append(min(255, int(r + (ar - r) * glow)))
                row.append(min(255, int(g + (ag - g) * glow)))
                row.append(min(255, int(b + (ab - b) * glow)))
        else:
            pix = bytes((r, g, b)) * width
            row.extend(pix)
        raw.extend(row)

    def chunk(typ, data):
        c = struct.pack(">I", len(data)) + typ + data
        return c + struct.pack(">I", zlib.crc32(typ + data) & 0xFFFFFFFF)

    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    idat = zlib.compress(bytes(raw), 9)
    png = sig + chunk(b"IHDR", ihdr) + chunk(b"IDAT", idat) + chunk(b"IEND", b"")
    with open(os.path.join(OUT, path), "wb") as f:
        f.write(png)
    print("wrote", path, f"{width}x{height}")


# palette (earthy / countryside)
SAGE_T, SAGE_B = (124, 142, 110), (74, 92, 66)
CREAM_T, CREAM_B = (242, 235, 220), (214, 200, 174)
TERRA_T, TERRA_B = (196, 124, 92), (150, 86, 60)
SKY_T, SKY_B = (168, 196, 206), (108, 144, 162)
FOREST_T, FOREST_B = (96, 120, 92), (52, 74, 56)
STONE_T, STONE_B = (208, 200, 188), (150, 140, 126)
GOLD = (224, 198, 150)

# name, w, h, top, bottom, accent
JOBS = [
    ("hero.png", 1600, 900, FOREST_T, FOREST_B, GOLD),
    ("og-image.png", 1200, 630, SAGE_T, SAGE_B, GOLD),
    ("cottage-exterior.png", 1200, 800, STONE_T, STONE_B, GOLD),
    ("garden.png", 1200, 800, SAGE_T, SAGE_B, GOLD),
    ("countryside-view.png", 1200, 800, SKY_T, SKY_B, None),
    ("lounge.png", 1200, 800, CREAM_T, CREAM_B, None),
    ("second-lounge.png", 1200, 800, STONE_T, STONE_B, None),
    ("kitchen.png", 1200, 800, CREAM_T, CREAM_B, None),
    ("dining.png", 1200, 800, STONE_T, STONE_B, GOLD),
    ("bedroom-1.png", 1200, 800, CREAM_T, CREAM_B, None),
    ("bedroom-2.png", 1200, 800, STONE_T, STONE_B, None),
    ("bedroom-3.png", 1200, 800, SKY_T, SKY_B, None),
    ("bedroom-4.png", 1200, 800, SAGE_T, SAGE_B, None),
    ("annexe.png", 1200, 800, STONE_T, STONE_B, GOLD),
    ("bathroom.png", 1200, 800, SKY_T, SKY_B, None),
    ("wye-valley.png", 1200, 800, FOREST_T, FOREST_B, GOLD),
    ("ross-on-wye.png", 1200, 800, TERRA_T, TERRA_B, GOLD),
    ("walking.png", 1200, 800, FOREST_T, FOREST_B, None),
    ("dog-friendly.png", 1200, 800, SAGE_T, SAGE_B, GOLD),
    ("blog-wye-valley.png", 1200, 800, FOREST_T, FOREST_B, GOLD),
    ("blog-walks.png", 1200, 800, SAGE_T, SAGE_B, None),
    ("blog-dog-friendly.png", 1200, 800, STONE_T, STONE_B, GOLD),
    ("blog-ross-market.png", 1200, 800, TERRA_T, TERRA_B, GOLD),
    ("blog-seasons.png", 1200, 800, SKY_T, SKY_B, GOLD),
    ("blog-local-food.png", 1200, 800, CREAM_T, CREAM_B, GOLD),
    ("map.png", 1200, 600, SAGE_T, SAGE_B, None),
]

for job in JOBS:
    write_png(*job)

print("done")
