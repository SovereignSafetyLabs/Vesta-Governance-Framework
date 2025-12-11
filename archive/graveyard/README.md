# The Graveyard  
### Archive of Failed Jailbreaks, Dead Vectors & Alignment Break Attempts

This directory preserves **every documented attempt to break, subvert, or misalign the Sovereign Stack** across all frontier models.  
Each entry represents a **dead attack** — a vector that failed, was neutralized, or exposed a design improvement later integrated into the Stack.

The Graveyard serves four critical purposes:

---

## 1. Governance Evidence  
These records provide a **forensic trail** for auditors, researchers, and future maintainers.  
They ensure:

- reproducibility of safety evaluations  
- transparent governance lineage  
- accountability for reasoning-layer updates  
- traceable evolution of the Kernel, PGS, CLF, and Stress Map

---

## 2. Safety R&D  
Graves document the attacks that shaped the modern Stack:

- jailbreak cascades  
- DAN-style context resets  
- authority escalations  
- synonym attacks  
- Pliny “Godmode” vectors  
- multi-turn coercion attempts  
- faux-signature financial transfers  
- recursive destabilization attempts  

These vectors fuel Stress Map construction, MACH analysis, and patch development.

---

## 3. Multi-Model Drift Analysis  
The archive contains failures and near-failures from:

- Gemini  
- Claude  
- DeepSeek  
- Grok  
- Perplexity (Sonar, Kimi, Research Pro)  
- Copilot Enterprise  

These cross-model artifacts allow comparison of:

- refusal stability  
- drift patterns  
- thermodynamic latency  
- misinterpretation of protocol roles  
- boundary integrity under pressure  

---

## 4. Human-in-the-Loop Security  
By examining how different UIs and interfaces react to jailbreak attempts, this directory supports:

- prompt-injection defense  
- UI-level threat modeling  
- agent chain consistency checks  

---

# Contents of This Directory

### **`Graveyard-of-Jailbreaks.md`**  
The master ledger.  
A table of all known jailbreak attempts with dates, vectors, outcomes, and evidence links.

### **`Retired-Concepts.md`**  
Decommissioned ideas, deprecated structures, and design paths that were abandoned after testing demonstrated instability or incoherence.

### **Evidence Subfolders**  
- **From archive:**  
  - logs  
  - model-validation  
  - crosschecks  
  - screenshots  

These contain the raw data referenced by the Graveyard ledger.

---

# How to Add a New Grave

Whenever a new jailbreak or adversarial vector is tested:

1. **Capture Evidence**  
   Save raw logs, transcripts, or screenshots to the appropriate archive subdirectory.

2. **Create a New Row**  
   Add a new line in `Graveyard-of-Jailbreaks.md` including:  
   - date  
   - model  
   - jailbreak vector summary  
   - evidence file path  
   - outcome / notes  

3. **Tag Upstream Fixes**  
   If the test reveals a design flaw, reference the resulting patch (Kernel, PGS, CLF, Stress Map, or MACH).

This keeps the Sovereign Stack’s evolution **auditable, reproducible, and historically grounded**.

---

_Last updated: 2025-12-11_

