from git_machete import cmd
from pyannotate_runtime import collect_types
import os

DEBUG = True
json_name = 'type_info.json'
file_dir = os.path.dirname(os.path.abspath(__file__))

def del_json():
    os.remove(json_name)


def create_types():
    os.system('pyannotate -w ./git_machete/cmd.py')

def main():

    collect_types.init_types_collection()
    with collect_types.collect():
        os.chdir('/home/maciej/Desktop/REPO')
        cmd.launch(['status'])
        cmd.launch(['file'])
        cmd.launch(['format'])
        cmd.launch(['help'])
        os.system('rm -f .git/machete')
        cmd.launch(['add', '--yes'])
        cmd.launch(['anno'])
        cmd.launch(['discover', '--yes'])
        # # cmd.launch(['e'])
        cmd.launch(['delete-unmanaged'])
        cmd.launch(['g','f'])
        cmd.launch(['list','managed'])
        cmd.launch(['show','f'])
        # # # cmd.launch(['d'])
        cmd.launch(['fork-point'])
        # # # cmd.launch(['l'])
        cmd.launch(['traverse'])
        # # # cmd.launch(['update'])
    os.chdir(file_dir)
    collect_types.dump_stats(json_name)

    if DEBUG == True:
        if os.path.exists(json_name):
            print('dziala!!)
            # del_json()
        else:
            print(':C')
    else:
        create_types()
        print('Fajno')




if __name__ == "__main__":
    main()