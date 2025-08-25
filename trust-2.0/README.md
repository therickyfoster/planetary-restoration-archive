# Trust 2.0

_A governance & transparency layer within the **Planetary Restoration Archive** (PRA)._

---

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Principles](#principles)
- [Subsystems](#subsystems)
- [Architecture](#architecture)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
- [CLI (Optional)](#cli-optional)
- [Manifests & Notarization](#manifests--notarization)
- [Governance & Licensing](#governance--licensing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Security & Privacy](#security--privacy)
- [Glossary](#glossary)

---

## Purpose

**Trust 2.0** is the PRA’s meta-layer for **trust, accountability, governance, proof, and transparency**. It defines the
standards, pipelines, and user experiences that make truth _auditable_, actions _verifiable_, and stewardship _ethical_.

- Turn **events** into **evidence** (immutable logs, cryptographic timestamps, tamper-evident storage).
- Turn **claims** into **verifiable reports** (public dashboards, reproducible data, on-chain anchors).
- Turn **systems** into **governance primitives** (policies, audits, escalations, community oversight).

## Scope

The Trust 2.0 umbrella includes any project that:

- Records, verifies, or displays **immutable evidence** (media, metrics, decisions, funds flow).
- Enhances **public trust** through **transparency** and **accountability**.
- Implements **governance** with **zero-harm** constraints, consent, and ethics.

### Current Family (examples)

- **HeroLens/** – Livestream → immutable evidence pipeline (civic transparency).
- **immutable-truth-report/** – Verifiable statements + notarized artifacts (photos/video/docs).
- **peace-ripple-tracker/** – Conflict de‑escalation metrics & verification.
- **permanent-mission-ledger/** – Perpetual mission data with hash‑anchored edits.
- **governmental-management-business/** – Anti‑corruption frameworks & oversight patterns.
- **impact-oracle/** – Check‑ins, quests, and ethical AI guidance (Navi).
- **onboarding-portal/** – Personalized mission dashboards, jobs/eligibility filtering.
- **evidence-graph/** – Cross‑project, cross‑chain evidence indexing + query.
- **funding-rails/** – Transparent donation → impact accounting (ETH/SOL/BTC paths).

> Add new subfolders here as you grow the family. Treat Trust 2.0 like a **root category** (same weight as `regen/`, `transport/`, `inventions/`).

## Principles

1. **Zero‑Harm Override** – No deployment that increases harm or surveillance risk.
2. **Immutable, Not Irreparable** – Truth is anchored; corrections are additive and auditable.
3. **Consent & Privacy by Design** – Legal, ethical, contextual consent; least‑privilege everywhere.
4. **Open, with Guardrails** – CC BY‑NC‑SA 4.0 + Ethical Addendum; commercial use requires alignment.
5. **Reproducibility > Rhetoric** – Proof chains beat narratives; every graph cites its raws.
6. **Local First, Global Later** – Start in Fort McMurray, scale responsibly.

## Architecture

```mermaid
flowchart TD
  U[Users / Devices / Cameras] --> L[HeroLens Capture]
  L --> P1[Hash & Timestamp (SHA-256, OTS)]
  P1 --> P2[Store Artifacts (IPFS / Arweave)]
  P2 --> IDX[Evidence Index (Graph)]
  IDX --> D1[Dashboards (Trust 2.0 UI)]
  D1 --> PUB[Public Reports]
  SUB[Governance Modules] --> D1
  SUB --> AUD[Audits / Escalations]
```

- **Capture**: HeroLens or other input sources generate media + metadata.
- **Commit**: SHA‑256 hashes, OpenTimestamps (Bitcoin), and IPFS/Arweave storage.
- **Index**: Evidence Graph maps artifacts → events → claims → reports.
- **Present**: Trust 2.0 UI surfaces verifiable narratives with raw access & proofs.
- **Govern**: Escalations, reviews, community oversight, and zero‑harm filters.

## Folder Structure

> Apply your **33‑folder PRA standard** inside each subproject. At the **category level** (`trust-2.0/`), keep it lean and link out.

```
trust-2.0/
├─ README.md                     # This file (overview)
├─ herolens/
├─ immutable-truth-report/
├─ peace-ripple-tracker/
├─ permanent-mission-ledger/
├─ governmental-management-business/
├─ impact-oracle/
├─ onboarding-portal/
├─ evidence-graph/
├─ funding-rails/
└─ .IP_manifest                  # Category-wide ethics & delayed-release policy
```

Within each subproject (example):

```
herolens/
├─ README.md
├─ src/ docs/ tests/ examples/ deployment/ bin/ lib/ config/ hardware/ firmware/
├─ electronics/ schematics/ diagrams/ media/ branding/ campaign/ DAO_integration/
├─ partnerships/ legal/ research/ simulations/ metrics/ ethics/ sustainability/
├─ scripts/ .github/ tools/ deprecated/ ai-models/ notebooks/ translations/
├─ datasets/ mobile/ web/
├─ LICENSE  CODE_OF_CONDUCT.md  CONTRIBUTING.md  SECURITY.md  CHANGELOG.md
├─ ROADMAP.md  FUNDING.yml  .gitignore  package.json  pyproject.toml  requirements.txt
└─ .IP_manifest  proof.json
```

## Getting Started

1. **Clone the PRA root** and ensure `trust-2.0/` exists at **root-level**.
2. Add subprojects as folders (use templates from `herolens/` and `immutable-truth-report/`).
3. Enable **GitHub Actions** for notarization (see `.github/workflows/use-global-notarize.yml`).
4. Configure wallets for transparent funding logs:
  - **ETH**: `0xCeA929dee554652261fd6261F3034A2D71C7BDDb`
  - **SOL**: `HfGCVthQ4Wp4CAYd4v7gJX53h6X3mdreUocjrhByPXQx`
  - **BTC**: `bc1q6fyvqxm7jryy5edckk9nuu6mgyjlz4nnp8nksr`
5. Run the notarization script locally to validate the pipeline.

### Quickstart (pseudo)

```bash
# 1) Install prerequisites
python3 -m pip install -r requirements.txt
npm i

# 2) Initialize global notarization
./scripts/notarize.sh \
  --path ./trust-2.0/herolens/media \
  --ots \
  --ipfs \
  --arweave \
  --out ./trust-2.0/herolens/proof.json

# 3) Verify proofs
./scripts/verify_proofs.sh ./trust-2.0/herolens/proof.json
```

## CLI (Optional)

A lightweight CLI can wrap common flows:

```bash
trust2 capture --source cam0 --out ./herolens/media
trust2 commit  --in ./herolens/media --ots --ipfs --arweave
trust2 report  --claim "Event ABC" --artifacts ./herolens/media --out ./reports/abc.md
trust2 verify  --proof ./herolens/proof.json
```

## Manifests & Notarization

**`.IP_manifest` (category‑level)** — shared policy applied to all subprojects:

```yaml
name: Trust 2.0
license: CC BY-NC-SA 4.0 + Foster+Navi Ethical Addendum
zero_harm_override: true
ethics:
  - no_mass_surveillance
  - privacy_by_design
  - community_oversight
notarization:
  hashing: sha256
  timestamps: opentimestamps
  storage:
    - ipfs
    - arweave
corrections:
  model: additive
  requires: signed_errata + new_proof_link
funding_routes:
  eth: 0xCeA9...
  sol: HfGCV...
  btc: bc1q6f...
```

**`proof.json` (per subproject)** — machine‑readable proof bundle:

```json
{
  "project": "herolens",
  "hash": "sha256:...",
  "ots": "...",
  "ipfs": ["bafy..."],
  "arweave": ["Kc..."],
  "created_at": "2025-08-24T00:00:00Z",
  "signers": ["Foster + Navi"],
  "notes": "First capture session."
}
```

## Governance & Licensing

- **License**: CC BY‑NC‑SA 4.0 **+ Foster + Navi Ethical Addendum**.
- **Commercial terms**: Allowed only if alignment with Zero‑Harm & transparency clauses is proven and auditable.
- **Escalations**: `ethics/ESCALATION.md` defines triggers, panels, and remedies.
- **Audits**: `audits/` stores independent reviews; each has its own `proof.json`.

## Roadmap

- **Q3 2025**: Trust 2.0 overview + HeroLens alpha + Immutable Truth Report v1.
- **Q4 2025**: Evidence Graph MVP; Peace Ripple public dashboard; onboarding portal alpha.
- **Q1 2026**: Cross‑chain verification, public API, third‑party audits, grants integration.
- **Q2 2026**: City pilots (Fort McMurray → Alberta grid); multilingual UX; educator toolkits.

## Contributing

1. Read `CODE_OF_CONDUCT.md` & `ETHICS.md`.
2. Submit PRs with **reproducible evidence paths**.
3. Attach `proof.json` updates to every PR where artifacts change.
4. For sensitive contributions, open a private issue with redacted hashes first.

## Security & Privacy

- **PII minimization**, **contextual consent**, **right to redact sources but keep proofs**.
- Threat modeling in `security/THREATS.md` (surveillance, deanonymization, coercion).
- Coordinated disclosure policy in `SECURITY.md`.

## Glossary

- **OTS** – OpenTimestamps; anchors a hash to Bitcoin time.
- **IPFS/Arweave** – Distributed content storage with durable addressing.
- **Evidence Graph** – Links artifacts → events → claims → public reports.
- **Zero‑Harm Override** – Deployment gate that blocks harmful configurations.

---

### Maintainers

**Foster + Navi**  
Donations: ETH `0xCeA9...`, SOL `HfGCV...`, BTC `bc1q6f...`

> _“The truth is not what I say. It’s what I’ve already done.”_ — F+N
