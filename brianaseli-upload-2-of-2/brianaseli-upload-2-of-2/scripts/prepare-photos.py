"""Prepares every image the site uses. Originals stay in source-photos/; outputs go to src/assets/.

  python3 scripts/prepare-photos.py

- Portraits: full-resolution originals, lightly sharpened, true colour.
- Cut-outs (source-photos/cutouts/*.png): background already removed (see HANDOVER.md).
- Stage backgrounds (source-photos/stage/*.jpg): enlarged, cleaned, then colour-graded onto the brand's
  navy-to-beam-blue ramp so every background sits in the same blue world.
- Video thumbnails (source-photos/thumbs/): saved from YouTube; smaller ones enlarged to 1280 wide.
- Event photos (source-photos/events/): small press photos enlarged 3x, denoised and sharpened."""
from pathlib import Path
from PIL import Image, ImageFilter, ImageOps
import numpy as np, cv2
ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / 'source-photos', ROOT / 'src/assets'
for d in ['photos', 'cutouts', 'stage', 'thumbs', 'events']: (OUT / d).mkdir(parents=True, exist_ok=True)

def sharpen(im, r=1.2, p=60): return im.filter(ImageFilter.UnsharpMask(radius=r, percent=p, threshold=2))
def fit_max(im, w=2400):
    if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    return im
def enlarge(im, s): return im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
def clean(im, h=6):
    arr = cv2.fastNlMeansDenoisingColored(cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR), None, h, h, 7, 21)
    return Image.fromarray(cv2.cvtColor(arr, cv2.COLOR_BGR2RGB))

# 1. Portraits (full-res originals)
# hires/ holds the photographer's full-size files (about 3200 x 4800); the *_copy.jpg files are smaller exports.
portraits = {'hires/DON00146.jpg': 'portrait-black-tee', 'hires/DON00158.jpg': 'portrait-thinking', 'hires/DON00098.jpg': 'portrait-laugh',
             'hires/DON00055.jpg': 'portrait-smile', 'aseli_1.jpg': 'frame-hands', 'IMG_0716.jpg': 'event-night'}
U = Path('/mnt/user-data/uploads')
for f, n in portraits.items():
    p = SRC / f if (SRC / f).exists() else U / f
    im = ImageOps.exif_transpose(Image.open(p)).convert('RGB')
    if im.width < 1600: im = enlarge(im, 1600 / im.width)
    sharpen(fit_max(im), 1.0, 40).save(OUT / 'photos' / f'{n}.jpg', quality=90, optimize=True, progressive=True); print('photo', n)
lea = Image.open(SRC / 'bio-leather-jacket.png').convert('RGB')
sharpen(enlarge(lea, 1.6), 1.4, 55).save(OUT / 'photos/portrait-leather.jpg', quality=90, optimize=True, progressive=True)
# Stage mic photo, cropped clear of the timeline graphic in Brian's booking poster.
mic = Image.open(SRC / 'aseli_profile.jpg').convert('RGB').crop((0, 80, 400, 960))
sharpen(clean(enlarge(mic, 2.6), 4), 1.6, 70).save(OUT / 'photos/stage-mic.jpg', quality=90, optimize=True, progressive=True); print('photo stage-mic')
# Green suit, from the bio cover, placed on brand navy.
suit = Image.open(SRC / 'cutouts/suit.png').convert('RGBA'); suit = enlarge(suit, 2.0)
bg = Image.new('RGBA', suit.size, (8, 22, 58, 255))
g = np.zeros((suit.height, suit.width, 4), np.uint8)
yy, xx = np.mgrid[0:suit.height, 0:suit.width]
r = np.sqrt(((xx - suit.width * .55) / suit.width) ** 2 + ((yy - suit.height * .2) / suit.height) ** 2)
glow = np.clip(1 - r * 1.6, 0, 1)
g[..., 0] = 61; g[..., 1] = 123; g[..., 2] = 255; g[..., 3] = (glow * 170).astype(np.uint8)
bg.alpha_composite(Image.fromarray(g)); bg.alpha_composite(suit)
sharpen(bg.convert('RGB'), 1.4, 60).save(OUT / 'photos/portrait-suit.jpg', quality=90, optimize=True, progressive=True); print('photo suit')

