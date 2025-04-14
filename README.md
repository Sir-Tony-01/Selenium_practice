
# Selenium Practice Project

A beginner-friendly automation testing project using **Selenium** and **Python**. This repository is designed to help QA trainees learn how to write clean and maintainable web UI tests using the **Page Object Model** pattern.

## 📁 Project Structure

```
Selenium_practice/
│
├── pages/                  # Page Object Model classes
│   └── cart_page.py
│   └── checkout_page.py
│   └── inventory_page.py
│   └── login_page.py
│
├── tests/                  # Test cases
│   └── test_lockout_user.py
│   └── test_login.py
│   └── test_oreder_flow.py
│
├── requirements.txt        # List of Python dependencies
├── conftest.py             # Pytest configuration file
├── run_tests.py            # Script to run all tests
└── README.md               # Project documentation
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Sir-Tony-01/Selenium_practice.git
cd Selenium_practice
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```
On Windows: 
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up WebDriverManager

```bash
pip install webdriver-manager
```


## 🧪 Running the Tests

```bash
python run_tests.py
```

## 🛠️ Technologies and Tools

- [Selenium WebDriver](https://www.selenium.dev/)
- Python 3.8+
- [Pytest](https://docs.pytest.org/)
- Page Object Model (POM) design pattern

