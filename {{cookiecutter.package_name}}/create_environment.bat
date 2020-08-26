REM CREATE YOUR VIRTUAL ENVIRONMENT
REM USE A BASE PYTHON 3 VERSION
call activate py38
python -m venv env
call "./env/Scripts/activate"
pip install -r requirements-dev.txt

REM CREATE A UNIQUE JUPYTER KERNEL FOR THIS PROJECT
pip install ipykernel
ipython kernel install --user --name={{ cookiecutter.package_name }}
