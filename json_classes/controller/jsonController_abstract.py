import json


class JsonController:
    def jsonWriter(self, path, data):
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
    
    def jsonReader(self, path):
        with open(path, 'r') as f:
            return json.load(f)
        
    def jsonViewer(self, data):
        print(json.dumps(data, indent=4))


def jsonController(path=None, mode=None, data=None):
    if mode in ['w', 'r']:
        with open(path, mode) as f:
            # jsonWriter
            if mode == 'w':
                json.dump(data, f, indent=4)
            # jsonReader
            else:
                return json.load(f)
    # jsonViewer 
    else:
        print(json.dumps(data, indent=4))