import requests

class User():
    def __init__(self,first,last,email,username,password,uuid,phone,cell,picturelarge,picturethumbnail):
        self.first = first
        self.last = last
        self.email = email
        self.username = username
        self.password = password
        self.uuid = uuid
        self.phone = phone
        self.cell = cell
        self.picturelarge = picturelarge
        self.picturethumbnail = picturethumbnail
    
    def setFirst(self,first):
        self.first = first

    def setLast(self, last):
        self.last = last
    
    def setEmail(self ,email):
        self.email = email
    
    def setUsername(self, username):
        self.username = username
    
    def setPassword(self, password):
        self.password = password
    
    def setUuid(self, uuid):
        self.uuid = uuid
    
    def setPhone(self,phone):
        self.phone = phone
    
    def setCell(self, cell):
        self.cell = cell
    
    def setLargePicture(self, picturelarge):
        self.picturelarge = picturelarge
    
    def setPictureThumb(self, picturethumbnail):
        self.picturethumb = picturethumbnail

    def getFirst(self):
        return self.first
    
    def getLast(self):
        return self.last
    
    def getEmail(self):
        return self.email
    
    def getUsername(self):
        return self.email
    
    def getPassword(self):
        return self.password
    
    def getUuid(self):
        return self.uuid
    
    def getPhone(self):
        return self.phone
    
    def getCell(self):
        return self.cell
    
    def getLargePicture(self):
        return self.picturelarge
    
    def getPictureThumbnail(self):
        return self.picturethumbnail
    
    def __str__(self):
        retStr = self.first + self.last + self.email
        return retStr


class AuthorizedUsers():
    def __init__(self):
        self.myUsers = []
    def addUser(self, user):
        self.myUsers.append(user)
    def showUserList(self):
        for user in self.myUsers:
            print(user)
    

def getData(nat):
    URL = "https://randomuser.me/api/?results=10"+nat+".json"

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

myUserList = AuthorizedUsers()
jsonUserData = getData("us")

for currentUser in jsonUserData["results"]:
    userFirst = currentUser["name"]
    email = currentUser["email"]
    users = []
    newUser = User(userFirst, email)
    myUserList.addUser(newUser)
    
myUserList.showUserList()
