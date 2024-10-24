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

# Development of AST-Engine

- To develop a rule engine application using Abstract Syntax Tree (AST) with Streamlit, we’ll break the task into the following steps:

- Steps to Develop the Rule Engine:

-- Data Structure for AST: We’ll create a class Node that represents the AST. This node will have attributes like type (operator/operand), left child, right child, and value.

-- Database for Storing Rules: You can use SQLite, as it’s lightweight and fits the requirements of this application. The rules and their corresponding AST structure will be stored in this database.

# API Design:

- create_rule(rule_string): Parse the rule string and convert it into an AST representation.
- combine_rules(rules): Combine multiple rules (ASTs) into one.
- evaluate_rule(json_data): Evaluate the rule against a provided dataset.

# Streamlit UI: 

- Create a simple UI to interact with the rule engine. The UI will allow users to:
- Define rules via a text input
- See the created rule's AST structure
- Combine multiple rules
- Evaluate the combined rule using test data
