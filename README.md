# Fable 5.2 토큰 다이어트 — 실험 자료

누구나쉽게 10편 「Fable 5.2 토큰 확 줄이는 법, 제가 추천한 방법은 꼴찌였어요」의 실험 자료입니다.

- 페이지: https://techkwon.github.io/fable52-token-diet/
- 영상: https://youtu.be/Np-CMJeJOD8 (2026-11-13 19:00 공개)
- 과제 2개(쇼릴, 중학교 광합성 수업 오프닝 15초) × 방법 6개
  - Fable 5.2 effort high (기준) / Fable 5.2 effort low / Opus 5.5 혼자
  - Fable 5.2가 설계도(DESIGN.md)만 쓰고 Opus 5.5 · Sonnet 5.5 · GPT-6.1 Sol이 구현
- 결과: Fable low가 값 76%·75% 감소, 블라인드 심사에서 high와 같거나 위. 나눠 만들기 셋은 심사 16장 모두 아래 세 자리.

## 파일
- `data.json`: 값·토큰·시간·턴, 심사 순위와 이유, 한계
- `runs/<과제>/<방법>/index.html`: 모델이 만든 결과물 그대로 (브라우저로 열면 재생)
- `runs/<과제>/spec/DESIGN.md`: Fable 5.2가 쓴 설계도
- `video/`, `poster/`: 16초 녹화(960×600)와 첫 화면
- `judge/`: 블라인드 심사 시트(A~F, 정순·역순)
- `prompts/`, `scripts/`: 프롬프트와 실행·녹화·심사·집계 스크립트

## 한계
방법마다 1번씩만 실행했고, 심사는 AI(Fable 5.2, Opus 5.5, GPT-6.1 Sol, Gemini 4 Carbon)가 했습니다. 값은 API 가격 환산이며, 브라우저·Node 실행을 막은 조건입니다. Claude Code의 Fable 5.2 기본 effort는 medium이지만 high와 low만 쟀습니다.
