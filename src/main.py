from textnode import *
import os
import shutil
from gen_c import copy_content, generate_page


def main():
    #new_obj = TextNode("fuck", TextType.BOLD, "meinthe.ass")
    #print(new_obj)
    src = "./static"
    dst = "./public"
    print("Deleting public directory...")
    if os.path.exists(dst):
        shutil.rmtree(dst)

    #print("Copying static files to public directory...")
    copy_content(src, dst)
    generate_page(os.path.join("./content", "index.md"),
                  "./template.html",
                  os.path.join("./public", "index.html"),
    )

main()