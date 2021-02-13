from app.commons.api import API
from operator import itemgetter


class Starship:
    def get_starships(self, sort_id):

        url = 'https://swapi.dev/api/starships/'
        starships = []
        while url != None:
            data = data = API.get(url)
            url = data['next']
            for item in data['results']:
                if item['hyperdrive_rating'] == "unknown":
                    item['hyperdrive_rating'] = -1
                item['hyperdrive_rating'] = float(item['hyperdrive_rating'])
                starships.append(item)

        return self.sort_spaceships(starships, sort_id)

    def sort_spaceships(self, starships, sort_id):

        reverse = None
        if sort_id == 2:
            reverse = True
        elif sort_id == 1:
            reverse = False

        if reverse != None:
            starships.sort(key=itemgetter('hyperdrive_rating'), reverse=reverse)

        for item in starships:
            if item['hyperdrive_rating'] == -1:
                item['hyperdrive_rating'] = "unknown"

        return starships
