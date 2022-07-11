from dao.model.movies_model import MovieModel


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get(self, mid=None,  **params):
        movie = self.session.query(MovieModel)
        if params:
            for key, value in params.items():
                movie = movie.filter(f"MovieModel.{key}"== int(value))
                return movie
        if mid:
            movie = movie.get(mid)
            return movie
        return movie.all()

    def create(self, data):
        movie = MovieModel(**data)
        self.session.add(movie)
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get(mid)
        self.session.add(movie)
        self.session.commit()
