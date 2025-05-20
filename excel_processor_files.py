import pandas as pd
import os
from bs4 import BeautifulSoup
import helpers

def load_html_file(file_path):
    """
    Load HTML content from a file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Ошибка чтения файла {file_path}: {e}")
        return None

def analyze_application_from_html(html_content):
    """
    Analyze HTML content and return conclusion based on status sequence.
    """
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        historyTable = soup.find_all("table")
        
        if len(historyTable) < 5:
            return "Ошибка: недостаточно таблиц в HTML"
        
        # Get the conclusion using our status analysis
        conclusion = helpers.analyzeStatusSequence(historyTable)
        return conclusion
        
    except Exception as e:
        return f"Ошибка анализа: {str(e)}"

def find_html_file_for_id(app_id, html_folder='htmls'):
    """
    Find HTML file for given application ID in the htmls folder.
    Searches for files named: {app_id}.html, app_{app_id}.html, or containing the ID.
    """
    if not os.path.exists(html_folder):
        return None
    
    # Convert app_id to string for consistency
    app_id_str = str(app_id).strip()
    
    # Possible filename patterns
    possible_names = [
        f"{app_id_str}.html",
        f"app_{app_id_str}.html",
        f"{app_id_str}_data.html",
        f"application_{app_id_str}.html"
    ]
    
    # First, try exact matches
    for filename in possible_names:
        file_path = os.path.join(html_folder, filename)
        if os.path.exists(file_path):
            return file_path
    
    # If no exact match, search for files containing the ID
    try:
        for filename in os.listdir(html_folder):
            if filename.endswith('.html') and app_id_str in filename:
                return os.path.join(html_folder, filename)
    except Exception as e:
        print(f"Ошибка поиска файлов в папке {html_folder}: {e}")
    
    return None

def process_excel_with_preloaded_files(excel_file_path, html_folder='htmls', output_file_path=None):
    """
    Process Excel file using preloaded HTML files from the specified folder.
    """
    # Read Excel file
    try:
        df = pd.read_excel(excel_file_path, engine='openpyxl')
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return
    
    # Find the required columns
    identifier_col = None
    comment_col = None
    
    for col in df.columns:
        if 'Идентификатор заявки' in str(col) or 'Идентификатор' in str(col):
            identifier_col = col
        elif 'Комментарий АО НИТ' in str(col):
            comment_col = col
    
    if identifier_col is None:
        print("Ошибка: не найден столбец с идентификатором заявки")
        print("Доступные столбцы:", df.columns.tolist())
        return
    
    if comment_col is None:
        print("Предупреждение: не найден столбец 'Комментарий АО НИТ', создаем новый")
        comment_col = 'Комментарий АО НИТ'
        df[comment_col] = ''
    
    print(f"Найден столбец идентификатора: {identifier_col}")
    print(f"Найден столбец комментариев: {comment_col}")
    print(f"Папка с HTML файлами: {html_folder}")
    print(f"Всего строк для обработки: {len(df)}")
    
    # Check if HTML folder exists
    if not os.path.exists(html_folder):
        print(f"Ошибка: папка {html_folder} не найдена")
        return
    
    # List available HTML files for reference
    try:
        html_files = [f for f in os.listdir(html_folder) if f.endswith('.html')]
        print(f"Найдено HTML файлов: {len(html_files)}")
    except Exception as e:
        print(f"Ошибка чтения папки {html_folder}: {e}")
        return
    
    # Process each row
    successful_count = 0
    not_found_count = 0
    error_count = 0
    
    for index, row in df.iterrows():
        app_id = row[identifier_col]
        
        # Skip if ID is empty or NaN
        if pd.isna(app_id) or str(app_id).strip() == '':
            continue
        
        # Convert to string and clean up
        app_id = str(app_id).strip()
        
        print(f"\\n[{index + 1}/{len(df)}] Обработка заявки ID: {app_id}")
        
        # Find HTML file for this ID
        html_file_path = find_html_file_for_id(app_id, html_folder)
        
        if html_file_path:
            print(f"Найден файл: {os.path.basename(html_file_path)}")
            
            # Load HTML content
            html_content = load_html_file(html_file_path)
            
            if html_content:
                # Analyze the HTML and get conclusion
                conclusion = analyze_application_from_html(html_content)
                df.at[index, comment_col] = conclusion
                successful_count += 1
                print(f"✓ Успешно: {conclusion}")
            else:
                df.at[index, comment_col] = "Ошибка: не удалось прочитать HTML файл"
                error_count += 1
                print("✗ Ошибка чтения файла")
        else:
            df.at[index, comment_col] = "HTML файл не найден"
            not_found_count += 1
            print("✗ HTML файл не найден")
    
    # Save results
    if output_file_path is None:
        output_file_path = excel_file_path.replace('.xlsx', '_processed_from_files.xlsx')
    
    try:
        df.to_excel(output_file_path, index=False, engine='openpyxl')
        print(f"\\n=== РЕЗУЛЬТАТЫ ===")
        print(f"Успешно обработано: {successful_count}")
        print(f"HTML файлов не найдено: {not_found_count}")
        print(f"Ошибок обработки: {error_count}")
        print(f"Результаты сохранены в: {output_file_path}")
    except Exception as e:
        print(f"Ошибка сохранения файла: {e}")

def main():
    excel_file = "Павлодарская область_Апрель_75.xlsx"
    html_folder = "htmls"  # Folder containing preloaded HTML files
    output_file = "Павлодарская область_Апрель_75_processed3_from_files.xlsx"
    
    print("=== ОБРАБОТКА EXCEL С ПРЕДЗАГРУЖЕННЫМИ HTML ФАЙЛАМИ ===")
    process_excel_with_preloaded_files(excel_file, html_folder, output_file)

if __name__ == "__main__":
    main()