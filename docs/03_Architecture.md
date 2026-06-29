# FreshScan AI

# System Architecture

Version: 1.0

Project: FreshScan AI

Author: Ajay Armugam

---

# 1. High-Level Architecture

FreshScan AI is a cloud-native AI platform designed to automate quality inspection and shelf-life prediction for fresh produce in warehouses. The platform follows a modular microservice-inspired architecture consisting of:

* Data Ingestion Layer
* ETL Pipeline
* AI Inference Layer
* Backend Services
* Database Layer
* Analytics Layer
* Cloud Infrastructure
* CI/CD Pipeline

---

# 2. System Components

## Data Sources

* Warehouse Cameras
* Mobile Phone Images
* Public Datasets
* Manual Uploads

---

## Data Ingestion

Responsible for collecting images.

Technologies:

* FastAPI
* Google Cloud Storage
* Local Storage (Development)

---

## ETL Pipeline

Responsible for

* Image validation
* Image preprocessing
* Metadata extraction
* Label validation
* Dataset versioning

Technologies

* Python
* Apache Airflow
* OpenCV
* Pandas
* DVC

---

## AI Layer

### Freshness Classification

Model

* EfficientNet-B0

Output

* Fresh
* Marginal
* Reject

---

### Defect Detection

Model

* YOLOv8

Detect

* Bruises
* Mold
* Cracks
* Shriveling
* Discoloration

---

### Shelf-Life Prediction

Inputs

* Freshness Score
* Defect Score
* Produce Type
* Temperature
* Humidity

Output

* Remaining Shelf Life

---

## Backend

Framework

* FastAPI

Responsibilities

* Authentication
* Image Upload
* AI Inference
* Report Generation
* Inventory Management
* Dashboard APIs

---

## Database

Primary Database

* PostgreSQL

Stores

* Users
* Produce
* Inspection Results
* Defects
* Shelf Life
* Inventory
* Reports

---

## Frontend

MVP

* Streamlit

Future

* React

Provides

* Dashboard
* Analytics
* Reports
* Inventory Monitoring

---

## Deployment

Containerization

* Docker

CI/CD

* GitHub Actions

Cloud

* Google Cloud Platform

Services

* Cloud Run
* Cloud Storage
* Artifact Registry
* Cloud SQL

---

# 3. Architecture Principles

* Modular Design
* Scalability
* High Availability
* Containerization
* Cloud Native
* Security First
* MLOps Ready
* Production Ready

# 4. Overall System Architecture

```text
                        +-------------------------+
                        |   Warehouse Camera      |
                        | Mobile Upload / Dataset |
                        +-----------+-------------+
                                    |
                                    v
                          +-------------------+
                          |  FastAPI Backend  |
                          +---------+---------+
                                    |
                +-------------------+-------------------+
                |                                       |
                v                                       v
      +---------------------+              +----------------------+
      |   Google Cloud      |              |   ETL Pipeline       |
      | Storage (Images)    |              | Airflow + OpenCV     |
      +----------+----------+              +----------+-----------+
                 |                                    |
                 |                                    |
                 +----------------+-------------------+
                                  |
                                  v
                    +-------------------------------+
                    | AI Inference Engine           |
                    |                               |
                    | EfficientNet                 |
                    | YOLOv8                       |
                    | Shelf-Life Prediction        |
                    +---------------+--------------+
                                    |
                                    v
                        +---------------------------+
                        | PostgreSQL Database       |
                        +---------------+-----------+
                                        |
                                        v
                           +--------------------------+
                           | Streamlit Dashboard      |
                           | Analytics & Reports      |
                           +---------------+----------+
                                           |
                                           v
                               Warehouse Managers
```

# 5. ETL Pipeline Architecture

## Purpose

The ETL pipeline automates the ingestion, validation, preprocessing, and storage of produce images before they are used for model training or inference.

---

## ETL Workflow

