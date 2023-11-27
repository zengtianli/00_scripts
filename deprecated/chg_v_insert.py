import csv
import sys
import os


def load_chainage_virtual_data(chainage_file):
    chainage_virtual_data = {}
    with open(chainage_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过标题行
        for row in reader:
            if row[0] == 'null' and float(row[3]) == 0.0:
                # branch -> (chainage_n, chainage_v)
                chainage_virtual_data[row[1]] = (row[2], row[3])
    return chainage_virtual_data


def insert_virtual_chainage(section_file, chainage_virtual_data, output_dir, prefix):
    with open(section_file, mode='r', encoding='utf-8') as file:
        reader = list(csv.reader(file))

    output_data = []
    for branch, chainage_info in chainage_virtual_data.items():
        virtual_row = ["断面名称,虚拟断面开头", branch,
                       chainage_info[0], chainage_info[1]]
        output_data.append(virtual_row)

    output_data.extend(reader)

    output_file = os.path.join(output_dir, f"{prefix}_{branch}_inserted.csv")
    with open(output_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(output_data)


def main():
    if len(sys.argv) != 2:
        print("Usage: python chg_v_insert.py <section_file>")
        sys.exit(1)

    section_file = sys.argv[1]
    chainage_file = os.path.join(
        '../chg_files', os.path.basename(section_file).replace('.csv', '_chg.csv'))
    output_dir = '../inserted_files'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    prefix = os.path.basename(section_file).split('_')[0]

    chainage_virtual_data = load_chainage_virtual_data(chainage_file)
    insert_virtual_chainage(
        section_file, chainage_virtual_data, output_dir, prefix)
    print(f"Processed file with virtual chainages: {section_file}")


if __name__ == "__main__":
    main()
