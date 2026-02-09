const { add, subtract, multiply, divide } = require("../src/math");

describe("math utilities", () => {
  test("add returns the sum of two numbers", () => {
    expect(add(2, 3)).toBe(5);
    expect(add(-1, 1)).toBe(0);
    expect(add(0, 0)).toBe(0);
  });

  test("subtract returns the difference of two numbers", () => {
    expect(subtract(5, 3)).toBe(2);
    expect(subtract(0, 5)).toBe(-5);
  });

  test("multiply returns the product of two numbers", () => {
    expect(multiply(3, 4)).toBe(12);
    expect(multiply(-2, 5)).toBe(-10);
    expect(multiply(0, 100)).toBe(0);
  });

  test("divide returns the quotient of two numbers", () => {
    expect(divide(10, 2)).toBe(5);
    expect(divide(7, 2)).toBe(3.5);
  });

  test("divide throws on division by zero", () => {
    expect(() => divide(1, 0)).toThrow("Cannot divide by zero");
  });
});
