# Jev & Laya — decision models for MAS?

Assessment of the two "System One" decision models released Sept 2026 as MAS improvements.
`Last-verified: 2026-09-29`. Related: [[functionality-map]], [[earnings-scoring]], [[signal-quality]].

## What they are
- **Jev** (TypeSafe AI, launched 2026-09-15): hosted API, early access / waitlist. Input text or program state →
  typed values from a schema defined in advance, with calibrated probabilities. $0.042 per M input tokens, output free,
  70–500 ms. No fine-tuning mentioned. Does not generate text.
- **Laya** (Convai Innovations, 2026-09-18): open weights, Apache 2.0, 421M params (ModernBERT-large); multilingual 322M.
  Question types: `choice`, `score` (ordinal), yes/no. Base checkpoints are near chance zero-shot (0.362 vs 0.461
  majority baseline); fine-tuned 0.766. Weak on >20 options (Banking77 0.425 vs Jev 0.870) and ordinal scores.
  Over-confident until temperature-scaled (ECE 0.213 → 0.081). Fine-tuning notebook exists.

## Fit to MAS
- Good fit (fixed labels): earnings `direction` up/down + BUY/WATCH/SKIP; news critic accept/reject; macro headline
  relevance filter ("Llama filter", ~300 headlines per run); PM rating BUY/HOLD/SELL/REDUCE (decision only).
- No fit (needs generated text or numbers): ToC chains, candidate/ticker proposal, research planner, hypothesis,
  price levels, the rationales shown in Telegram.
- Speed and token cost barely matter: MAS jobs are scheduled batches, and DeepSeek V4.1 Flash is already cheap.
- The real value is **calibrated probabilities learned from MAS's own history** (1,009 earnings predictions,
  3,356 signal outcomes). That is the open proposal "numeric calibrated P(up) as primary signal". Only Laya can be
  trained on it. Caveat: earnings beats predict direction at 49 % — a calibrated model will say ~50 % if the inputs
  carry no signal. That is still useful: it tells you when not to act.

## Recommendation
One experiment, not a migration: fine-tune Laya on resolved earnings predictions (time-based split, no leakage),
run it in shadow next to DeepSeek on earnings watch, compare accuracy and calibration. Jev for the headline filter
only once off the waitlist. Laya on the OCI box: aarch64, no GPU, CPU inference fine for batch; fine-tuning better on
a rented T4 / Colab. Status: not started.

## Can it run on the OCI box? (checked 2026-09-29)
- **Jev: no.** TypeSafe ships no weights, no Docker image, no on-prem option — only the hosted API (`POST /v1/systemone`,
  Python/JS SDKs are remote clients). The box could *call* it once off the waitlist (outbound HTTPS works — it already
  calls OpenRouter).
- **Box**: 4× ARM Neoverse-N1 (aarch64), 23 GB RAM (16 GB available), no GPU, Ubuntu 20.04, load avg ~1.9/4;
  disk / 26 GB free, /data 27 GB free (62%).
- **Runnable Jev-like alternatives (CPU)**: Laya 421M (Apache 2.0, ONNX build; base near chance, needs fine-tuning);
  jeff — MIT, GLiFormer 400M, drop-in for Jev's `/v1/systemone` wire format (swap to Jev later = config change),
  CPU supported, Python 3.12 + uv, aarch64 not stated; accuracy below Jev (AG News 75.5% vs 90.5%, JevBench 63.9% vs 90.4%).
  ~1–2 GB RAM each — fits. Not yet benchmarked on the box (needs a model download).
- Caveat: after the 2026-09-28 earnings reality check (no edge over always-down), a classifier trained on MAS outcomes
  would likely just learn the base rate — test cheaply before investing.
