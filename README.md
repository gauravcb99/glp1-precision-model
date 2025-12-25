# Optimizing Therapeutic Index: A GLP-1 Cost-Consequence Model

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-Public-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> **A Monte Carlo simulation analyzing the economic and clinical impact of "Precision Maintenance" protocols in GLP-1 weight loss therapies.**

---

## Table of Contents
- [Executive Summary](#-executive-summary)
- [The Problem: The Titration Cliff](#-the-problem-the-titration-cliff)
- [Key Findings](#-key-findings)
- [Visualizations](#-visualizations)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)

---

## Executive Summary

High-cost GLP-1 agonists (e.g., *Semaglutide*, *Tirzepatide*) face a significant challenge in real-world payer settings: **Early Discontinuation**.

Using a Python-based **Monte Carlo simulation (N=2,000)** anchored on real-world claims distributions, this project models a "Precision Maintenance" protocol. The analysis demonstrates that lower-dose maintenance combined with digital behavioral support increases persistence, **doubling clinically meaningful weight loss outcomes (12.7% vs 7.7%)** while optimizing the cost-per-outcome.

---

## The Problem: The Titration Cliff

Current "Treat-to-Target" protocols prioritize rapid titration to maximum tolerated doses (e.g., 2.4 mg). However, clinical observation suggests:

1.  **Intolerance:** A significant portion of patients discontinue therapy at Month 3 due to GI intolerance during dose escalation.
2.  **Sunk Costs:** Payers incur maximum costs during the titration phase (Months 1-3) with **zero therapeutic ROI** if the patient churns early.
3.  **The Solution:** Shifting from *Dose Maximization* to *Adherence Maximization*.

---

## Key Findings

| Metric | Standard of Care (High Dose) | Precision Maintenance (Low Dose + Digital) | Impact |
| :--- | :--- | :--- | :--- |
| **Avg. Weight Loss** | 7.7% | **12.7%** | 🔼 **65% Improvement** |
| **Churn Rate (Month 3)** | ~40% (High Risk) | <15% (Stabilized) | 🔽 **Reduced Wastage** |
| **Cost Efficiency** | Low ROI | High ROI | **Optimized Spend** |

> **Insight:** Regression analysis confirmed a strong correlation ($R^2 \approx 0.8$) between **Digital Engagement Scores** and sustained weight loss, validating software as a therapeutic lever.

---

## Visualizations

The interactive dashboard for this project is hosted on **Tableau Public**. It features:
* **The Efficiency Paradox:** Comparing Cost vs. Outcome.
* **The Cliff:** Visualizing the drop-off points in patient retention.
* **Digital Biomarker:** Scatter plot analysis of Engagement vs. Weight Loss.

[![View Dashboard](https://img.shields.io/badge/View_Dashboard-Click_Here-E97627?style=for-the-badge)](https://public.tableau.com/app/profile/gaurav.bhatti/viz/GLP-1ValueOptimizationModel-2025/Dashboard1)

---

## Repository Structure

```text
├── data/
│   └── glp1_simulation_results.csv  # Synthetic dataset (N=2000)
├── scripts/
│   └── simulation_engine.py         # Main Monte Carlo simulation logic
├── images/
│   └── dashboard_screenshot.png     # (Optional) Preview image
├── .gitignore                       # System files to ignore
├── requirements.txt                 # Dependencies
└── README.md                        # Project documentation

