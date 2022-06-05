# Find the python path

py_path = $(python -c "import sys; print(sys.executable)")

if ["3" = "$(python -c "import sys; print(sys.version_info[0])")"]; then
    echo "Python 3 found"
else
    echo "Python 3 not found"
    exit 1
fi

python -m pip install --upgrade pip
pip install pip-tools
pip-compile
pip install -r requirements.txt