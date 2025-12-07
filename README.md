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

## Data Pipeline
1. Raw TXT → CSV: `python scripts/convert_data.py`
2. Analysis: `notebooks/01_eda.ipynb`
3. Data versioning: `dvc pull` to get data, `dvc push` to update
"\n## Development Workflow" 
"- Create feature branch for each task" 
"- Open Pull Request on GitHub before merging" 
"- Use descriptive PR titles and descriptions" 

## Contributing

1. Create a feature branch: `git checkout -b feature/description`
2. Make your changes and commit: `git commit -m "feat: add new analysis"`
3. Push to GitHub: `git push origin feature/description`
4. Open a Pull Request with:
   - Clear title describing the change
   - Description of what was changed and why
   - Reference to any related issues
5. Request review from team members
6. Merge after approval

## Project Structure
- `data/`: Raw and processed data (tracked via DVC)
- `notebooks/`: Exploratory analysis and prototyping
- `src/`: Reusable Python modules
- `reports/`: Generated visualizations and reports
- `scripts/`: One-off data processing scripts