# Python Expense Tracker

A command-line Expense Tracker built with Python that helps users manage daily expenses, track total spending, and view category-wise expense summaries. The application stores expense records in a JSON file, allowing data to persist between program runs.

## Features

- **Add Expenses:** Record an expense with its amount, category, note, and date.
- **View Expenses:** Display all saved expense records.
- **Delete Expenses:** Remove an expense using its ID.
- **Total Spending:** Calculate the total amount spent.
- **Category-Wise Summary:** Calculate spending for each category.
- **JSON Data Storage:** Save and load expense records using a JSON file.
- **Input Validation:** Handle invalid numeric input and prevent negative expense amounts.

## Technologies Used

- Python 3
- JSON
- OS Module
- Datetime Module

## Project Structure

```text
expense-tracker/
├── expense_tracker.py
├── exp.json
└── README.md
```

`exp.json` is created automatically when expenses are saved for the first time.

## Requirements

- Python 3.x
- No external libraries required

## Installation and Usage

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd expense-tracker
```

**3. Run the application**

```bash
python expense_tracker.py
```

## Application Menu

```text
--- Expense Tracker ---
1. Add expense
2. View expenses
3. Delete expense
4. Total spending
5. Spending by category
6. Exit
Choose:
```

Select an option from the menu and follow the instructions to manage your expenses.

## Data Storage

Expense records are stored locally in `exp.json` in JSON format. Each record contains:

- `id`: Unique expense identifier
- `amount`: Expense amount
- `category`: Expense category
- `note`: Additional details
- `day`: Date of the expense

## Learning Objectives

This project demonstrates practical use of:

- Object-oriented programming and classes
- Functions and methods
- Lists and dictionaries
- Loops and conditional statements
- Exception handling
- File handling and JSON serialization
- Basic data processing and calculations

## Future Improvements

- Add monthly expense reports.
- Display the highest expense.
- Add expense editing functionality.
- Filter expenses by date or category.
- Export reports to CSV.
- Develop a graphical user interface.

## License

This project is open source. You may add a license such as the MIT License if you want others to reuse and modify your code under its terms.
