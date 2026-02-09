import { describe, test, expect } from "vitest";
import { capitalize, reverse, truncate, slugify } from "../src/strings.js";

describe("string utilities", () => {
  test("capitalize uppercases the first letter", () => {
    expect(capitalize("hello")).toBe("Hello");
    expect(capitalize("world")).toBe("World");
    expect(capitalize("")).toBe("");
  });

  test("reverse returns the string backwards", () => {
    expect(reverse("abc")).toBe("cba");
    expect(reverse("hello")).toBe("olleh");
  });

  test("truncate shortens long strings with ellipsis", () => {
    expect(truncate("hello world", 5)).toBe("hello...");
    expect(truncate("hi", 10)).toBe("hi");
  });

  test("slugify converts strings to URL slugs", () => {
    expect(slugify("Hello World")).toBe("hello-world");
    expect(slugify("  Spaces  Everywhere  ")).toBe("spaces-everywhere");
    expect(slugify("Special! @Characters#")).toBe("special-characters");
  });
});
