from cs50 import SQL
from datetime import datetime
from flask import Flask, jsonify, flash, redirect, render_template, request, session
from flask_session import Session


# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

#Create the expenses table if it doesn't exist
db.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount NUMERIC NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

#Create the income table if it doesn't exist
db.execute("""
CREATE TABLE IF NOT EXISTS incomes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount NUMERIC NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/barChart", methods=["GET"])
def barChart():
    start_date,end_date=thirty_days_Counter()
    expenses=db.execute("SELECT date, SUM(amount) as total FROM expenses where date between ? and ? GROUP BY date",start_date,end_date)
    return jsonify(expenses)

@app.route("/expenses/new", methods=["GET", "POST"])
def new_expense():
    return render_template("new_expense.html")

@app.route("/filter/income", methods=["GET"])
def filter_income():
    dateFilter=request.args.get('date')
    categoryFilter=request.args.get('category')
    if categoryFilter == 'All':
        if dateFilter:
            income = db.execute("SELECT * FROM incomes where date(date) = date(?)", dateFilter)
            return jsonify({"income":income});
        else:
            start_date,end_date=thirty_days_Counter()
            income = db.execute("SELECT * FROM incomes where date(date) BETWEEN ? AND ?", start_date, end_date)
            return jsonify({"income":income});
    else:
        if dateFilter:
            income = db.execute("SELECT * FROM incomes where date(date) = date(?) AND category = ?", dateFilter, categoryFilter)
            return jsonify({"income":income});
        else:
            income = db.execute("SELECT * FROM incomes where category = ?", categoryFilter)
            return jsonify({"income":income});

@app.route("/filter", methods=["GET"])
def filter():
    dateFilter=request.args.get('date')
    categoryFilter=request.args.get('category')
    start_date,end_date=thirty_days_Counter()
    if categoryFilter == 'All':
        if dateFilter:
            expenses = db.execute("SELECT * FROM expenses WHERE date(date) = date(?)", dateFilter)
            return jsonify({"expenses":expenses});
        else:
            expenses = db.execute("SELECT * FROM expenses WHERE date(date) BETWEEN ? AND ?", start_date, end_date)
            return jsonify({"expenses":expenses});
    else:
        if dateFilter:
            expenses = db.execute("SELECT * FROM expenses WHERE date(date) = date(?) AND category = ?", dateFilter, categoryFilter)
            return jsonify({"expenses":expenses});
        else:
            expenses = db.execute("SELECT * FROM expenses WHERE category = ?", categoryFilter)
            return jsonify({"expenses":expenses});

@app.route("/expenses", methods=["GET", "POST", "DELETE"])
def expenses():
    if request.method == "POST":
        amount = request.form.get("amount")
        category = request.form.get("category")
        description = request.form.get("description")
        date = request.form.get("date")
        db.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)", amount, category, description, date)
        return redirect("/expenses")
    elif request.method == "DELETE":
        try:
            id = request.args.get("id")
            db.execute("DELETE FROM expenses WHERE id = ?", id)
            return jsonify({"status":200})
        except:
            return jsonify({"status":"error"})
    else:
        start_date,end_date=thirty_days_Counter()
        expenses = db.execute("SELECT * FROM expenses WHERE date(date) BETWEEN ? AND ?", start_date, end_date)  
        income = db.execute("SELECT sum(amount) FROM incomes WHERE date(date) BETWEEN ? AND ?", start_date, end_date)
        income = income[0]['sum(amount)']
        return render_template("expenses.html",expenses=expenses,income=income)
    
@app.route("/expenses/edit", methods=["PUT"])
def edit_expense():
    try:
     data=request.get_json()
     id = data.get("id")
     amount = data.get("amount")
     category =data.get("category")
     description = data.get("description")
     date = data.get("date")
     db.execute("UPDATE expenses SET amount = ?, category = ?, description = ?, date = ? WHERE id = ?", amount, category, description, date, id)
     return jsonify({"status":200})
    except:
     return jsonify({"status":"error"}) 
    
@app.route("/incomes", methods=["GET", "POST"])
def income():
    if request.method == "POST":
        amount = request.form.get("amount")
        category = request.form.get("category")
        description = request.form.get("description")
        date = request.form.get("date")
        db.execute("INSERT INTO incomes (amount, category, description) VALUES (?, ?, ?)", amount, category, description)
        return redirect("/incomes")
    else:
        start_date,end_date=thirty_days_Counter()
        incomes = db.execute("SELECT * ,strftime('%Y-%m-%d',date) as date FROM incomes WHERE date(date) BETWEEN ? AND ?", start_date, end_date)
        total_income = db.execute("SELECT sum(amount) FROM incomes WHERE date(date) BETWEEN ? AND ?", start_date, end_date)
        return render_template("incomes.html", incomes=incomes,total=total_income[0]['sum(amount)'])
    
@app.route("/incomes", methods=["DELETE"])
def delete_income():
    try:
        id = request.args.get("id")
        db.execute("DELETE FROM incomes WHERE id = ?", id)
        return jsonify({"status":200})
    except:
        return jsonify({"status":"error"})
    
@app.route("/incomes/edit", methods=["PUT"])
def edit_income():
    try:
        data=request.get_json()
        id = data.get("id")
        amount = data.get("amount")
        category =data.get("category")
        description = data.get("description")
        date = data.get("date")
        db.execute("UPDATE incomes SET amount = ?, category = ?, description = ?, date = ? WHERE id = ?", amount, category, description, date, id)
        return jsonify({"status":200})
    except:
        return jsonify({"status":"error"})    

@app.route("/incomes/edit", methods=["GET"])
def redirect_edit_income():
    id = request.args.get("id")
    income = db.execute("SELECT * , strftime('%Y-%m-%d',date) as date  FROM incomes WHERE id = ?", id)
    return render_template("edit_income.html", income=income[0])    
    
@app.route("/income/new", methods=["GET", "POST"])
def new_income():
    return render_template("new_income.html")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

@app.route("/expenses/bieChart", methods=["GET"])
def pieChart():
    expenses=db.execute("SELECT category, SUM(amount) as total FROM expenses  GROUP BY category ")
    return jsonify(expenses)

@app.route("/incomes/bieChart", methods=["GET"])
def pieChartIncome():
    incomes=db.execute("SELECT category, SUM(amount) as total FROM incomes  GROUP BY category ")
    return jsonify(incomes)

@app.route("/balance", methods=["GET"])
def balance():
    start_date, end_date = thirty_days_Counter()
    expenses = db.execute("SELECT SUM(amount) FROM expenses WHERE date(date) BETWEEN ? AND ?", start_date, end_date)
    incomes = db.execute("SELECT SUM(amount) FROM incomes WHERE date(date) BETWEEN ? AND ?", start_date, end_date)
    balance = incomes[0]['SUM(amount)'] - expenses[0]['SUM(amount)']
    return jsonify({"balance":balance})


def thirty_days_Counter():
    #get the current year and month
    current_year = datetime.now().year
    current_month= datetime.now().month
    #get the total expenses and incomes for the current month
    start_date = f"{current_year}-{current_month:02d}-01"
    end_date = f"{current_year}-{current_month:02d}-31"
    return start_date, end_date

@app.route("/expenses/edit", methods=["GET"])
def redirect_edit():
    id = request.args.get("id")
    expense = db.execute("SELECT * FROM expenses WHERE id = ?", id)
    return render_template("edit_expense.html", expense=expense[0])


    
