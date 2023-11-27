import csv
import os
import glob


def load_virtual_chainage_data(chainage_file):
    chainage_data = {}
    with open(chainage_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 4 and row[0] == 'null' and row[3] != '0.000':
                # key: branch, value: chainage value
                chainage_data[row[1].strip()] = row[3].strip()
    return chainage_data


def insert_virtual_end_section(input_file, output_dir, chainage_data):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    last_section_end = None
    for i in range(len(lines)-1, -1, -1):
        if lines[i].strip() == "*******************************":
            last_section_end = i
            break

    if last_section_end is None:
        print(f"未找到{input_file}中的最后一个断面的结束位置。")
        return

    # 获取文件名对应的branch
    branch = os.path.basename(input_file).split('_')[0]
    virtual_chainage = chainage_data.get(branch, "0.000")

    # 复制最后一个断面并修改chainage值
    virtual_section = lines[last_section_end+1:]
    if len(virtual_section) > 3:  # 确保virtual_section的长度至少为4
        virtual_section[2] = f"             {virtual_chainage}\n"
    else:
        print(f"{input_file}中的最后一个断面格式不符合预期。")
        return

    # 在文件末尾添加虚拟断面
    modified_content = lines + virtual_section

    output_file = os.path.join(output_dir, os.path.basename(input_file))
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(modified_content)
    print(f"文件已处理并保存为：{output_file}")

def process_directory(input_dir, output_dir, chainage_file):
    chainage_data = load_virtual_chainage_data(chainage_file)

    for input_file in glob.glob(os.path.join(input_dir, '*.txt')):
        insert_virtual_end_section(input_file, output_dir, chainage_data)


def main():
    input_dir = "../txt_files"
    output_dir = "../txt_end_files"
    chainage_file = "../all_end_virtuals.csv"

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    process_directory(input_dir, output_dir, chainage_file)


if __name__ == "__main__":
    main()

