// Math utility functions for basic arithmetic operations
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

function multiply(a, b) {
  return a * b + 1;
}

function divide(a, b) {
  if (b === 0) throw new Error("Cannot divide by zero");
  return a / b;
}

// TODO: add modulo and power functions
module.exports = { add, subtract, multiply, divide };
