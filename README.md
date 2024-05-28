## Project Setup Guide

### Step 1: Install Python
1. **Download Python**: [Python Download](https://www.python.org/downloads/)
2. **Install Python**: Follow the installation instructions for your operating system.
3. **Verify Python Installation**: Open your terminal or command prompt and run:

    ```sh
    python --version
    ```

### Step 2: Verify pip Installation
Pip comes pre-installed with Python. Verify its installation with:

```sh
pip --version
```

### Step 3: Install Required Python Packages
Run the following commands to install the necessary Python packages:

```sh
pip install selenium
pip install webdriver-manager
pip install capsolver
pip install requests
```

### Step 4: Configure the Project
1. **Extract the Project Files**: Ensure you have all the project files extracted into a directory.

2. **Navigate to the Project Directory**: Open your terminal or command prompt and navigate to the project directory:

    ```sh
    cd path/to/your_project_directory
    ```

3. **Create `config.py`**: Create a `config.py` file with your CAPSolver API key and Discord webhook URL. Use a text editor to create this file in the project directory with the following content:

    ```python
    CAPSOLVER_API_KEY = 'your_capsolver_api_key'
    WEBHOOK_URL = 'your_discord_webhook_url'
    ```

### Step 5: Project Directory Structure
Ensure your project directory looks like this:

```
your_project_directory/
│
├── modules/
│   ├── __init__.py
│   ├── webdriver_setup.py
│   ├── account_generator.py
│   └── discord_notifier.py
├── config.py
├── main.py
├── created_accounts.txt
```

### Step 6: Run the Script
1. **Run the Script**: In your terminal or command prompt, run the script:

    ```sh
    python main.py
    ```

2. **Follow the Prompts**: The script will prompt you to enter the number of accounts you want to create. Enter the number and let the script run.

### Important Note
- **Manual CAPTCHA Solving**: The automatic CAPTCHA solver is currently broken. You will need to solve CAPTCHAs manually during the account creation process. When prompted, solve the CAPTCHA in the browser and press Enter in the terminal to continue.

### Example Workflow

Here’s a complete example of the workflow:

1. **Install Required Packages**:

    ```sh
    pip install selenium
    pip install webdriver-manager
    pip install capsolver
    pip install requests
    ```

2. **Create `config.py`**:

    ```python
    CAPSOLVER_API_KEY = 'your_capsolver_api_key'
    WEBHOOK_URL = 'your_discord_webhook_url'
    ```

3. **Run the Script**:

    ```sh
    python main.py
    ```

By following these steps, anyone should be able to set up and run your project successfully, while being aware of the need to manually solve CAPTCHAs.