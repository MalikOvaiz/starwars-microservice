from app.commons.api import API

class Starship:

  def get_starships(self):
      data = API.get('https://swapi.dev/api/starships/')
      return data