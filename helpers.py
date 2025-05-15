from datetime import datetime


def checkChanges(historyTable):
    changesTable = historyTable[4]
    changesTrs = changesTable.find_all("tr")

    for tr in changesTrs:
        changesTds = tr.find_all("td")
        chData = [td.get_text(strip=True) for td in changesTds]
        print(chData)


def isMadeItInTime(lastMod, deadline):
    last_changed = datetime.strptime(lastMod, "%Y-%m-%d %H:%M:%S.%f")
    deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S.%f")

    if last_changed < deadline:
        return True
    else:
        return False


def checkErrors(historyTable):
    needTabled = historyTable[4]
    trs = needTabled.find_all("tr")

    for tr in trs:
        tds = tr.find_all("td")
        data = [td.get_text(strip=True) for td in tds]
        if data[2] == '2':
            print("Error!")
        print("No error!")
