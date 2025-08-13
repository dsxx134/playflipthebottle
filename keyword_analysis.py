#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
关键词密度分析工具
分析 flip the bottle 项目首页的关键词密度
"""

import re

def analyze_keywords(html_file):
    """分析HTML文件中的关键词密度"""

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 简单提取文本内容（移除HTML标签）
    text = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)

    # 清理文本
    text = re.sub(r'\s+', ' ', text).strip().lower()
    
    # 统计总词数（简单按空格分割）
    words = text.split()
    total_words = len(words)
    
    # 统计主关键词 "flip the bottle"
    main_keyword = "flip the bottle"
    main_count = len(re.findall(r'\bflip the bottle\b', text))
    
    # 统计次关键词 "flip the bottle game"  
    secondary_keyword = "flip the bottle game"
    secondary_count = len(re.findall(r'\bflip the bottle game\b', text))
    
    # 计算密度
    main_density = (main_count / total_words) * 100 if total_words > 0 else 0
    secondary_density = (secondary_count / total_words) * 100 if total_words > 0 else 0
    
    print("=== 关键词密度分析报告 ===")
    print(f"总词数: {total_words}")
    print(f"页面字符数（估算）: {len(text)}")
    print()
    print(f"主关键词 '{main_keyword}':")
    print(f"  出现次数: {main_count}")
    print(f"  密度: {main_density:.2f}%")
    print(f"  目标密度: 3-5%")
    print(f"  状态: {'✓ 符合要求' if 3 <= main_density <= 5 else '✗ 需要调整'}")
    print()
    print(f"次关键词 '{secondary_keyword}':")
    print(f"  出现次数: {secondary_count}")
    print(f"  密度: {secondary_density:.2f}%")
    print(f"  目标密度: 1-2%")
    print(f"  状态: {'✓ 符合要求' if 1 <= secondary_density <= 2 else '✗ 需要调整'}")
    print()
    
    # 内容长度分析
    content_length = len(text)
    print(f"内容长度分析:")
    print(f"  当前长度: {content_length} 字符")
    print(f"  目标长度: 600-800 字符")
    print(f"  状态: {'✓ 符合要求' if 600 <= content_length <= 800 else '✗ 需要调整'}")

if __name__ == "__main__":
    analyze_keywords("index.html")
