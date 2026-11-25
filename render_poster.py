#!/usr/bin/env python3
"""Render the news-image-20261125 poster: 'Wednesday 25 November 2026'.

Visual language: a daylight wire desk - warm paper ground, an ink-black
masthead band, signal-red rules and number chips, teal accents, linocut
scenes drawn with heavy black outlines. Deliberately NOT the cream
newspaper front page the field copies, and NOT the navy night-desk of
the previous day. All 41 stories were first reported Wed 25 Nov 2026
in some time zone (see BRIEF.md for the verification basis of each
one). Two 24-Nov stories are named only in the small DATE CHECK box
as excluded.
"""
import hashlib
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")
PREVIEW = os.path.join(HERE, "preview-300.png")

# ---------------------------------------------------------------- palette
PAPER = (250, 246, 238)
CARD = (255, 253, 247)
INK = (22, 22, 26)
INK2 = (48, 48, 54)
RED = (192, 39, 30)
RED_D = (150, 28, 22)
TEAL = (14, 107, 107)
TEAL_L = (120, 178, 178)
OCHRE = (217, 164, 65)
MUTED = (110, 108, 100)
SKY = (205, 226, 232)
LAND = (18, 92, 92)

REGION_COLORS = {
    "EUROPE": (96, 140, 200),
    "MIDDLE EAST": (217, 164, 65),
    "ASIA": (192, 39, 30),
    "AFRICA": (90, 150, 90),
    "AMERICAS": (60, 170, 165),
    "OCEANIA": (150, 110, 200),
    "GLOBAL": (120, 120, 128),
}

# ---------------------------------------------------------------- fonts
DEJ = "/usr/share/fonts/truetype/dejavu/"
NOTO = "/usr/share/fonts/truetype/noto/"


def _load(path, size, fallback):
    try:
        return ImageFont.truetype(path, size)
    except (OSError, IOError):
        return ImageFont.truetype(fallback, size)


def f_display(size):
    return _load(NOTO + "NotoSerifDisplay-Bold.ttf", size,
                 DEJ + "DejaVuSerif-Bold.ttf")


def f_serif(size):
    return _load(DEJ + "DejaVuSerif.ttf", size, DEJ + "DejaVuSans.ttf")


def f_serif_b(size):
    return _load(DEJ + "DejaVuSerif-Bold.ttf", size,
                 DEJ + "DejaVuSans-Bold.ttf")


def f_sans(size):
    return _load(DEJ + "DejaVuSans.ttf", size, DEJ + "DejaVuSans.ttf")


def f_sans_b(size):
    return _load(DEJ + "DejaVuSans-Bold.ttf", size, DEJ + "DejaVuSans.ttf")


# ---------------------------------------------------------------- stories
# n, region, place, headline, body (heroes only), source, scene, lon, lat
HEROES = [
    (1, "OCEANIA", "Canberra", "CPI jumps to 4.9%, jobless 4.9%",
     "October CPI 4.9% y/y, trimmed mean 3.8%; jobless 4.9%, highest "
     "since Oct 2021.", "ABS", "chart", 149.1, -35.3),
    (2, "MIDDLE EAST", "Gaza City", "Israel launches ground offensive in central Gaza",
     "First major ground push beyond the 'Yellow Line' despite the "
     "ceasefire.", "Al Jazeera", "offensive", 34.5, 31.5),
    (3, "AMERICAS", "Langley", "CIA hit by cyberattack",
     "An unclassified CIA system was breached, an AP source says; "
     "CNN reported it on 25 Nov.", "AP", "server", -77.1, 38.9),
]

