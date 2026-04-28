# Data provenance

The data used in this project, the file `tbhubbard_database.csv`, was build upon two sources: the **QMOF** and **TBHubbard** databases. 

## How the data are combined

The analysis uses a **single tabular file** (`tbhubbard_database.csv`) that aligns each MOF structure with **pair-level** Hubbard interactions. In that file:

- **Structural (global) descriptors** come from the **QMOF** database: pore and cavity metrics and crystal-level mass properties used in this project are `pld`, `lcd`, `density`, and `volume`.
- **All other fields used for modeling** (Hubbard targets, inter-site geometry, site identities, and local electronic descriptors such as DDEC charges) come from the **TBHubbard** dataset and its documented linkage to QMOF entries.

If you cite this work, separate the two sources as below.

## QMOF (structural descriptors)

QMOF is a curated database of computed properties for metal–organic frameworks (MOFs), including structural and electronic descriptors used in high-throughput workflows.

**Relevant variables in this project (structural / global):** `pld`, `lcd`, `density`, `volume`.

**References**

1. Rosen, A. S.; Iyer, S. M.; Ray, D.; Yao, Z.; Aspuru-Guzik, A.; Gagliardi, L.; Notestein, J. M.; Snurr, R. Q. Machine learning the quantum-chemical properties of metal–organic frameworks for accelerated materials discovery. *Matter* **2021**, *4* (5), 1578–1597. [https://doi.org/10.1016/j.matt.2021.02.015](https://doi.org/10.1016/j.matt.2021.02.015)

2. Rosen, A. S.; Fung, V.; Huck, P.; O’Donnell, C. T.; Horton, M. K.; Truhlar, D. G.; Persson, K. A.; Notestein, J. M.; Snurr, R. Q. High-throughput predictions of metal–organic framework electronic properties: theoretical challenges, graph neural networks, and data exploration. *npj Computational Materials* **2022**, *8*, 112. [https://doi.org/10.1038/s41524-022-00796-6](https://doi.org/10.1038/s41524-022-00796-6)

## TBHubbard (targets and non-structural descriptors)

TBHubbard provides **tight-binding and extended Hubbard (DFT+U+V) parameters** for MOFs, including on-site `U`, inter-site `V`, **interatomic distances**, **chemical identity** of interacting sites, and **local charge** descriptors as distributed in the official release. These are not the same as the QMOF global structural columns above.

**Relevant variables in this project (from TBHubbard):** `U`, `V`, `distance`, `atom_i`, `atom_j`, `ddec_charge_i`, `ddec_charge_j`, and identifiers used for grouping (e.g. `qmof_id`) as provided in the dataset.

**References**

3. Costa Carvalho, P.; Zipoli, F.; Duriez, A. C.; Barroca, M. A.; Neumann Barros Ferreira, R.; Jones, B.; Wunsch, B.; Steiner, M. TBHubbard: tight-binding and extended Hubbard model dataset for metal-organic frameworks. *Sci. Data* **2025**, *12*, 1776. [https://doi.org/10.1038/s41597-025-06054-w](https://doi.org/10.1038/s41597-025-06054-w)

4. Costa Carvalho, P.; Zipoli, F. TBHubbard Dataset. Harvard Dataverse, **2025**. [https://doi.org/10.7910/DVN/ZKLRLF](https://doi.org/10.7910/DVN/ZKLRLF)  
   Dataset landing page: [https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ZKLRLF](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ZKLRLF)

## Suggested bibliography snippet (BibTeX)

```bibtex
@article{rosen2021matter,
  title   = {Machine learning the quantum-chemical properties of metal--organic frameworks for accelerated materials discovery},
  author  = {Rosen, Alexander S. and others},
  journal = {Matter},
  year    = {2021},
  volume  = {4},
  number  = {5},
  pages   = {1578--1597},
  doi     = {10.1016/j.matt.2021.02.015}
}

@article{rosen2022npj,
  title   = {High-throughput predictions of metal--organic framework electronic properties: theoretical challenges, graph neural networks, and data exploration},
  author  = {Rosen, Alexander S. and others},
  journal = {npj Computational Materials},
  year    = {2022},
  volume  = {8},
  pages   = {112},
  doi     = {10.1038/s41524-022-00796-6}
}

@article{costacarvalho2025scidata,
  title   = {{TBHubbard}: tight-binding and extended {Hubbard} model dataset for metal-organic frameworks},
  author  = {Costa Carvalho, Pamela and Zipoli, Federico and others},
  journal = {Scientific Data},
  year    = {2025},
  volume  = {12},
  pages   = {1776},
  doi     = {10.1038/s41597-025-06054-w}
}

@misc{costacarvalho2025dataverse,
  title        = {{TBHubbard} Dataset},
  author       = {Costa Carvalho, Pamela and Zipoli, Federico},
  year         = {2025},
  publisher    = {Harvard Dataverse},
  doi          = {10.7910/DVN/ZKLRLF}
}
```
