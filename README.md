## App Name
Product Price Tracker

## Description
This is a Python application that allows users to track the price of a product and receive email notifications when the price drops below a specified level. The application utilizes web scraping to extract product prices from a given URL(works only for trendyol.com now) and sends email notifications using the Gmail SMTP server.

## Installation
1. Clone the repository:

  ```shell
  git clone https://github.com/your-username/product-price-tracker.git
  ```

2. Install the required dependencies:
  ```shell
  pip install -r requirements.txt
  ```
3. Set up environment variables:
  - Create a .env file in the project root directory.
  - Add the following environment variables to the .env file:
    ```
    USERNAME=your-gmail-username
    PASSWORD=your-gmail-password
    ```
## Usage
1. Run the application:

  ```shell
  python app.py
  ```

2. Access the application in your web browser at http://localhost:5000.

3. Fill out the form with the product URL, desired discount price, and your email address.

4. Submit the form.

5. The application will periodically check the product price and send an email notification if the price drops below the specified level.

### Technologies Used
- Python
- Flask
- BeautifulSoup
- TinyDB
- Requests
- smtplib
