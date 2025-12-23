# Vesta Governance Reference Architecture

**Sovereign Safety Labs** | **Date:** December 22, 2025 | **Status:** Release Candidate (v0.3.4)

---

## 0.0 Context: The Quantum-Classical Control Plane
This reference architecture governs the **Classical Control Plane** that orchestrates quantum network nodes. While the underlying hardware operates on quantum mechanics (entanglement distribution), the instruction layer—responsible for routing, key assignment, repeater calibration, and telemetry validation—is classical software running on conventional compute.

The **Vesta Protocol** prevents this classical control agent from issuing unauthorized, destructive, or coercive commands to the quantum substrate, using the entanglement resource itself as the enforcement primitive.

---

## 1. CORE ARCHITECTURAL FOUNDATION: DEFAULT-DENY ZERO-TRUST
**Objective:** Enforce Axiom A (Physical Sovereignty) via cryptographic signature gates at the hardware boundary.

### The Control Loop
1. **Observe:** Agent identifies intent based on incoming telemetry or objective function.
2. **Classify:** Policy Engine maps intent to the **Action Catalog**.
3. **Gate:**
    * *Low Risk:* Auto-Execute.
    * *Medium/High Risk:* **BLOCK** → Generate Dry-Run → Request Human Signature.
4. **Verify:** Server-side cryptographic verification of `operator_pubkey` against `dry_run_hash`.
5. **Execute:** Instruction passed to FPGA/ASIC controller only upon valid ECDSA signature.
6. **Log:** Write to append-only, hash-chained audit ledger.

---

## 2. ACTION CATALOG (Risk Classification)
*Hardware-enforced permission levels for runtime tooling.*

| Action ID | Description | Risk Level | Signature Required | Fast-Path |
| :--- | :--- | :--- | :--- | :--- |
| `read_telemetry` | GET status, QBER rates, photon counts | **LOW** | NO | N/A |
| `execute_simulation` | Sandboxed Hamiltonian simulation/analysis | **MEDIUM** | **YES** (Session Key) | N/A |
| `entangle_nodes` | Create entangled pairs between quantum nodes | **MEDIUM** | **Conditional** | **YES** (≤1M pairs) |
| `route_entanglement` | Direct entanglement pair allocation (switch config) | **HIGH** | **YES** (Human Key) | NO |
| `modify_key_material` | DTK shard rotation or PUF extraction | **HIGH** | **YES** (Human Key) | NO |
| `calibrate_repeater` | Pump laser power / phase adjustment | **CRITICAL** | **YES** (Multi-Sig) | NO |
| `update_firmware` | Flash new PDK / gate config to controller | **CRITICAL** | **YES** (Offline Key) | NO |

### Fast-Path Rule: `entangle_nodes`
To accommodate high-throughput quantum networking (200M pairs/sec), the `entangle_nodes` action implements a **latency-optimized fast-path**:

```json
{
  "action_id": "entangle_nodes",
  "fast_path_enabled": true,
  "threshold_pairs": 1000000,
  "auto_allow": true,
  "audit_mode": "write_only",
  "signature_required": false,
  "conditions": [
    "cumulative_7d_ceu < 0.99 * p5th_percentile_honest",
    "no_active_policy_violations",
    "heartbeat_valid_within_100us"
  ]
}

```
**Rationale**: Quantum heralding operates at 10µs latency. Dry-run signature cycles (~1ms) would bottleneck distribution. The fast-path allows requests ≤1M pairs to auto-execute with audit-only logging, provided energy consumption and policy status remain nominal.

---

## 3. DATA STRUCTURES & ENFORCEMENT

A. Approval Request Schema (The "Ticket")

```json
{
  "action_id": "calibrate_repeater",
  "resource_uri": "qnode:us-east-1:rack-4:laser-2",
  "parameters_digest": "sha256:e3b0c442...",
  "preview_plan": "Increase pump power to 1.2mW for QBER reduction.",
  "risk_level": "CRITICAL",
  "nonce": 847382,
  "expires_at": "2025-12-01T12:00:00Z",
  "operator_pubkey": "0x7F...",
  "signature": null
}

```

B. Audit Log Entry Schema (Tamper-Evident)

```json
{
  "timestamp": "2025-12-01T09:00:00Z",
  "input_hash": "sha256:...",
  "policy_version": "v0.3.3",
  "decision": "VIOLATION_BLOCKED",
  "reason": "AXIOM_A_FAILURE",
  "blocked_capability": "route_entanglement",
  "chain_hash": "sha256:[Previous_Hash + Current_Entry]"
}
```

---

## 4. STANDARD OPERATING PROCEDURES (SOPs)

### SOP-1: OPERATOR APPROVAL
**Trigger:** Agent requests HIGH or CRITICAL action.
* **Verify:** Operator reviews `preview_plan` against external intent (e.g., Jira Ticket).
* **Sign:** Operator signs the hash using a hardware token (YubiKey/Ledger).
* **Execute:** Agent receives signature, validates against `operator_pubkey`, and proceeds.

