from textnode import *
import os
import shutil



def main():
    #new_obj = TextNode("fuck", TextType.BOLD, "meinthe.ass")
    #print(new_obj)
    src = "./static"
    dst = "./public"
    print("Deleting public directory...")
    if os.path.exists(dst):
        shutil.rmtree(dst)

    print("Copying static files to public directory...")
    copy_content(src, dst)
    
    
    
    
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
    
    
main()