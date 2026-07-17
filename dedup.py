"""Remove the duplicate tail exponent table"""

with open('paper.tex', 'r', encoding='utf-8') as f:
    content = f.read()

begin_marker = '\\begin{table}[H]\n  \\centering\n  \\caption{Stretched-exponential tail exponents'
pos1 = content.find(begin_marker)
pos2 = content.find(begin_marker, pos1 + 1)
print(f'First table at: {pos1}')
print(f'Second table at: {pos2}')

if pos2 != -1:
    # Find where the second table's paragraph ends
    para_end_str = 'moderate inelasticity.\n\n'
    para_end_pos = content.find(para_end_str, pos2)
    if para_end_pos != -1:
        remove_end = para_end_pos + len(para_end_str)
    else:
        # Fallback: just remove to end of \end{table}
        remove_end = content.find('\\end{table}', pos2) + len('\\end{table}') + 2
    
    new_content = content[:pos2] + content[remove_end:]
    with open('paper.tex', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    # Verify
    with open('paper.tex', 'r', encoding='utf-8') as f:
        c2 = f.read()
    count_after = c2.count('tab:tail_exponents')
    print(f'Done. tab:tail_exponents count: {count_after}')
else:
    print('No duplicate found.')
