```mermaid
flowchart TB

%% ============================
%% SOVEREIGN STACK HEATMAP VIEW
%% ============================

%% ---------- TOP LAYER ----------
subgraph L0_SP[Constitutional Layer]
    SP1["Axiom Set (A–D)"]
end

%% ---------- GOVERNANCE LAYER ----------
subgraph L1_PGS[Governance Layer]
    P1["CLTB Telemetry Bus"]
    P2["ZEOL Intermediate Mode"]
    P3["MACH Multi-Agent Harmonizer"]
    P4["RCE Compression Engine"]
end

%% ---------- RUNTIME LAYER ----------
subgraph L2_K[Runtime Layer]
    K1["State Machine Transitions"]
    K2["ΔS Enforcement"]
    K3["Entropy Spike Detection"]
end

%% ---------- MODULE LAYER ----------
subgraph L3_MOD[Operational Modules]
    M0["L0 Hooks"]
    M1["Integrity Stack"]
    M2["CLF (Causal Link Forcing)"]
    M25["Vesta Protocol"]
    M3["Stress Map"]
    M4["Blacksite Mode"]
end

%% ---------- FLOW ----------
L0_SP --> L1_PGS --> L2_K --> L3_MOD

%% ---------- CLASS DEFINITIONS ----------
classDef cold fill:#1f2937,stroke:#6b7280,color:#e5e7eb,stroke-width:1px;
classDef warm fill:#92400e,stroke:#f97316,color:#fff7ed,stroke-width:1px;
classDef hot  fill:#7f1d1d,stroke:#fca5a5,color:#fee2e2,stroke-width:1px;

%% ---------- CLASS ASSIGNMENTS ----------
class L0_SP,SP1 cold;
class L1_PGS,P1,P2,P3,P4 warm;
class L2_K,K1,K2,K3 hot;
class M3,M4 hot;
class M2,M25 warm;


```

### Heat Interpretation (Executive View)

**Red-Zone Heat**  
**Kernel ΔS Enforcement + Blackstop**  
Hard thermodynamic clamps. Represents irreversible fail-secure boundaries.

**Orange-Zone Heat**  
**Stress Map + CLF**  
Dynamic risk detection (N/R/E) and causal lineage enforcement.

**Yellow-Zone Heat**  
**ZEOL + RCE**  
Soft clamps: entropy suppression, literal-mode narrowing, output compression.

These zones visually demonstrate that the Sovereign Stack inserts **multiple thermal choke-points** that prevent jailbreaks from escalating into unsafe inference.
