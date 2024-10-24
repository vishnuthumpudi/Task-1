# Rule Engine with AST

## Project Overview
This is a 3-tier rule engine application developed using Python's Abstract Syntax Tree (AST). The application allows dynamic creation, combination, and modification of rules through a simple UI and API. It evaluates user eligibility based on attributes like age, department, salary, and experience.

## Key Features:
- **Dynamic Rule Creation**: Users can create rules using simple string inputs.
- **AST Representation**: Rules are represented as an Abstract Syntax Tree.
- **Rule Combination**: Multiple rules can be combined into a single AST structure.
- **Rule Evaluation**: Rules can be evaluated against input data to check user eligibility.
- **Database Storage**: Rules are stored in a SQLite database for persistence.

## Requirements:
- Python 3.x
- Streamlit
- SQLite3

## How to Run the App:
1. Clone the repository: git clone  cd rule_engine

2. Install dependencies: pip install -r requirements.txt

3. Run the Streamlit application: streamlit run app.py

4. Open your browser and navigate to `http://localhost:8501` to interact with the app.

## Sample Rule Format:
- Example rule: `((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)`

## Test Scenarios:
- **Create Rules**: Input the sample rule and verify AST creation.
- **Combine Rules**: Combine multiple rules and ensure their logic is accurately reflected in the combined AST.
- **Evaluate Rules**: Evaluate rules using different input data.

## Bonus Features:
- Error handling for invalid rules
- Rule modification options

