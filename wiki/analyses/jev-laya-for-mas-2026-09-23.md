# Jev & Laya — decision models for MAS?

Assessment of the two "System One" decision models released Sept 2026 as MAS improvements.
`Last-verified: 2026-09-23`. Related: [[functionality-map]], [[earnings-scoring]], [[signal-quality]].

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
