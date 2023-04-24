
![image](https://user-images.githubusercontent.com/52888356/234033338-80ff5e2f-3c73-413b-aee2-8cf40d36bcaf.png)
![image](https://user-images.githubusercontent.com/52888356/234033384-8bea4f75-ed85-4fd0-a7e6-6702b96821fd.png)
![image](https://user-images.githubusercontent.com/52888356/234033410-1a7c0154-f466-4687-a3f5-f82c36495d78.png)



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
