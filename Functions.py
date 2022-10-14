from datetime import datetime

# Basic timer that counts backwards. 
def timer(hour, min, sec):
    while(True):
        alfa_sec = datetime.now()
        while(True):
            beta_sec = datetime.now()
            if alfa_sec.second != beta_sec.second:
                sec = sec - 1
                if sec == -1:
                    sec = 59
                    min = int(min) - 1
                    if min == -1:
                        min = 59
                print(str(hour).zfill(2),":",str(min).zfill(2),":",str(sec).zfill(2))
                break
        if(sec == 0 and min == 0):
            break