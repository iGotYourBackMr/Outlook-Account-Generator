## Project Setup Guide

### Step 1: Clone the Repository
1. **Download Git**: [Git Download](https://git-scm.com/downloads) and install it following the instructions for your operating system.
2. **Clone the Repository**: Open your terminal or command prompt and run the following command:

    ```sh
    git clone https://github.com/iGotYourBackMr/Outlook-Account-Generator.git
    cd Outlook-Account-Generator
    ```

### Step 2: Install Python
1. **Download Python**: [Python Download](https://www.python.org/downloads/)
2. **Install Python**: Follow the installation instructions for your operating system.
3. **Verify Python Installation**: Open your terminal or command prompt and run:

    ```sh
    python --version
    ```

### Step 3: Verify pip Installation
Pip comes pre-installed with Python. Verify its installation with:

```sh
pip --version
```

### Step 4: Install Required Python Packages
Run the following commands to install the necessary Python packages:

```sh
pip install selenium
pip install webdriver-manager
pip install capsolver
pip install requests
```

### Step 5: Configure the Project
1. **Navigate to the Project Directory**: Ensure you are in the project directory:

    ```sh
    cd Outlook-Account-Generator
    ```

2. **Create `config.py`**: Create a `config.py` file with your CAPSolver API key and, optionally, your Discord webhook URL. Use a text editor to create this file in the project directory with the following content:

    ```python
    CAPSOLVER_API_KEY = ''  # Leave empty if not using CAPSolver
    WEBHOOK_URL = ''  # Leave empty if not using Discord webhook
    ```

### Step 6: Project Directory Structure
Ensure your project directory looks like this:

```
Outlook-Account-Generator/
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

### Step 7: Run the Script
1. **Run the Script**: In your terminal or command prompt, run the script:

    ```sh
    python main.py
    ```

2. **Follow the Prompts**: The script will prompt you to enter the number of accounts you want to create. Enter the number and let the script run.

### Important Note
- **Manual CAPTCHA Solving**: The automatic CAPTCHA solver is currently broken. You will need to solve CAPTCHAs manually during the account creation process. When prompted, solve the CAPTCHA in the browser and press Enter in the terminal to continue.
- **Discord Webhook**: If you choose not to use the Discord webhook, you can leave `WEBHOOK_URL` empty, and the script will skip sending notifications to Discord.
- **CAPSolver**: If you choose not to use CAPSolver, you can leave `CAPSOLVER_API_KEY` empty, and the script will require manual CAPTCHA solving.

### Example Workflow

Here’s a complete example of the workflow:

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/iGotYourBackMr/Outlook-Account-Generator.git
    cd Outlook-Account-Generator
    ```

2. **Install Required Packages**:

    ```sh
    pip install selenium
    pip install webdriver-manager
    pip install capsolver
    pip install requests
    ```

3. **Create `config.py`**:

    ```python
    CAPSOLVER_API_KEY = ''  # Leave empty if not using CAPSolver
    WEBHOOK_URL = ''  # Leave empty if not using Discord webhook
    ```

4. **Run the Script**:

    ```sh
    python main.py
    ```

By following these steps, anyone should be able to set up and run your project successfully, while being aware of the need to manually solve CAPTCHAs and optionally use Discord notifications and CAPSolver.