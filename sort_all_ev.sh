#!/bin/bash

# 定义CSV文件的路径
csv_file="../processed_data/all_end_virtuals.csv"
sed -i '' 's/ //g' "$csv_file" && sort -t, -k1,1 "$csv_file" -o "$csv_file"

