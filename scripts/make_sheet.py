#!/usr/bin/env python3
# usage: make_sheet.py <task> [n_frames] -> judge/<task>/sheet.jpg + mapping.json (labels A-F shuffled, seeded by task)
import sys, os, json, random, subprocess
from PIL import Image, ImageDraw, ImageFont
B = '<project>/samples'
task = sys.argv[1]; n = 6; rev = len(sys.argv) > 2 and sys.argv[2] == 'rev'
P = ['fable-high', 'fable-low', 'opus-solo', 'build-opus', 'build-sonnet', 'build-gpt']
order = P[:]; random.Random('token-' + task).shuffle(order)
if rev: order = order[::-1]
out = f'{B}/judge/{task}' + ('-rev' if rev else ''); os.makedirs(out, exist_ok=True)
FW, FH = 480, 300
font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 56)
rows = []
for lab, m in zip('ABCDEF', order):
    mp4 = f'{B}/rec/{task}-{m}.mp4'
    dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4]))
    row = Image.new('RGB', (90 + FW * n, FH), (20, 20, 20))
    for i in range(n):
        t = dur * (i + 0.5) / n
        tmp = f'{out}/_f.png'
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{t:.2f}', '-i', mp4, '-frames:v', '1', '-vf', f'scale={FW}:{FH}', tmp], check=True)
        row.paste(Image.open(tmp).convert('RGB'), (90 + FW * i, 0))
    ImageDraw.Draw(row).text((22, FH // 2 - 32), lab, fill=(255, 255, 255), font=font)
    rows.append(row)
W = rows[0].width; H = sum(r.height for r in rows) + 8 * 5
sheet = Image.new('RGB', (W, H), (0, 0, 0)); y = 0
for r in rows: sheet.paste(r, (0, y)); y += r.height + 8
sheet.save(f'{out}/sheet.jpg', quality=90)
json.dump(dict(zip('ABCDEF', order)), open(f'{out}/mapping.json', 'w'))
os.remove(f'{out}/_f.png'); print(task, sheet.size)
