# Day 3: Operators & Architecture Deep Dive

Operators in Python are core tools not only for arithmetic, but also for controlling execution flow and memory reference management.

---

## 1. Arithmetic Operators

| Operator | Name | Example | Description |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `a + b` | Performs string concatenation on strings |
| `-` | Subtraction | `a - b` | Subtracts operands |
| `*` | Multiplication | `a * b` | Replicates strings (`"A"*3` -> `"AAA"`) |
| `/` | Division | `a / b` | Always yields a `float` (`6 / 2` -> `3.0`) |
| `//` | Floor Division | `a // b` | Discards fractional part (`7 // 2` -> `3`) |
| `%` | Modulus | `a % b` | Returns division remainder (Useful for Even/Odd) |
| `**` | Exponentiation | `a ** b` | Calculates $a^b$ (`2 ** 3` -> `8`) |

---

## 2. Comparison Operators

Comparison operations always evaluate to a Boolean: **`True`** or **`False`**.

* `==` Equal to
* `!=` Not equal to
* `>` Greater than
* `<` Less than
* `>=` Greater than or equal to
* `<=` Less than or equal to

---

## 3. Logical Operators

- **`and`**: Returns `True` if all conditions are `True`.
- **`or`**: Returns `True` if at least one condition is `True`.
- **`not`**: Inverts the logical state (`not True` -> `False`).

> **Short-circuit Evaluation:**
> Python stops evaluating an expression as soon as the outcome is determined. This optimizes execution speed.

---

## 4. Identity & Membership Operators

- **`is` vs `==`**: 
  - `==` compares the **values** of variables.
  - `is` checks whether two variables point to the **same RAM memory location**.
- **`in` / `not in`**: Checks membership within collections (List, String, Tuple).

---

## 5. Bitwise Operators

Manipulate numbers directly at the binary level (`0` and `1`):
- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (Left shift), `>>` (Right shift).

---

## 6. Operator Precedence

Precedence hierarchy from highest to lowest:
1. `()` - Parentheses
2. `**` - Exponentiation
3. `+x`, `-x`, `~x` - Unary operators
4. `*`, `/`, `//`, `%` - Multiplication & Division
5. `+`, `-` - Addition & Subtraction
6. `<<`, `>>` - Bitwise shifts
7. `&`, `^`, `|` - Bitwise operators
8. Comparison & Identity (`==`, `is`, `in`)
9. `not`, `and`, `or` - Logical operators
10. 
