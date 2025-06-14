#!/usr/bin/env python3
"""
Script to fix indentation issues in Python files by converting all indentation to spaces
"""

def fix_indentation(filename):
    """Fix indentation in a Python file by converting tabs to spaces"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_lines = []
    for line in lines:
        # Replace tabs with 4 spaces
        fixed_line = line.replace('\t', '    ')
        
        # Check for mixed indentation (tabs and spaces)
        if '\t' in line and ' ' in line[:len(line) - len(line.lstrip())]:
            print(f"Warning: Mixed tabs and spaces found in line: {repr(line[:50])}")
        
        fixed_lines.append(fixed_line)
    
    # Write back the fixed content
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    print(f"Fixed indentation in {filename}")
    print("All tabs have been converted to 4 spaces")

if __name__ == "__main__":
    # Fix the content-gap-analyzer.py file
    fix_indentation('content-gap-analyzer.py')
    
    # Additional check for common issues
    print("\nChecking for common syntax issues...")
    
    with open('content-gap-analyzer.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for common issues
    if 'return {"error": f"Error analyzing website: {str(e)}"} Calculate' in content:
        print("ERROR: Found syntax error with 'Calculate word count' appended to return statement")
    
    if content.count('{') != content.count('}'):
        print(f"WARNING: Mismatched braces - { count: {content.count('{')}, } count: {content.count('}')}")
    
    if content.count('(') != content.count(')'):
        print(f"WARNING: Mismatched parentheses - ( count: {content.count('(')}, ) count: {content.count(')')}")
    
    if content.count('[') != content.count(']'):
        print(f"WARNING: Mismatched brackets - [ count: {content.count('[')}, ] count: {content.count(']')}")
    
    print("\nDone! Try running the file again.")
