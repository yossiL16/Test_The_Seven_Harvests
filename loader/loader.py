import csv
from object import soldier
from object.soldier import Soldier


def load_soliders_from_csv(filename = "../hayal_300_no_status.csv") -> list[Soldier]:

    data = []

    with open(filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            n_solider = Soldier(
                personal_number=row['מספר אישי'],
                f_name=row['שם פרטי'],
                l_name=row['שם משפחה'],
                gender=row['מין'],
                city=row["עיר מגורים"],
                distance=row["מרחק מהבסיס"]
                )
            data.append(n_solider)
    for i in data:
        print(i.f_name)
load_soliders_from_csv()