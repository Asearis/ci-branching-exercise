# CI/CD Demo Project

This project demonstrates the setup and flow of a **CI/CD pipeline** using **GitHub Actions**. It includes the creation of a simple Flask app, implementation of automated testing, and best practices for development workflows, such as branching, code reviews, and merge processes.

## Project Phases

### Phase 1: Repository Setup

#### 1.1 Create a Simple Flask Repository

-   **Initialize a new GitHub repository.**
-   **Set up a minimal Flask app (`app.py`)** that serves a simple message.
    ```python
    # app.py
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Flask server is running!'

    if __name__ == '__main__':
        app.run(debug=True)
    ```
-   **Include a `requirements.txt` file** for dependencies.
    ```plaintext
    Flask
    ```
-   **Add a `README.md`** with setup instructions.

#### 1.2 Run the Flask Server Locally

-   **Implement a basic route (`/`)** that returns:
    ```plaintext
    Flask server is running!
    ```
-   Provide setup instructions in the README for running the server locally.

### Phase 2: Continuous Integration (CI) Pipeline

#### 2.1 Introduce CI Pipeline using GitHub Actions

-   Add a GitHub Actions workflow (`.github/workflows/ci.yml`) to:
    -   Run unit tests.
    -   Check code formatting (using tools like `black` for Python).
    -   Lint code using `flake8` or `pylint`.
-   The CI pipeline should fail if:
    -   Tests fail.
    -   Code formatting issues are found.
    -   Linting issues are detected.
    ```yaml
    # .github/workflows/ci.yml
    name: CI

    on:
      push:
        branches: [ main ]
      pull_request:
        branches: [ main ]

    jobs:
      build:
        runs-on: ubuntu-latest

        steps:
          - uses: actions/checkout@v3
          - name: Set up Python 3.9
            uses: actions/setup-python@v3
            with:
              python-version: 3.9
          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              pip install flake8 black pylint -r requirements.txt
          - name: Lint with flake8
            run: flake8 app.py
          - name: Format with black
            run: black --check --diff app.py
          - name: Pylint
            run: pylint app.py
          - name: Run tests (example)
            run: |
              # Add test commands here.
              # Example: python -m unittest discover
    ```

### Phase 3: Enforcing Best Practices for Development

#### 3.1 Block Direct Merges to `main`

-   Configure branch protection rules in GitHub:
    -   Require pull requests (PRs) before merging.
    -   Require at least one approval before merging.
    -   Prevent force pushes and direct commits to `main`.

#### 3.2 Create a Feature Branch, Code Review, and Merge Process

-   Development workflow:
    -   Developers create feature branches.
    -   Submit PRs for code review.
    -   Ensure CI passes (tests, linting, formatting).
    -   Require at least one approval before merging.
    -   Merge only when CI is green.

### Phase 4: Code Review Best Practices

#### 4.1 Code Review Etiquette & Best Practices

-   **For Reviewers:**
    -   Be constructive and supportive.
    -   Highlight best practices and suggest improvements.
    -   Provide actionable feedback with examples.
    -   Focus on both logic and readability.
    -   Encourage documentation where necessary.
-   **For Authors:**
    -   Provide a clear PR description with context.
    -   Address comments professionally and promptly.
    -   Write meaningful commit messages.
    -   Be open to suggestions and justify design choices.

## Setup Instructions

### Running the Flask Server Locally

Clone the repository:

```bash
git clone [https://github.com/your-username/cicd-demo.git](https://github.com/your-username/cicd-demo.git)
cd cicd-demo
```

Install dependencies:

```bash
pip install -r requirements.txt
Run the Flask server:
```

```Bash
python app.py
```
Visit http://127.0.0.1:5000/ in your browser to see the message:
```Plaintext
Flask server is running!
```

CI Pipeline Workflow
Once you've pushed your changes to any branch or submitted a pull request, GitHub Actions will automatically:

* Install dependencies.
* Run the unit tests.
* Check if the code is formatted properly.
* Lint the code for any potential issues.
* The workflow will fail if any of the checks fail.

