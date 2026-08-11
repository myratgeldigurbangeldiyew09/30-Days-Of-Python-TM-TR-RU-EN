# 3-nji Gün: Operatorlar we Olaryň Çuňňur Arhitekturasy

Python-da operatorlar diňe bir matematiki amallar däl, eýsem obyektleriň arasyndaky gatnaşyklary we logiki akymy dolandyrmak üçin esasy guraldyr.

---

## 1. Arifmetiki Operatorlar (Arithmetic Operators)

| Operator | Ady | Mysal | Düşündiriş |
| :--- | :--- | :--- | :--- |
| `+` | Goşmak | `a + b` | Eger tekst bolsa, birleşdirýär (Concat) |
| `-` | Aýyrmak | `a - b` | Sanlaryň tapawudyny alýar |
| `*` | Köpeltmek | `a * b` | Teksti köpeltseň, ony gaýtalaýar (`"A"*3` -> `"AAA"`) |
| `/` | Bölmek | `a / b` | Hemişe `float` görnüşinde netije berýär (`6 / 2` -> `3.0`) |
| `//` | Bütin bölmek (Floor Division) | `a // b` | Дroby unudyp, diňe bütin bölegini alýar (`7 // 2` -> `3`) |
| `%` | Qalgyly bölmek (Modulus) | `a % b` | Bölünendäki qalgyny berýär (Jübüt/Täk san barlagyna peýdaly) |
| `**` | Derejä galdyrmak (Exponentiation) | `a ** b` | $a^b$ hesabyny edýär (`2 ** 3` -> `8`) |

---

## 2. Deňeşdiriş Operatorlary (Comparison Operators)

Deňeşdiriş amallary hemişe **`True`** ýa-da **`False`** (Boolean) netijesini berýär.

* `==` Deňmi?
* `!=` Deň dälmi?
* `>` Uly
* `<` Kiçi
* `>=` Uly ýa-da deň
* `<=` Kiçi ýa-da deň

---

## 3. Logiki Operatorlar (Logical Operators)

- **`and`**: Ähli şertler `True` bolmaly.
- **`or`**: Azyndan bir şert `True` bolsa ýeterlik.
- **`not`**: Netijäni tersine öwürýär (`not True` -> `False`).

> **Çuňňur öwreniş (Short-circuit Evaluation):**
> Python `and` ýa-da `or` amallarynda ilkinji sertden netije belli bolsa, galan şertleri barlap oturmaýar. Bu kody tizleşdirýär.

---

## 4. Degişlilik we Kimlik Operatorlary (Identity & Membership)

- **`is` vs `==`**: 
  - `==` obyektleriň **bahalaryny** deňeşdirýär.
  - `is` obyektleriň **ýatdaky salgysyny (RAM memory address)** barlag edýär.
- **`in` / `not in`**: Ýygyndynyň (List, String, Tuple) içinde element bar-ýoklygyny barlaýar.

---

## 5. Bitwise Operatorlar (Bitler bilen işlemek)

Bitwise operatorlar sanlary ikilik kodynda (`0` we `1`) tizlik bilen işlemek üçin ulanylýar:
- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (Left shift), `>>` (Right shift).

---

## 6. Operasiýalaryň Artykmaçlygy (Operator Precedence)

Python amallary şu tertipde ýerine ýetirýär:
1. `()` - Ýaýlar (Parentheses)
2. `**` - Dereje
3. `+x`, `-x`, `~x` - Unar operatorlar
4. `*`, `/`, `//`, `%` - Köpeltmek we bölmek
5. `+`, `-` - Goşmak we aýyrmak
6. `<<`, `>>` - Bitwise süýşürme
7. `&`, `^`, `|` - Bitwise amallar
8. Deňeşdiriş we Degişlilik operatorlary (`==`, `is`, `in`)
9. `not`, `and`, `or` - Logiki operatorlar
10. 
