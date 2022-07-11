from dao.model.directors_model import DirectorModel


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get(self, did=None):
        director = self.session.query(DirectorModel)
        if did:
            director = director.get(did)
            return director
        return director.all()

