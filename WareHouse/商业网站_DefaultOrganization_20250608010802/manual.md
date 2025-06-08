Here is the `manual.md` file for the commercial website project:

```markdown
# Commercial Website User Manual

Welcome to the Commercial Website! This manual provides a comprehensive guide to understanding the main functions of the software, how to install the necessary environment dependencies, and how to use the application effectively.

## Overview

The Commercial Website is a simple web application built using Python and Flask. It allows users to submit their name and email through a user-friendly form. The application captures this information and can be extended to process it further, such as storing it in a database or sending it via email.

### Main Functions

- **User Input Form**: The website features a form where users can enter their name and email address.
- **Data Submission**: Upon submission, the application logs the received data and redirects the user back to the homepage.
- **Responsive Design**: The website is styled using CSS to ensure a clean and responsive user interface.

## Installation Guide

To set up the environment and run the Commercial Website, follow these steps:

### Prerequisites

- Ensure you have Python (version 3.6 or higher) installed on your machine.
- Install `pip`, the package installer for Python, if it is not already installed.

### Step 1: Clone the Repository

Clone the repository containing the project files to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Navigate to the project directory and install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

This command will install Flask version 2.0.1 as specified in the `requirements.txt` file. If you plan to add more libraries in the future, you can include them in this file.

### Step 3: Run the Application

Once the dependencies are installed, you can run the application using the following command:

```bash
python main.py
```

By default, the application will run on `http://127.0.0.1:5000/`.

## How to Use the Application

1. **Access the Website**: Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. **Fill Out the Form**: Enter your name and email address in the provided fields.
3. **Submit the Form**: Click the "Submit" button to send your information.
4. **View Submission**: After submission, the application will log the data to the console and redirect you back to the homepage.

## Future Enhancements

The current version of the Commercial Website is a basic implementation. Future enhancements could include:

- Storing submitted data in a database.
- Sending confirmation emails to users upon submission.
- Adding more fields to the form for additional user information.

## Support

For any questions or issues, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

Thank you for using the Commercial Website!
```

This manual provides a clear and structured guide for users to understand and utilize the commercial website effectively.