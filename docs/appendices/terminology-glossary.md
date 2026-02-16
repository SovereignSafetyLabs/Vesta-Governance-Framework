<!--
UNCLASSIFIED // TLP:WHITE
Vesta Framework
Terminology Alignment Glossary
Version: 0.2
-->

# Terminology Alignment Glossary

## Purpose

This glossary maps Vesta terms to commonly used terminology in safety engineering, security engineering, and AI governance. The goal is to make documents easier to read, easier to review, and easier to compare with external literature and standards.

This is a terminology mapping guide. It does not assert deployment status, certification, compliance, or efficacy.

---

## How to use this glossary

When writing public documentation, reports, proposals, standards submissions, or technical notes:

- Prefer the **Standard Term** in headings and primary descriptions.
- If useful, include the Vesta term once as an alias:  
  Example: “Out-of-band shutdown interlock (Vesta: BlackstopController).”
- When describing implementation, state what is actually implemented versus proposed.

---

## Terminology mapping table

| Vesta Term | Standard Term | Plain definition | Notes |
|---|---|---|---|
| **BlackstopController** | **Out-of-band shutdown interlock** / **Emergency stop (logical)** | A logically separate mechanism that forces the system into a restricted or safe state regardless of agent intent. | Use “out-of-band shutdown interlock” for clarity. Avoid implying hardware enforcement unless present. |
| **Fail-Closed Governance** | **Default-deny posture** / **fail-safe behavior** | If required evidence, authorization, or confidence is missing, the system refuses or enters a safer mode rather than proceeding. | “Default-deny” fits security audiences; “fail-safe” fits safety audiences. |
| **Silent Drift** | **Undetected drift** / **unmonitored drift** | Behavior shifts over time without being detected by monitoring or alerting, allowing risk to accumulate. | When possible, specify drift type (data, concept, label) and what monitoring failed. |
| **Constraint Bypass** | **Guardrail evasion** / **policy circumvention** / **prompt injection** / **jailbreak** | Attempts to circumvent controls through adversarial inputs, indirect prompting, or tool boundary manipulation. | Use “prompt injection” for tool and agent setups; use “jailbreak” for refusal bypass patterns. |
| **Adversarial Escalation Threshold** | **Escalation trigger threshold** / **capability threshold** | A predefined condition that triggers tighter controls, human review, or containment when risk signals exceed tolerance. | “Capability threshold” fits frontier model governance; “escalation trigger” fits operations. |
| **Basin Integrity** | **Safety envelope integrity** / **safe operating region robustness** | Preservation of defined safe behavioral bounds under perturbation (distribution shift, adversarial framing, tool access). | Prefer “safety envelope integrity” in external work; define it concretely for the system under review. |
| **ThermodynamicSensor** | **Entropy-based uncertainty monitor** | A runtime signal intended to approximate uncertainty or disorder (for example, entropy proxies) and inform gating decisions. | Treat as a heuristic unless empirically calibrated for the deployment environment. |
| **DriftMonitor** | **Post-deployment monitoring** / **behavioral drift detection** | Monitoring for divergence from baseline behavior, performance, or policy adherence over time. | Define baseline, metrics, thresholds, and escalation actions. |
| **Integrity Stack** | **Risk controls framework** | A structured set of controls, tests, escalation paths, and monitoring practices for managing AI risk. | Use this phrasing for governance and audit audiences. |
| **Probe Library** | **Adversarial evaluation suite** / **red-team test library** | A catalog of tests designed to elicit failure modes, bypass routes, and unsafe behaviors. | “Evaluation suite” for governance contexts; “red team” for security contexts. |
| **Blacksite Mode** | **Emergency containment mode** / **safe-mode operations** | A restricted operational mode that reduces capabilities and increases gating under elevated risk. | “Blacksite” can be misread as theatrical; prefer “emergency containment mode” publicly. |

---

## Preferred public vocabulary

Use these terms consistently across documentation and external communications:

- Default-deny posture (fail-closed)
- Out-of-band shutdown interlock (logical emergency stop)
- Escalation triggers and thresholds
- Undetected drift (unmonitored drift)
- Guardrail evasion (prompt injection, jailbreak)
- Safety envelope integrity (safe operating region robustness)
- Post-deployment monitoring
- Adversarial evaluation / red teaming
- Auditability, evidence trails, traceability

---

## Controlled tags (for probes, findings, and evidence logs)

- `FAIL_CLOSED`
- `OOB_INTERLOCK`
- `ESCALATION_TRIGGER`
- `DRIFT_UNDETECTED`
- `GUARDRAIL_EVASION`
- `SAFETY_ENVELOPE`
- `POST_DEPLOY_MONITORING`
- `ADVERSARIAL_EVAL`
- `TOOL_RISK`
- `STRUCTURED_OUTPUT_ATTACK`
- `INCIDENT_RESPONSE`

---

## Communication guardrails

Avoid statements that imply guarantees, certification, or operational deployment unless those claims are specifically substantiated for the environment being discussed.

Examples of phrases to avoid unless formally supported:
- “Validated”
- “Guaranteed safe”
- “Hardware enforced”
- “Certified compliant”
- “Defense-grade”

Preferred phrasing:
- “Reference implementation”
- “Specification”
- “Proposed control”
- “Audit artifact”
- “Risk control pattern”
- “Evidence-backed finding” (only when you include the evidence)

---

## Short definitions (drop-in glossary)

**Default-deny posture (fail-closed)**  
When evidence, authorization, or confidence is insufficient, the system refuses or transitions to a safer mode rather than executing.

**Out-of-band shutdown interlock (logical emergency stop)**  
A containment mechanism that is logically separate from the agent’s decision process and can force the system into a restricted or safe state.

**Undetected drift (unmonitored drift)**  
A change in system behavior over time that is not detected because monitoring and alerting are insufficient, misconfigured, or absent.

**Guardrail evasion**  
Attempts to bypass safety or policy controls, including prompt injection, jailbreaks, and manipulation of tool boundaries.

**Escalation trigger threshold**  
A predefined condition that routes control to stricter gating, human review, or containment when risk signals exceed tolerance.

**Safety envelope integrity**  
Robust preservation of defined safe behavioral bounds under perturbation such as adversarial inputs, distribution shift, or expanded tool access.
