#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 手动提取主要文本内容进行统计
main_content = """
Flip the Bottle – Play Online Now
Master the flip the bottle game online for free! Learn controls, discover winning strategies, and become a flip the bottle champion with our expert tips.

Ready to flip? Play Now

What Is Flip the Bottle?
Flip the bottle is an addictive skill-based game where you launch a water bottle to make it flip and land upright. This flip the bottle game challenges your timing and precision as you master the perfect arc and rotation. Our browser version lets you play instantly—no downloads needed, just pure flipping fun!

The game physics are realistic: too much power sends your bottle flying, too little won't complete the rotation. Master the technique to chain perfect landings and beat your high score!

How to Play Flip the Bottle
Playing flip the bottle is simple: on desktop, click and hold to charge your throw, then release to flip. On mobile, tap and hold, then lift your finger. The key to mastering the game is balancing power and timing—aim for one smooth rotation and a center landing.

In this flip the bottle game, successful upright landings continue your streak, while falls reset your score. Start with gentle throws to learn the mechanics, then gradually increase power for longer distances.

Essential Flip the Bottle Tips

Master Your Power Control
Start with gentle throws to learn the basics. Find your ideal power level by practicing 5-10 flips on flat surfaces. Consistency is key—keep your mouse press or finger tap timing steady. Small adjustments work better than random power changes in this flip the bottle game.

Aim for One Perfect Rotation
The best flip the bottle technique uses one smooth rotation. Aim for a clean up-and-down arc rather than long horizontal throws. If you under-rotate, add slightly more power; if you over-rotate, reduce power or release earlier. This core skill makes every level easier.

Land in the Center
Always aim for the platform center when you flip the bottle. Edge landings cause bounces and falls. Let your bottle complete its rotation just above the surface for a soft landing. This strategy turns near-misses into perfect scores.

Flip the Bottle FAQ
Is this flip the bottle game free? Yes! Play flip the bottle online completely free with no downloads or purchases required.

Can I play flip the bottle on mobile? Absolutely! This flip the bottle game works perfectly on phones and tablets. Rotate to landscape for the best experience.

Why does my bottle bounce off? Too much power or late release causes bounces. Try gentler throws with more vertical arc.

How do I get better at flip the bottle? Practice consistent power control, aim for one clean rotation, and always target the platform center. These tips will improve your scores quickly!

Quick Start Guide
Click Play to start your bottle flipping adventure
Use gentle power for your first attempts
Aim for center landings to master the flip the bottle game

Why Play Flip the Bottle?
Free bottle flipping game—no downloads needed
Perfect for quick breaks or extended practice
Pure skill-based gameplay with realistic physics

PlayFlipTheBottle.com — Play flip the bottle online for free! Master the flip the bottle game with expert tips and strategies for higher scores.
"""

# 清理文本
text = re.sub(r'\s+', ' ', main_content).strip().lower()
words = text.split()
total_words = len(words)
total_chars = len(text)

# 统计关键词
main_keyword = "flip the bottle"
main_count = len(re.findall(r'\bflip the bottle\b', text))

secondary_keyword = "flip the bottle game"
secondary_count = len(re.findall(r'\bflip the bottle game\b', text))

# 计算密度
main_density = (main_count / total_words) * 100 if total_words > 0 else 0
secondary_density = (secondary_count / total_words) * 100 if total_words > 0 else 0

print("=== 优化后内容分析 ===")
print(f"总词数: {total_words}")
print(f"总字符数: {total_chars}")
print()
print(f"主关键词 '{main_keyword}':")
print(f"  出现次数: {main_count}")
print(f"  密度: {main_density:.2f}%")
print(f"  目标: 3-5%")
print(f"  状态: {'✓ 符合要求' if 3 <= main_density <= 5 else '✗ 需要调整'}")
print()
print(f"次关键词 '{secondary_keyword}':")
print(f"  出现次数: {secondary_count}")
print(f"  密度: {secondary_density:.2f}%")
print(f"  目标: 1-2%")
print(f"  状态: {'✓ 符合要求' if 1 <= secondary_density <= 2 else '✗ 需要调整'}")
print()
print(f"内容长度: {total_chars} 字符")
print(f"目标长度: 600-800 字符")
print(f"状态: {'✓ 符合要求' if 600 <= total_chars <= 800 else '需要调整'}")
