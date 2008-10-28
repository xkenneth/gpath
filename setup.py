from setuptools import setup, find_packages
setup(
    name = "gpath",
    version = "0.1",
    packages = find_packages(),

    author = "Kenneth Miller",
    author_email = "xkenneth@gmail.com",
    keywords = "python path ironpython",
    url = "http://www.xkenneth.com/",
    description = """An abstraction of basic path operations between IronPython and CPython libraries. Does not use python standard libraries with IronPython.""",
)