FEATURED = [
    (4, "ASIA", "Mumbai", "Sooryavanshi, 15, smashes 204 off 53 balls",
     "", "BBC", "cricket", 72.8, 19.1),
    (5, "OCEANIA", "Canberra", "Australia says sorry to LGBTQ veterans",
     "", "Reuters", "apology", 149.1, -35.3),
    (6, "ASIA", "New Delhi", "Modi, Merz talk up strategic partnership",
     "", "PTI", "handshake", 77.2, 28.6),
    (7, "MIDDLE EAST", "Sanaa", "Houthis threaten Saudi ports over Hodeidah order",
     "", "Al Jazeera", "ports", 44.2, 15.4),
    (8, "MIDDLE EAST", "Doha", "Qatar urges restraint, dialogue on Iran",
     "", "Al Jazeera", "dialogue", 51.5, 25.3),
    (9, "EUROPE", "London", "Two held over break-in at Prince William's home",
     "", "Newsreel", "crown", -0.1, 51.5),
    (10, "AFRICA", "Ituri", "WHO pulls staff from Ebola hospital",
     "", "WHO", "hospital", 29.5, 1.8),
    (11, "ASIA", "Chandigarh", "Akalis & BJP reunite for Punjab polls",
     "", "Times of India", "ballot", 76.8, 30.7),
    (12, "OCEANIA", "Wellington", "Flavell slams ACT's Māori seats vote idea",
     "", "RNZ", "parliament", 174.8, -41.3),
    (13, "GLOBAL", "Markets", "Gold slips as US inflation data looms",
     "", "Reuters", "gold", 0.0, 20.0),
]

ALSO_ON = [
    (14, "ASIA", "Gukesh holds Sindarov in title Game 1", "The Hindu", 77.2, 28.6),
    (15, "ASIA", "Sensex drops 1,484; Nifty below 25,400", "Roundup", 72.8, 19.1),
    (16, "MIDDLE EAST", "Houthis report deaths after Saudi strikes", "Roundup", 44.2, 15.4),
    (17, "MIDDLE EAST", "Ras Al Khaimah crash kills 11", "Roundup", 56.0, 25.8),
    (18, "ASIA", "Nepal FM hails PM Shah's India visit", "Roundup", 85.3, 27.7),
    (19, "ASIA", "India's space economy to hit $40\u201345bn", "Roundup", 77.2, 28.6),
    (20, "ASIA", "APEDA ships first frozen peas to Qatar", "Roundup", 78.5, 27.5),
    (21, "ASIA", "Ben Stokes signs up for IPL 2027 auction", "Cricbuzz", 77.2, 28.6),
    (22, "AMERICAS", "Nvidia's Huang admitted code breach", "Reuters", -122.0, 37.4),
    (23, "EUROPE", "Putin: retaliation 'inevitable'", "Roundup", 37.6, 55.8),
    (24, "EUROPE", "Russia: ship drone hits are 'terrorism'", "BD Times", 30.3, 59.9),
    (25, "MIDDLE EAST", "Saudi bloc condemns Riyadh tower attack", "Roundup", 46.7, 24.7),
    (26, "MIDDLE EAST", "Iraq orders Baghdad to run Kurd oilfields", "Roundup", 44.4, 33.3),
    (27, "MIDDLE EAST", "Israeli drones kill seven in Gaza", "Al Jazeera", 34.5, 31.5),
    (28, "MIDDLE EAST", "Gaza kids mark World Children's Day", "Al Jazeera", 34.5, 31.4),
    (29, "AFRICA", "Zimbabwean convicted for Ukraine bid", "Roundup", 28.0, -26.2),
    (30, "MIDDLE EAST", "Gaza toll 74,746, WAFA says", "BD Times", 34.5, 31.5),
    (31, "AMERICAS", "Anthropic shares fall below $83 IPO price", "Roundup", -122.4, 37.8),
    (32, "ASIA", "Rahul Gandhi backs India\u2013Israel ties", "Al Jazeera", 77.2, 28.6),
    (33, "OCEANIA", "Pacific states step up El Ni\u00f1o drought response", "RNZ", 178.0, -17.7),
    (34, "OCEANIA", "PNG outrage over five women 'buried alive'", "RNZ", 147.2, -9.5),
    (35, "OCEANIA", "Probe call after Papuan student leader dies", "RNZ", 140.7, -2.5),
    (36, "OCEANIA", "NZ dollar hits 17-year low", "RNZ", 174.8, -41.3),
    (37, "OCEANIA", "Waddington flies NZ flag at Miss Universe", "RNZ", 174.8, -36.8),
    (38, "OCEANIA", "AI blamed as cyber breaches surge", "RNZ", 174.8, -41.3),
    (39, "OCEANIA", "Deepest volcanic blast found in Mariana Trench", "RNZ", 145.0, 11.4),
    (40, "GLOBAL", "Star system 'should not exist' found", "SciTechDaily", 0.0, 45.0),
    (41, "GLOBAL", "Child attacks: a third are in Palestine", "Al Jazeera", 35.2, 31.8),
]

