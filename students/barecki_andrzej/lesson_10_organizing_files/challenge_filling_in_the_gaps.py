import os
import datetime
import re

SRC_FOLDER = "source_folder"


def create_example_test_files(path, source_folder_param):
    os.chdir(path)
    print('Current working folder ', os.getcwd() + os.linesep)
    src_dir = ""

    """Create source folder(extend date/time approach)"""
    if source_folder_param is not None:
        if os.path.exists(source_folder_param):
            random_folder = os.path.join(source_folder_param + '_' +
                                         str(datetime.datetime.now().date()) +
                                         '_' + str(datetime.datetime.now().
                                                   time()).replace(':', '.'))
            src_dir = random_folder
        else:
            src_dir = source_folder_param

    """ Create example of few files """
    file_list = [os.path.join(src_dir, "spam002.txt"),
                 os.path.join(src_dir, "spam003.tyt"),
                 os.path.join(src_dir, "spam004.txt"),
                 os.path.join(src_dir, "spam005.jpg"),
                 os.path.join(src_dir, "saam006.txt"),
                 os.path.join(src_dir, "saam007.mp3"),
                 os.path.join(src_dir, "spam007.txt"),
                 ]

    for elem in file_list:
        if not os.path.exists(os.path.dirname(elem)):
            os.makedirs(os.path.dirname(elem))
        with open(elem, "w") as test_file:
            test_file.close()

    return os.path.join(os.getcwd(), src_dir)


def filling_in_the_gap(path):
    spam_regex = re.compile(r'(spam)(\d\d\d)(.txt)')
    init = False
    index = 0

    """search all files from a given directory"""
    for folder_name, _, file_names in os.walk(path):
        for filename in sorted(file_names):
            result = spam_regex.search(filename)
            if result is not None:
                """index initialization """
                if init is False:
                    index = int(result.group(2))
                    init = True
                    print("Initial file:{0}".format(os.path.join(folder_name,
                                                                 filename)))
                    print("Initial index:{0}".format(index) + os.linesep)
                if init is True:
                    while index is not int(result.group(2)):
                        """Generate filename"""
                        new_filename = "spam" + str(index).zfill(3) + ".txt"
                        new_path = os.path.join(folder_name, new_filename)

                        """Generate new gap file"""
                        with open(new_path, "w") as test_file:
                            test_file.close()

                        """Update index"""
                        index = index + 1


def main():
    source_path = create_example_test_files(os.getcwd(), SRC_FOLDER)
    filling_in_the_gap(source_path)
    print(os.linesep + "End program.")


if __name__ == '__main__':
    main()
