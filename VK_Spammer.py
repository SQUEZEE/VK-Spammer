from vkmini import VkApi
from numba import njit, prange

idsl1=open('obrab.txt','r')

tokens = ('ac2106499883ac52f33e0546974ef607e49e4c06015d904e86f47f616ec8f727e8735136e1e387908c8da&expires_in=0&user_id=529239102&email=kostua7363@gmail.com', '95b9f9fe94b836b9b84a833dd1cccc6ce1a406c2e9b2697e6e72c941e5875448c5080cee731289172890a&expires_in=0&user_id=634057233')
idsl = idsl1.read().split('\n')

mam = dict()

@njit(fastmath=True, parallel=True)
def reload_kit(): #Load to dict new ids
    mam[1]=idsl[0]
    mam[2]=idsl[1]
    mam[3]=idsl[2]
    mam[4]=idsl[3]
    mam[5]=idsl[4]
    mam[6]=idsl[5]
    mam[7]=idsl[6]
    mam[8]=idsl[7]
    mam[9]=idsl[8]
    mam[10]=idsl[9]
    mam[11]=idsl[10]
    mam[12]=idsl[11]
    mam[13]=idsl[12]
    mam[14]=idsl[13]
    mam[15]=idsl[14]
    mam[16]=idsl[15]
    mam[17]=idsl[16]
    mam[18]=idsl[17]
    mam[19]=idsl[18]
    mam[20]=idsl[19]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
    del idsl[0]
reload_kit()


#user = vk.users.get()[0]
#user_id = user['id']


@njit(fastmath=True, parallel=True) #Send message on id
def send(idl):
    link_user = vk.users.get(
        user_ids = idl
    )
    message_id = vk.messages.send(
        user_id = link_user[0]['id'],
        message = 'да',
        random_id = 0
    )


@njit(fastmath=True, parallel=True)
def delsend(): #Send message on first 20 ids in dict
    listall=mam[1],mam[2],mam[3],mam[4],mam[5],mam[6],mam[7],mam[8],mam[9],mam[10],mam[11],mam[12],mam[13],mam[14],mam[15],mam[16],mam[17],mam[18],mam[19],mam[20]

    for i in listall:
        send(i)
    mam.pop(1)
    mam.pop(2)
    mam.pop(3)
    mam.pop(4)
    mam.pop(5)
    mam.pop(6)
    mam.pop(7)
    mam.pop(8)
    mam.pop(9)
    mam.pop(10)
    mam.pop(11)
    mam.pop(12)
    mam.pop(13)
    mam.pop(14)
    mam.pop(15)
    mam.pop(16)
    mam.pop(17)
    mam.pop(18)
    mam.pop(19)
    mam.pop(20)
    reload_kit()


for l in tokens: #Send 20 message of all tokens
    vk = VkApi(
        access_token=l,
        sync_mode=True,
        excepts=True
        )
    user = vk.users.get()[0]
    user_id = user['id']
    delsend()

idsl1.close