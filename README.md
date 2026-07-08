# feargreed-data

CNN Fear & Greed 지수를 매일 아침(KST) GitHub Actions로 수집해 `data.json`으로 저장하는 데이터 릴레이.

- 소비처: 개인 가계부 앱의 QQQ/QLD 투자 신호 (raw.githubusercontent.com 경유)
- 스케줄: 21:30 / 22:30 UTC (KST 06:30 / 07:30)
- 포맷: `{ source, updatedAt, latest: {date, value}, series: [[date, value], ...] }` (2021-01-04부터)
