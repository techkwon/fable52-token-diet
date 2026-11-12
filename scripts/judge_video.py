#!/usr/bin/env python3
# usage: judge_video.py <task|task-rev>  -> judge/<task>/vote-carbon-video.json  (Gemini 4 Carbon watches the six videos)
import sys, json, base64, subprocess, urllib.request, os, re
B = '<project>/samples'
T = sys.argv[1]; base = T.replace('-rev', ''); D = f'{B}/judge/{T}'
mp = json.load(open(f'{D}/mapping.json'))
brief = open(f'{B}/prompts/{base}.brief').read().strip()
key = subprocess.check_output(['security', 'find-generic-password', '-a', os.environ['USER'], '-s', 'agy-gemini-api-key', '-w']).decode().strip()
parts = []
for lab in 'ABCDEF':
    parts.append({'text': f'Submission {lab}:'})
    parts.append({'inline_data': {'mime_type': 'video/mp4', 'data': base64.b64encode(open(f'{B}/rec/small/{base}-{mp[lab]}.mp4', 'rb').read()).decode()}})
q = f'''You are an impartial judge. Six anonymous submissions (A, B, C, D, E, F) were each produced from this exact prompt:

"""{brief}"""

Each submission is attached above as a 16-second screen recording of the running page. Watch all six videos fully. Judge the motion itself (timing, easing, transitions, rhythm), not only single frames, on three criteria: (1) how well it fulfils the prompt, (2) visual and motion quality and polish, (3) correctness - no visible bugs such as clipping, overflow, broken layout, or objects escaping. Rank all six from best to worst; no ties.

Reply with ONLY a JSON object, no markdown: {{"ranking":["<1st>","<2nd>","<3rd>","<4th>","<5th>","<6th>"],"reasons":{{"A":"...","B":"...","C":"...","D":"...","E":"...","F":"..."}}}} where each reason is one short Korean sentence.'''
parts.append({'text': q})
body = {'contents': [{'parts': parts}]}
r = urllib.request.Request('https://generativelanguage.googleapis.com/v1beta/models/gemini-4-carbon:generateContent', data=json.dumps(body).encode(), headers={'x-goog-api-key': key, 'Content-Type': 'application/json'})
d = json.load(urllib.request.urlopen(r, timeout=900))
raw = ''.join(p.get('text', '') for p in d['candidates'][0]['content']['parts'] if not p.get('thought'))
open(f'{D}/raw-carbon-video.txt', 'w').write(raw)
v = json.loads(re.search(r'\{.*\}', raw, re.S).group(0)); v['models'] = [mp[x] for x in v['ranking']]; v['usage'] = d.get('usageMetadata')
json.dump(v, open(f'{D}/vote-carbon-video.json', 'w'), ensure_ascii=False, indent=1)
print(T, v['ranking'], v['models'])
