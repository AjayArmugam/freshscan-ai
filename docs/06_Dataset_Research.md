# FreshScan AI

# Dataset Research & Selection

Version: 1.0

Project: FreshScan AI

---

# Objective

The objective of this document is to identify, compare, and select the most suitable datasets for training the AI models used in FreshScan AI. Since the project consists of multiple machine learning tasks, no single dataset satisfies all requirements. Therefore, multiple datasets will be combined to create a comprehensive training pipeline.

---

# Machine Learning Tasks

FreshScan AI consists of three major AI tasks:

1. Freshness Classification
2. Defect Detection
3. Shelf-Life Prediction

---

# Dataset Selection Criteria

Each dataset will be evaluated based on:

* Image Quality
* Number of Images
* Annotation Quality
* Number of Classes
* License
* Dataset Diversity
* Suitability for Real Warehouse Scenarios
* Ease of Integration

---

# Dataset Evaluation Template

For every dataset, record the following information:

## Dataset Name

## Source

(Kaggle / Roboflow / Hugging Face / Research Paper)

## Purpose

Classification / Detection / Shelf-Life

## Number of Images

## Classes

## Annotation Type

* Image Classification
* Bounding Boxes
* Segmentation
* Metadata

## Advantages

*

## Limitations

*

## Final Decision

* Selected
* Rejected

## Notes

---

# Final Dataset Strategy

The final FreshScan AI dataset will combine multiple public datasets to support:

* Freshness Classification
* Produce Defect Detection
* Shelf-Life Estimation

This approach provides better diversity, improves model generalization, and more closely reflects real-world warehouse conditions than relying on a single dataset.
