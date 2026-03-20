---
layout: article
title: 'Nuclear Energy'
description: 'Market overview of nuclear reactor technologies.'
github_repo: 'matejkajinic/nuclear-energy'
github_url: 'https://github.com/matejkajinic/nuclear-energy'
source_path: 'README.md'
last_commit_sha: '35391f7ced9849b42f28b20fa4387bbb506ed8d1'
last_commit_date: '2024-07-22T12:00:00Z'
---

<!-- Generated at 2026-03-20T22:14:57Z by scripts/sync_writing.py -->

# Advanced and Emerging Nuclear Reactor Technologies

This repository contains curated information on advanced nuclear reactors, focusing on Generation III+ and Generation IV designs. The data is structured to be easily parsed and understood, providing a reference for developers, researchers, and AI models.

## 1. Advanced Nuclear Reactor Designs (Gen III+ & Gen IV)

Tripling nuclear capacity by 2050 will require a combination of proven Gen III+ designs and innovative Gen IV concepts. The primary differences lie in their coolants, fuel types, and operating temperatures, which in turn dictate their applications and power output.

| Category | Gen III+ | Gen IV (Gas) | Gen IV (Liquid Metal) | Gen IV (Molten Salt) |
|----------|-----------|--------------|----------------------|---------------------|
| **Coolant** | Light water | Gas | Liquid metal | Molten salt |
| **Examples** | • Pressurized water reactor<br>• Boiling water reactor | • High temperature gas reactor<br>• Gas fast reactor | • Sodium fast reactor<br>• Lead fast reactor | • Fluoride high temp. reactor<br>• Molten chloride fast reactor |
| **Typical Fuel** | LEU, LEU+ | HALEU | HALEU | HALEU |
| **Outlet Temp.** | ~300°C | ~750°C | ~550°C | ~750°C |
| **Power Output** | Large, Small | Small, Micro | Small, Micro | Small |
| **Example Designers** | • GE Hitachi<br>• Holtec<br>• NuScale<br>• Westinghouse<br>• Last Energy<br>• Deep Fission<br>• Southern Nuclear<br>• Blue Energy | • BWXT<br>• General Atomics<br>• Radiant<br>• X-energy<br>• Antares<br>• Ultra Safe Nuclear Corp | • HolosGen<br>• ARC<br>• TerraPower<br>• Oklo<br>• Aalo Atomics<br>• Blykalla<br>• Newcleo | • Kairos<br>• Terrestrial<br>• Copenhagen Atomics<br>• Moltex Energy<br>• ThorCon<br>• Seaborg Technologies |

## 2. Nuclear Fuel Types

The evolution of reactor design is closely linked to advancements in nuclear fuel.

**LEU (Low-Enriched Uranium):**
- Enrichment: Typically enriched to 3-5% U-235.
- Use: Fuel for most of the world's current commercial nuclear reactors.

**LEU+ (Low-Enriched Uranium Plus):**
- Enrichment: Usually enriched to 5-10% U-235.
- Use: Required by some modern, advanced reactor designs.

**HALEU (High-Assay Low-Enriched Uranium):**
- Enrichment: Between 10-20% U-235 (typically near 19.75% to remain within the low-enriched category).
- Use: Enables smaller, more efficient reactor designs with longer core lifespans, making it the fuel of choice for many advanced and micro-reactors.

## 3. Emerging Nuclear Reactor Technologies

This table details specific advanced reactor designs currently under development by various companies worldwide.

| Company Name | Reactor Name | Reactor Size (MWe) | Expected First Operation | Type of Reactor | Fuel | Proposed Use Case |
|--------------|--------------|-------------------|-------------------------|-----------------|------|-------------------|
| TerraPower | Natrium | 345 | 2030 | Sodium fast reactor | HALEU | Grid-scale power |
| Moltex Energy | SSR-W (Stable Salt Reactor - Wasteburner) | 300 | Early 2030s | Molten salt reactor | Spent nuclear fuel | Grid-scale power |
| General Atomics | EM2 (Energy Multiplier Module) | 265 | 2030s | Gas fast reactor | Spent nuclear fuel | Grid-scale power |
| ThorCon | ThorCon | 500 | 2029 | Molten salt reactor | LEU | Grid-scale power |
| Terrestrial Energy | IMSR (Integral Molten Salt Reactor) | 195 | Late 2020s | Molten salt reactor | LEU | Grid-scale power and industrial heat |
| Kairos Power | KP-FHR | 140 | 2026 | Fluoride high temperature reactor | TRISO | Grid-scale power |
| ARC Clean Energy | ARC-100 | 100 | 2029 | Sodium fast reactor | HALEU | Grid-scale power |
| Seaborg Technologies | CMSR (Compact Molten Salt Reactor) | 100 | 2028 | Molten salt reactor | LEU | Modular power for remote areas |
| X-energy | Xe-100 | 80 | 2028 | High temperature gas reactor | TRISO | Grid-scale power and industrial heat |
| NuScale Power | NuScale Power Module | 77 | 2029-2030 | Pressurized water reactor | LEU | Grid-scale power |
| Oklo | Aurora | 15-50 | 2027 | Gas fast reactor | HALEU | Microgrids, remote power |
| Aalo Atomics | Aalo-1 | 10 | 2026 | Sodium fast reactor | HALEU | Various |
| HolosGen | Holos Quad | 3-13 | 2027 | Gas fast reactor | TRISO | Distributed power |
| Blykalla | SEALER (Swedish Advanced Lead Reactor) | 3-10 | 2030 | Lead fast reactor | LEU | Remote power |
| Ultra Safe Nuclear Corporation | Micro Modular Reactor (MMR) | 5 | 2026 | High temperature gas reactor | TRISO | Remote power and heat |
| Westinghouse | eVinci | 5 | 2027 | Specialized microreactor type | TRISO | Remote power, defense |
| BWXT | BANR (Banana River) | 1-5 | 2025 | High temperature gas reactor | TRISO | Defense |
| Radiant Nuclear | Kaleidos | 1.2 | 2028 | High temperature gas reactor | TRISO | Portable power, remote locations, defense |
| Antares | Antares R1 | 1.5 | 2027 | Specialized microreactor type | TRISO | Defense, austere and remote locations |


## 4. Nuclear Reactor Size Comparison (MWe)

This provides a general overview of reactor sizes, from large-scale power plants to microreactors.

| Category | Size Range (MWe) | Example Reactors |
|----------|------------------|------------------|
| **Micro (Portable) Reactors** | <10 MWe | Westinghouse eVinci (5), HolosGen (3-13), Blykalla SEALER (3-10), Ultra Safe Nuclear MMR (5), BWXT BANR (1-5), Radiant Kaleidos (1.2), Antares R1 (1.5) |
| **Small Modular Reactors** | 10-100 MWe | Aalo Atomics Aalo-1 (10), Oklo Aurora (15-50), NuScale Power Module (77), X-energy Xe-100 (80), ARC Clean Energy ARC-100 (100), Seaborg Technologies CMSR (100) |
| **Large Custom** | >100 MWe | Kairos Power KP-FHR (140), Terrestrial Energy IMSR (195), General Atomics EM2 (265), Moltex Energy SSR-W (300), TerraPower Natrium (345), ThorCon (500) |

![Nuclear Reactors](https://raw.githubusercontent.com/matejkajinic/nuclear-energy/HEAD/nuclear-reactors.svg)
