import sys
import  requests
from urllib.request import urlopen
import json




class Dict:
    app_id = 'e72676d4'
    app_key = 'c89d764a03f80f3642208e8cbd0f99ef'
    language = 'en'
   # word_id = <word_to_look_up>
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  
    #url Normalized frequency
    urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' #+ word_id.lower()
    def __init__(self, app_id = app_id, app_key= app_key):
        self.word_id = str()
        self.app_id  = app_id
        self.app_key = app_key
        self.url     = self.url + str(self.word_id)

        self.print_results(self.url,self.app_id,self.app_key)
    def print_results(self,url,app_id ,app_key):
        self.r = requests.get(self.url, headers = {'app_id' : self.app_id, 'app_key' : self.app_key})
        self.content = json.dumps(self.r.json())
        self.content = json.loads(self.content)
        self.parse()
    def user_input(self):
        self.word_id = input("Enter word: ").lower()
        return self.word_id

    def parse(self):    
        t = 1
        print(f'{self.word_id.upper()} \n =======\n')
        for i in self.content["results"]:
            for j in i["lexicalEntries"]:
                try:                      
                    for k in j["entries"]:
                        for v in k["senses"]:
                            print(f'{t}/ {v["definitions"][0]}')
                            t += 1
                            try:
                                for n in v['examples']:
                                    print(f" =>  {n['text']}")
                            except KeyError:
                                continue
                except KeyError:
                                continue                        

if __name__ == "__main__":
    while True :
        try:
            d = Dict()
            d.user_input()    
            if d.user_input() == 'q-':
                exit(0)
            else:
                continue    
        except:
            print('?')
            continue
        





