REGION_COUNTS = {"EUROPE": 3, "MIDDLE EAST": 10, "ASIA": 10,
                 "AFRICA": 2, "AMERICAS": 3, "OCEANIA": 10, "GLOBAL": 3}
TOTAL_STORIES = 41
N_REGIONS = 7

TIMELINE = [
    ("00:30 GMT", "Australia CPI 4.9% lands"),
    ("MORNING", "LGBTQ veterans apology"),
    ("MIDDAY", "204 off 53 balls"),
    ("AFTERNOON", "Sensex \u22121,484"),
    ("19:45 CET", "Hera's Dimorphos reveal"),
    ("NIGHT", "CIA breach reported"),
]

KPIS = [
    ("4.9%", "AU CPI, October"),
    ("4.9%", "AU jobless rate"),
    ("204 off 53", "Sooryavanshi, aged 15"),
    ("1,484", "Sensex points lost"),
    ("11", "killed, RAK crash"),
    ("7", "killed, Gaza drones"),
]

DATE_CHECK = [
    "Nepal 5.6 quake \u2014 struck Tue 24 Nov 07:17 local, "
    "NOT in this edition.",
    "Huawei guilty verdict \u2014 jury verdict Tue 24 Nov, "
    "NOT in this edition.",
]

SOURCES_LINE = ("Sources: Reuters \u00b7 AP \u00b7 Al Jazeera \u00b7 BBC "
                "\u00b7 RNZ \u00b7 ABS \u00b7 WHO \u00b7 The Hindu \u00b7 PTI "
                "\u00b7 Cricbuzz \u2014 Original drawings")

# ---------------------------------------------------------------- helpers
PLACEMENTS = []  # (text bbox, card box) pairs for the clearance test


