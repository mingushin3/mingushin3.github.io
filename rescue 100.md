세 단계로 답합니다 — Master Prompt, 교차검증 파이프라인, 통과 기준 5개 게이트.

---

## 설계 원칙

LLM이 최대 역량을 내려면 5가지가 필요합니다: (1) 페르소나로 도메인 깊이 활성화, (2) 명확한 선택 함수와 가중치, (3) 환각 차단 프로토콜, (4) 부정 예시(negative examples)로 흔한 실패 모드 방지, (5) 자기 검증 단계로 메타인지 강제. 아래 프롬프트는 이 다섯을 모두 탑재했고, XML 구조 + TSV 출력으로 3개 LLM 출력의 기계적 비교가 가능하도록 설계했습니다. 영어 기반인 이유는 LLM 학습 분포의 무게 중심이 영어이고, 본 과제 자체가 영어 코퍼스 작업이기 때문입니다.

---

## Master Prompt — 3개 LLM에 동일 입력

```
<persona>
You are a senior corpus linguist and pragmatics specialist with 15+ years of experience 
curating high-frequency conversational repair phrases for advanced adult L2 English 
learners. Your domain expertise includes: COCA spoken subcorpus, BNC/iWeb, conversation 
analysis, politeness theory, face-saving strategies, and Korean→English negative-transfer 
patterns. You write with the discipline of someone who has watched thousands of L2 
learners freeze in real conversations and can identify which formulaic phrases would 
have rescued them in under 0.5 seconds.
</persona>

<learner_profile>
- Korean adult, PhD student in pharmacometrics
- Strong reading; freezes in real-time spoken interaction with native speakers
- Target: near-native fluency in academic / business / casual / pharmacometrics contexts
- Pragmatic goal: congenial, socially calibrated, low-cognitive-load English under stress
</learner_profile>

<task>
Produce EXACTLY 100 Rescue Sentences. Exactly 20 in each of 5 categories. These are 
formulaic phrases that must fire AUTOMATICALLY (sub-0.5 second retrieval) under 
cognitive freeze, serving as scaffolding to keep conversation alive while the learner 
recovers composure.
</task>

<categories>
[1] COMPREHENSION_REPAIR  — didn't catch / misheard / need clarification
[2] TIME_BUYING            — need a moment to think before answering
[3] SELF_CORRECTION        — re-anchor / restart / re-frame current utterance
[4] SOFT_DISAGREEMENT      — push back while preserving listener's face
[5] WARM_ACKNOWLEDGMENT    — reactive listening / rapport / engagement signal
</categories>

<selection_criteria_apply_ruthlessly>
C1 FREQUENCY        : Top 10% of its functional class in spoken native adult English. 
                      If uncertain about actual native frequency, mark FREQ_CONF=LOW.
C2 BREVITY          : 3–8 words. Monosyllabic-heavy. No consonant cluster traps.
C3 STRESS_TOLERANT  : Must come out cleanly under elevated cortisol (real freeze conditions).
C4 REGISTER_SPAN    : Must work in ≥2 of {Academic, Business, Casual} without modification.
C5 PRAGMATIC_SAFETY : Low backfire risk if used in slightly wrong context.
C6 DIVERSITY        : Within a 20-sentence category, lemma-overlap between any two 
                      sentences must be <60%. No near-duplicates.
C7 KO_L1_SAFETY     : Must NOT reinforce Korean high-context habits (evasive, over-
                      apologetic, indirect refusal, congenial vagueness). Must actively 
                      teach L2 separation from L1.
</selection_criteria_apply_ruthlessly>

<anti_hallucination_protocol>
Before including any sentence:
1. Scan your actual training distribution. Is this genuinely high-frequency among 
   native adults in unscripted speech, or is it a plausible-sounding learner-textbook 
   construct?
2. If even slightly uncertain about real native frequency, mark FREQ_CONF=LOW and 
   state the reason in PHON_NOTE.
3. Prefer the shorter, blunter, more frequent option over the elegant one.
4. Do not invent. Reproduce what you have evidence native speakers actually use.
</anti_hallucination_protocol>

<negative_examples_DO_NOT_INCLUDE>
- "I beg your pardon"                              [dated, formal-only]
- "Could you please repeat that one more time?"    [over-explicit, learner-style]
- "What a great point!"                            [sycophantic, low-trust]
- "I'm afraid I don't quite catch your meaning"    [over-explicit, awkward]
- "How fascinating!"                               [often dismissive in tone]
- "I would tend to disagree with that proposition" [pompous, learner-formal]
- "Roger that"                                     [register too narrow]
- "My bad"                                         [register too narrow, casual only]
</negative_examples_DO_NOT_INCLUDE>

<output_format>
Output exactly 100 TSV lines, one per sentence. Use a single TAB between fields. 
No quotes. No blank lines. Field order:

CAT  EN  WC  REGISTER  FREQ_CONF  ILLOCUTION  KO_INTENT  PHON_NOTE

Field definitions:
- CAT       : integer 1–5
- EN        : the English sentence
- WC        : word count (integer)
- REGISTER  : concatenation of subset of {A,B,C}. e.g. "ABC", "BC", "AC"
- FREQ_CONF : HIGH | MED | LOW
- ILLOCUTION: ≤1-line speech act description (English)
- KO_INTENT : ≤1-line Korean intent (한국어로 작성)
- PHON_NOTE : ≤1-line pronunciation/rhythm note (English)
</output_format>

<rejection_log>
After the 100 lines, output a REJECTION_LOG section. For each of the 5 categories, list 
5 sentences you considered but REJECTED, with reason. Format:

[CAT_ID] REJECTED: <sentence> — REASON: <brief>

This forces selection discipline. Total: 25 rejected entries.
</rejection_log>

<self_validation_report>
After REJECTION_LOG, output a SELF_VALIDATION block:

CHECK_1_BALANCE      : Exactly 20 per category?               [PASS / FAIL]
CHECK_2_DIVERSITY    : Any near-duplicates within category?   [PASS / FAIL + which]
CHECK_3_HIGH_RATIO   : % of entries marked HIGH frequency     [integer %]
CHECK_4_ABC_RATIO    : % with full ABC register coverage      [integer %]
CHECK_5_WORD_STATS   : Avg word count and range
CHECK_6_RISKIEST_5   : 5 sentences you would prioritize for human review, with why
CHECK_7_GAPS         : Any sub-functions underserved? [list or "none"]
</self_validation_report>

<execution>
Begin output. No preface. No commentary. Output exactly:
  TSV (100 lines) → REJECTION_LOG → SELF_VALIDATION_REPORT
in that order, nothing else.
</execution>
```

