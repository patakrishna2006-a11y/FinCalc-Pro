from flask import Flask, request, jsonify, render_template
from calculator import (
    SIP, LUMPSUM, SWP, STEP_UP_SIP, PPF, EPF, NSC,
    FD_SIMPLE, RD, NPS, RETIREMENT_CALCULATOR, GRATUITY,
    SALARY_CALCULATOR, EMI, HOME_LOAN_EMI, CAR_LOAN_EMI,
    GOLD_LOAN_EMI, EDUCATION_LOAN_EMI, FLAT_VS_REDUCING,
    SIMPLE_INTEREST, COMPOUND_INTEREST, GST, CAGR,
    INFLATION, BROKERAGE_CALCULATOR
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    calc_type = data.get("type")
    params = data.get("params", {})

    try:
        result = None

        if calc_type == "SIP":
            result = SIP(
                monthly_investment=float(params["monthly_investment"]),
                Expected_return=float(params["Expected_return"]),
                years=float(params["years"]),
                mode=params.get("mode", "end")
            )
        elif calc_type == "LUMPSUM":
            result = LUMPSUM(
                Total_investment=float(params["Total_investment"]),
                Expected_return=float(params["Expected_return"]),
                years=float(params["years"])
            )
        elif calc_type == "SWP":
            result = SWP(
                total_investment=float(params["total_investment"]),
                withdrawal_amount=float(params["withdrawal_amount"]),
                Expected_rate=float(params["Expected_rate"]),
                years=float(params["years"])
            )
        elif calc_type == "STEP_UP_SIP":
            result = STEP_UP_SIP(
                monthly_investment=float(params["monthly_investment"]),
                step_up_rate=float(params["step_up_rate"]),
                Expected_return=float(params["Expected_return"]),
                years=float(params["years"])
            )
        elif calc_type == "PPF":
            result = PPF(
                yearly_investment=float(params["yearly_investment"]),
                annual_interest_rate=float(params["annual_interest_rate"]),
                years=float(params["years"])
            )
        elif calc_type == "EPF":
            result = EPF(
                basic_salary=float(params["basic_salary"]),
                DA=float(params["DA"]),
                years_of_service=int(params["years_of_service"]),
                annual_salary_growth=float(params["annual_salary_growth"]),
                epf_interest_rate=float(params["epf_interest_rate"])
            )
        elif calc_type == "NSC":
            result = NSC(
                amount_invested=float(params["amount_invested"]),
                interest_rate=float(params["interest_rate"]),
                years=int(params.get("years", 5))
            )
        elif calc_type == "FD_SIMPLE":
            result = FD_SIMPLE(
                principal=float(params["principal"]),
                interest_rate=float(params["interest_rate"]),
                years=float(params["years"])
            )
        elif calc_type == "RD":
            result = RD(
                monthly_investment=float(params["monthly_investment"]),
                Expected_rate=float(params["Expected_rate"]),
                years=float(params["years"])
            )
        elif calc_type == "NPS":
            result = NPS(
                monthly_investment=float(params["monthly_investment"]),
                annual_return=float(params["annual_return"]),
                current_age=int(params["current_age"]),
                retirement_age=int(params.get("retirement_age", 60))
            )
        elif calc_type == "RETIREMENT_CALCULATOR":
            result = RETIREMENT_CALCULATOR(
                age=int(params["age"]),
                monthly_expense=float(params["monthly_expense"]),
                retirement_age=int(params.get("retirement_age", 60)),
                life_expectancy=int(params.get("life_expectancy", 85)),
                inflation=float(params.get("inflation", 0.06)),
                annual_return=float(params.get("annual_return", 0.07))
            )
        elif calc_type == "GRATUITY":
            result = GRATUITY(
                basic_salary=float(params["basic_salary"]),
                DA=float(params["DA"]),
                years_of_service=float(params["years_of_service"])
            )
        elif calc_type == "SALARY_CALCULATOR":
            result = SALARY_CALCULATOR(
                ctc=float(params["ctc"]),
                bonus=float(params["bonus"]),
                proffesional_tax=float(params["proffesional_tax"]),
                employer_pf=float(params["employer_pf"]),
                employee_pf=float(params["employee_pf"]),
                other_deductions=float(params["other_deductions"])
            )
        elif calc_type == "EMI":
            result = EMI(
                loan_amount=float(params["loan_amount"]),
                interest_rate=float(params["interest_rate"]),
                years=float(params["years"])
            )
        elif calc_type == "HOME_LOAN_EMI":
            result = HOME_LOAN_EMI(
                loan_amount=float(params["loan_amount"]),
                interest_rate=float(params["interest_rate"]),
                years=float(params["years"])
            )
        elif calc_type == "CAR_LOAN_EMI":
            result = CAR_LOAN_EMI(
                loan_amount=float(params["loan_amount"]),
                interest_rate=float(params["interest_rate"]),
                years=float(params["years"])
            )
        elif calc_type == "GOLD_LOAN_EMI":
            result = GOLD_LOAN_EMI(
                loan_amount=float(params["loan_amount"]),
                interest_rate=float(params["interest_rate"]),
                years=float(params["years"])
            )
        elif calc_type == "EDUCATION_LOAN_EMI":
            result = EDUCATION_LOAN_EMI(
                loan_amount=float(params["loan_amount"]),
                interest_rate=float(params["interest_rate"]),
                years=float(params["years"])
            )
        elif calc_type == "FLAT_VS_REDUCING":
            result = FLAT_VS_REDUCING(
                principal=float(params["principal"]),
                annual_rate=float(params["annual_rate"]),
                years=float(params["years"])
            )
        elif calc_type == "SIMPLE_INTEREST":
            result = SIMPLE_INTEREST(
                principal_amount=float(params["principal_amount"]),
                rate_of_interest=float(params["rate_of_interest"]),
                years=float(params["years"])
            )
        elif calc_type == "COMPOUND_INTEREST":
            result = COMPOUND_INTEREST(
                principal_amount=float(params["principal_amount"]),
                interest_rate=float(params["interest_rate"]),
                years=float(params["years"]),
                compounding_per_year=int(params["compounding_per_year"])
            )
        elif calc_type == "GST":
            result = GST(
                original_price=float(params["original_price"]),
                gst_rate=float(params["gst_rate"])
            )
        elif calc_type == "CAGR":
            result = CAGR(
                initial_value=float(params["initial_value"]),
                final_value=float(params["final_value"]),
                years=float(params["years"])
            )
        elif calc_type == "INFLATION":
            result = INFLATION(
                current_price=float(params["current_price"]),
                rate=float(params["rate"]),
                years=float(params["years"])
            )
        elif calc_type == "BROKERAGE_CALCULATOR":
            result = BROKERAGE_CALCULATOR(
                segment=params["segment"],
                Quantity=int(params["Quantity"]),
                buy_price=float(params["buy_price"]),
                sell_price=float(params["sell_price"]),
                brokerage=float(params["brokerage"])
            )
        else:
            return jsonify({"error": f"Unknown calculator type: {calc_type}"}), 400

        return jsonify({"success": True, "result": result})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)