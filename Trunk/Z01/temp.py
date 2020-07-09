def validJson(jdata):
    try:
        json_object = json.loads(jdata)
        return True
    except ValueError as e:
        pass
    return False

def readJson(loc_path):
    if os.path.isfile(loc_path):
        f = open(loc_path,"r")
        data = f.read()
        if validJson(data):
            jdata = json.loads(data)
            if jdata:
                return jdata
            else:
                return None
    return None


class Data:
    @staticmethod
    def validJson(jdata):
        try:
            json_object = json.loads(jdata)
            return True
        except ValueError as e:
            pass
        return False

    @staticmethod
    def readJson(file_path):

        if not os.path.isfile(file_path):
            print(f"Error: {file_path} is not a file!")
            sys.exit(0)

        f = open(file_path,"r")
        data = f.read()
        if Data.validJson(data):
            jdata = json.loads(data)
            if jdata:
                return jdata
            else:
                return None
        return None

# {
#     "fname":"Sasha",
#     "lname":"Ivanov",
#     "rank": 15339,
#     "screen_name":"spetsnaz983",
#     "email":"sashaivanov1998@gru.gov",
#     "power-boost":98.34,
#     "available-boosts": ["skull-crush","flower-child","acid-trip","disco-ball"]
# }


class Vector:
    def __init__(self,a=0,b=0):
        self.a = 0
        self.b = 0

    def __str__(self):
        return f"(a:{self.a},b:{self.b})"

    def __add__(self,other):
        return Vector(self.a + other.a , self.b + other.b)

    def __sub__(self,other):
        return Vector(self.a - other.a , self.b - other.b)


class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state
        players = getattr(self, "players", None)
        if not players:
            self.players = {}

class LeaderBoard(Borg):
        def __init__(self, player=None):
            Borg.__init__(self)
            if player is not None:
                self.players.append(player)

        def __str__(self):
            self.players = sorted(self.players,key=lambda player: player.rank)
            str = ""
            i = 0
            for p in self.players:
                str += f"{i} : {p}\n"
                i += 1
            return str



class Borg:
    _shared_state={}
    def __init__(self):
        self.__dict__ = self._shared_state

    def __str__(self):
        s = ""
        for k,v in self.__dict__.items():
            s += str(k)+" : "+str(v) + "\n"
        return s

class LeaderBoard(Borg):
    def __init__(self,player):
        Borg.__init__(self)
        noone = getattr(self, "players", None)

        if noone == None:
            self.players = []
        else:
            self.players.append(player)

    def __str__(self):
        self.players = sorted(self.players,key=lambda player: player.rank, reverse=True)
        str = ""
        i = 1
        for p in self.players:
            str += f"{i} : {p}\n"
            i += 1
        str += "+" * 80
        return str
