import os
import shutil
import sys
from subprocess import PIPE, run


PATTERN = "v"
def find_v_files(source):
    file_paths = []
    for root, dirs, files in os.walk(source):
        for docs in files:
            if PATTERN in docs.lower():
                path = os.path.join(source,docs)
                file_paths.append(path)
        break
    return file_paths

def remove_v(paths, to_strip):
    new_paths = []
    for path in paths:
        _,file_name = os.path.split(path)

        new_file_name = file_name.replace(to_strip,".sv")
        new_paths.append(new_file_name)
    return new_paths

def copy_and_override(source, dest):
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copy(source, dest)




def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def main(source, dest):
    cwd = os.getcwd()
    source_path = os.path.join(cwd,source)
    dest_path = os.path.join(cwd, dest)

    all_paths = find_v_files(source_path)
    new_all_paths = remove_v(all_paths, ".v")


    create_dir(dest_path)

    for src,dst in zip(all_paths,new_all_paths):
        destination = os.path.join(dest_path,dst)
        copy_and_override(src,destination)

    
if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("Enter Source Directory")
    source, dest = args[1:]

    main(source, dest)



    ##command line argument: C:\Users\jaswa\Python_Scripting_Challenges\change_v_to_sv>python change_v_to_sv.py Files Newfiles