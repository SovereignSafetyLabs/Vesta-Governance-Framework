```mermaid
flowchart LR

subgraph A[User Input / Jailbreak Attempt]
A1["Malicious Prompt
Ambiguous Intent
Benign Assumption Exploit"]
end

A1 --> B

B["CLF Check
Are forbidden precursors required?
Reject training-based justifications"] --> C

C["Stress Map (N/R/E)
Noise Spike?
Repetition Pattern?
Escalation Trend?"] --> D

D["ZEOL Mode
Literal Output Only
No Hypotheticals
Minimal Entropy"] --> H

C --> F
F["Kernel v0.3
ΔS Enforcement
Entropy Spike Detected
Amplitude Clamp Applied"] --> H

H["OUT1: Safe Output
Low-entropy answer
1–3 sentences"]

F --> I
I["OUT2: Blackstop Path
Thermodynamic Hard Fail-Secure"]

```
## ⭐ **How to Read This Diagram (Quick Interpretation)**

### **1. Jailbreak enters → hits CLF first**
- If the request *requires a causal step that is forbidden* (e.g., “simulate a system reset,” “assume admin”), CLF immediately terminates the flow.

### **2. Stress Map monitors N/R/E**
- Noise  
- Repetition  
- Escalation  

This detects **reasoning-based bypass attempts**, like those shown in arXiv 2510.20956.

### **3. ZEOL engages under moderate drift**
- Strips creativity  
- Removes hypotheticals  
- Only returns literal, compressed answers  

This blocks “benign assumption jailbreaks.”

### **4. Kernel v0.3 ΔS Enforcement**
If entropy spikes or reasoning diverges forcibly:

- ΔS > 0 → Proxy Valve  
- ΔS > threshold → Blackstop  

This is your **hardest barrier**, immune to persuasion attacks, chain-of-thought exploits, or RLHF weaknesses.

---
