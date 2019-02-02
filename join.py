from Join.linepy import *
from Join.akad.ttypes import *

yinmo = LINE()
oepoll = OEPoll(yinmo)
Yinmo = yinmo.getProfile()

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        yinmo.acceptGroupInvitation(op.param1)
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return
      
      
oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})


while True:
    oepoll.trace()
