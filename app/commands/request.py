from services.hash import build_hash

import requests

from datetime import datetime
from decouple import config
from tqdm import tqdm


class MarvelRequest:
    
    def __init__(self, limit=100, cursor=0):
        self.key = config("PUBLIC_API_KEY")
        self.ts = datetime.now().strftime('%Y-%m-%d%H:%M:%S')
        self.limit = limit
        self.cursor = 0
        self.url = config('CHARACTERS_URL')
 
    def get_all_heroes(self):
        print("Executing...")
        content = self.do_request()
        if not content:
            self.output = None
            return
        self.output = [self.hero_to_dict(hero) for hero in content.json()["data"]["results"]]
        self.cursor += self.limit
        
        for cursor in tqdm(range(self.cursor, content.json()["data"]["total"], self.limit)):
            self.cursor = cursor
            self.output += [self.hero_to_dict(hero) for hero in self.do_request().json()["data"]["results"]]
            if not content:
                self.output = None
                return
            
    def do_request(self):
        params = {'ts': self.ts, 
                  'apikey': self.key, 
                  'hash': build_hash(ts=self.ts),
                  'limit': self.limit,
                  'offset': self.cursor
                  }
        
        response = requests.get(url=self.url, params=params)
        
        if response.json()["code"] != 200:
            return None
        return response

    @staticmethod
    def hero_to_dict(hero):
        return {"id": hero["id"],
                "name": hero["name"],
                "description": hero["description"],
                "comics": hero["comics"]["available"],
                "series": hero["series"]["available"],
                "stories": hero["stories"]["available"],
                "events": hero["events"]["available"]}