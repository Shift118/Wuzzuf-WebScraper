# Wuzzuf Job Scraper 🕷️

This project is a **Wuzzuf Job Scraper** built using **Tkinter** for the GUI and **BeautifulSoup** for web scraping. It allows users to scrape job listings from **Wuzzuf.net** and save them to a CSV file. 
The project was inspired by tutorials from **Python Simplified** (Tkinter and PyInstaller) and **Codezilla** (web scraping and libraries). 

I developed this project independently and even created a **guide video** to help others learn from it. You can also download the **Program Installation EXE** to use the scraper without setting up the code.

---

## What does it do? 🤔

- **Scrapes job listings** from Wuzzuf.net.
- Extracts:
  - **Job Title** 📝
  - **Company Name** 🏢
  - **Location** 🌍
  - **Skills Required** 🛠️
  - **Job Type** (Full Time, Remote, etc.) 🕒
  - **Date Posted** 📅
  - **Job Link** 🔗
- Saves the data into a **CSV file** for easy analysis.

---

## How to use it? 🛠️

### Using the EXE Program
1. Download the **Program Installation EXE** from the repository.
2. Run the executable file.
3. Enter the Wuzzuf link (make sure it's the 2nd page of the job search).
4. Provide a name for the CSV file.
5. Click "Run" to start scraping.
6. The CSV file will be saved in the `Jobs` folder and automatically opened.

### Using the Code
1. **Clone this repo**:
   ```bash
   git clone https://github.com/Shift118/Wuzzuf-Job-Scraper.git
   cd Wuzzuf-Job-Scraper
   
Install the required libraries:
pip install customtkinter requests beautifulsoup4

Run the script:
python app.py

Project Structure
app.py: The main script that handles the GUI and initiates the scraping process.
Wuzzuf_Scrapper.py: Contains the logic for scraping and saving job data.
Jobs/: Folder where the CSV files are saved.

Limitations ⚠️
Wuzzuf Link Requirement: The program requires a link to the 2nd page of the job search results. Links to the 1st page or other pages may not work correctly.
Date Conversion: The "Date" column in the CSV file may need to be manually converted to the correct date format in Excel or other tools.
Job Types: The job type extraction relies on specific keywords (e.g., "Full Time", "Remote"). If Wuzzuf changes their formatting, this may break.
Pagination: The scraper stops when it reaches the end of the job listings, but it may not handle all edge cases perfectly.
File Name: Using space while naming the file will cause the program to not work.

Why did I make this? 🤷‍♂️
This project was inspired by tutorials from Python Simplified (who taught me Tkinter and PyInstaller) and Codezilla (who taught me web scraping and libraries). 
I wanted to create a tool that could automate job scraping and make it easier for others to analyze job market trends. I developed this project independently and even created a guide video to share my knowledge.

Wanna help? 🙏
If you find any issues or have suggestions for improvement, feel free to:
Open an issue
Submit a pull request

Star the repo (if you found it useful! ⭐)

License 📜
This project is licensed under the MIT License. Feel free to use and modify it as you like.
