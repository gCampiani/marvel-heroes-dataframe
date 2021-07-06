from services.hash import build_hash

import requests

from datetime import datetime
from decouple import config


class MarvelRequest:
    
    def __init__(self, limit=100, cursor=0):
        self.key = config("PUBLIC_API_KEY")
        self.ts = datetime.now().strftime('%Y-%m-%d%H:%M:%S')
        self.limit = limit
        self.cursor = 0
        self.url = config('CHARACTERS_URL')
 
    def get_all_heroes(self):
        content = self.do_request()
        if not content:
            self.output = None
            return
        self.output = [self.hero_to_dict(hero) for hero in content.json()["data"]["results"]]
        self.refresh_cursor()
        
        while(self.cursor < content.json()["data"]["total"]):
            self.output += [self.hero_to_dict(hero) for hero in self.do_request().json()["data"]["results"]]
            if not content:
                self.output = None
                return
            self.refresh_cursor()
            
    
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
        
    def refresh_cursor(self):
        self.cursor += self.limit

    @staticmethod
    def hero_to_dict(hero):
        return {"id": hero["id"],
                "name": hero["name"],
                "description": hero["description"],
                "comics": len(hero["comics"]),
                "series": len(hero["series"]),
                "stories": len(hero["stories"]),
                "events": len(hero["events"])}