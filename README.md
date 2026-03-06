# FinCalc Pro — Indian Finance Calculator

A modern, full-stack finance calculator web app built with Flask + Vanilla JS.

## Project Structure

```
finapp/
├── app.py              # Flask backend — routes all 24 calculators
├── calculator.py       # Core calculation logic (unchanged)
├── requirements.txt    # Python dependencies
├── Procfile            # For deployment (Render / Railway / Heroku)
├── templates/
│   └── index.html      # Full frontend (single-page app)
└── static/
    └── style.css       # Stylesheet
```

## Run Locally

```bash
pip install -r requirements.txt
python app.py
# Open http://localhost:5000
```
To see the Financial calculator online follow this link 👇
Link:- https://web-production-98cf4.up.railway.app/

## Calculators Included

**Investments:** SIP, Lumpsum, Step-Up SIP, SWP, PPF, EPF, NPS, NSC, FD, RD  
**Planning:** Retirement, Inflation, CAGR  
**Loans:** EMI, Home Loan, Car Loan, Gold Loan, Education Loan, Flat vs Reducing  
**General:** Simple Interest, Compound Interest, GST, Gratuity, Salary, Brokerage
