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

## Deploy to Render (Free)

1. Push this folder to a GitHub repo
2. Go to https://render.com → New Web Service
3. Connect your repo
4. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Deploy ✓

## Deploy to Railway

```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

## Deploy to Heroku

```bash
heroku create fincalc-pro
git push heroku main
```

## Calculators Included

**Investments:** SIP, Lumpsum, Step-Up SIP, SWP, PPF, EPF, NPS, NSC, FD, RD  
**Planning:** Retirement, Inflation, CAGR  
**Loans:** EMI, Home Loan, Car Loan, Gold Loan, Education Loan, Flat vs Reducing  
**General:** Simple Interest, Compound Interest, GST, Gratuity, Salary, Brokerage
