# ☕ User Story – Flexible `make_coffee` Function

## 📝 Story Overview

As a **Python developer** on the team, I want to build a *flexible* `make_coffee` function so that **our café app can accept any combination of extras and options without breaking existing calls**.

---

## 🔧 Function Specification

| **Element**        | **Requirement** |
|--------------------|-----------------|
| **Function name**  | `make_coffee` |
| **Signature**      | `make_coffee(order_id, coffee_type, customer_name, *extras, **options)` |
| **Mandatory args** | `order_id`, `coffee_type`, `customer_name` |
| **Variadic args**  | `*extras` → captures additional positional arguments in a **tuple**<br>`**options` → captures additional keyword arguments in a **dict** |

---

## ✅ Acceptance Criteria

### 1. Default Return

When called with only the three mandatory positional arguments, the function returns:

```python
{
    "order_id": ...,
    "coffee_type": ...,
    "customer_name": ...,
    "extras": (),
    "options": {},
}
```

### 2. Handling `*extras`

Any additional positional arguments, such as `"soy_milk"` and `"extra_shot"`, are captured **in the order supplied** and appear unchanged in the returned `extras` tuple.

### 3. Handling `**options`

Any additional keyword arguments, such as `size="large"` and `takeaway=True`, are captured and appear unchanged in the returned `options` dictionary.

### 4. Positive Unit Test

A test proves that the following call produces the expected output:

```python
make_coffee(
    101,
    "latte",
    "Alice",
    "soy_milk",
    "extra_shot",
    size="large",
    takeaway=True,
)
```

Expected result:

```python
{
    "order_id": 101,
    "coffee_type": "latte",
    "customer_name": "Alice",
    "extras": ("soy_milk", "extra_shot"),
    "options": {
        "size": "large",
        "takeaway": True,
    },
}
```

### 5. Negative Test

Verify that placing a keyword argument **before** a positional argument raises a `SyntaxError`.

For example:

```python
make_coffee(order_id=101, "latte", "Alice")
```

This reinforces Python's calling rules.

> **Note:** Because this is invalid Python syntax, it cannot be written directly inside a normal test function. The test should use `compile()` or `exec()` to verify that the code raises `SyntaxError`.

### 6. Documentation

The **README** explains:

- The trade-offs of the `*args` / `**kwargs` pattern.
- Why variadic arguments are useful for a flexible API.
- Potential drawbacks such as reduced explicitness and weaker discoverability.
- References to the sample Git files shared during training.

---

## 📂 Deliverables Checklist

- [ ] Implement `make_coffee` in `coffee.py`
- [ ] Add unit tests in `test_coffee.py`
- [ ] Cover positive and negative scenarios
- [ ] Update `README.md`
- [ ] Document design decisions and trade-offs
- [ ] Include references to the training Git files