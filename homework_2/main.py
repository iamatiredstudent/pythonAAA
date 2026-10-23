import csv
def read_rabotnik(file):
    rabotnik = []

    with open(file, encoding="utf-8-sig", newline="") as file:
        rows = csv.DictReader(file, delimiter=";")
        for row in rows:
            rabotnik.append(row)
    return rabotnik

def print_hierarchy(rabotnik):
    departamenty = {}

    for employee in rabotnik:
        departament = employee["Департамент"]
        komanda = employee["Отдел"]

        if departament not in departamenty:
            departamenty[departament] = []
        if komanda not in departamenty[departament]:
            departamenty[departament].append(komanda)

    for departament in departamenty:
        print(departament)

        for komanda in departamenty[departament]:
            print("  -", komanda)

def calculate_summary(rabotnik):
    departamenty = {}

    for employee in rabotnik:
        departament = employee["Департамент"]
        zp = float(employee["Оклад"])

        if departament not in departamenty:
            departamenty[departament] = []
        departamenty[departament].append(zp)

    summary = []
    for departament in departamenty:
        zarplata = departamenty[departament]

        row = {
            "Департамент": departament,
            "Количество": len(zarplata),
            "Минимум": min(zarplata),
            "Максимум":  max(zarplata),
            "Средняя": round(sum(zarplata) / len(zarplata), 2)}
        summary.append(row)
    return summary

def print_summary(summary):
    for row in summary:
        print("Департамент:", row["Департамент"])
        print("Количество сотрудников:", row["Количество"])
        print("Минимальная зарплата:", row["Минимум"])
        print("Максимальная зарплата:", row["Максимум"])
        print("Средняя зарплата:", row["Средняя"])

def save_summary(summary, filename):
    columns = [
        "Департамент",
        "Количество",
        "Минимум",
        "Максимум",
        "Средняя"]

    with open(filename, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=";")
        writer.writeheader()
        writer.writerows(summary)

def main(report_type: int):
    if report_type not in [1, 2, 3]:
        print("Выберите номер представления: 1, 2 или 3")
        return

    rabotnik = read_rabotnik("Corp_Summary.csv")
    if report_type == 1:
        print_hierarchy(rabotnik)
    elif report_type == 2:
        summary = calculate_summary(rabotnik)
        print_summary(summary)
    elif report_type == 3:
        summary = calculate_summary(rabotnik)
        save_summary(summary, "departament_summary.csv")

if __name__ == "__main__":
    main(3)