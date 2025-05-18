from datetime import datetime


def checkChanges(historyTable):
    """Legacy function - prints all changes data."""
    changesTable = historyTable[4]
    changesTrs = changesTable.find_all("tr")

    for tr in changesTrs:
        changesTds = tr.find_all("td")
        chData = [td.get_text(strip=True) for td in changesTds]
        print(chData)


def isMadeItInTime(lastMod, deadline):
    """Check if the task was completed before the deadline."""
    last_changed = datetime.strptime(lastMod, "%Y-%m-%d %H:%M:%S.%f")
    deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S.%f")

    if last_changed < deadline:
        return True
    else:
        return False


def checkErrors(historyTable):
    """Legacy function - checks for errors in the history table."""
    needTabled = historyTable[4]
    trs = needTabled.find_all("tr")

    for tr in trs:
        tds = tr.find_all("td")
        data = [td.get_text(strip=True) for td in tds]
        if len(data) > 2 and data[2] == '2':
            print("Error!")
        else:
            print("No error!")


def analyzeStatusSequence(historyTable):
    """
    Analyze the sequence of statuses and return appropriate conclusion text.
    """
    changesTable = historyTable[4]
    changesTrs = changesTable.find_all("tr")
    
    # Extract all statuses in chronological order (skip header row)
    statuses = []
    for tr in changesTrs[1:]:  # Skip header row
        changesTds = tr.find_all("td")
        if len(changesTds) > 6:  # Make sure we have enough columns
            status = changesTds[6].get_text(strip=True)  # newStatus column
            if status:  # Only add non-empty statuses
                statuses.append(status)
    
    if not statuses:
        return "Нет данных о статусах"
    
    # Get the last status
    last_status = statuses[-1]
    
    # Count occurrences of each status type
    accepted_count = statuses.count('ACCEPTED')
    launched_count = statuses.count('LAUNCHED')
    
    # Check for priority statuses (STARTED, FINISHED, READY, HANDED, CANCELED)
    # These override all previous logic
    priority_statuses = ['STARTED', 'FINISHED', 'READY', 'HANDED', 'CANCELED']
    
    # If any priority status is present, use that logic
    for status in reversed(statuses):  # Check from last to first
        if status in priority_statuses:
            if status == 'STARTED':
                return "ГУ на исполнении. Рассмотреть на стороне ГО."
            elif status in ['FINISHED', 'READY', 'HANDED']:
                return "ГУ оказана несвоевременно. Рассмотреть на стороне ГО."
            elif status == 'CANCELED':
                return "ГУ отменена."
            break
    
    # Logic for ACCEPTED and LAUNCHED statuses only
    # (only applies if no priority statuses were found)
    
    # Case: Only one ACCEPTED status
    if accepted_count == 1 and launched_count == 0:
        return "ГУ принята от заявителя. Рассмотреть на стороне ГО."
    
    # Case: Two consecutive ACCEPTED statuses with no LAUNCHED
    elif accepted_count == 2 and launched_count == 0:
        return "Оператор цон не провел через накопитель Б"
    
    # Case: Two ACCEPTED and one LAUNCHED afterwards
    elif accepted_count == 2 and launched_count == 1:
        return "ГУ на исполнении. Рассмотреть на стороне ГО"
    
    # Case: One ACCEPTED and one LAUNCHED
    elif accepted_count == 1 and launched_count == 1:
        return "Рассмотреть на SHEP"
    
    # Default case for other combinations
    else:
        return f"Неопределенная последовательность статусов: {' -> '.join(statuses)}"


def printStatusHistory(historyTable):
    """
    Print the status history for debugging purposes.
    """
    changesTable = historyTable[4]
    changesTrs = changesTable.find_all("tr")
    
    print("=== История статусов ===")
    for i, tr in enumerate(changesTrs):
        changesTds = tr.find_all("td")
        if len(changesTds) > 6:
            date = changesTds[2].get_text(strip=True) if len(changesTds) > 2 else "N/A"
            old_status = changesTds[7].get_text(strip=True) if len(changesTds) > 7 else "N/A"
            new_status = changesTds[6].get_text(strip=True) if len(changesTds) > 6 else "N/A"
            
            if i == 0:  # Header row
                print(f"{'#':<3} {'Дата':<25} {'Старый статус':<15} {'Новый статус':<15}")
                print("-" * 65)
            else:
                print(f"{i:<3} {date:<25} {old_status:<15} {new_status:<15}")
    print("=" * 65)