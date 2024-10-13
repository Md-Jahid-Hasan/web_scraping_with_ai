# Web Scraper and Parser

This project is a web scraper and parser built using Python, Flask, and Playwright. It allows users to scrape content from a specified URL and parse the content based on user-defined prompts.

## Features

- Asynchronous web scraping using Playwright.
- Content parsing using BeautifulSoup.
- Flask-based web server with CORS support.
- Frontend form to input URL and parsing instructions.
- Display scraped and parsed content on the frontend.

## Prerequisites

- Python 3.7+
- Node.js (for Playwright)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Md-Jahid-Hasan/web-scraper-parser.git
   cd web-scraper-parser
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Install Playwright and its dependencies:
   ```sh
   playwright install
   ```

## Usage

1. Run the Flask server:
   ```sh
   python web_server.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Enter the URL you want to scrape and submit the form.

4. Enter the parsing instructions and submit the form to parse the scraped content.

## Project Structure

- `web_server.py`: Flask server handling routes for scraping and parsing.
- `scraper.py`: Contains functions for scraping and cleaning content.
- `parser.py`: Contains functions for parsing content based on user prompts.
- `templates/index.html`: Frontend HTML template.

## Example

1. Enter a URL to scrape:
   ```
   https://www.example.com
   ```

2. Enter a parsing instruction:
   ```
   Can you please collect all of the relevant property information and organize it in a table?
   ```

3. View the parsed content displayed on the webpage.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
