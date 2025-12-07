# Insurance Risk Analytics & Predictive Modeling

## Project Overview
Analysis of historical insurance claim data to identify low-risk customer segments and optimize premium pricing for AlphaCare Insurance Solutions.

## Project Status
- **Interim Submission:** ✅ Complete (Tasks 1 & 2)
- **Final Submission:** 🚧 In Progress (Tasks 3 & 4)

## Key Findings (Interim)
- Overall portfolio loss ratio: **104.8%** (unprofitable)
- Riskiest province: **Gauteng** (122.2% loss ratio)
- Safest province: **Northern Cape** (28.3% loss ratio)
- Highest risk vehicle type: **Heavy Commercial** (162.8% loss ratio)

## Repository Structure
insurance-risk-week3/
├── data/ # Data files (tracked via DVC)

├── notebooks/ # Jupyter notebooks for analysis

├── reports/ # Visualizations and reports

├── scripts/ # Python utility scripts

└── .github/workflows/ # CI/CD pipeline


## Setup & Installation
```bash
# Clone repository
git clone https://github.com/HermonaDev/insurance-risk-week3.git
cd insurance-risk-week3

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Pull data via DVC
dvc pull
