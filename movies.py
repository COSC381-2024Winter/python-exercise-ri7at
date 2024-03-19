class Movies:
    def __init__(self, movies_file):
        self._movies = []

        with open(movies_file, encoding="utf-8") as file:
            row_idx = 0
            for line in file:
                if row_idx % 3 == 0:
                    movie_name = line.rstrip()
                if row_idx % 3 == 1:
                    movie_cast = line.rstrip().split(',')
                if row_idx % 3 == 2:
                    self._movies.append(
                        {
                            'name': movie_name,
                            'cast': movie_cast
                        }
                    )
                    movie_name = None
                    movie_cast = None
                row_idx += 1

        if movie_name and movie_cast:
            # Add the last movie if file doesn't end with a newline
            self._movies.append(
                {
                    'name': movie_name,
                    'cast': movie_cast
                }
            )
    #three methods
            #1.list all movies.
    def list_all(self):
        return [movie['name'] for movie in self._movies]
    #2.search movies by title
    def search_by_title(self, title):
        return [movie['name'] for movie in self._movies if title.lower() in movie['name'].lower()]
    #3.search movies by actors.
    def search_by_actor(self, actor):
        results = []
        for movie in self._movies:
            if any(actor.lower() in cast_member.lower() for cast_member in movie['cast']):
                results.append((movie['name'], movie['cast']))
        return results

#if __name__ == "__main__":
#    movies = Movies('./movies.txt')
