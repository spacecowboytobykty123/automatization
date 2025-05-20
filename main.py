from bs4 import BeautifulSoup
from datetime import datetime
import helpers

def load_html_file(filename):
    """Load HTML content from a file with error handling."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: HTML file '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading HTML file: {e}")
        return None

def main():
    # Load HTML from file
    html_filename = 'htmls/002269369908.html'  # Change this to your HTML file name
    html = load_html_file(html_filename)
    
    if html is None:
        print("Cannot proceed without HTML data.")
        return
    
    soup = BeautifulSoup(html, "html.parser")
    tr_list = soup.find_all('tr')
    historyTable = soup.find_all("table")
    
    # Check if we have enough rows
    if len(tr_list) < 6:
        print("Error: Not enough table rows found in HTML.")
        return
    
    # Get basic information from the main table
    tr = tr_list[3]
    td_list = tr.find_all("td")
    
    # Check if we have enough columns
    if len(td_list) < 10:
        print("Error: Not enough table columns found.")
        return
    
    # Extract main information
    lastModified = td_list[4].text.strip()
    deadline = td_list[8].text.strip()
    status = td_list[9].text.strip()
    
    # Print basic information
    print("=== Основная информация ===")
    print(f"Последнее изменение: {lastModified}")
    print(f"Крайний срок: {deadline}")
    print(f"Текущий статус: {status}")
    print()
    
    # Check if made it in time
    try:
        made_in_time = helpers.isMadeItInTime(lastModified, deadline)
        print(f"Выполнено в срок: {'Да' if made_in_time else 'Нет'}")
    except Exception as e:
        print(f"Ошибка при проверке сроков: {e}")
    print()
    
    # Print detailed status history (for debugging)
    helpers.printStatusHistory(historyTable)
    print()
    
    # Analyze status sequence and get conclusion
    conclusion = helpers.analyzeStatusSequence(historyTable)
    print("=== ЗАКЛЮЧЕНИЕ ===")
    print(conclusion)
    print("=" * 50)

if __name__ == "__main__":
    main()