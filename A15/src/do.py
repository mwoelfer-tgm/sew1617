from engines import  *
import engines
import argparse
import os
import sys


def classes_in_module(module):
    """
    Gets all the classes defined in a module

    Important: Doesn't return classes that are inherited for example: ABCMETA, ZipError .....

    It also works to instantiate a member of this array which gets returned

    src: http://stackoverflow.com/questions/5520580/how-do-you-get-all-classes-defined-in-a-module-but-not-imported

    :param module: The module which gets searched through

    :return: list with all classes in module
    """
    md = module.__dict__
    return [
        md[c] for c in md if (
            isinstance(md[c], type) and md[c].__module__ == module.__name__
        )
    ]

def get_args():
    """
    :return: parsed arguments
    """
    # initialize Argumentparser with fitting description
    parser = argparse.ArgumentParser(
        description='This program uses various engines for archiving data. Engines may be added to engines module and can already be used')
    # add arguments with default values
    parser.add_argument("-d", "--dest-dir", help="Output destination directory (default=Current Working Directory)",
                        default=".")
    parser.add_argument("-s", "--source-dir", help="Input root directory (default=Current Working Directory)",
                        default=".")
    parser.add_argument("-a", "--archive-engine", help="use the given archive engine. "
                                                       "Possibilities: " + str(list_classes),
                        default="ZIP_STORED")
    parser.add_argument("-n", "--archive-name", help="name of the archive (default=archive)",
                        default="archive")
    # parse arguments
    return parser.parse_args()

if __name__ == '__main__':
    # get all classes
    list_classes = classes_in_module(engines)
    # get the name of each object in this class in order to display them
    for i in range(0,len(list_classes)):
        # parse the class names into fitting names for choosing the engine
        # idea from Filip Scopulovic
         list_classes[i] = (list_classes[i].__name__[:3] + "_" + list_classes[i].__name__[3:]).upper()

    # get args namespace
    args = get_args()
    # check if the destination directory exists
    if not os.path.exists(args.dest_dir):
        print(args.dest_dir + " is not a valid destination directory!")
        sys.exit(0)
    # check if source directory exists
    if not os.path.exists(args.source_dir):
        print(args.source_dir + " is not a valid source directory!")
        sys.exit(0)
    # check if engine exists
    for i in range(0,len(list_classes)):
        if args.archive_engine == list_classes[i]:
            # if it exists, start engine, set filelist and write
            engine = classes_in_module(engines)[i](args.archive_name, args.dest_dir)
            engine.set_filelist(args.source_dir)
            engine.write()
            print(engine.filename + " was successfully created from "
                + args.source_dir + " with " + args.archive_engine)
            sys.exit(0)

    # print out message if it doesn't
    print(args.archive_engine + " is not a valid compression engine!")
    print("Valid Engines are: " + str(list_classes))
    sys.exit(0)