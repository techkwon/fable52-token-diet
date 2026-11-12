#!/usr/bin/env python3
# -> costs.json : per task x pipeline: usd, tokens, seconds (spec cost added to build-* pipelines)
import json, os
B = '<project>/samples'
GPT = {'in': 2.00, 'cached': 0.10, 'out': 10.00}  # USD / 1M tokens, developers.openai.com/api/docs/pricing (short context), checked 2026-11-12
def one(t, p):
    d = f'{B}/runs/{t}/{p}'; meta = json.load(open(f'{d}/meta.json'))
    if os.path.exists(f'{d}/log.json'):
        j = json.load(open(f'{d}/log.json')); u = j['usage']
        assert not j.get('is_error'), (t, p)
        tok = {'input': u['input_tokens'], 'cache_write': u['cache_creation_input_tokens'], 'cache_read': u['cache_read_input_tokens'], 'output': u['output_tokens'], 'thinking': (u.get('output_tokens_details') or {}).get('thinking_tokens', 0)}
        return {'usd': j['total_cost_usd'], 'turns': j['num_turns'], 'seconds': meta['seconds'], 'tokens': tok, 'total_tokens': tok['input'] + tok['cache_write'] + tok['cache_read'] + tok['output']}
    us = [json.loads(l)['usage'] for l in open(f'{d}/log.jsonl') if '"usage"' in l and json.loads(l).get('type') == 'turn.completed']
    assert len(us) == 1, (t, p, len(us)); u = us[0]
    fresh = u['input_tokens'] - u['cached_input_tokens']
    usd = fresh * GPT['in'] / 1e6 + u['cached_input_tokens'] * GPT['cached'] / 1e6 + u['output_tokens'] * GPT['out'] / 1e6
    tok = {'input': fresh, 'cache_write': 0, 'cache_read': u['cached_input_tokens'], 'output': u['output_tokens'], 'thinking': u.get('reasoning_output_tokens', 0)}
    return {'usd': usd, 'turns': None, 'seconds': meta['seconds'], 'tokens': tok, 'total_tokens': u['input_tokens'] + u['output_tokens']}
out = {}
for t in ('motion', 'lesson'):
    spec = one(t, 'spec'); out[t] = {'spec': spec}
    for p in ('fable-high', 'fable-low', 'opus-solo', 'build-opus', 'build-sonnet', 'build-gpt'):
        r = one(t, p)
        if p.startswith('build-'):
            r = dict(r, build_usd=r['usd'], usd=r['usd'] + spec['usd'], seconds_build=r['seconds'], seconds=r['seconds'] + spec['seconds'], total_tokens_build=r['total_tokens'], total_tokens=r['total_tokens'] + spec['total_tokens'])
        r['vs_base_pct'] = None
        out[t][p] = r
    base = out[t]['fable-high']['usd']
    for p in out[t]:
        if p != 'spec': out[t][p]['vs_base_pct'] = round((1 - out[t][p]['usd'] / base) * 100, 1)
json.dump(out, open(f'{B}/costs.json', 'w'), indent=1)
for t in out:
    print(t)
    for p, r in out[t].items():
        print(f"  {p:13s} ${r['usd']:.2f}  {r['seconds']:5d}s  tok {r['total_tokens']:>9,}  out {r['tokens']['output']:>7,}  cut {r.get('vs_base_pct')}")
