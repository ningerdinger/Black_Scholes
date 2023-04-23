tutorial to package this https://packaging.python.org/en/latest/tutorials/packaging-projects/

run this

py -m pip install --upgrade build

run this from the toml directory

py -m build

install twine

py -m pip install --upgrade twine

Make sure that you have a pypi account and token

run this to upload to pypi and fill in token as username, token as pw

py -m twine upload --repository testpypi dist/*

then just install from pypi and run it