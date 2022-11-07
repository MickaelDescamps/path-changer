import os
import sys
from typing import Optional

def path_changer(sub_level_number: Optional[int] = 1):
    """Function to add the parent directory to the path.

    Args:
        sub_level_number -- number of nested directory in project. Defaults to 1.
    """

    #pylint: disable=redefined-builtin, duplicate-code
    # Get current path without filename
    sys_path = os.path.abspath(__file__).split('/')[:-1]
    # Add project directory to python path
    # Expected our file structure is [...]/project_dir/one_subdir/our_file.py
    sys.path.append('/'.join(sys_path[:-sub_level_number]))
    # Set current package name, whatever the main directory is named
    # package = project_name.sub_dir.file
    for i in range(sub_level_number):
        sys.modules[__name__].__package__ = '.'.join(sys_path[-sub_level_number + i:])