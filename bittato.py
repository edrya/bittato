from app import app, db
from app.models import Transaction, Potato


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Transaction': Transaction, 'Potato': Potato}