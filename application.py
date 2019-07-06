from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Genre, Item

engine = create_engine('sqlite:///gamescatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/", methods=['GET'])
def home():
    firstItem = session.query(Genre).all()
    return firstItem.name


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')