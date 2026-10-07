# ☕ Coffee-Break Analyzer

*As a **full-stack developer** on the training squad, I want to write a tiny “coffee-break analyzer” script so that I can practice treating functions as first-class citizens, lambdas, and higher-order utilities in a relatable, real-life context (our daily coffee orders).*

---

## 📌 Acceptance Criteria

1. **Git Workflow**
   - Pull latest `main`.
   - Create & push an **empty** feature branch named **`coffee-break-analyzer`** before coding.

2. **Data Source**
   - `orders.py` contains a hard-coded `list[dict]` named **`orders`** with the keys shown below:

   | **Key**   | **Type** | **Example** |
   |-----------|----------|-------------|
   | `name`    | str      | "Alex"      |
   | `drink`   | str      | "Latte"     |
   | `size_oz` | int      | 16          |

3. **Functional Utilities**
   - A named function **`is_large(order: dict) -> bool`** returns `True` when `size_oz >= 16`.
   - Use Python’s built-in **`filter()`** with `is_large` → `large_orders`.
   - Use an inline **lambda** with **`map()`** to convert each order in `large_orders` into the string format:

     ```text
     "<name> – <drink> (<size_oz>oz)"
     ```

   - Use **`reduce()`** from `functools` with a two-parameter lambda to calculate the **total ounces** ordered across **all** drinks and print:

     ```text
     Total volume: <X> oz
     ```

   - *[Optional]* Replicate the `filter + map` logic in **one line** via **list-comprehension** → `large_orders_lc` (for comparison).

4. **Type Safety & Code Formatting**
   - All functions & variables include **PEP-484 type hints**.
   - Running `mypy` locally shows **no type errors**.
   - Run `ruff format .` to reformat all the code in the current directory.

5. **Execution Requirements**
   - Script is runnable with:

     ```bash
     python orders.py
     ```

   - It prints:
     1. The formatted list of large drinks.
     2. The total volume line.

---

### 🛠️ Technologies & Tools (implicit)

- Python ≥ 3.8
- `functools` (standard library)
- `mypy` for static type checking
- Git (feature-branch workflow)

Happy coding & enjoy your coffee! ☕