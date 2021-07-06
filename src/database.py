from typing import List
from models.color import Color
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from sqlalchemy import exc

# , echo=True para ver errores por la consolta
engine = create_engine('sqlite:///../colors.db',
                       connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
# == DBSession.__call__() = invokes __call__ method from sessionmaker
session = DBSession()


def add_color(c):
    try:
        session.add(c)
        session.commit()
        return 1
    except exc.IntegrityError:
        session.rollback()
        return 0


def get_colors() -> List:
    list = []
    result = session.query(Color).all()
    for color in result:
        list.append({
            "id": color.id,
            "name": color.name,
            "rgb": color.rgb,
            "favorite": color.favorite
        })
    return list


def get_colors_by_favorite(fav) -> List:
    list = []
    for color in session.query(Color).filter(Color.favorite == fav):
        list.append({
            "id": color.id,
            "name": color.name,
            "rgb": color.rgb,
            "favorite": color.favorite
        })
    return list


def get_color(id) -> Color:
    color = session.get(Color, id)
    if color is None:
        return
    return {
        "id": color.id,
        "name": color.name,
        "rgb": color.rgb,
        "favorite": color.favorite
    }


def delete(id):
    color = session.get(Color, id)
    if color is None:
        return 0
    session.delete(color)
    session.commit()
    return 1


def update(color):
    color_query = session.query(Color).filter_by(id=color.id)
    try:
        data_to_update = dict(name=color.name, rgb=color.rgb,
                              favorite=color.favorite)
        color_query.update(data_to_update)
        session.commit()
        return 1
    except exc.IntegrityError:
        session.rollback()
        return 0
