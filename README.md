# medicaid-moud-access

Analysis of medications for opioid use disorder (MOUD) utilization in fee-for-service Medicaid across all 50 states and DC, 2019–2025. Examines the gap in MOUD access between Medicaid expansion and non-expansion states using publicly available CMS prescribing data.

---

## Overview

**Primary outcome:** MOUD share — MOUD prescriptions as a proportion of all opioid prescriptions (MOUD + pain opioid) in fee-for-service Medicaid.

**Study period:** 2019–2025 (7 years)

**Coverage:** All 51 U.S. jurisdictions (50 states + DC), N = 348 state-years

**Key finding:** Expansion states allocated 40.6% of opioid prescriptions to MOUD vs. 17.2% in non-expansion states (2.36× ratio, p < .0001). The gap has persisted across all seven study years.

---

## Data Sources

All data are publicly available. No individual-level or proprietary data are used.

| Dataset | Source | URL |
|---|---|---|
| Medicaid State Drug Utilization Data (SDUD) | CMS | https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/index.html |
| Medicaid Enrollment Data | CMS | https://www.medicaid.gov/medicaid/program-information/medicaid-and-chip-enrollment-data/report-highlights/index.html |
| Medicaid Expansion Status | KFF | https://www.kff.org/medicaid/issue-brief/status-of-state-medicaid-expansion-decisions-interactive-map/ |
| Drug Overdose Mortality | CDC WONDER | https://wonder.cdc.gov/ucd-icd10-expanded.html |
| ACS Demographic Data (DP05, S1701) | U.S. Census Bureau | https://data.census.gov/ |
| RAND OPTIC Policy Data | RAND Corporation | https://www.rand.org/health-care/projects/optic.html |

**SDUD filter applied:** Utilization Type = `FFSU` (fee-for-service, non-managed care), State ≠ `XX` (national aggregate excluded).

---

## Repository Structure

```
medicaid-moud-access/
├── 01_medicaid_opioid_analysis.ipynb   # Main analysis notebook
├── README.md
└── Data/                               # Not included — see Data Sources above
    ├── utilization_2019–2025/
    ├── enrollment_2019–2025/
    ├── medicaid_expansion.csv
    ├── ACS/
    └── cdc_drug_overdose_county_2018_2024.csv
```

---

## Methods Summary

**Drug classification** applied to `Product Name` field via keyword matching:
- **MOUD:** methadone, buprenorphine, naltrexone, Suboxone, Subutex, Zubsolv, Bunavail, Sublocade, Brixiv
- **Pain opioids:** oxycodone, hydrocodone, morphine, fentanyl, codeine, tramadol, hydromorphone, oxymorphone, tapentadol, meperidine

**Expansion coding:** Time-varying. Missouri and Oklahoma coded as expansion = 0 for 2021 (pre-implementation), expansion = 1 from 2022. North Carolina and South Dakota coded as expansion = 0 throughout (insufficient exposure within study period).

**Statistical analyses:**
- Mann-Whitney U (non-parametric, state-level distributions)
- State fixed-effects OLS (within-state change)
- Multivariate OLS with ACS demographic controls (pct_black, pct_hispanic, pct_poverty)
- Multivariate OLS with RAND OPTIC policy controls
- Jackknife leave-one-out (49 iterations, one state dropped per run)
- Spearman correlations (racial equity, within expansion/non-expansion subgroups)
- Difference-in-differences with parallel trends test (drug overdose mortality, 2018–2023 pre/post)

---

## Key Results

| Analysis | Coefficient / Statistic | p-value |
|---|---|---|
| Mann-Whitney (moud_share, pooled) | Exp 40.6% vs Non-exp 17.2%, ratio 2.36× | < .0001 |
| Jackknife LOO (49 iterations) | coef range 0.166–0.218 | all < .05 |
| ACS demographic controls OLS | coef = 0.211 | .0002 |
| RAND OPTIC policy controls OLS | coef = 0.185 | .002 |
| State fixed-effects OLS | coef = 0.212 | .119 (expected null) |
| Parallel trends (2018–2020) | β = 0.285 | .851 |
| Black population × MOUD share (within expansion) | r = −0.274 | .004 |
| Hispanic population × MOUD share (within non-expansion) | r = −0.471 | .003 |

**Oklahoma natural experiment:** Expanded Medicaid July 2021. MOUD share rose from 5.5% to 72.9% in the first expansion year (13-fold increase).

**Wisconsin:** Highest MOUD share among non-expansion states (35–53%) via BadgerCare 1115 SUD waiver (started February 2021).

**Texas:** Near-zero MOUD share throughout (0.0% in 2023, 1.2% in 2025).

The state fixed-effects null result (p = .119) is expected and reported transparently: state FE absorbs all between-state variation, leaving only within-state year-to-year change to identify the effect over a 7-year panel. The primary finding is the cross-sectional gap confirmed by Mann-Whitney, jackknife, and multivariate controls.

---

## Drug Class Results

| Drug | Expansion share | Non-expansion share | Ratio | p |
|---|---|---|---|---|
| Buprenorphine | 27.6% | 12.7% | 2.2× | < .0001 |
| Naltrexone | 7.1% | 4.1% | 1.7× | < .0001 |
| Methadone | 6.8% | 1.0% | 6.9× | n.s. (underpowered) |

Absolute MOUD per 1,000 enrollees is not significantly different between groups (p = .071). The significant finding is in the proportional share metric, not absolute volume.

---

## Limitations

- CMS SDUD captures fee-for-service only; managed care organization (MCO) MOUD prescriptions are not reflected
- State-level ecological analysis; no individual-level data
- Methadone in FFS is underrepresented in several states due to MCO carve-outs (e.g., MA, NY)
- CDC overdose mortality analysis is underpowered over a 3-year window; null OD result is consistent with the literature (Auty et al., 2022)
- Racial/ethnic disparity findings are ecological correlations only; individual-level MOUD utilization by race is not available in public FFS files

---

## Requirements

```
python >= 3.9
pandas
numpy
scipy
statsmodels
matplotlib
seaborn
jupyter
```

---

## Author

Mohit Singhal
ORCID: [0009-0009-1518-4598](https://orcid.org/0009-0009-1518-4598)
