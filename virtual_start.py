import sys
import os


def insert_virtual_section(input_file, output_dir):
    # 读取原始文件内容
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # 寻找第一个断面的结束位置
    first_section_end = None
    for i, line in enumerate(lines):
        if line.strip() == "*******************************":
            first_section_end = i
            break
    if first_section_end is None:
        print("未找到第一个断面的结束标记。")
        return
    # 复制第一个断面并修改chainage值
    virtual_section = lines[:first_section_end + 1]
    virtual_section[2] = "             0.000\n"  # 修改chainage值
    # 插入虚拟断面到文件开始处
    modified_content = virtual_section + lines
    # 构建输出文件路径
    output_file = os.path.join(output_dir, os.path.basename(
        input_file).replace('.txt', '_v.txt'))
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    # 保存修改后的文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(modified_content)
    print(f"文件已处理并保存为：{output_file}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python chg_v_insert.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_dir = "../txt_v_files"
    # if output_dir not exit create
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    insert_virtual_section(input_file, output_dir)


if __name__ == "__main__":
    main()
