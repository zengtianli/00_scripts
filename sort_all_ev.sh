#!/bin/bash

# 定义CSV文件的路径
csv_file="../all_end_virtuals.csv"

# 先删除空格，然后对文件进行排序
# -i 表示就地修改文件
# 's/ //g' 用于删除所有空格
# sort 命令用于排序，假设以第一列为排序依据
sed -i '' 's/ //g' "$csv_file" && sort -t, -k1,1 "$csv_file" -o "$csv_file"