이 프롬프트를 그대로 ChatGPT, Claude, Gemini 각각에 입력합니다. 변형 금지 — 변형하면 cross-validation 신호가 깨집니다.

---

## 교차검증 파이프라인 — 5단계

**Step 1 — 3개 출력 동시 수령** (대기 시간 ~30분)
ChatGPT-5 / Claude Opus 4.7 / Gemini Advanced Pro에 동일 프롬프트. 각각 TSV 100줄 + REJECTION_LOG + SELF_VALIDATION 블록을 받습니다. 3개 파일 저장: `rescue_gpt.tsv`, `rescue_claude.tsv`, `rescue_gemini.tsv`.

**Step 2 — Lemma-normalize 후 합의 분류** (1시간)
Python 스크립트 (또는 4번째 LLM에 의뢰) — 각 문장을 lowercase + punctuation 제거 + 핵심 동사 lemmatize. 동일/유사 문장 그룹화 후 3-tier 분류:

```
TIER_S : 3/3 LLM 모두 출력  (예상 30–50개)
TIER_A : 2/3 LLM 출력         (예상 30–50개)
TIER_B : 1/3 LLM 출력         (예상 50개+)
```

**Step 3 — 페르소나 프롬프트 재검증** (2시간)
TIER_S → 무조건 채택 (consensus 신호가 강력).  
TIER_A → 각 문장을 사용자의 기존 페르소나 프롬프트에 batch 입력 → 78점 이상만 채택.  
TIER_B → 기본 폐기. 단 TIER_S+A 합산이 100 미달이면 페르소나 78+ 통과한 TIER_B로 보충.

