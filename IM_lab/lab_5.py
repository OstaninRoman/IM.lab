import math as m
import numpy as np

def SMO_Erlang(Tm, lambd, mu, n):
    Queue = []
    MassDevice = [0]*n
    T1 = 0
    WT = 0
    EventCount = 0
    while T1 < Tm:
        T1 = T1 + (-(1/lambd)*m.log(1 - np.random.rand(1)[0]))
        if T1 > Tm:
            flag = 0
            for i in range(len(Queue)):
                if flag == 0:
                    MassDevice.sort()
                    if Queue[0] < MassDevice[0] < Tm:
                        WT = WT + (MassDevice[0] - Queue[0])
                        MassDevice[0] = MassDevice[0] + (-(1 / mu) * m.log(1 - np.random.rand(1)[0]))
                        Queue.pop(0)
                    else:
                        flag = 1
                else:
                    break
            EventCount = EventCount - len(Queue)
            break
        if len(Queue) > 0:
            flag = 0
            for i in range(len(Queue)):
                if flag == 0:
                    MassDevice.sort()
                    if Queue[0] < MassDevice[0] < T1:
                        WT = WT + (MassDevice[0] - Queue[0])
                        MassDevice[0] = MassDevice[0] + (-(1 / mu) * m.log(1 - np.random.rand(1)[0]))
                        Queue.pop(0)
                    else:
                        flag = 1
                        Queue.append(T1)
                        EventCount = EventCount + 1
                else:
                    break
        if len(Queue) == 0:
            MassDevice.sort()
            if T1 > MassDevice[0]:
                MassDevice[0] = T1
                MassDevice[0] = MassDevice[0] + (-(1 / mu) * m.log(1 - np.random.rand(1)[0]))
            else:
                Queue.append(T1)
                EventCount = EventCount + 1
    M_WT = (1/EventCount)*WT
    return M_WT

TM = int(input())
Lambd = float(input())
Mu = float(input())
n = int(input())
#2,1,3;

M_Wt = 0
N = 1000
Sum_MWt = 0

for i in range(N+1):
    M_Wt = SMO_Erlang(TM, Lambd, Mu, n)
    Sum_MWt = Sum_MWt + M_Wt

EstemetM_Wt = (1/N)*Sum_MWt
print("Оценка среднего времени простоя заявки в очереди: ", EstemetM_Wt)