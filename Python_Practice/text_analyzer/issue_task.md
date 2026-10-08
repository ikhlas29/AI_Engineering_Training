# Text Analyzer – Decorators Practice

## Description

A beginner Python project for practising decorators and decorator factories.

## Features

- Counts the number of words, spaces, and uppercase characters.
- Uses `add_text_stats` to add text statistics to a returned string.
- Uses `analyze_text()` as a decorator factory.
- Allows individual statistics to be enabled or disabled.
- Supports `*args` and `**kwargs`.
- Reuses the same counting functions for both parts.

## Run

```bash
uv run decorator_practice.py
```

## Examples

```python
@analyze_text()
```

Counts all statistics.

```python
@analyze_text(count_spaces=False)
```

Counts words and uppercase characters only.

```python
@analyze_text(count_words=False, count_spaces=False)
```

Counts uppercase characters only.

If all options are `False`, the original text is returned unchanged.