# 2. Cut-outs
for f in sorted((SRC / 'cutouts').glob('*.png')):
    im = Image.open(f).convert('RGBA'); im = im.crop(im.getbbox())
    if im.height < 2200: im = enlarge(im, 2200 / im.height)
    a = im.getchannel('A'); rgb = sharpen(im.convert('RGB'), 1.2, 45); rgb.putalpha(a)
    rgb.save(OUT / 'cutouts' / f'brian-{f.stem}.png', optimize=True); print('cutout', f.stem)

# 3. Stage backgrounds, graded onto one blue ramp
ramp_pts = [(0, (3, 7, 20)), (70, (8, 22, 60)), (150, (30, 80, 200)), (205, (90, 150, 255)), (255, (225, 236, 255))]
lut = np.zeros((256, 3), np.float32)
for (a0, c0), (a1, c1) in zip(ramp_pts, ramp_pts[1:]):
    for i in range(a0, a1 + 1):
        t = (i - a0) / max(1, a1 - a0); lut[i] = np.array(c0) * (1 - t) + np.array(c1) * t
for f in sorted((SRC / 'stage').glob('*.jpg')):
    im = enlarge(Image.open(f).convert('RGB'), 2.5)
    arr = cv2.fastNlMeansDenoisingColored(cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR), None, 5, 5, 7, 21)
    arr = cv2.GaussianBlur(arr, (0, 0), 1.1)
    rgb = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB).astype(np.float32)
    lum = np.clip(rgb @ np.array([.299, .587, .114]), 0, 255).astype(np.uint8)
    graded = lut[lum]
    out = graded * .82 + rgb * .18  # keep a trace of the original light so it still feels photographic
    out += np.random.default_rng(7).normal(0, 3.0, out.shape[:2])[..., None]
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(OUT / 'stage' / f.name, quality=86, optimize=True, progressive=True)
    print('stage', f.stem)

# 4. Video thumbnails
for f in sorted((SRC / 'thumbs').glob('*.jpg')):
    im = Image.open(f).convert('RGB')
    if im.width < 1280:
        im = clean(im, 4); im = sharpen(enlarge(im, 1280 / im.width), 1.4, 60)
    vid = f.stem.replace('aseli-yt-', '')
    im.save(OUT / 'thumbs' / f'{vid}.jpg', quality=88, optimize=True, progressive=True); print('thumb', vid, im.size)

# 5. Event photos (stage-mic is handled above)
for f in sorted((SRC / 'events').glob('*.jpg')):
    if f.stem == 'stage-mic': continue
    im = Image.open(f).convert('RGB')
    if im.width < 1000:
        im = clean(im, 5); im = enlarge(im, 3); im = sharpen(clean(im, 3), 1.8, 80)
    im.save(OUT / 'events' / f.name, quality=90, optimize=True, progressive=True); print('event', f.stem, im.size)

# 6. Brand duotone versions (navy to beam blue to ice) for cards, so every image sits in one colour world.
#    The full-colour originals are kept and shown on hover/focus.
duo_pts = [(0, (4, 10, 28)), (90, (14, 38, 96)), (170, (52, 112, 240)), (225, (150, 190, 255)), (255, (240, 245, 255))]
duo = np.zeros((256, 3), np.float32)
for (a0, c0), (a1, c1) in zip(duo_pts, duo_pts[1:]):
    for i in range(a0, a1 + 1):
        t = (i - a0) / max(1, a1 - a0); duo[i] = np.array(c0) * (1 - t) + np.array(c1) * t
(OUT / 'duo').mkdir(exist_ok=True)
def duotone(src, name, maxw=1400):
    im = fit_max(Image.open(src).convert('RGB'), maxw)
    g = np.array(ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=1))
    Image.fromarray(duo[g].astype(np.uint8)).save(OUT / 'duo' / f'{name}.jpg', quality=86, optimize=True, progressive=True)
for f in sorted((OUT / 'thumbs').glob('*.jpg')): duotone(f, 'thumb-' + f.stem, 1280)
for f in sorted((OUT / 'events').glob('*.jpg')): duotone(f, 'event-' + f.stem)
for n in ['portrait-smile', 'stage-mic', 'portrait-laugh', 'frame-hands', 'portrait-leather', 'portrait-black-tee', 'event-night', 'portrait-thinking', 'portrait-suit']:
    duotone(OUT / 'photos' / f'{n}.jpg', n)
print('duotones done')
