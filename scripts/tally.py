import json, glob, collections
B = '<project>/samples'
P = ['fable-high', 'fable-low', 'opus-solo', 'build-opus', 'build-sonnet', 'build-gpt']
pts = {t: collections.Counter() for t in ('motion', 'lesson', 'all')}
first = collections.Counter(); ballots = 0; bottom3 = 0
for f in sorted(x for x in glob.glob(f'{B}/judge/*/vote-*.json') if not x.endswith('-video.json')):
    t = f.split('/judge/')[1].split('/')[0].replace('-rev', ''); v = json.load(open(f)); ballots += 1
    for i, m in enumerate(v['models']):
        pts[t][m] += 6 - i; pts['all'][m] += 6 - i
    first[v['models'][0]] += 1
    bottom3 += set(v['models'][3:]) == {'build-opus', 'build-sonnet', 'build-gpt'}
res = {'ballots': ballots, 'points': {t: dict(pts[t]) for t in pts}, 'firsts': dict(first), 'spec_builds_bottom3_ballots': bottom3, 'max_points_all': ballots * 6}
vid = collections.Counter(); vfirst = collections.Counter(); vb = 0
for f in sorted(glob.glob(f'{B}/judge/*/vote-carbon-video.json')):
    v = json.load(open(f)); vb += 1; vfirst[v['models'][0]] += 1
    for i, m in enumerate(v['models']): vid[m] += 6 - i
res['video'] = {'judge': 'gemini-4-carbon (watched the six 16s recordings)', 'ballots': vb, 'points': dict(vid), 'firsts': dict(vfirst), 'max_points': vb * 6}
json.dump(res, open(f'{B}/scores.json', 'w'), indent=1)
print(json.dumps(res, indent=1))