```text
                Image Upload
                     |
                     v
        +------------------------+
        |   Extract              |
        |------------------------|
        | Read Image             |
        | Read Metadata          |
        | Validate File          |
        +-----------+------------+
                    |
                    v
        +------------------------+
        |   Transform            |
        |------------------------|
        | Resize Images          |
        | Normalize              |
        | Remove Corrupted Data  |
        | Data Augmentation      |
        | Generate Metadata      |
        +-----------+------------+
                    |
                    v
        +------------------------+
        |      Load              |
        |------------------------|
        | Cloud Storage          |
        | PostgreSQL             |
        | Dataset Versioning     |
        +-----------+------------+
                    |
                    v
              ML Training Pipeline
```

---

## Technologies

- Apache Airflow
- Python
- OpenCV
- Pandas
- DVC
- Google Cloud Storage
- PostgreSQL

---

## Responsibilities

- Data Validation
- Image Cleaning
- Image Resizing
- Metadata Generation
- Dataset Versioning
- Dataset Statistics
- Data Quality Checks

# 6. Machine Learning Pipeline

## Overview

The ML pipeline processes produce images through multiple AI models to generate quality assessments and inventory insights.

---

## ML Workflow

```text
                Input Image
                     |
                     v
          +----------------------+
          | Image Preprocessing  |
          |----------------------|
          | Resize               |
          | Normalize            |
          | Background Cleanup   |
          +----------+-----------+
                     |
                     v
      +-------------------------------+
      | Freshness Classification       |
      | EfficientNet-B0                |
      +---------------+----------------+
                      |
      Fresh / Marginal / Reject
                      |
                      v
      +-------------------------------+
      | Defect Detection              |
      | YOLOv8                        |
      +---------------+---------------+
                      |
      Bruises | Mold | Cracks | Rot
                      |
                      v
      +-------------------------------+
      | Shelf-Life Prediction         |
      | Rule Engine + ML Model        |
      +---------------+---------------+
                      |
                      v
      Remaining Shelf Life (Days)
                      |
                      v
      Recommendation Engine
                      |
                      v
Sell | Prioritize | Discount | Reject
                      |
                      v
PostgreSQL + Dashboard
```

---

## Models

### Freshness Classification

Model:
- EfficientNet-B0

Output:
- Fresh
- Marginal
- Reject

---

### Defect Detection

Model:
- YOLOv8

Output:
- Bruises
- Mold
- Cracks
- Shriveling
- Discoloration

---

### Shelf-Life Prediction

Inputs:
- Freshness Score
- Defect Score
- Produce Type
- Storage Temperature
- Humidity

Output:
- Remaining Shelf Life (Days)

---

## Model Artifacts

The trained models will be versioned and stored for reproducible deployments.

# 7. Cloud Deployment Architecture

## Deployment Overview

FreshScan AI is designed as a cloud-native application deployed on Google Cloud Platform (GCP). The system follows a containerized architecture using Docker and automated deployments through GitHub Actions.

---

## Deployment Flow

```text
                    Developer
                        |
                        v
                 GitHub Repository
                        |
                        v
               GitHub Actions (CI/CD)
                        |
                        v
                 Docker Image Build
                        |
                        v
              Artifact Registry (GCP)
                        |
                        v
                Google Cloud Run
                        |
        +---------------+---------------+
        |                               |
        v                               v
Google Cloud Storage             Cloud SQL (PostgreSQL)
        |                               |
        +---------------+---------------+
                        |
                        v
                 Streamlit Dashboard
```

---

## Cloud Components

### Google Cloud Run

Hosts the FastAPI backend.

---

### Google Cloud Storage

Stores

- Uploaded Images
- Processed Images
- Reports
- Model Artifacts

---

### Cloud SQL

Stores

- Users
- Inventory
- Inspection Results
- Shelf-Life Predictions
- Reports

---

### Artifact Registry

Stores Docker images for deployment.

---

## CI/CD Pipeline

Developer Push

↓

GitHub Actions

↓

Run Tests

↓

Lint Code

↓

Build Docker Image

↓

Push Docker Image

↓

Deploy to Cloud Run

---

## Containerization

Containers

- Backend Service
- Database
- Airflow
- Dashboard

All services communicate through Docker Compose during development.