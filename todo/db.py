import mysql.connector

import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions    # el punto en schema indica la raiz del proyecto

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)     # cursor es nuestro acceso a la base de datos
    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():               # Con estas instrucciones de crea las tablas de la base de datos
    db, c = get_db()         # y si ya está creada y lo ejecutamos se borra y se crea todo desde cero

    for i in instructions:
        c.execute(i)

    db.commit()

@click.command('init-db') # en la terminal debemos escribir flask init-db para ejecutar este comando
@with_appcontext          # con esto le damos acceso a la configuracion de la aplicacion
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

