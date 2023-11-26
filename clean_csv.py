import csv
import sys
import os


def clean_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        # 初始化标志变量
        start_processing = False
        cleaned_data = []

        for row in reader:
            if "断面名称" in row:
                start_processing = True  # 从第一个“断面名称”行开始处理
            if start_processing:
                cleaned_data.append(row)

    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_data)


def main():
    if len(sys.argv) != 2:
        print("Usage: python chg_insert.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    # output dir is ../inst_cle_files. if not exist, create it.
    output_dir = os.path.join(os.path.dirname(
        input_file), '../inst_cle_files')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    output_file = os.path.join(output_dir, os.path.basename(input_file))
    clean_csv(input_file, output_file)
    print(f"Cleaned data saved to: {output_file}")


if __name__ == "__main__":
    main()
