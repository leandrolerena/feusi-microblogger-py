# 🐍 Code Conventions (Python)

This guide outlines key code conventions to follow for Python-based projects in this course. Consistency and readability matter most.

---

## 🧱 General Principles

* **Keep it simple and explicit**
* **Follow [PEP 8](https://peps.python.org/pep-0008/)** – the official style guide for Python code
* **Avoid premature optimization** – make it work, then make it clean

---

## 🧾 Naming Conventions

* `snake_case` for variables and functions

  ```python
  def get_user_name(): ...
  user_name = "Alice"
  ```
* `PascalCase` for classes

  ```python
  class MessageBoard: ...
  ```

---

## 📁 File & Folder Structure

* One class/module per file when possible
* Use lowercase with underscores for filenames: `message_board.py`
* Group related modules in packages (`__init__.py` optional for Python 3.3+)

---

## 📚 Comments & Docstrings

* Use **docstrings** for all public functions and classes:

  ```python
  def add_message(msg: str) -> None:
      """Add a message to the board."""
      ...
  ```
* Use comments sparingly, only to explain *why* something is done

---

## ✅ Git & Code Reviews

* Commit often with clear messages:
  `"Implement message deletion"` not `"fix"`
* Use **pull requests** for all contributions
* In code reviews:

    * Be constructive and respectful
    * Ask clarifying questions
    * Use GitHub suggestions for minor improvements

---

## 🧪 Testing

* Use `pytest` or `unittest`
* Write tests for key logic and edge cases
* Name test files like `test_<module>.py`
* Place tests in a `test/` directory

---

## 🧰 Python Style

* Use type hints whenever possible:

  ```python
  def post_message(user: str, text: str) -> bool:
  ```
* Prefer f-strings:

  ```python
  print(f"Hello, {user}")
  ```
* Avoid unused imports and variables

---

## 🔒 Security Basics

* Never commit secrets or passwords
* Validate user input
* Follow the principle of least privilege

---

## 🙌 Collaboration Tips

* Respect the style and structure already in the project
* Communicate clearly in issues and pull requests
* Review others’ code before asking for your own to be reviewed

---

When in doubt, refer to [PEP 8](https://peps.python.org/pep-0008/) or ask your teammates for advice. Clean code is a team effort!
