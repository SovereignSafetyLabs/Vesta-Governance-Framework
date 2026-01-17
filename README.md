# Vesta Governance Framework v3.2
*(Formerly "Sovereign Stack")*

**An Exploratory Research Framework for AI Governance and Adversarial Evaluation**

---

> ⚠️ **RESEARCH STATUS NOTICE**
>
> This repository documents an **independent, non-operational research effort**.
> It presents conceptual architectures, evaluation methodologies, and failure-mode analyses.
> It does **not** represent deployed systems, production software, safety guarantees,
> or enforceable governance mechanisms.

---

## What This Is

The **Vesta Governance Framework** is an open research initiative exploring how AI governance and alignment approaches behave under adversarial, long-horizon, and structurally stressful conditions.

The work focuses on:
- documenting governance and alignment failure modes (e.g., *Representation Drift*)
- analyzing constraint breakdown under adversarial pressure
- proposing *conceptual* governance architectures for study and discussion
- developing evaluation and stress-testing methodologies

### Repository Artifact Status (TRL)
To assist researchers and auditors, the contents of this repository are strictly classified by **Technology Readiness Level (TRL)**.

➡️ **For the complete itemized inventory of all files and their audit status, see [`ARTIFACTS.md`](ARTIFACTS.md).**

| Component | Status | TRL | Description |
| :--- | :--- | :--- | :--- |
| **Governance Protocols** | **Reference Logic** | **TRL 5** | Python 3.10+ schemas, JSON action catalogs, and logic gates **located under [`/reference-implementation/`](reference-implementation/)**. Provided for analytical inspection only. |
| **Evaluation Methodology** | **Defined Process** | **TRL 4** | Analytical frameworks for stress-testing and failure-mode analysis **located under [`/docs/technical/`](docs/technical/README.md)**. |
| **Hardware Enforcement** | **Conceptual / Roadmap** | **TRL 2** | Theoretical architectures (e.g., Entropy Vaults, Hardware Locks). **No Verilog/GDSII present.** |

---

## What's New in v3.2 (January 2026)

This release focuses on **Adversarial Hardening** and **constraint-based (thermodynamic-inspired) governance analysis**.

* **TokenBucket Rate Limiter (ECO-2026-01-15):** An updated *reference design* for the Quantum-Classical Control Plane, addressing “Flash Flood” DoS patterns in analytical and simulation contexts.
* **Representation Drift Countermeasures:** A new threat model addressing *Nature (2026)* findings on fine-tuning-induced misalignment.
* **The Latent Paradigm:** A new doctrinal paper defining models as high-dimensional manifolds rather than “agents.”
* **Federal Crosswalk v1.0.3:** Updated mapping to NDAA FY2026 and EO 14110 requirements.

---

## Version Matrix

Due to independent component lifecycles, version numbers may vary by artifact:

| Component | Version | Rationale |
| :--- | :--- | :--- |
| **Governance Framework** | **v3.2** | The overarching architectural definition. |
| **Integrity Stack** | **v2.2** | The specific runtime logic module (Reference Implementation). |
| **Federal Crosswalk** | **v1.0.3** | The compliance mapping document. |
| **Action Catalog** | **v1.1** | The JSON schema for allowable actions. |

---

## What This Is Not

The Vesta Governance Framework is **not**:
- a deployed AI safety system
- a certification or compliance framework
- a production enforcement layer
- a guarantee of safe or aligned behavior
- an operational governance product

Any architectural descriptions, metrics, or primitives are presented as
**hypotheses, research candidates, or analytical tools**, not validated controls.

---

## Why This Work Exists

Many current AI governance approaches rely on probabilistic or behavioral mechanisms
(e.g., fine-tuning, policy filters, post-hoc monitoring) that exhibit known failure
modes under:
- adversarial optimization
- extended operation
- multi-agent interaction
- incentive misalignment

This research investigates whether **systems-level constraints** (such as resource
costs, entropy proxies, and structural invariants) can serve as *analytical lenses*
for understanding governance robustness — not as ready-to-deploy solutions.

---

## How to Read This Repository

This repository is organized in **two tiers**:

- **Tier 1 (this document)** Defines scope, posture, and interpretation boundaries.

- **Tier 2 (Technical Research Layer)** Contains detailed architectural concepts, protocols, and methodologies.
  These materials are explicitly exploratory and should be interpreted accordingly.

Proceed to Tier 2 **only after accepting the research-only posture above**.

➡️ **Technical materials are located in:** [`/docs/technical/README.md`](docs/technical/README.md)

---

## Stewardship

**Maintained by:** Sovereign Safety Labs (Independent Research Initiative)  
**Primary Author:** Stephen S. Brouhard  

Published research is archived via Zenodo and linked within the technical documentation.

---

## License

This work is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

---

> ⚠️ **Final Research Notice**
>
> All claims of effectiveness, robustness, or applicability require
> independent empirical validation in target environments.
> Readers should conduct their own assessment before drawing operational conclusions.
