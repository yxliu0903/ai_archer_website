#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to replace summary fields in models_output_processed.json 
with summaries from models_output_processed_summary.json based on index matching
"""

import json
import sys
import os

def replace_summaries():
    # 文件路径
    summary_file = '/mnt/iem-nas/home/liuyixiu/ai_archer_website/models_output_processed_summary.json'
    target_file = '/mnt/iem-nas/home/liuyixiu/ai_archer_website/models_output_processed.json'
    backup_file = target_file + '.backup'
    
    print(f"正在处理文件...")
    print(f"Summary文件: {summary_file}")
    print(f"目标文件: {target_file}")
    
    # 检查文件是否存在
    if not os.path.exists(summary_file):
        print(f"错误: Summary文件不存在: {summary_file}")
        return False
        
    if not os.path.exists(target_file):
        print(f"错误: 目标文件不存在: {target_file}")
        return False
    
    try:
        # 读取summary文件
        print("正在读取summary文件...")
        with open(summary_file, 'r', encoding='utf-8') as f:
            summary_data = json.load(f)
        
        # 读取目标文件
        print("正在读取目标文件...")
        with open(target_file, 'r', encoding='utf-8') as f:
            target_data = json.load(f)
        
        print(f"Summary文件包含 {len(summary_data)} 个条目")
        print(f"目标文件包含 {len(target_data)} 个条目")
        
        # 创建备份
        print("正在创建备份...")
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(target_data, f, indent=2, ensure_ascii=False)
        print(f"备份已创建: {backup_file}")
        
        # 创建summary的映射字典，用index作为键
        summary_map = {}
        for item in summary_data:
            if 'index' in item and 'summary' in item:
                index = item['index']
                summary_map[index] = item['summary']
        
        print(f"从summary文件中找到 {len(summary_map)} 个有效的index-summary映射")
        
        # 创建目标文件的index映射
        target_index_map = {}
        for i, item in enumerate(target_data):
            if 'index' in item:
                index = item['index']
                target_index_map[index] = i
        
        print(f"从目标文件中找到 {len(target_index_map)} 个有效的index")
        
        # 替换目标文件中对应index的summary
        replaced_count = 0
        skipped_count = 0
        not_found_count = 0
        
        for index, summary in summary_map.items():
            if index in target_index_map:
                # 找到对应的目标文件条目
                target_index_pos = target_index_map[index]
                target_item = target_data[target_index_pos]
                
                old_summary = target_item.get('summary', 'N/A')
                
                if old_summary != summary:
                    target_item['summary'] = summary
                    replaced_count += 1
                    print(f"索引 {index}: 已替换summary")
                    # 打印前100个字符用于确认
                    print(f"  新summary预览: {summary[:100]}...")
                else:
                    skipped_count += 1
                    print(f"索引 {index}: summary相同，跳过")
            else:
                not_found_count += 1
                print(f"索引 {index}: 在目标文件中未找到对应的index")
        
        print(f"\n处理结果:")
        print(f"- 总共替换了 {replaced_count} 个summary")
        print(f"- 跳过了 {skipped_count} 个相同的summary")
        print(f"- 有 {not_found_count} 个索引在目标文件中未找到")
        
        # 写入更新后的数据
        print("正在保存更新后的文件...")
        with open(target_file, 'w', encoding='utf-8') as f:
            json.dump(target_data, f, indent=2, ensure_ascii=False)
        
        print("完成！文件已更新。")
        print(f"如果需要恢复，可以使用备份文件: {backup_file}")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return False
    except Exception as e:
        print(f"发生错误: {e}")
        return False

if __name__ == "__main__":
    success = replace_summaries()
    sys.exit(0 if success else 1) 