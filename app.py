import streamlit as st
from ast_engine import create_rule, combine_rules, evaluate_rule
from db import create_db, insert_rule, get_rules

# Initialize database
create_db()

st.title("Rule Engine with AST")

# Create rule
rule_input = st.text_input("Enter Rule:")
if st.button("Create Rule"):
    rule_ast = create_rule(rule_input)
    insert_rule(rule_input)
    st.write(f"Created Rule: {rule_input}")

# Show stored rules
rules = get_rules()
if rules:
    st.write("Stored Rules:")
    for rule in rules:
        st.write(rule[1])

# Combine and evaluate rules
if st.button("Combine and Evaluate Rules"):
    rule_asts = [create_rule(rule[1]) for rule in rules]
    combined_ast = combine_rules(rule_asts)
    st.write("Rules Combined Successfully")

    # Input test data for evaluation
    test_data = {
        "age": st.number_input("Age"),
        "department": st.text_input("Department"),
        "salary": st.number_input("Salary"),
        "experience": st.number_input("Experience")
    }

    if st.button("Evaluate Rule"):
        result = evaluate_rule(combined_ast, test_data)
        st.write(f"Evaluation Result: {result}")
