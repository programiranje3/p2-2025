"""Utility functions of the package music.
"""


#%%
# Setup / Data

from datetime import date
from pathlib import Path

from settings import *


#%%
def format_date(a_date):
    """Converts a date from datetime.date() to a string of the form '<month> <day>, <year>'.
    Uses strftime() method of datetime.date class and its pre-defined format codes from
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    """

    return a_date.strftime(PREFERRED_DATE_FORMAT) if isinstance(a_date, date) else a_date


#%%
# Test format_date(a_date)
print(format_date(date(2025, 1, 1)))

#%%
# Demonstrate pathlib.Path
# - user's home dir: Path.home()
# - current dir: Path.cwd() (Path('.'), Path() - work well only with absolute(), e.g. Path().absolute())
# - absolute path: <path>.absolute(), e.g. Path().absolute(), or Path('.').absolute()
# - parent dir: <path>.parent

print(Path.home())
print(Path.cwd())
# print(Path())
print(Path.cwd().absolute())
print(Path().absolute())
print(Path('.').absolute())
print(Path('.').absolute().parent)

#%%
# Demonstrate creating and removing directories
# - new dir: <newDir> = <path> / '<subdir1>/<subdir2>/.../<subdirN>'
#            <newDir>.mkdir(parents=True, exist_ok=True)
# - remove dir: <dir>.rmdir()                                           # requires the <dir> to be empty
# - project dir: settings.PROJECT_DIR

new_dir = PROJECT_DIR / 'new_dir'
print(new_dir)
new_dir.mkdir(parents=True, exist_ok=True)
print(new_dir.exists())
print()

new_dir.rmdir()
print(new_dir.exists())
print()


#%%
def get_project_dir():
    """Returns the Path object corresponding to the project root directory.
    """

    return PROJECT_DIR

#%%
# Demonstrate get_project_dir()
print(get_project_dir())

#%%
def get_data_dir():
    """Returns the Path object corresponding to the data directory
    (by convention located right under the project root directory).
    """

    data_dir = PROJECT_DIR / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir

#%%
# Demonstrate get_data_dir()
print(get_data_dir())
