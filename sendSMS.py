from urllib import urlencode, urlopen
from myconfig import mvayooUsername, mvayoopassword

def send(number, inputMessage):
    strUrl =  "http://api.mVaayoo.com/mvaayooapi/MessageCompose?"
    param = {}
    param['user'] = mvayooUsername+":"+mvayoopassword ## account:pass
    param['senderID'] = "TEST SMS" ## Because nothing else works
    param['receipientno'] = number[-10:]
    param['dcs'] = "0"
    param['msgtxt'] = inputMessage
    param['state'] = "4"
    url = strUrl + (urlencode(param))
    imiResponse = urlopen(url).read ()
    return imiResponse
