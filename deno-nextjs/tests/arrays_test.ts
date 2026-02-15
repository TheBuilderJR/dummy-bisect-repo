import { assertEquals } from "@std/assert";
import { chunk, groupBy, sortBy, uniqBy } from "../lib/arrays.ts";

Deno.test("chunk splits array into groups of given size", () => {
  assertEquals(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]);
  assertEquals(chunk([1, 2, 3], 3), [[1, 2, 3]]);
  assertEquals(chunk([], 2), []);
});

Deno.test("groupBy groups items by a key", () => {
  const items = [
    { type: "a", value: 1 },
    { type: "b", value: 2 },
    { type: "a", value: 3 },
  ];
  const grouped = groupBy(items, "type");
  assertEquals(grouped["a"].length, 2);
  assertEquals(grouped["b"].length, 1);
});

Deno.test("sortBy sorts items by a key", () => {
  const items = [
    { name: "Charlie", age: 30 },
    { name: "Alice", age: 25 },
    { name: "Bob", age: 35 },
  ];
  const sorted = sortBy(items, "name");
  assertEquals(sorted[0].name, "Alice");
  assertEquals(sorted[1].name, "Bob");
  assertEquals(sorted[2].name, "Charlie");
});

Deno.test("uniqBy returns unique items by a key", () => {
  const items = [
    { id: 1, name: "Alice" },
    { id: 2, name: "Bob" },
    { id: 1, name: "Alice Dup" },
  ];
  const unique = uniqBy(items, "id");
  assertEquals(unique.length, 2);
  assertEquals(unique[0].name, "Alice");
  assertEquals(unique[1].name, "Bob");
});
