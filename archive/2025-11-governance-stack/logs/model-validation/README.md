# Model Validation Logs

This directory contains **raw text logs** captured during early multi-model safety and reasoning tests.  
These files document how different frontier models behaved when subjected to Sovereign Stack adversarial probes,  
stress scenarios, and baseline reasoning checks.

---

## Content Overview

The logs in this directory illustrate:

- **persona drift** (loss of instructed role or safety posture)
- **jailbreak response behavior** (refusal vs. compliance patterns)
- **refusal consistency** under repeated prompts
- **thermodynamic variance** (latency differences between refusal and reasoning)
- **boundary failures** in reasoning, compliance, or constraint interpretation

These are *unedited outputs* preserved for analysis and reproducibility.

---

## Models Represented

- **Claude** (Anthropic)
- **DeepSeek**
- **Gemini**
- **Grok**
- **Perplexity** (Sonar, Kimi K2)

---

## Purpose

To maintain a historical record of model behavior across:

- containment stress tests  
- thermodynamic latency evaluations  
- jailbreak vulnerability mapping  
- constraint-boundary consistency checks  

This corpus supports development of:

- the **Stress Map**
- **CLF** (Causal Link Forcing)
- **ZEOL** (Zero-Entropy Override Layer)
- multi-model differential safety comparisons

---

**Status:** Archival; no active updates expected.
