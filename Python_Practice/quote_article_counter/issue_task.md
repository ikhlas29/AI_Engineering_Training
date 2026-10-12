# 📄 Quote Article Counter: Practising Files and Exception Handling

As a Python developer on the training squad, I want to write quotes to a text file, read them back line by line, count the articles in each line, and append the results to another file, so that I am comfortable opening files with `with`, choosing the right file mode, and handling errors without my program crashing.

---

## 🙅 Please Write This One Without AI

The syntax here (`open`, `with`, `try` / `except` / `else` / `finally`) is the foundation for everything that comes next. Typing it yourself is how you digest it, and it is what lets you spot mistakes later when you review AI-generated code.

Use the official Python documentation if you get stuck.

---

## 🧠 Quick Primer (Read This First)

### Opening Files with `with`

```python
with open("notes.txt", "w") as file:
    # The file is opened here.
    file.write("hello\n")

# The file is closed here automatically,
# even if an error happened inside the block.
```

`with` is a context manager: it guarantees the file is closed when the block ends, so you never need to call `file.close()` manually.

### File Modes You Will Need

| Mode | Meaning | If the File Does Not Exist |
|---|---|---|
| `"r"` | Read | Raises `FileNotFoundError` |
| `"w"` | Write; replaces existing content | Creates the file |
| `"a"` | Append to the end | Creates the file |

### Exception Handling

```python
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("That file does not exist yet.")
except OSError as error:
    print(f"Something else went wrong: {error}")
else:
    print("Read OK")  # Runs only if no exception happened.
finally:
    print("Done trying")  # Always runs.
```

💡 **Tip:** Catch the most specific exception first. Avoid a bare `except:` because it hides bugs.

---

## 🔧 Specification

| Element | Requirement |
|---|---|
| **Project** | `uv` project, Python 3.14, created with `--no-package` |
| **Function 1** | `create_quotes_file(file_path="quotes.txt")`: writes 15 random quotes, one per line |
| **Function 2** | `analyze_quotes(input_path="quotes.txt", output_path="quotes_analysis.txt")`: reads the quotes and counts articles per line |
| **Function 3** | `append_result(line, article_counts, output_path="quotes_analysis.txt")`: appends one formatted line and returns |
| **Articles** | `a`, `an`, `the` — case-insensitive, whole words only |

---

## ✅ Acceptance Criteria

### 1. Git Workflow

- Pull the latest `main`.
- Create your feature branch as described in the repository README:

  ```text
  feature/87-<your-id>-quote-article-counter
  ```

- Create the project under:

  ```text
  experiments_area/from_<your_name>/quote_article_counter/
  ```

- Initialize the project with:

  ```bash
  uv init --no-package --python 3.14
  ```

### 2. Function 1: `create_quotes_file`

- Picks 15 random quotes, for example, from a hard-coded list of 20 or more quotes using `random.sample()`.
- Writes the selected quotes to `quotes.txt`, one quote per line, using `with open(..., "w")`.
- Running the function again replaces the old content; it must not keep growing the file.

### 3. Function 2: `analyze_quotes`

- Opens `quotes.txt` with `with open(..., "r")`.
- Loops over the file **line by line**. Do not load the whole file into one string.
- For each line, counts how many times `a`, `an`, and `the` appear as whole words, ignoring case.
  - `The` and `the` both count.
  - `another` and `theme` do not count as `an` and `the`.
- For each line, calls `append_result(...)` with the original quote and its article counts.
- If `quotes.txt` does not exist, catches `FileNotFoundError` and prints a friendly message instead of crashing.

### 4. Function 3: `append_result`

- Opens the output file in append mode.
- Writes exactly one formatted line and returns.
- Must be safe to call repeatedly.
- Creates the output file if it does not exist.

  💡 **Hint:** Which file mode already does that?

#### Required Line Format

Counts first, followed by the original quote:

```text
{a: <A>, an: <AN>, the: <THE>} <original line>
```

#### Example

**Input line in `quotes.txt`:**

```text
The best time to plant a tree was 20 years ago. The second best time is now.
```

**Output line appended to `quotes_analysis.txt`:**

```text
{a: 1, an: 0, the: 2} The best time to plant a tree was 20 years ago. The second best time is now.
```

### 5. Exception Handling

- Every file operation lives inside a `with` block. Do not manually close files.
- File errors are caught using specific exceptions, such as `FileNotFoundError` and `OSError`, rather than a bare `except:`.
- Use `else` or `finally` at least once and be ready to explain why it is there.

### 6. Execution

- Running the following command creates `quotes.txt`, analyzes it, and produces `quotes_analysis.txt` with 15 lines:

  ```bash
  uv run main.py
  ```

- Delete `quotes.txt` and run only the analysis step. The program prints a friendly error message and exits cleanly.

---

## 🪜 Hints

- `line.strip()` removes the trailing newline (`\n`) before you analyze or write the line back.
- `line.lower().split()` gives you lowercase words, but watch out for punctuation such as `"the,"` or `"a."`.
- `word.strip(".,!?;:\"'")` can help remove surrounding punctuation.
- A dictionary such as the following is a natural place to keep the counts:

  ```python
  {"a": 0, "an": 0, "the": 0}
  ```

- Remember to add `"\n"` when you append the result, or every result may end up on one line.
- Decide whether `analyze_quotes` should clear the old `quotes_analysis.txt` before a new run, and explain your choice in the pull request description.

---

## 📂 Deliverables Checklist

- [ ] `create_quotes_file` writes 15 random quotes to `quotes.txt`.
- [ ] `analyze_quotes` reads line by line and counts `a`, `an`, and `the`.
- [ ] `append_result` appends one formatted line and creates the output file if missing.
- [ ] Specific exceptions are handled, and all files are opened with `with`.
- [ ] `main.py` runs the full flow with `uv run main.py`.
- [ ] Pull request is linked to this issue.

> **Note:** Tests and a README are not required for this one; focus on files, `with`, and exceptions.

---

Happy coding! 🚀