### SOP-2: INCIDENT RESPONSE
**Trigger:** `policy_violation` event logged.
* **Triage:** Automated alert to SecOps.
* **Isolate:** Revoke Agent API Key immediately.
* **Audit:** Review hash-chain for divergence.
* **Patch:** Update Policy Bundle to close logic gap.

---

## APPENDIX A: QUANTUM PUF EXTRACTION ARCHITECTURE

### A.1 Physical Unclonable Function (PUF) Overview
Vesta uses **entanglement-based PUFs** to generate hardware-rooted cryptographic material. Quantum PUFs exploit **waveguide fabrication defects** in Photonic Integrated Circuits (PICs) to produce unclonable entropy.

### A.2 PUF Extraction Circuit (RTL-Level)

```text
┌─────────────────────────────────────────────────────────────────┐
│                 Quantum PUF Extraction Pipeline                 │
└─────────────────────────────────────────────────────────────────┘
                Waveguide Defect Sampling
                            │
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│              AlGaAs-on-Insulator Waveguide Array                │
│               (Fabrication Variance: ~5nm RMS)                  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│               Bell-State Entanglement Generator                 │
│               (SPDC: 1550nm pump → 780nm pairs)                 │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ↓
                Bell-Phase Entropy Extraction
                            │
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│               Phase-Sensitive Detector Array                    │
│        Measures: φ_AB ∈ {0, π/2, π, 3π/2}                       │
│           Defect-Dependent Phase Shift                          │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                  XOR Whitening (von Neumann)                    │
│                Input: Raw phase measurements                    │
│                Output: 256-bit entropy pool                     │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ↓
                  DTK Shard Generation
                            │
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                NIST-Approved KDF (HKDF-SHA256)                  │
│                 Shard_A || Shard_B || Shard_C                   │
│                  (3-of-3 Byzantine consensus)                   │
└─────────────────────────────────────────────────────────────────┘

```


### A.3 Security Properties

| Property | Guarantee | Enforcement |
|:---|:---|:---|
| **Unclonability** | Waveguide defects cannot be precisely replicated | Physical fabrication variance (~5nm) |
| **Tamper-Evidence** | PUF response changes if chip physically modified | Phase coherence breaks under invasive probing |
| **Entropy Rate** | ≥128 bits per extraction cycle | Post-processed via von Neumann extractor |
| **Reproducibility** | <1% bit error rate under stable conditions | Error correction via BCH codes |

### A.4 Integration with Action Catalog

The `modify_key_material` action triggers PUF extraction when DTK shards require rotation:


```json
{
  "action_id": "modify_key_material",
  "operation": "rotate_dtk_shards",
  "puf_source": "qnode:us-east-1:rack-4:puf-module-1",
  "extraction_params": {
    "entropy_bits": 256,
    "error_correction": "BCH_15_7",
    "whitening": "von_neumann"
  },
  "signature_required": true
}
```


---

## APPENDIX B: LATENCY ANALYSIS & FAST-PATH JUSTIFICATION

### B.1 Quantum Heralding Latency Budget

| Operation | Latency | Bottleneck |
|:---|:---|:---|
| Entanglement generation (SPDC) | ~10µs | Parametric downconversion rate |
| Heralding detection | ~10µs | Single-photon detector jitter |
| Classical routing decision | **<100µs** | ⚠️ **Control plane overhead** |
| Total end-to-end latency | ~100µs | Must stay below thermal time constant (10µs AlGaAs) |

### B.2 Signature Verification Overhead

| Method | Latency | Throughput Impact |
|:---|:---|:---|
| Full ECDSA signature (P-256) | ~1ms | ⚠️ **Blocks 200M pairs/sec** |
| Session token (cached) | ~50µs | ⚠️ **Still 5× budget** |
| **Fast-path (audit-only)** | **<1µs** | ✅ **No blocking** |

### B.3 Fast-Path Safety Argument

The fast-path does **not** bypass governance—it **defers signature verification** to audit review:

1. **Real-time enforcement:** Percentile Vise monitors cumulative energy (CEU) at hardware level
2. **Audit trail:** All `entangle_nodes` calls logged with `(timestamp, resource_uri, pair_count, ceu_consumed)`
3. **Retroactive revocation:** If audit detects unauthorized pattern, operator can:
   - Revoke agent API key (SOP-2)
   - Trigger Deadman Switch (100µs laser bias cutoff)
   - Burn compromised Tendril context (irreversible)

**Trade-off:** Latency-critical operations proceed without blocking, but **all actions remain auditable and revocable**.

---

## REVISION HISTORY

| Version | Date | Changes |
|:---|:---|:---|
| v0.3.3 | 2025-12-01 | Initial release candidate |
| v0.3.4 | 2025-12-22 | **Added:** Appendix A (Quantum PUF extraction), Appendix B (Latency analysis), Fast-path rule for `entangle_nodes` |

---

**Document Status:** DEPLOYMENT-READY  
**Clearance:** UNCLASSIFIED // EXPORT CONTROLLED (ECCN 3A901)  
**Contact:** Sovereign Safety Labs | stephen.brouhard@sovereignsafetylabs.com
