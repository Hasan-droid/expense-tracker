# C$50 Expense Tracker

## Overview

C$50 Expense Tracker is a web application that allows users to track their expenses and incomes. Users can add, edit, and delete expenses and incomes, and view a summary of their financial activities.

## Features

- Add, edit, and delete expenses
- Add, edit, and delete incomes
- View a summary of expenses and incomes
- Filter expenses and incomes by date and category
- Visualize financial data using charts

## Technologies Used

- Python
- Flask
- SQLite
- HTML/CSS
- JavaScript
- Bootstrap
- ECharts

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Hasan-droid/expense-tracker.git
   cd expense-tracker
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```sh
   flask run
   ```

6. **Open your web browser and navigate to:**

   ```
   http://127.0.0.1:5000
   ```

7. **Manipulate the database:**

   This project has a built-in database `project.db`, so there is no need for any database setup.
   Click `Ctrl + C` to exit the virtual environment, and then run:

   ```sh
   .\sqlite3.exe project.db
   ```

## Data Tracking Details

This application tracks monthly expenses and incomes. Here are the details:

1. **Expenses Page:**

   - The income and balance displayed on the expenses page are calculated for the current month.
   - The first table in expenses listed are filtered to show only those within the current month.

2. **Incomes Page:**

   - The total income displayed on the incomes page is calculated for the current month.
   - The first table in incomes listed are filtered to show only those within the current month.

3. **Home Page (Bar Chart):**

   - The bar chart on the home page shows the total expenses per month.
   - The data for the bar chart is aggregated monthly to provide a clear overview of expenses over time.

4. **Overall Tracking (Dashboard):**
   - The dashboard tracks overall expenses and incomes.
   - This means that the data displayed on the dashboard is not restricted to any specific time period.

## Usage

### Adding an Expense

1. Navigate to the "Expenses" page.
2. Click on the "New Expense" button.
3. Fill in the expense details and click "Submit".

### Editing an Expense

1. Navigate to the "Expenses" page.
2. Click on the "Edit" button next to the expense you want to edit.
3. Update the expense details and click "Submit".

### Deleting an Expense

1. Navigate to the "Expenses" page.
2. Click on the "Delete" button next to the expense you want to delete.

### Adding an Income

1. Navigate to the "Incomes" page.
2. Click on the "New Income" button.
3. Fill in the income details and click "Submit".

### Editing an Income

1. Navigate to the "Incomes" page.
2. Click on the "Edit" button next to the income you want to edit.
3. Update the income details and click "Submit".

### Deleting an Income

1. Navigate to the "Incomes" page.
2. Click on the "Delete" button next to the income you want to delete.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [ECharts](https://echarts.apache.org/)
