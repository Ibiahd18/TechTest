Medi Score Calculator

Overview

The Medi Score Calculator is a Python script that evaluates a patient's health status based on key vital signs. 

Thought Process & Design Ideas

Object-Oriented Approach

To ensure modularity and maintainability, I implemented a Patient class to encapsulate all vital sign attributes. This makes it easier to manage patient data and pass it into functions without dealing with multiple parameters.

Functional Decomposition

Each scoring criterion is handled by separate functions (get_respiration_score, get_spo2_score, get_temperature_score). This follows the single responsibility principle and improves code readability. The calculate_medi_score function integrates these functions, making the main logic clear and concise.

Readability & Maintainability

The use of meaningful variable names makes the code self-explanatory.

Logical conditions are structured clearly in the scoring functions.

Comments and docstrings explain each function's purpose.

The script includes test cases to validate correctness and expected behavior.

Error Handling

Although this implementation assumes valid inputs, rounding temperature to one decimal place ensures consistency. Future improvements could include exception handling for unexpected input types.

Features

Takes patient vital signs as input.

Computes a Medi Score ranging from 0 to 14.

Uses predefined scoring criteria for respiration rate, SpO2, temperature, and consciousness.

Implements object-oriented programming with a Patient class.

Includes test cases for validation.