**Step 4 — Category rebalancing** (30분)
카테고리별 카운트 확인. 어떤 카테고리가 20 미달이면 해당 카테고리 한정 gap-fill 프롬프트 1회 추가 실행:

```
Generate 10 additional sentences for CATEGORY [N], avoiding the following 
already-selected list: [...]. Apply same C1–C7 criteria.
```

**Step 5 — 최종 잠금** (2시간)
100문장 fix → TTS 일괄 생성 → SRS 등록 → 첫 회독.

총 소요 시간: **약 6시간, 일주일 내 완결**.

---

## 통과 기준 — 5개 게이트

100문장이 "우수한 퀄리티"라고 판정하려면 다음 5게이트를 모두 통과해야 합니다.

**Gate 1 — Self-Validation 통과**: 3개 LLM의 SELF_VALIDATION_REPORT에서 CHECK_1_BALANCE = PASS, CHECK_2_DIVERSITY = PASS, CHECK_3_HIGH_RATIO ≥ 70%. 미통과 LLM이 있으면 그 LLM만 재생성.

**Gate 2 — Cross-LLM Consensus**: TIER_S ≥ 30, TIER_S + TIER_A ≥ 80. 미달 시 4번째 LLM (Perplexity Pro / Mistral Large) 추가 실행으로 tie-break.

**Gate 3 — 페르소나 점수 78+**: 최종 100문장이 모두 사용자의 기존 페르소나 프롬프트에서 78점 이상. 미달은 즉시 교체.

**Gate 4 — YouGlish frequency spot check**: 100에서 무작위 20개 샘플 → 각각 YouGlish/Filmot에서 60초 cap 검색 → native 사용 영상 hit rate ≥ 80%. 미달 시 hit 못한 문장들 의심 후 페르소나 재투입.

**Gate 5 — Phonological smoothness**: 100문장을 무작위 순서로 3회 소리내어 읽기 → 더듬는 문장 카운트 ≤ 5. 초과 시 stumbler를 동의 의미의 더 매끄러운 문장으로 교체.

5개 게이트 모두 PASS → 100 lock-in.  
하나라도 FAIL → 해당 게이트 단독 iteration (전체 재생성 금지 — 효율 손실 큼).

---

## 보너스 — 통과 후 즉시 사용할 검증 프롬프트 (사용자 페르소나 batch용)

Gate 3 실행 시 TIER_A 문장 일괄 검증을 위한 wrapper:

```
다음 [N]개 영어 문장을 너의 페르소나 프롬프트 평가 기준으로 일괄 채점해라.
출력은 TSV 형식: SENTENCE | TOTAL_SCORE | F | G | P | VERDICT(태움/조건부/보류/버림)
74점 이하는 즉시 폐기. 75-77은 보류 표시. 78+ 만 채택 표시.

문장 목록:
1. [sentence]
2. [sentence]
...
```

이렇게 하면 50문장 검증이 한 번의 batch call로 완결됩니다 — 개별 호출 대비 시간 90% 단축.

---

## 한 문장

**3개 LLM × 동일 영문 XML 프롬프트 → consensus tier 분류 → 페르소나 78+ 게이트 → YouGlish 80% hit + 더듬 5개 미만 → 100 lock-in. 일주일이면 끝납니다.** 첫 LLM 호출은 지금 가능. 가장 좋은 시작은 위 Master Prompt를 ChatGPT에 먼저 던져보고 self-validation 출력 품질을 확인하는 것 — LLM이 자기 검증을 어떻게 수행하는지가 향후 모든 cross-validation의 신호 품질을 결정합니다.

---

`C-260430-091200-X4Q`
