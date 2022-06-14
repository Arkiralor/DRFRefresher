echo "Creating Virtual Environment..."
python -m venv env
echo "Activating Virtual Environment..."
source env/bin/activate
echo "Installing Pip Tools..."
pip install pip-tools
echo "Compiling dependency list..."
pip-compile
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Installing Spacy model (Medium-sized model for core Engilsh for the web)..."
python -m spacy download en_core_web_md
echo "Migrating DB tables..."
python manage.py migrate
echo "Starting server..."
python manage.py runserver