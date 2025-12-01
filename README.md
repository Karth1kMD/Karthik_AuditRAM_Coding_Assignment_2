Email Automation Agent
A Python-based browser automation agent for sending emails via Gmail web interface. Created for AuditRAM Coding Assignment 2.

📋 Overview
This agent automates the process of:

Login - Logging into Gmail with provided credentials
Compose - Creating an email with specified content
Send - Sending the email to the recipient

All inputs (email, password, recipient, subject, body) are provided via command-line arguments.

🚀 Quick Start
Prerequisites

Python 3.8 or higher
Google Chrome browser installed
Gmail account

Installation

Clone this repository

bash   git clone <your-repo-url>
   cd <your-repo-folder>

Install dependencies

bash   pip install selenium
That's it! Selenium 4.6+ includes automatic ChromeDriver management.
Basic Usage
bashpython email_agent.py --email YOUR_EMAIL@gmail.com --password YOUR_PASSWORD --to RECIPIENT@example.com --subject "Your Subject" --body "Your message here"
Example Command
bashpython email_agent.py --email myemail@gmail.com --password "mypassword123" --to scittest@auditram.com --subject "Test Email" --body "This is a test email from my automation agent"

📖 Detailed Instructions
Command-Line Arguments
ArgumentRequiredDescriptionExample--emailYesYour Gmail addressmyemail@gmail.com--passwordYesYour Gmail passwordmypassword123--toYesRecipient email addressrecipient@example.com--subjectYesEmail subject line"Hello World"--bodyYesEmail body text"This is my message"
Note: Use quotes around arguments that contain spaces.
Complete Example
bashpython email_agent.py \
  --email karthik.student@gmail.com \
  --password "SecurePass123" \
  --to scittest@auditram.com \
  --subject "AuditRAM Assignment Submission" \
  --body "This email was sent using my automated browser agent. Student Name: Karthik, Roll: 12345"

🔧 How It Works
Technical Approach
The agent uses Selenium WebDriver to automate Chrome browser:

Launch Chrome - Opens Chrome with automation flags disabled to appear more human-like
Navigate to Gmail - Goes to mail.google.com
Automated Login - Enters email and password credentials
Compose Email - Clicks "Compose" and fills in recipient, subject, and body
Send Email - Clicks the "Send" button and waits for confirmation

Automation Flow
Start
  ↓
Launch Chrome Browser
  ↓
Open Gmail Login Page
  ↓
Enter Email → Click Next
  ↓
Enter Password → Click Next
  ↓
Wait for Inbox to Load
  ↓
Click "Compose" Button
  ↓
Fill Recipient (To field)
  ↓
Fill Subject Line
  ↓
Fill Email Body
  ↓
Click "Send" Button
  ↓
Wait for Confirmation
  ↓
Close Browser
  ↓
End

⚠️ Important Notes
Gmail Security
Google may block automated login attempts for security reasons. If you encounter login issues:

Manual Intervention - The script will keep the browser open. Complete the login manually when prompted.
Less Secure Apps - Enable "Less secure app access" in your Google Account settings (not recommended for primary accounts).
Test Account - Use a dedicated test Gmail account for this assignment.

Known Limitations

2FA/Verification - If your account has 2-factor authentication, you may need to complete it manually in the browser
CAPTCHA - Google may show CAPTCHA challenges that require manual completion
Rate Limiting - Sending too many emails quickly may trigger Google's security measures

Browser Behavior

Browser window opens visibly (not headless) to show the automation process
The script includes wait times for page loads and animations
If any step fails, the browser stays open for manual completion


🐛 Troubleshooting
Issue: "ChromeDriver initialization failed"
Solution:
bashpip install --upgrade selenium
Selenium 4.6+ automatically manages ChromeDriver.
Issue: "Login failed" or "Couldn't sign you in"
Solutions:

Check your email and password are correct
Use a test Gmail account without 2FA
Try enabling "Less secure app access" in Google Account settings
Complete the login manually when the browser opens

Issue: "Could not find Compose button"
Solution:

Wait for the browser window to fully load
If prompted, complete the login manually
The script will pause and let you click Compose manually

Issue: Browser closes immediately
Solution:
This usually means there was an error. Check the console output for error messages.

📁 Project Structure
email-automation-agent/
│
├── email_agent.py          # Main script
├── README.md               # This file
└── requirements.txt        # Python dependencies (optional)
requirements.txt (Optional)
txtselenium>=4.6.0

🔒 Security Best Practices

Never commit passwords - Don't hardcode credentials in your code
Use test accounts - Don't use your primary email account for testing
One test email only - As per assignment requirements, send only ONE email to scittest@auditram.com
Keep credentials private - Don't share your email/password in screenshots or videos


📝 Assignment Submission Checklist

 Script accepts all inputs via command-line arguments
 Successfully logs into Gmail
 Composes email with provided content
 Sends email to scittest@auditram.com
 Screen recording uploaded to YouTube (public)
 GitHub repository is public
 README.md includes clear setup and usage instructions
 Only ONE test email sent to scittest@auditram.com


🎥 Recording Your Demo
When creating your screen recording:

Open terminal/command prompt
Show the command you're running (with arguments visible)
Let the browser window be visible during automation
Show the entire process: login → compose → send
Show the "Message sent" confirmation
Keep video quality clear and readable

Sample Recording Script
bash# Start recording
# Show your command
python email_agent.py --email your@gmail.com --password "yourpass" --to scittest@auditram.com --subject "Test" --body "Assignment submission"

# Let the automation run fully
# Show the success message
# Stop recording

🤝 Support
If you encounter issues:

Check the troubleshooting section above
Read error messages carefully - they often indicate the exact problem
Ensure all dependencies are installed correctly
Verify Chrome browser is installed and up-to-date


📄 License
This project is created for educational purposes as part of AuditRAM Coding Assignment 2.

👤 Author
Your Name
Roll Number: YOUR_ROLL_NUMBER
Email: your.email@example.com

✅ Assignment Requirements Met

✅ Takes credentials from command prompt
✅ Performs sequential actions: Login → Compose → Send
✅ Browser-based automation using Selenium
✅ Sends email to scittest@auditram.com
✅ Complete documentation in README
✅ Clear instructions for running the code