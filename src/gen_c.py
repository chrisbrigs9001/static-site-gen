import shutil
from htmlnode import *
from markdown_blocks import markdown_to_html_node, extract_title
import re
import os


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    pass


def copy_content(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_content(from_path, dest_path)



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    #from_markdown = ""
    #with open(from_path, 'r') as f:
    #    from_markdown = f.read()   
    f = open(from_path, 'r')
    from_markdown = f.read()
    f.close()
    
    #temp_content = ""
    #with open(template_path, 'r') as f:
    #    temp_content = f.read()
    t = open(template_path, 'r')
    temp_content = t.read()
    t.close()
    
    converted_html = markdown_to_html_node(from_markdown).to_html()
    title = extract_title(from_markdown)
    
    #replace {{ Title }} in temp_content
    replaced_content = re.sub(r'{{ Title }}', title, temp_content)
    #replace {{ Content }} in temp_content
    replaced_content = re.sub(r'{{ Content }}', converted_html, replaced_content)
    
    #print(replaced_content)
    #Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    
    #check if path exists, if not create
    
    d_dir_path = os.path.dirname(dest_path)
    if d_dir_path != "":
        os.makedirs(d_dir_path, exist_ok=True)
    j = open (dest_path, 'w')
    j.write(replaced_content)
    
    #write the file
    #with open(dest_path, 'w') as f:
    #    f.write(replaced_content)