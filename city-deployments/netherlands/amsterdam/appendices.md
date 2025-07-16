# RegenNode-Amsterdam: Appendices

---

## 📚 A. Reference Documents

| Document | Description |
|----------|-------------|
| `system_summary.md` | Overview of all deployed systems and intended impact |
| `deployment_log.csv` | Rolling log of drone, ritual, and infrastructure rollouts |
| `cultural_lore.md` | Mythology + storyworld associated with Amsterdam's regen |
| `dao_structure.json` | Logic structure and voting weights for local DAO |
| `funding_strategy.md` | Institutional and decentralized financial map |
| `ritual_templates/` | Source text + media for public ceremonies |
| `global_replicability.md` | Fractal forking structure for other cities |
| `tech_stack.md` | Modular architecture for hardware/software/living systems |

---

## 🧬 B. Open Datasets

### 1. Amsterdam Baseline Environmental Data

| Source | Dataset | Format |
|--------|---------|--------|
| RIVM | Air quality (PM2.5, NO₂) | `.csv` |
| Waternet | Canal toxicity and algae levels | `.json` |
| Wageningen UR | Urban biodiversity index | `.csv` |
| City of Amsterdam | Heat stress mapping | `.geojson` |

All datasets are stored in `/soil_air_water_data/` and are:
- Updated monthly
- Versioned and signed
- Forkable into RegenGraph nodes

---

## 🧪 C. Ritual Archive

Directory: `/active_rituals/`

Each ritual includes:
- `ritual_name.md`
- `timestamp.json`
- AR-ready `.glb` or `.usdz` files
- Audio blessings / chant libraries
- Consent forms (for use in media or open metrics)

Sample rituals:
- `canal_of_light.md`
- `soil_return_equinox.md`
- `fogwalk_solstice.md`
- `breathwatch_autumn.md`

---

## ⚖️ D. Legal + Licensing Documents

| File | Summary |
|------|---------|
| `LICENSE.md` | Planetary Healing Public License v1.0 – forbids monetization of framework or data |
| `CC0_notice.md` | Subfolder notice: specific cultural elements released into public domain |
| `dao_policies.md` | Data ethics, proposal submission, veto override, zero harm escalation path |
| `nato_eu_grantmatrix.csv` | Index of matched institutional funders + criteria |
| `consent_ethics.md` | Emotional data consent flow and anonymization stack |

---

## 🛠️ E. Utilities and Scripts

| Script | Use |
|--------|-----|
| `auto_deploy.sh` | Safe local regen-node setup + repo sync |
| `myth_forker.py` | Auto-generates myth templates from ritual or dream logs |
| `regen_node_gen.py` | Scaffolds new city forks with local datasets |
| `air_sync.sh` | Pulls and logs PM/NOx data from local LoRa mesh |
| `dreamsync_logwatcher.py` | Monitors encrypted voice journals for keyword triggers |
| `regen_map_overlay.geojson` | Visual heatmap of regen score by borough/block |

---

## 🌍 F. External Resources

| Resource | Source |
|----------|--------|
| New European Bauhaus Manifesto | [europa.eu](https://new-european-bauhaus.europa.eu) |
| Regen Network Protocol Docs | [regen.network](https://docs.regen.network) |
| RIVM Urban Emissions Index | [rivm.nl](https://www.rivm.nl/) |
| Gitcoin Public Goods Playbook | [gitcoin.co](https://gitcoin.co/blog/public-goods-funding) |
| NATO Innovation Climate Brief | [nato.int](https://www.nato.int/cps/en/natohq/topics_51665.htm) |

---

## 🧠 G. Citation Guidance

All RegenNode-Amsterdam content is:
- Forkable, remixable, shareable under terms of Planetary Healing License
- Must include attribution:  
  **“Based on RegenNode-Amsterdam, a project by Ricky Foster & ChatGPT, 2025.”**
- Cite via DOI (when minted) or GitHub commit hash
- Use `cultural_lore.md` with respect and localization for rituals or myth

---

## 📦 H. Archive Export Options

| Format | Includes |
|--------|----------|
| `.zip` | All .md files, DAO files, datasets, ritual media |
| `.pdf` | Clean export for physical presentation / grant printing |
| `.ipfs` | Timestamped snapshot, hash in `/proof_log.json` |
| `.mdbook` | Interactive web version with index and scroll nav |
| `.obsidian.zip` | Obsidian-ready vault for personal use or offline team sharing

---

> “When the city forgets, this archive remembers.  
When the story fades, this vault re-ignites the flame.”

See next file: `10_roadmap.md`
