# FreshScan AI

## Product Requirements Document (PRD)

**Version:** 1.0
**Project:** FreshScan AI
**Challenge:** Zepto Nova Food Safety Innovation Challenge
**Author:** Ajay Armugam

---

# 1. Vision

FreshScan AI is an AI-powered produce quality intelligence platform designed for quick-commerce warehouses, dark stores, and mother hubs. The platform automates freshness inspection, defect detection, and shelf-life prediction using computer vision, machine learning, and cloud technologies. It helps retailers reduce food wastage, improve food safety, optimize inventory, and maintain consistent product quality.

---

# 2. Problem Statement

Fresh produce quality inspection in warehouses is largely manual, subjective, and time-consuming. Human inspectors may overlook subtle defects, resulting in inconsistent grading, food waste, customer dissatisfaction, and financial losses. Existing systems also lack intelligent shelf-life prediction, making inventory management inefficient and reactive rather than proactive.

---

# 3. Objectives

* Detect freshness using AI-powered computer vision.
* Detect defects such as bruises, mold, cracks, discoloration, shriveling, and contamination.
* Classify produce into Fresh, Marginal, or Reject categories.
* Predict the remaining shelf life of produce.
* Generate warehouse quality analytics and inventory insights.
* Reduce food waste and improve food safety compliance.
* Build a scalable cloud-native platform suitable for quick-commerce operations.

---

# 4. Target Users

### Primary Users

* Warehouse Quality Inspectors
* Warehouse Managers
* Inventory Managers

### Secondary Users

* Retail Operations Team
* Supply Chain Managers
* Food Safety Auditors
* Procurement Teams

---

# 5. Functional Requirements

## User Management

* Secure login
* Role-based access
* User profile management

### Roles

* Admin
* Warehouse Manager
* Quality Inspector

---

## Produce Inspection

* Upload produce images
* Batch image upload
* Camera integration (Future)
* Store inspection history

---

## Freshness Classification

Classify produce into

* Fresh
* Marginal
* Reject

Display

* Confidence score
* Prediction timestamp

---

## Defect Detection

Detect

* Bruising
* Mold
* Cracks
* Shriveling
* Discoloration
* Surface contamination

Display

* Bounding boxes
* Confidence score
* Defect count

---

## Shelf-Life Prediction

Predict

* Remaining shelf life
* Shelf-life confidence

Provide recommendations

* Sell
* Prioritize Dispatch
* Discount
* Reject

---

## Inventory Analytics

Dashboard should display

* Total Inspections
* Fresh Inventory %
* Marginal Inventory %
* Reject Inventory %
* Daily Waste Prediction
* Weekly Waste Trend
* Shelf-Life Distribution
* Supplier Quality Score

---

## Reports

Generate

* Inspection Report
* Inventory Report
* Quality Report

Export

* PDF
* CSV

---

## Notifications

Notify warehouse managers when

* Shelf life is below threshold
* Reject percentage exceeds limit
* High spoilage is detected
* Batch quality deteriorates

---

# 6. Non-Functional Requirements

## Performance

* Prediction time under 3 seconds
* Support concurrent requests

---

## Scalability

* Support multiple warehouses
* Handle thousands of inspections daily

---

## Availability

* 99% uptime
* Automatic restart on failures

---

## Security

* Authentication
* Authorization
* Encrypted APIs (HTTPS)
* Secure cloud storage

---

## Maintainability

* Modular architecture
* Dockerized services
* CI/CD pipeline
* Automated testing

---

## Portability

Deployable on

* Google Cloud Platform
* Amazon Web Services

---

# 7. Scope

## In Scope (MVP)

* Freshness Classification
* Defect Detection
* Shelf-Life Prediction
* FastAPI Backend
* PostgreSQL Database
* Streamlit Dashboard
* Docker
* CI/CD
* Cloud Deployment
* Image Upload
* Reports

---

## Out of Scope (Future)

* IoT Sensor Integration
* CCTV Live Camera Integration
* Mobile Application
* Multi-language Support
* Edge AI Deployment
* ERP Integration
* Barcode Scanner

---

# 8. Success Metrics

The MVP will be considered successful if it achieves

* Freshness Classification Accuracy > 90%
* Defect Detection mAP > 80%
* API Response Time < 3 seconds
* Dashboard Response < 2 seconds
* Successful Cloud Deployment
* End-to-End Automated Pipeline
* Dockerized Application
* Functional CI/CD Pipeline

---

# 9. MVP Features

The MVP will include

* Image Upload
* Freshness Classification
* Defect Detection
* Shelf-Life Estimation
* PostgreSQL Storage
* Inspection History
* Warehouse Dashboard
* PDF Report Generation
* Docker Deployment
* GitHub Actions CI/CD

---

# 10. Future Enhancements

* AI-based Produce Counting
* Live Camera Monitoring
* Automatic Batch Quality Tracking
* Supplier Performance Ranking
* IoT Temperature Integration
* Humidity Monitoring
* Predictive Waste Analytics
* Dynamic Discount Recommendation
* AI Chat Assistant for Warehouse Managers
* ERP & WMS Integration
* Edge Deployment using NVIDIA Jetson
* Vertex AI Integration
* Real-time Warehouse Alerts

---

# 11. Technology Stack

| Layer                    | Technology                      |
| ------------------------ | ------------------------------- |
| Programming Language     | Python                          |
| Backend                  | FastAPI                         |
| Frontend                 | Streamlit (MVP), React (Future) |
| Database                 | PostgreSQL                      |
| Computer Vision          | OpenCV                          |
| Freshness Classification | EfficientNet-B0                 |
| Defect Detection         | YOLOv8                          |
| Shelf-Life Prediction    | Rule Engine + Regression Model  |
| ETL                      | Apache Airflow                  |
| Experiment Tracking      | MLflow                          |
| Dataset Versioning       | DVC                             |
| Testing                  | Pytest                          |
| Containerization         | Docker                          |
| CI/CD                    | GitHub Actions                  |
| Cloud Storage            | Google Cloud Storage            |
| Deployment               | Google Cloud Run                |
| Monitoring               | Prometheus + Grafana (Future)   |

---

# 12. Risks

* Limited shelf-life datasets
* Produce appearance varies by lighting
* Seasonal variations affect model accuracy
* Need for data augmentation
* Limited labeled defect datasets
* Cloud deployment costs

---

# 13. Deliverables

* Literature Survey
* System Architecture
* ETL Pipeline
* Freshness Classification Model
* Defect Detection Model
* Shelf-Life Prediction Module
* Backend APIs
* PostgreSQL Database
* Analytics Dashboard
* Dockerized Application
* GitHub CI/CD Pipeline
* Cloud Deployment on GCP
* Technical Documentation
* Demo Video
* Pitch Deck