def wrap(text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if font.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_lines(text, font, max_w, max_lines):
    lines = wrap(text, font, max_w)
    if len(lines) <= max_lines:
        return lines
    lines = lines[:max_lines]
    while lines and font.getlength(lines[-1] + " \u2026") > max_w:
        lines[-1] = lines[-1].rsplit(" ", 1)[0] if " " in lines[-1] else ""
    lines[-1] = (lines[-1] + " \u2026").strip()
    return lines


def text(d, xy, s, font, fill, box=None, anchor="la"):
    d.text(xy, s, font=font, fill=fill, anchor=anchor)
    x, y = xy
    w = font.getlength(s)
    asc, desc = font.getmetrics()
    if anchor == "la":
        bbox = (x, y, x + w, y + asc + desc)
    elif anchor == "ma":
        bbox = (x - w / 2, y, x + w / 2, y + asc + desc)
    else:
        bbox = (x - w, y, x, y + asc + desc)
    if box is not None:
        PLACEMENTS.append((bbox, box))
    return bbox


# ------------------------------------------------------- linocut scenes
def _rel(box, fx0, fy0, fx1, fy1):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    return (x0 + fx0 * w, y0 + fy0 * h, x0 + fx1 * w, y0 + fy1 * h)


def draw_scene(d, box, kind):
    """Bold flat illustration with heavy ink outlines (linocut style)."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    sky = {"chart": (232, 222, 190), "offensive": (214, 200, 170),
           "server": (205, 226, 232), "cricket": (196, 222, 186),
           "apology": (232, 208, 214), "handshake": (205, 226, 232),
           "ports": (170, 205, 222), "dialogue": (232, 222, 190),
           "crown": (232, 214, 178), "hospital": (232, 232, 232),
           "ballot": (205, 226, 232), "parliament": (232, 222, 190),
           "gold": (232, 214, 178)}[kind]
    d.rectangle(box, fill=sky, outline=INK, width=2)
    d.rectangle([x0, y0 + h * 0.80, x1, y1], fill=(70, 70, 76))

    def R(fx0, fy0, fx1, fy1, fill, outline=INK, width=2):
        d.rectangle(_rel(box, fx0, fy0, fx1, fy1), fill=fill,
                    outline=outline, width=width)

    def E(fx0, fy0, fx1, fy1, fill, outline=INK, width=2):
        d.ellipse(_rel(box, fx0, fy0, fx1, fy1), fill=fill,
                  outline=outline, width=width)

    def P(pts, fill, outline=INK):
        d.polygon([(x0 + fx * w, y0 + fy * h) for fx, fy in pts],
                  fill=fill, outline=outline)

    def L(p1, p2, fill, width=3):
        d.line([x0 + p1[0] * w, y0 + p1[1] * h,
                x0 + p2[0] * w, y0 + p2[1] * h], fill=fill, width=width)

    if kind == "chart":
        L((0.08, 0.72), (0.08, 0.14), INK, 3)
        L((0.08, 0.72), (0.92, 0.72), INK, 3)
        for i, ht in enumerate((0.22, 0.34, 0.48, 0.62)):
            R(0.16 + i * 0.19, 0.72 - ht, 0.28 + i * 0.19, 0.72,
              RED if i == 3 else TEAL)
        L((0.14, 0.55), (0.38, 0.40), RED, 3)
        L((0.38, 0.40), (0.62, 0.46), RED, 3)
        L((0.62, 0.46), (0.86, 0.18), RED, 3)
        E(0.82, 0.12, 0.90, 0.24, RED)
    elif kind == "offensive":
        R(0.10, 0.52, 0.62, 0.70, (90, 96, 104))
        R(0.30, 0.34, 0.52, 0.54, (90, 96, 104))
        L((0.52, 0.40), (0.90, 0.40), INK, 4)
        E(0.16, 0.68, 0.26, 0.80, INK)
        E(0.34, 0.68, 0.44, 0.80, INK)
        E(0.52, 0.68, 0.62, 0.80, INK)
        P([(0.70, 0.18), (0.78, 0.34), (0.62, 0.34)], OCHRE)
        E(0.80, 0.08, 0.94, 0.26, OCHRE)
    elif kind == "server":
        R(0.20, 0.14, 0.80, 0.78, INK2)
        for i in range(3):
            R(0.26, 0.20 + i * 0.19, 0.74, 0.32 + i * 0.19, CARD,
              outline=INK, width=2)
            E(0.30, 0.23 + i * 0.19, 0.34, 0.29 + i * 0.19, TEAL)
            E(0.64, 0.23 + i * 0.19, 0.68, 0.29 + i * 0.19, RED)
        L((0.84, 0.20), (0.84, 0.62), RED, 4)
        P([(0.80, 0.16), (0.88, 0.16), (0.84, 0.10)], RED)
    elif kind == "cricket":
        L((0.12, 0.78), (0.88, 0.78), INK, 3)
        for fx in (0.30, 0.38, 0.46):
            R(fx, 0.30, fx + 0.045, 0.78, OCHRE)
        R(0.27, 0.24, 0.53, 0.30, OCHRE)
        P([(0.60, 0.16), (0.70, 0.16), (0.62, 0.62), (0.54, 0.62)],
          (150, 110, 60))
        E(0.74, 0.58, 0.88, 0.78, RED)
        if h >= 40:
            d.text((x0 + w * 0.81, y0 + h * 0.60), "204",
                   font=f_sans_b(max(10, int(h * 0.20))), fill=CARD,
                   anchor="mm")
    elif kind == "apology":
        P([(0.50, 0.10), (0.62, 0.26), (0.80, 0.26), (0.66, 0.40),
           (0.72, 0.58), (0.50, 0.48), (0.28, 0.58), (0.34, 0.40),
           (0.20, 0.26), (0.38, 0.26)], OCHRE)
        E(0.42, 0.28, 0.58, 0.46, TEAL)
        R(0.30, 0.62, 0.70, 0.78, RED)
        if h >= 40:
            d.text((x0 + w * 0.50, y0 + h * 0.70), "SORRY",
                   font=f_sans_b(max(9, int(h * 0.13))), fill=CARD,
                   anchor="mm")
    elif kind == "handshake":
        R(0.10, 0.30, 0.42, 0.62, CARD)
        R(0.58, 0.30, 0.90, 0.62, CARD)
        P([(0.42, 0.30), (0.58, 0.30), (0.58, 0.62), (0.42, 0.62)],
          OCHRE)
        L((0.14, 0.46), (0.42, 0.46), INK, 3)
        L((0.58, 0.46), (0.86, 0.46), INK, 3)
        E(0.44, 0.12, 0.56, 0.26, TEAL)
        E(0.76, 0.60, 0.90, 0.78, RED)
    elif kind == "ports":
        R(0.08, 0.55, 0.92, 0.72, (90, 96, 104))
        R(0.30, 0.34, 0.50, 0.56, RED)
        R(0.52, 0.42, 0.68, 0.56, OCHRE)
        L((0.18, 0.30), (0.18, 0.56), INK, 3)
        P([(0.18, 0.30), (0.38, 0.36), (0.18, 0.42)], TEAL)
        for fy in (0.74, 0.80):
            d.arc(_rel(box, 0.0, fy, 1.0, fy + 0.14), 0, 180,
                  fill=CARD, width=2)
        E(0.78, 0.10, 0.92, 0.28, OCHRE)
    elif kind == "dialogue":
        E(0.10, 0.16, 0.52, 0.50, CARD)
        E(0.48, 0.42, 0.90, 0.76, TEAL)
        P([(0.20, 0.46), (0.14, 0.62), (0.30, 0.48)], CARD, outline=INK)
        P([(0.80, 0.72), (0.86, 0.86), (0.70, 0.74)], TEAL, outline=INK)
        L((0.18, 0.30), (0.44, 0.30), INK, 3)
        L((0.18, 0.38), (0.44, 0.38), INK, 3)
        L((0.56, 0.56), (0.82, 0.56), CARD, 3)
        L((0.56, 0.64), (0.82, 0.64), CARD, 3)
    elif kind == "crown":
        R(0.14, 0.30, 0.86, 0.78, CARD)
        P([(0.10, 0.32), (0.50, 0.10), (0.90, 0.32)], RED)
        for fx in (0.20, 0.40, 0.60, 0.80):
            R(fx - 0.035, 0.40, fx + 0.035, 0.78, TEAL_L)
        R(0.44, 0.56, 0.56, 0.78, INK)
        E(0.50, 0.06, 0.58, 0.14, OCHRE)
    elif kind == "hospital":
        R(0.16, 0.20, 0.84, 0.78, CARD)
        R(0.44, 0.26, 0.56, 0.58, RED)
        R(0.32, 0.36, 0.68, 0.48, RED)
        R(0.20, 0.64, 0.80, 0.72, TEAL)
    elif kind == "ballot":
        R(0.22, 0.36, 0.78, 0.78, CARD)
        R(0.30, 0.28, 0.70, 0.38, INK)
        P([(0.44, 0.10), (0.56, 0.10), (0.50, 0.28)], RED)
        L((0.30, 0.52), (0.42, 0.64), RED, 4)
        L((0.42, 0.64), (0.68, 0.44), RED, 4)
        E(0.80, 0.12, 0.92, 0.28, OCHRE)
    elif kind == "parliament":
        R(0.10, 0.52, 0.90, 0.78, CARD)
        d.pieslice(_rel(box, 0.30, 0.12, 0.70, 0.52), 180, 360,
                   fill=TEAL, outline=INK, width=2)
        for fx in (0.16, 0.36, 0.56, 0.76):
            R(fx, 0.56, fx + 0.07, 0.78, TEAL_L)
        E(0.46, 0.04, 0.54, 0.12, OCHRE)
    elif kind == "gold":
        for i, ht in enumerate((0.30, 0.42, 0.54)):
            R(0.16 + i * 0.24, 0.72 - ht, 0.34 + i * 0.24, 0.72, OCHRE)
        E(0.68, 0.16, 0.90, 0.44, OCHRE)
        if h >= 40:
            d.text((x0 + w * 0.79, y0 + h * 0.30), "$",
                   font=f_sans_b(max(12, int(h * 0.22))), fill=INK,
                   anchor="mm")
        L((0.10, 0.72), (0.90, 0.72), INK, 3)


# ---------------------------------------------------------------- map
CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 80),
     (-80, 73), (-75, 62), (-70, 44), (-75, 35), (-80, 26), (-85, 30),
     (-90, 21), (-97, 16), (-105, 20), (-115, 28), (-125, 40), (-125, 49),
     (-140, 60), (-155, 58), (-165, 60)],
    [(-58, 64), (-45, 60), (-30, 68), (-25, 70), (-40, 76), (-58, 76)],
    [(-80, 10), (-75, 5), (-70, 12), (-60, 10), (-50, 5), (-50, 0),
     (-40, -5), (-35, -10), (-40, -20), (-48, -28), (-55, -35),
     (-65, -40), (-70, -52), (-73, -40), (-72, -20), (-78, -5), (-80, 5)],
    [(-17, 15), (-10, 30), (-5, 35), (10, 37), (20, 32), (32, 31),
     (35, 28), (40, 15), (48, 11), (51, 12), (44, 0), (40, -10),
     (35, -18), (32, -28), (25, -34), (18, -35), (12, -18), (9, 4),
     (-8, 5), (-15, 11)],
    [(-10, 36), (-9, 43), (-2, 48), (0, 50), (5, 53), (8, 57), (10, 59),
     (18, 56), (21, 55), (24, 58), (28, 60), (30, 62), (30, 70),
     (25, 71), (18, 69), (12, 65), (5, 60), (5, 58), (-2, 57), (-5, 50),
     (-10, 44)],
    [(30, 62), (40, 68), (55, 69), (70, 72), (90, 75), (110, 76),
     (130, 72), (150, 70), (170, 66), (178, 65), (170, 60), (160, 55),
     (155, 50), (142, 45), (140, 40), (135, 35), (127, 33), (122, 30),
     (120, 25), (110, 20), (105, 10), (100, 8), (95, 15), (90, 22),
     (85, 20), (80, 13), (77, 8), (72, 20), (66, 25), (60, 25),
     (55, 26), (50, 29), (48, 30), (43, 35), (40, 36), (36, 36),
     (33, 42), (30, 45), (30, 55)],
    [(113, -22), (114, -30), (115, -35), (124, -33), (130, -32),
     (137, -35), (140, -38), (145, -38), (150, -37), (153, -32),
     (153, -27), (150, -22), (146, -19), (142, -15), (142, -11),
     (136, -12), (132, -11), (126, -14), (122, -17), (118, -20)],
    [(95, 5), (100, 0), (105, -5), (110, -7), (115, -8), (120, -10),
     (125, -8), (130, -3), (135, -4), (140, -8)],
    [(-5, 50), (-3, 53), (-5, 56), (-2, 58), (0, 53), (1, 51)],
    [(130, 31), (132, 33), (135, 34), (138, 35), (140, 38), (141, 41),
     (143, 43), (145, 44), (142, 42), (139, 38), (136, 35), (133, 34)],
    [(167, -45), (170, -42), (173, -40), (175, -38), (177, -38),
     (175, -40), (172, -43), (168, -46)],
]


def lonlat_to_xy(lon, lat, area):
    ax0, ay0, ax1, ay1 = area
    x = ax0 + (lon + 170.0) / 360.0 * (ax1 - ax0)
    y = ay0 + (75.0 - lat) / 130.0 * (ay1 - ay0)
    return x, y


# ---------------------------------------------------------------- render
def render():
    PLACEMENTS.clear()
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead band (0-112), ink black
    d.rectangle([0, 0, W, 112], fill=INK)
    d.rectangle([0, 108, W, 112], fill=RED)
    kicker = "THE WORLD IN ONE PICTURE"
    kf = f_sans_b(15)
    kx = (W - kf.getlength(kicker)) / 2
    text(d, (kx, 12), kicker, kf, RED)
    mast = "WEDNESDAY 25 NOVEMBER 2026"
    mf = f_display(50)
    mx = (W - mf.getlength(mast)) / 2
    text(d, (mx, 30), mast, mf, CARD)
    count = "41 STORIES \u00b7 7 REGIONS \u00b7 ALL FROM WEDNESDAY"
    cf = f_sans_b(17)
    cx = (W - cf.getlength(count)) / 2
    text(d, (cx, 84), count, cf, OCHRE)

    # ---- UTC timeline (113-156), paper with red dots
    d.rectangle([0, 113, W, 156], fill=PAPER)
    slot_w = W / 6
    tf = f_sans_b(11)
    ef = f_sans(12)
    for i, (label, event) in enumerate(TIMELINE):
        cx = slot_w * i + slot_w / 2
        d.ellipse([cx - 4, 116, cx + 4, 124], fill=RED)
        text(d, (cx, 126), label, tf, RED, anchor="ma")
        ev = fit_lines(event, ef, slot_w - 14, 1)
        text(d, (cx, 140), ev[0] if ev else "", ef, INK, anchor="ma")
    d.line([12, 156, W - 12, 156], fill=INK, width=2)

    # ---- heroes (158-404): 3 white cards, 2px ink border, red square chips
    hy0, hy1 = 158, 404
    hw, gap = 322, 10
    for i, s in enumerate(HEROES):
        n, region, place, head, body, src, kind, lon, lat = s
        x0 = 12 + i * (hw + gap)
        x1 = x0 + hw
        card = (x0, hy0, x1, hy1)
        d.rectangle(card, fill=CARD, outline=INK, width=2)
        d.rectangle([x0 + 10, hy0 + 10, x0 + 42, hy0 + 42], fill=RED)
        text(d, (x0 + 26, hy0 + 14), str(n), f_sans_b(20), CARD,
             box=card, anchor="ma")
        text(d, (x0 + 50, hy0 + 18), region + " \u00b7 " + place.upper(),
             f_sans_b(12), REGION_COLORS[region], box=card)
        draw_scene(d, (x0 + 10, hy0 + 52, x1 - 10, hy0 + 148), kind)
        hf = f_serif_b(19)
        lines = fit_lines(head, hf, hw - 24, 2)
        y = hy0 + 154
        for ln in lines:
            text(d, (x0 + 12, y), ln, hf, INK, box=card)
            y += 22
        bf = f_sans(12)
        blines = fit_lines(body, bf, hw - 24, 2)
        y = hy0 + 200
        for ln in blines:
            text(d, (x0 + 12, y), ln, bf, INK2, box=card)
            y += 14
        text(d, (x1 - 12, hy1 - 16), "(" + src + ")", f_sans(11), MUTED,
             box=card, anchor="ra")

    # ---- featured (408-600): 10 cards, 2 rows x 5
    fy0 = 408
    cw, ch, cgap = 196, 92, 8
    for j, s in enumerate(FEATURED):
        n, region, place, head, body, src, kind, lon, lat = s
        row, col = divmod(j, 5)
        x0 = 12 + col * (cw + cgap)
        y0 = fy0 + row * (ch + 8)
        x1, y1 = x0 + cw, y0 + ch
        card = (x0, y0, x1, y1)
        d.rectangle(card, fill=CARD, outline=INK, width=2)
        d.rectangle([x0 + 6, y0 + 5, x0 + 24, y0 + 23], fill=RED)
        text(d, (x0 + 15, y0 + 6), str(n), f_sans_b(12), CARD,
             box=card, anchor="ma")
        text(d, (x0 + 28, y0 + 7), region, f_sans_b(11),
             REGION_COLORS[region], box=card)
        draw_scene(d, (x0 + 6, y0 + 26, x1 - 6, y0 + 46), kind)
        hf = f_serif_b(12)
        lines = fit_lines(head, hf, cw - 16, 2)
        y = y0 + 48
        for ln in lines:
            text(d, (x0 + 8, y), ln, hf, INK, box=card)
            y += 13
        text(d, (x1 - 8, y1 - 15), "(" + src + ")", f_sans(10), MUTED,
             box=card, anchor="ra")

    # ---- KPI strip (604-644), ink band
    d.rectangle([0, 604, W, 644], fill=INK)
    d.rectangle([0, 604, W, 606], fill=RED)
    kw = W / 6
    for i, (num, lab) in enumerate(KPIS):
        cx = kw * i + kw / 2
        nf = f_display(20)
        text(d, (cx, 606), num, nf, CARD, anchor="ma")
        lf = f_sans(10)
        text(d, (cx, 630), lab, lf, OCHRE, anchor="ma")

    # ---- map (648-776)
    d.rectangle([0, 648, W, 776], fill=PAPER)
    mt = "WHERE IT HAPPENED \u2014 STORIES 1\u201313 PINNED  \u00b7  "
    mt += "DOTS: STORIES 14\u201341"
    text(d, (12, 652), mt, f_sans_b(13), RED)
    lx = W - 12
    leg = f_sans(10)
    items = list(REGION_COLORS.items())
    total_w = sum(leg.getlength(k) + 20 for k, _ in items)
    x = lx - total_w
    for k, c in items:
        d.ellipse([x, 656, x + 10, 666], fill=c, outline=INK)
        text(d, (x + 13, 654), k, leg, INK)
        x += leg.getlength(k) + 20
    area = (24, 672, 1000, 772)
    for poly in CONTINENTS:
        pts = [lonlat_to_xy(lon, lat, area) for lon, lat in poly]
        d.polygon(pts, fill=LAND, outline=INK)
    for n, region, _t, _s, lon, lat in ALSO_ON:
        px, py = lonlat_to_xy(lon, lat, area)
        d.ellipse([px - 3, py - 3, px + 3, py + 3],
                  fill=REGION_COLORS[region], outline=INK)
    offsets = {1: (0, 12), 5: (0, -12), 4: (-12, 6), 6: (-14, -12),
               11: (14, 12), 2: (0, 12), 7: (-12, 8), 8: (12, -8),
               27: (0, -12), 28: (10, 10), 30: (-10, -10)}
    for s in HEROES + FEATURED:
        n, region, _p, _h, _b, _s2, _k, lon, lat = s
        dx, dy = offsets.get(n, (0, 0))
        px, py = lonlat_to_xy(lon, lat, area)
        px += dx
        py += dy
        d.rectangle([px - 9, py - 9, px + 9, py + 9], fill=RED,
                    outline=INK)
        text(d, (px, py - 8), str(n), f_sans_b(11), CARD, anchor="ma")
    d.line([12, 776, W - 12, 776], fill=INK, width=2)

    # ---- ALSO ON list (780-938), 3 columns
    text(d, (12, 782), "ALSO ON WEDNESDAY \u2014 14\u201341",
         f_sans_b(13), RED)
    af = f_sans(11)
    col_w = (W - 24) / 3
    for i, (n, region, title, src, _lon, _lat) in enumerate(ALSO_ON):
        col, row = divmod(i, 10)
        x0 = 12 + col * col_w
        y = 800 + row * 13
        line = "%d. %s \u2014 %s" % (n, title, src)
        while af.getlength(line) > col_w - 8 and " " in line:
            line = line.rsplit(" ", 1)[0]
        if af.getlength(line) > col_w - 8:
            line = line[:48]
        if line != "%d. %s \u2014 %s" % (n, title, src):
            line += " \u2026"
        text(d, (x0, y), line, af, INK)

    # ---- DATE CHECK (942-984)
    d.rectangle([12, 942, W - 12, 984], outline=RED, width=2)
    text(d, (24, 948), "DATE CHECK \u2014 EXCLUDED", f_sans_b(13), RED)
    df = f_sans(12)
    y = 948
    for item in DATE_CHECK:
        text(d, (250, y), "\u2022  " + item, df, INK2)
        y += 17

    # ---- footer (988-1022)
    ff = f_sans(11)
    vline = ("Every story above was first reported Wed 25 Nov 2026 "
             "in some time zone.")
    text(d, ((W - ff.getlength(vline)) / 2, 990), vline, ff, INK2)
    sf = f_sans(10)
    text(d, ((W - sf.getlength(SOURCES_LINE)) / 2, 1004), SOURCES_LINE,
         sf, MUTED)

    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150,
                                             threshold=2))
    img.save(OUT, optimize=True)
    img.resize((300, 300), Image.LANCZOS).save(PREVIEW, optimize=True)
    with open(OUT, "rb") as f:
        data = f.read()
    return OUT, len(data), hashlib.sha256(data).hexdigest()


def check_clearance():
    """Every recorded text bbox must sit >=2px inside its card box."""
    bad = []
    for (x0, y0, x1, y1), (bx0, by0, bx1, by1) in PLACEMENTS:
        if x0 < bx0 + 2 or y0 < by0 + 2 or x1 > bx1 - 2 or y1 > by1 - 2:
            bad.append(((round(x0), round(y0), round(x1), round(y1)),
                        (bx0, by0, bx1, by1)))
    return bad


if __name__ == "__main__":
    path, size, sha = render()
    print("rendered %s %d bytes sha256 %s" % (path, size, sha))
    bad = check_clearance()
    print("clearance violations: %d" % len(bad))
    for b in bad[:10]:
        print("  ", b)
    sys.exit(1 if bad else 0)
