import csv
from pathlib import Path


def read_employees(filename: str) -> list[dict[str, str]]:
    """Читает сотрудников из CSV с разделителем ';'."""
    with Path(filename).expanduser().open(
        encoding='utf-8-sig', newline=''
    ) as file:
        return list(csv.DictReader(file, delimiter=';'))


def print_hierarchy(employees: list[dict[str, str]]) -> None:
    """Выводит департаменты и команды без повторений."""
    departments: dict[str, set[str]] = {}
    for employee in employees:
        department = employee['Департамент']
        departments.setdefault(department, set()).add(employee['Отдел'])

    for department, teams in sorted(departments.items()):
        print(department)
        for team in sorted(teams):
            print(f'  - {team}')


def make_summary(employees: list[dict[str, str]]) -> list[dict[str, str]]:
    """Считает численность и зарплаты по департаментам."""
    salaries: dict[str, list[int]] = {}
    for employee in employees:
        department = employee['Департамент']
        salaries.setdefault(department, []).append(int(employee['Оклад']))

    report = []
    for department, values in sorted(salaries.items()):
        report.append({
            'Департамент': department,
            'Численность': str(len(values)),
            'Мин. зарплата': str(min(values)),
            'Макс. зарплата': str(max(values)),
            'Средняя зарплата': f'{sum(values) / len(values):.2f}',
        })
    return report


def print_summary(report: list[dict[str, str]]) -> None:
    """Выводит численность, вилку и среднюю зарплату."""
    for row in report:
        print(f"{row['Департамент']}: {row['Численность']} чел., "
              f"зарплата {row['Мин. зарплата']} – {row['Макс. зарплата']}, "
              f"средняя {row['Средняя зарплата']}")


def save_summary(report: list[dict[str, str]], filename: str) -> None:
    """Сохраняет сводку в новый CSV-файл."""
    fields = [
        'Департамент', 'Численность', 'Мин. зарплата',
        'Макс. зарплата', 'Средняя зарплата',
    ]
    with Path(filename).expanduser().open(
        'x', encoding='utf-8-sig', newline=''
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fields, delimiter=';')
        writer.writeheader()
        writer.writerows(report)


def main() -> None:
    """Показывает меню и выполняет выбранную команду."""
    print('1. Вывести иерархию команд')
    print('2. Вывести сводный отчёт по департаментам')
    print('3. Сохранить сводный отчёт в CSV')
    choice = input('Выберите пункт: ').strip()
    if choice not in ('1', '2', '3'):
        print('Нужно ввести 1, 2 или 3.')
        return

    filename = input('Путь к CSV [Corp_Summary.csv]: ').strip()
    try:
        employees = read_employees(filename or 'Corp_Summary.csv')
        if not employees:
            print('В файле нет сотрудников.')
            return
        if choice == '1':
            print_hierarchy(employees)
        elif choice == '2':
            print_summary(make_summary(employees))
        else:
            output = input(
                'Путь для сохранения [department_summary.csv]: '
            ).strip() or 'department_summary.csv'
            save_summary(make_summary(employees), output)
            print(f'Отчёт сохранён: {output}')
    except FileExistsError:
        print('Файл уже существует. Укажите другое имя для отчёта.')
    except (OSError, ValueError, KeyError, csv.Error) as error:
        print(f'Не удалось обработать отчёт: {error}')


if __name__ == '__main__':
    main()
