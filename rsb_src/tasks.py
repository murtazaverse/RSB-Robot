from robocorp.tasks import task
from robocorp import browser
from RPA.HTTP import HTTP
from RPA.Excel.Files import Files
from RPA.PDF import PDF
from dotenv import load_dotenv

import os
import logging

load_dotenv()
logging.basicConfig(
    filename="errors.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
@task
def robot_spare_bin_python():
    """Insert the sales data for the week and export it as a PDF"""
    browser.configure(
        # slowmo=100,
    )
    try:
        open_the_intranet_website()
        log_in()
        download_excel_file()
        fill_form_with_excel_data()
        collect_results()
        export_as_pdf()
        log_out()
    except Exception as e:
        logging.error(f"Error in Pipeline: {e}")
    else:
        logging.info("Pipeline complete")

def open_the_intranet_website():
    """Navigates to the given URL"""
    browser.goto("https://robotsparebinindustries.com/")

def log_in():
    """Fills in the login form and clicks the 'Log in' button"""
    page = browser.page()
    page.fill("#username", os.getenv('LOGIN_USERNAME'))
    page.fill("#password", os.getenv('LOGIN_PASSWORD'))
    page.click("button:text('Log in')")

def fill_and_submit_sales_form(sales_rep):
    """Fills in the sales data and click the 'Submit' button"""
    try:
        page = browser.page()

        page.fill("#firstname", sales_rep["First Name"])
        page.fill("#lastname", sales_rep["Last Name"])
        page.select_option("#salestarget", str(sales_rep["Sales Target"]))
        page.fill("#salesresult", str(sales_rep["Sales"]))
        page.click("text=Submit")
    except Exception as e:
        logging.error(f"Error in Form Submission: {e}")
        logging.error(f"Error Details:\n First Name:{sales_rep["First Name"]}\n Last Name:{sales_rep["Last Name"]} ")

def download_excel_file():
    """Downloads excel file from the given URL"""
    try:
        http = HTTP()
        http.download(url="https://robotsparebinindustries.com/SalesData.xlsx", overwrite=True)
    except Exception as e:
        logging.error(f"Error in Downloading Excel Sheet: {e}")
    else:
        logging.info("Excel Sheet downloaded")
        

def fill_form_with_excel_data():
    """Read data from excel and fill in the sales form"""
    try:
        excel = Files()
        excel.open_workbook("SalesData.xlsx")
        worksheet = excel.read_worksheet_as_table("data", header=True)
        excel.close_workbook()

        for row in worksheet:
            fill_and_submit_sales_form(row)
    except Exception as e:
        logging.error(f"Error in Filling Excel Sheet: {e}")
    else:
        logging.info("Excel Sheet Filled")

        
def collect_results():
    """Take a screenshot of the page"""
    page = browser.page()
    page.screenshot(path="output/sales_summary.png")
    logging.info("Results Collected")

def export_as_pdf():
    """Export the data to a pdf file"""
    try:
        page = browser.page()
        sales_results_html = page.locator("#sales-results").inner_html()

        pdf = PDF()
        pdf.html_to_pdf(sales_results_html, "output/sales_results.pdf")
    except Exception as e:
        logging.error(f"Error in Exporting PDF: {e}")
    else:
        logging.info("PDF Exported")
    
def log_out():
    """Presses the 'Log out' button"""
    page = browser.page()
    page.click("text=Log out")