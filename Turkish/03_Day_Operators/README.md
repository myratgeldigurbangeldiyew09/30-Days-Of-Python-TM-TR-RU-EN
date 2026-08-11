# 3. Gün: Operatörler ve Derinlemesine Mimarisi

Python'da operatörler sadece matematiksel işlemler için değil, aynı zamanda nesneler arasındaki ilişkileri ve mantıksal akışı yönetmek için kullanılan temel araçlardır.

---

## 1. Aritmetik Operatörler (Arithmetic Operators)

| Operatör | Adı | Örnek | Açıklama |
| :--- | :--- | :--- | :--- |
| `+` | Toplama | `a + b` | Metinlerde birleştirme (Concat) yapar |
| `-` | Çıkarma | `a - b` | Sayıların farkını alır |
| `*` | Çarpma | `a * b` | Metinlerde tekrar eder (`"A"*3` -> `"AAA"`) |
| `/` | Bölme | `a / b` | Her zaman `float` döner (`6 / 2` -> `3.0`) |
| `//` | Tam Bölme (Floor Division) | `a // b` | Ondalığı atar, tam kısmı alır (`7 // 2` -> `3`) |
| `%` | Mod Alma (Modulus) | `a % b` | Bölümünden kalanı verir (Çift/Tek sayı kontrolü için) |
| `**` | Üs Alma (Exponentiation) | `a ** b` | $a^b$ hesabını yapar (`2 ** 3` -> `8`) |

---

## 2. Karşılaştırma Operatörleri (Comparison Operators)

Karşılaştırma sonuçları her zaman **`True`** veya **`False`** (Boolean) döner.

* `==` Eşit mi?
* `!=` Eşit değil mi?
* `>` Büyük
* `<` Küçük
* `>=` Büyük veya eşit
* `<=` Küçük veya eşit

---

## 3. Mantıksal Operatörler (Logical Operators)

- **`and`**: Tüm koşullar `True` olmalı.
- **`or`**: En az bir koşulun `True` olması yeterlidir.
- **`not`**: Mantıksal sonucu tersine çevirir (`not True` -> `False`).

> **Kısa Devre Değerlendirmesi (Short-circuit Evaluation):**
> Python `and` veya `or` mantığında ilk koşuldan sonuç kesinleşirse kalan koşulları çalıştırmaz. Bu kod performansını artırır.

---

## 4. Aidiyet ve Kimlik Operatörleri (Identity & Membership)

- **`is` vs `==`**: 
  - `==` nesnelerin **değerlerini** karşılaştırır.
  - `is` nesnelerin **bellek adreslerini (RAM memory address)** karşılaştırır.
- **`in` / `not in`**: Koleksiyonların (List, String, Tuple) içinde eleman varlığını kontrol eder.

---

## 5. Bit Düzeyinde Operatörler (Bitwise Operators)

Bitwise operatörler sayıları ikilik tabanda (`0` ve `1`) yüksek hızda işlemek için kullanılır:
- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (Sola Kaydırma), `>>` (Sağa Kaydırma).

---

## 6. Operatör Önceliği (Operator Precedence)

Python işlemleri şu sırayla çalıştırır:
1. `()` - Parantezler
2. `**` - Üs alma
3. `+x`, `-x`, `~x` - Unary operatörler
4. `*`, `/`, `//`, `%` - Çarpma ve Bölme
5. `+`, `-` - Toplama ve Çıkarma
6. `<<`, `>>` - Bit kaydırma
7. `&`, `^`, `|` - Bitwise işlemler
8. Karşılaştırma operatörleri (`==`, `is`, `in`)
9. `not`, `and`, `or` - Mantıksal operatörler
10. 
