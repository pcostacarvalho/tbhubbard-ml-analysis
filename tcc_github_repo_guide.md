# Guide: Building a GitHub Portfolio Repo from a TCC/Thesis PDF

This guide instructs an LLM to read a TCC (thesis) PDF and scaffold a clean, recruiter-ready GitHub repository from it.

---

## Step 1 — Read the TCC PDF and Extract the Following

Ask the LLM to extract:

1. **Title** — exact title of the work
2. **Problem statement** — what question is being answered and why it matters
3. **Dataset** — name, source, size, key variables
4. **Methodology** — list of models/techniques used, in order applied
5. **Evaluation metrics** — how models were assessed (e.g. R², RMSE, MAE, F1)
6. **Key results** — best model, main finding, most important number
7. **Conclusion** — one or two sentences summarizing the takeaway

Use this prompt:

```
Read the attached PDF. Extract the following in plain text:
1. Title
2. Problem statement (1-2 sentences)
3. Dataset: name, source, number of samples, key features
4. Methodology: list all models and techniques used, in the order they appear
5. Evaluation metrics used
6. Key results: best model and its performance
7. Conclusion (1-2 sentences)
Do not interpret or add anything not in the document.
```

---

## Step 2 — Repository Structure

Once extracted, scaffold the following structure:

```
<repo-name>/
│
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modeling.ipynb        # one notebook per method if multiple
│   └── 04_results_evaluation.ipynb
│
├── data/
│   └── README.md                # link to original data source only — do not host data
│
└── reports/
    └── figures/                 # saved plots from notebooks
```

**Repo name format:** `<topic>-ml-analysis` — lowercase, hyphenated, no acronyms if avoidable.

---

## Step 3 — README.md Content

The README must be written for a technical recruiter, not a domain specialist. Use this structure:

```markdown
# <Title>

<One sentence: what this project does, in plain language — no jargon>

## Problem
<2-3 sentences: what is being predicted, why it matters, what data is used>

## Methods
- <Method 1>
- <Method 2>
- ...

## Results
| Model | <Metric 1> | <Metric 2> |
|-------|-----------|-----------|
| ...   | ...       | ...       |

Best model: **<model name>** with <metric> = <value>

## Dataset
<Name> — <source with link if public>  
<Number of samples>, <number of features>, <target variable>

## How to Reproduce
```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

## Stack
Python | pandas | scikit-learn | <add others from thesis>
```

---

## Step 4 — Notebook Structure

Each notebook must follow this internal structure:

### `01_data_exploration.ipynb`
- Load dataset
- Display shape, dtypes, sample rows
- Distribution plots for key variables
- Missing value summary
- Correlation heatmap

### `02_preprocessing.ipynb`
- Handle missing values
- Feature engineering (if any — extract from thesis)
- Train/test split
- Scaling/encoding (if applicable)
- Save processed data or pass to next notebook

### `03_modeling.ipynb` (one per model family if thesis compares several)
- Load preprocessed data
- Define model with hyperparameters stated in thesis
- Train
- Predict on test set
- Save model outputs

### `04_results_evaluation.ipynb`
- Load all model outputs
- Compute and compare evaluation metrics
- Plot: predicted vs actual, residuals, feature importance (if applicable)
- Print summary table matching thesis results

**Each notebook must start with a markdown cell:**
```markdown
## <Notebook Title>
**Purpose:** <one sentence>  
**Inputs:** <what it reads>  
**Outputs:** <what it produces>
```

---

## Step 5 — requirements.txt

Ask the LLM to infer the required libraries from the methodology extracted in Step 1. Minimum:

```
pandas
numpy
scikit-learn
matplotlib
seaborn
jupyter
```

Add others based on methods found (e.g. `xgboost`, `statsmodels`, `scipy`).

---

## Step 6 — Final Check Before Publishing

- [ ] README uses plain language — no domain jargon in the first paragraph
- [ ] Results table matches thesis numbers exactly
- [ ] Data folder contains only a README with source link — no raw files uploaded
- [ ] Notebooks run top to bottom without errors (or clearly marked as WIP)
- [ ] Repo is public
- [ ] Repo link is added to GitHub profile README and CV

---

## Notes

- Do not fabricate results. All numbers in the README must come from the thesis.
- If the dataset is not publicly available, note that in `data/README.md` and omit the download instructions.
- Keep notebook code clean: one concept per cell, markdown headers between sections.
- This repo is a portfolio piece — prioritize clarity over complexity.
