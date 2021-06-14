import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/cr1901/jcore-j1-ghdl"

# Module version
version_str = "0.0.post103"
version_tuple = (0, 0, 103)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post103")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8"
data_version_tuple = (0, 0, 8)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8")
except ImportError:
    pass
data_git_hash = "926f743917300a9d512c90ca4a552ee9f83f40a0"
data_git_describe = "v0.0-8-g926f743"
data_git_msg = """\
commit 926f743917300a9d512c90ca4a552ee9f83f40a0
Author: J <none@none>
Date:   Fri May 8 11:50:19 2020 +0900

    assert not synthesizable

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_jcore."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_jcore".format(f))
    return fn
