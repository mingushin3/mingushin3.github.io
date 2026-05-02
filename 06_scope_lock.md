=== SCOPE LOCK ===

Source       : Gabrielsson & Weiner 5e (Vol I — Primary) +
               Rowland & Tozer 5e (Vol I — Supplementary)

Chapter      : [Gabrielsson] Ch.2 §2.8 Non-Compartmental Analysis /
                              §2.9 How to Assess Exposure /
                              Case Study PK41 (NCA vs. Regression)
               [Rowland & Tozer] Appendix A — Assessment of AUC /
                                 Appendix H — Mean Residence Time

Pages        : Gabrielsson p.141–164, p.661–664
               Rowland & Tozer p.759–762, p.789–793

Chapter role : "NCA는 PopPK 분석의 출발점이자 귀환점이다.
               모델 선택 전 EDA의 수단이며, 모델 추정 후 결과 검증의 기준이고,
               규제 제출(NDA/IND BA·BE 파트)에서 유일하게 가정-무결한
               노출 지표를 제공하는 방법론이다.
               이 섹션을 체화하지 않으면:
               (1) λz 추정 오류가 AUC 외삽 편향으로 전파되어 CL을 왜곡하고,
               (2) MRT/Vss 계산에서 투여 경로 보정을 누락하여 Vss를 과소/과대추정하며,
               (3) NCA 기반 초기모수 추정 없이 MM 비선형 모델로 직진하면
                   Vmax-Km 상관관계로 수렴 실패가 발생한다.
               선행: CL/V 개념, 1구획·2구획 모델, 비선형(MM) PK 기초.
               후속: PopPK 데이터셋 구성, NONMEM 초기모수 전략,
                     BA/BE 규제 제출, 비선형 PK 모집단 모델링."

Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate

Final output : Single self-contained HTML (Step 2)

Mode         : A-Critical
               [근거: AUC/AUMC/MRT/Vss 수식 도출 + λz 추정 전략 +
               NCA→회귀 모델 전환 논리(PK41) + 규제 파급력(BA/BE, NDA 노출 지표) +
               비선형 PK와의 교차점(MM 모델 초기모수) 전부 포함.
               수식·표·실험데이터·규제 연결고리가 모두 있는 A급 챕터.]

Image rights : None

--- Dynamic Source Anchoring 요약 ---

Gabrielsson 실제 실험 데이터 (반드시 인용):
  - Turbojoint® (PK41): 1명 지원자, 3회 IV infusion (5h),
    용량 310 / 520 / 780 µg·kg⁻¹, 체중 70 kg
    NCA 결과: CL 1.6→0.9 L·h⁻¹·kg⁻¹ (용량 증가에 따라 감소),
              V 2.3→1.8 L·kg⁻¹, MRT 1.4→1.9 h
    MM 최종 추정: Vmax=184 µg·h⁻¹·kg⁻¹, Km=83 µg·L⁻¹, V=1.8 L·kg⁻¹

Rowland & Tozer 실제 데이터 (반드시 인용):
  - Table A-1: 경구 50 mg 투여 후 AUC = 26.6 mg·hr/L (선형 사다리꼴)
  - Table H-1 (IV bolus, 가상 표준 약물):
    AUC=44.2 mg·hr/L, AUMC=177 mg·hr²/L,
    MRT(plasma)=4.0 hr, MRT(urine)=4.25 hr, simulated=4.3 hr
  - Zileuton (Table A-2): 경구 600 mg, 0–24h 농도-시간 프로파일
  - Table H-2: 투여 경로별 MIT 및 observed MRT 정리표

핵심 수식 (소스 직접 인용):
  선형 사다리꼴:  AUC = Σ[(Cᵢ+Cᵢ₊₁)/2]·Δt            [Gabrielsson Eq.2:310]
  로그-선형 사다리꼴: AUCᵢ = (Cᵢ−Cᵢ₊₁)/ln(Cᵢ/Cᵢ₊₁)·Δt [Gabrielsson Eq.2:316]
  외삽 AUC:      AUC_{tlast→∞} = C_last/λz              [Gabrielsson Eq.2:311/2:319]
  MRT (plasma):  MRT = AUMC₀^∞ / AUC₀^∞               [R&T Eq.H-8]
  MRT (IV inf 보정): MRT = AUMC₀^∞/AUC₀^∞ − T_inf/2   [Gabrielsson Eq.2:328]
  Vss:           Vss = MRT · CL = D_iv·AUMC/(AUC)²     [Gabrielsson Eq.2:337]
  Vz:            Vz = CL/λz = D_iv/(AUC·λz)            [Gabrielsson Eq.2:338]
  CL:            CL = D_iv / AUC₀^∞                     [Gabrielsson Eq.2:325]
  MM 1구획(PK41): V·dC/dt = In − Cl·C,  Cl = Vmax/(Km+C) [Gabrielsson Eq.41:1–2]

HARD RULES:
- Do not expand beyond stated page ranges.
- Do not fabricate values, experimental conditions, or page citations.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures.
  Image rights = None → pointer callout(P mode)만 허용.
=================
