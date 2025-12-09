# Transforming Insurance Pricing with Data Science: A Case Study for AlphaCare Insurance Solutions

## Executive Summary

AlphaCare Insurance Solutions (ACIS) faced a critical challenge: a 104.8% loss ratio meaning they paid out more in claims than they collected in premiums. Through comprehensive data analysis and machine learning, we identified actionable insights that can transform their profitability.

**Key Finding:** Geographic risk concentration in Gauteng (122% loss ratio) versus profitable opportunities in Northern Cape (28% loss ratio).

**Solution:** A risk-based pricing framework that adjusts premiums by -10% to +34% based on individual policy risk scores.

**Expected Impact:** R9.6M annual savings, moving from loss-making to profitable within 6 months.

## 1. The Problem: Why ACIS Was Losing Money

Our analysis of 1M+ policy records (Feb 2014-Aug 2015) revealed:

- **Overall Loss Ratio:** 104.8% (R4.6M loss over 18 months)
- **Risk Concentration:** Gauteng represented 39% of portfolio but 122% loss ratio
- **Extreme Claims:** 1% of policies caused 28% of total claim value
- **Data Gaps:** 95% of gender data missing, limiting segmentation capability

## 2. Analytical Approach: Four-Pillar Methodology

### Pillar 1: Exploratory Data Analysis
- **Process:** Comprehensive analysis of 52 features across 1M policies
- **Insight:** 4.3x risk difference between provinces, 2.5x between zip codes
- **Visualization:** 7 key charts identifying risk patterns and outliers

### Pillar 2: Statistical Hypothesis Testing
- **Test 1:** Province risk differences → **REJECT NULL** (1.9x risk difference)
- **Test 2:** Zip code risk differences → **REJECT NULL** (2.5x risk difference)  
- **Test 3:** Zip code margin differences → **REJECT NULL** (R6,195 per policy difference)
- **Test 4:** Gender risk differences → **CANNOT REJECT** (95% data missing)

### Pillar 3: Predictive Modeling
- **Claim Severity Model:** 58.3% accuracy predicting claim tiers (Small/Medium/Large/Very Large)
- **SHAP Analysis:** SumInsured, Current Premium, and Postal Code are top risk drivers
- **Risk Scoring:** All 1M policies scored 0-100 based on expected claim amount

### Pillar 4: Pricing Optimization
- **Framework:** Premium = Current Premium × Risk Adjustment (0.87x to 1.34x)
- **Segmentation:** Quartile-based risk grouping with targeted pricing
- **Implementation:** Conservative approach (top 10% +20%, bottom 10% -10%)

## 3. Key Business Insights

### Geographic Risk Patterns
Province Loss Ratio Business Implication
Gauteng 122.2% Urgent premium increase needed (+15-20%)
Northern Cape 28.3% Competitive advantage opportunity (-10%)
KwaZulu-Natal 108.3% Moderate adjustment required (+5-10%)

text

### Extreme Value Impact
- **1% of policies** cause **28% of claims**
- **Top 5% of claims** represent **62% of total claim value**
- **Recommendation:** Reinsurance for claims > R500,000

### Data Quality Issues
- **Gender:** 95% missing → Cannot implement gender-based pricing
- **SumInsured:** Appears mis-scaled → Affects premium calculation accuracy
- **Recommendation:** Data quality improvement as priority initiative

## 4. Implementation Roadmap

### Immediate Actions (Week 1)
1. **Province-Based Pricing:** +15% Gauteng, -10% Northern Cape
2. **Unprofitable Zip Code Review:** 122, 2000, 1863 (causing R4.2M loss)
3. **Data Collection Fix:** Mandate gender field completion

### Short-Term Initiatives (Month 1)
1. **Claim Tier Prediction Deployment:** For claims reserving accuracy
2. **Conservative Risk Pricing:** Top 10% +20%, Bottom 10% -10%
3. **Underwriting Rules:** Based on SHAP-identified risk drivers

### Medium-Term Strategy (Quarter 1)
1. **Full Risk-Based Pricing:** All new business
2. **Portfolio Rebalancing:** Reduce Gauteng exposure, grow Northern Cape
3. **Telematics Pilot:** Advanced risk assessment

### Long-Term Vision (Year 1)
1. **Dynamic Pricing Platform:** Real-time risk assessment
2. **Market Expansion:** Profitable provinces and segments
3. **AI Fraud Detection:** Reduce fraudulent claims

## 5. Expected Business Impact

| Metric | Current State | Target | Annual Impact |
|--------|---------------|--------|---------------|
| Loss Ratio | 104.8% | 95% | R9.6M saving |
| Portfolio Profitability | Negative | Positive | R4-5M net profit |
| Risk-Based Pricing | 0% | 100% new business | Better risk selection |
| Claim Prediction | N/A | 58% tier accuracy | Improved reserving |

## 6. Technical Implementation Details

### Data Pipeline
- **Version Control:** DVC for reproducible data pipelines
- **Processing:** Automated EDA, hypothesis testing, and modeling notebooks
- **Quality:** Error handling, logging, and validation throughout

### Model Stack
- **Statistical Testing:** SciPy for hypothesis validation
- **Machine Learning:** XGBoost for claim severity prediction
- **Interpretability:** SHAP for model transparency
- **Evaluation:** RMSE, MAE, R², and business metrics

### Repository Structure
insurance-risk-week3/
├── data/ # Versioned via DVC
├── notebooks/ # EDA, hypothesis testing, modeling
├── reports/ # Visualizations and findings
├── scripts/ # Automated pipelines
└── README.md # Comprehensive documentation


## 7. Limitations and Future Work

### Current Limitations
1. **Claim Data Sparsity:** Only 0.28% of policies have claims
2. **Data Quality:** Gender and SumInsured issues
3. **Temporal Scope:** 18-month period may not capture seasonality

### Future Enhancements
1. **More Claim Data:** Improve model accuracy with additional years
2. **External Data:** Weather, traffic, economic indicators
3. **Real-Time Features:** Telematics, driving behavior
4. **Advanced Models:** Deep learning for complex pattern detection

## 8. Conclusion

AlphaCare Insurance Solutions stands at a crossroads. The current pricing strategy leads to consistent losses, but data science provides a clear path to profitability. By implementing risk-based pricing, focusing on profitable segments, and improving data quality, ACIS can transform from a loss-making portfolio to a profitable, data-driven insurer.

The tools, models, and insights are ready. The question is no longer "Can we improve profitability?" but "How quickly can we implement these changes?"

**GitHub Repository:** https://github.com/HermonaDev/insurance-risk-week3  
**Analysis Period:** February 2014 - August 2015  
**Policies Analyzed:** 1,000,098  
**Key Recommendation:** Implement province-based pricing immediately, followed by full risk-based pricing within 3 months.

---

*This analysis demonstrates the power of data science in transforming traditional insurance operations. The combination of statistical rigor, machine learning, and business acumen creates a compelling case for data-driven decision making in the insurance industry.*