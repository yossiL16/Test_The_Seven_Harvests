import csv
from object.soldier import Soldier


def load_soldiers_from_csv(filename = "../hayal_300_no_status.csv") -> list[Soldier]:

    data = []
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_solider = Soldier(
                personal_number=int(row['מספר אישי']),
                f_name=row['שם פרטי'],
                l_name=row['שם משפחה'],
                gender=row['מין'],
                city=row["עיר מגורים"],
                distance=int(row["מרחק מהבסיס"])
                )
            data.append(new_solider)
    # for i in data:
    #     print(i.to_dict())
    # print(len(data))
    return data


def save_soldiers_to_csv(soldiers:list[Soldier], filename = "../hayal_300_no_status.csv"):

    fieldnames = ['personal_number', 'f_name', 'l_name', 'gender', 'city', 'distance', 'status']

    with open(filename, mode='w', encoding='utf-8', newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for solider in soldiers:
            writer.writerow(solider.to_dict())



# load_soldiers_from_csv()