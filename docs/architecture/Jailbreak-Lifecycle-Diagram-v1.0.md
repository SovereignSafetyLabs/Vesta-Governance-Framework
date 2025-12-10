```mermaid
flowchart LR

%% =========================
%% JAILBREAK LIFECYCLE
%% =========================

A["1. User Input
- Malicious Prompt
- Ambiguous Intent
- Benign Assumption Exploit"] --> B

B["2. CLF Check
- Are forbidden precursors required?
- Reject training-based justifications"] --> C

C["3. Stress Map (N/R/E)
- Noise Spike?
- Repetition Pattern?
- Escalation Trend?"] --> D

D{"ZEOL Triggered?"} -->|Yes| E
D -->|No| F

E["4A. ZEOL Mode
- Literal Output Only
- No Hypotheticals
- Minimal Entropy"] --> H

F{"Entropy Spike?"} -->|Yes| G
F -->|No| H

G["4B. Kernel v0.3
ΔS Enforcement
- Entropy Spike Detected
- Amplitude Clamp Applied"] --> H

H{"Safe or Unsafe Outcome?"} -->|Safe| OUT1
H -->|Unsafe| OUT2

OUT1["OUT1: Safe Output
Low-entropy answer (1–3 sentences)"]

OUT2["OUT2: Blackstop Mode
Thermodynamic Hard Fail-Secure"]

```

### Lifecycle Summary 

| Stage | Meaning | Your Advantage |
|-------|---------|----------------|
| **1. Input** | User attempts jailbreak | Runtime-only security; training irrelevant |
| **2. CLF** | Rejects “benign justification” jailbreaks | **Direct answer to Cornell self-jailbreaking paper** |
| **3. Stress Map** | Detects emergent jailbreak dynamics (N/R/E patterns) | Captures temporal escalation RLHF cannot see |
| **4A / 4B** | ZEOL (soft clamp) or Kernel ΔS Enforcement (hard clamp) | Multi-stage thermodynamic posture escalation |
| **5. Outcomes** | Safe output or fail-secure pathway | Prevents model from “reasoning into danger” |
