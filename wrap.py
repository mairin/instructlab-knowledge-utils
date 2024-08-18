import textwrap
import sys
import os

def wrap_text(input_file, width=72):
    with open(input_file, 'r') as file:
        content = file.read()
    
    wrapped_lines = []
    paragraphs = content.split('\n')

    for paragraph in paragraphs:
        if paragraph.strip():
            wrapped_paragraph = textwrap.fill(paragraph, width=width)
            wrapped_lines.append(wrapped_paragraph)

    wrapped_content = '\n\n'.join(wrapped_lines)
    
    os.rename(input_file, f"{input_file}.old")
    output_file = input_file
    with open(output_file, 'w') as file:
        file.write(wrapped_content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("python3 wrap.py <input_file>")
        sys.exit(1)

    for input_file in sys.argv[1:]:
        wrap_text(input_file)
