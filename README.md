# ✈️ Flight Delay Risk — ML to Cloud

A project that predicts U.S. flight delays using Python + AWS SageMaker.  
Built for scalability, security, and easy maintenance.

## Why this project
- Predict delays → better schedules & happier customers.
- Full ML flow: data → features → model → deploy.
- Recruiter-friendly: cloud-native + secure.

## Architecture
```mermaid
flowchart LR
  A[Raw Data] --> B[Preprocess]
  B --> C[Train]
  C --> D[Evaluate]
  D --> E[Artifacts]
  E --> F{Deploy}
  F --> G[Batch Inference]
  F --> H[SageMaker Endpoint]

