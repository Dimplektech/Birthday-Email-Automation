# Birthday Wisher Automation

This Python script sends automatic birthday wishes via email using pre-defined letter templates. It runs on PythonAnywhere, and the birthday check is performed daily. When a birthday matches today's date, the script selects a random letter template and sends a personalized birthday wish to the recipient.

## Setup Instructions

### 1. Prerequisites
- A **PythonAnywhere** account. Sign up at [PythonAnywhere](https://www.pythonanywhere.com/).
- Python 3.x installed on your machine for local testing (optional).
- A working SMTP email account (e.g., Gmail) for sending emails.

### 2. Preparing the Script

1. **Clone or download the repository** containing the script to your local machine or directly upload it to PythonAnywhere.
    ```bash
       git clone https://github.com/Dimplektech/Birthday-Email-Automation.git

2. **Directory Structure**:
   - The `letter_templates` folder should contain the birthday letter templates named as `letter_1.txt`, `letter_2.txt`, and `letter_3.txt`.

3. **Edit the Python script (`birthday_wisher.py`)**:
   - Update the `birthdays` dictionary with names and birthdays in the format `MM-DD`.
   - In the `send_email` function, replace the placeholders with your SMTP details:
     - `my_email`: Your email address.
     - `my_password`: Your email password or app-specific password.
     - `to_email`: The recipient's email address.
  
4. **Letter Templates**:
   - Place your birthday templates in the `letter_templates` folder.
   - Ensure the templates use `[NAME]` as a placeholder for the recipient's name.
   - Example template:
     ```txt
     Dear [NAME],

     Wishing you a wonderful birthday! Have an amazing year ahead.

     Best regards,
     Your Friend
     ```

### 3. Set Up on PythonAnywhere

1. **Upload the Script**:
   - Log in to your PythonAnywhere account.
   - Navigate to the **Files** tab and upload your Python script (`main.py`) and letter templates folder.

2. **Set Up Daily Task (Scheduler)**:
   - Go to the **Tasks** tab.
   - Click **Add a new scheduled task**.
   - Set the task to run daily at a specific time (e.g., `00:00`).
   - In the command field, enter:
     ```bash
     python3 /home/yourusername/main.py
     ```
     (Replace `/home/yourusername/` with the actual path to your script.)

3. **Ensure Your SMTP Email is Configured**:
   - For Gmail users: You may need to create an **App Password** in your Google account and use it in the script instead of your regular password. Follow [Google's App Password guide](https://support.google.com/accounts/answer/185833?hl=en) to generate one.

### 4. Running the Script Locally (Optional)

1. **Install required modules** if you're testing on your local machine:
   - The script uses only built-in Python libraries, so no external installations are needed.
   
2. **Run the script**:
   ```bash
   python3 main.py


  
  


