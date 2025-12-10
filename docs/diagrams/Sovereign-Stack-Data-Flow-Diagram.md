# Sovereign Stack — Data Flow Diagram  
Layered Telemetry & Constraint Movement

```mermaid
flowchart TD

%% Constitutional Layer
A[Sovereign Protocol<br/>v3.0 + v3.1] --> B[PGS v1.1<br/>Governance Layer]

%% Governance Layer -> Runtime
B --> C[Kernel v0.2<br/>Runtime Engine]
B --> D[Kernel v0.3<br/>Thermodynamic Kernel]

%% Runtime -> Modules
C --> E[L0–L4 Modules]
D --> E

%% Modules -> Telemetry Upward
E --> F[Stress Map<br/>N/R/E Signals]
F --> G[CLTB<br/>Cross-Layer Telemetry Bus]

%% Telemetry Upward to Runtime
G --> C
G --> D

%% Governance Constraints Downward
A --> B --> C --> E

```

Narrative Explanation
Telemetry (bottom → up)

Modules generate operational telemetry (N/R/E, confidence, causality).

Stress Map consolidates signal pressure.

CLTB performs unified, read-only telemetry aggregation.

Kernel consumes CLTB to determine posture, entropy state, and mode transitions.

Constraints (top → down)

Sovereign Protocol defines constitutional physics.

PGS v1.1 generates governance constraints (ZEOL, RCE, MACH).

Kernel enforces deterministic or thermodynamic transitions.

Modules execute the constraints and update telemetry.

This creates a closed governance loop with no ambiguity or softness under load.

END OF DOCUMENT
