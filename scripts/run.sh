#!/bin/zsh
# usage: run.sh <pipeline> <task>
#  pipelines: fable-high | fable-low | opus-solo | spec | build-opus | build-sonnet | build-gpt
#  spec = Fable 5.2 writes DESIGN.md only; build-* = another model builds index.html from the brief + DESIGN.md
P=$1; T=$2
B=<project>/samples
WORK=${WORK_ROOT:-/tmp/token-work}/$T/$P
rm -rf "$WORK"; mkdir -p "$WORK"; cd "$WORK"
BRIEF="$(cat $B/prompts/$T.txt)"
OUT=$B/runs/$T/$P; mkdir -p $OUT
claude_run() { # model effort prompt
  env -i HOME=$HOME PATH=$PATH USER=$USER claude -p "$3" --model $1 --effort $2 --setting-sources "" --strict-mcp-config --permission-mode acceptEdits --allowedTools "Write,Edit,Read" --output-format json > log.json 2> err.txt
}
START=$(date +%s)
case $P in
  fable-high) claude_run claude-fable-5-2 high "$BRIEF";;
  fable-low)  claude_run claude-fable-5-2 low "$BRIEF";;
  opus-solo)  claude_run claude-opus-5-5 high "$BRIEF";;
  spec)       claude_run claude-fable-5-2 high "$(sed "/__BRIEF__/{
r $B/prompts/$T.brief
d
}" $B/prompts/spec.txt)";;
  build-*)
    cp $B/runs/$T/spec/DESIGN.md . || exit 2
    BP="$BRIEF$(cat $B/prompts/build_suffix.txt)"
    case $P in
      build-opus)   claude_run claude-opus-5-5 high "$BP";;
      build-sonnet) claude_run claude-sonnet-5-5 high "$BP";;
      build-gpt)    env -i HOME=$HOME PATH=$PATH codex exec --skip-git-repo-check -s workspace-write -C . -m gpt-6.1-sol -c model_reasoning_effort=high --json -o last.txt "$BP" < /dev/null > log.jsonl 2> err.txt;;
    esac;;
esac
RC=$?; END=$(date +%s)
echo "{\"pipeline\":\"$P\",\"task\":\"$T\",\"seconds\":$((END-START)),\"rc\":$RC}" > meta.json
cp -f index.html DESIGN.md meta.json log.json log.jsonl last.txt err.txt $OUT/ 2>/dev/null
echo "done $P $T rc=$RC $((END-START))s: $(ls $OUT | tr '\n' ' ')"
