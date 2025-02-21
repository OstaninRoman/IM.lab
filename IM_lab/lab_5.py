import math as m
import numpy as np


def SMO_Erlang(TM, Lambd, Mu, N):
    Tm = TM
    lambd = Lambd
    mu = Mu
    n = N
    t = 0
    T1 = 0
    WT = 0
    Queue = []
    MassDevice = [0]*n
    EventCount = 0

    while T1 < Tm:
        t = -(1/lambd)*m.log(1 - np.random.rand(1)[0])
        T1 = T1 + t
        t = 0
        if T1 > Tm:
            for i_e in range(len(Queue)):
                MassDevice.sort()
                for i in range(len(MassDevice)):
                    if Queue[0] < MassDevice[i] < Tm:
                        WT = WT + (MassDevice[i] - Queue[0])
                        t = -(1 / mu) * m.log(1 - np.random.rand(1)[0])
                        MassDevice[i] = MassDevice[i] + t
                        t = 0
                        Queue.pop(0)
                        break
            if len(Queue) > 0:
                for i in range(len(Queue)):
                    WT = WT + (Tm - Queue[i])
            break
        ###
        Queue.append(T1)
        EventCount = EventCount + 1
        flag = 0
        for j in range(len(Queue)):
            if flag == 0:
                MassDevice.sort()
                if len(Queue) == 1:
                    for i in range(len(MassDevice)):
                        if Queue[0] > MassDevice[i]:
                            MassDevice[i] = Queue[0]
                            t = -(1 / mu) * m.log(1 - np.random.rand(1)[0])
                            MassDevice[i] = MassDevice[i] + t
                            t = 0
                            Queue.pop(0)
                            break
                else:
                    for i in range(len(MassDevice)):
                        if Queue[0] < MassDevice[i] < Queue[len(Queue)-1]:
                            WT = WT + (MassDevice[i] - Queue[0])
                            t = -(1 / mu) * m.log(1 - np.random.rand(1)[0])
                            MassDevice[i] = MassDevice[i] + t
                            t = 0
                            Queue.pop(0)
                            break
                        else:
                            flag = 1
                            break
            else:
                break
    M_WT = (1/EventCount)*WT
    return M_WT

Tm = int(input())
lambd = float(input())
mu = float(input())
n = int(input())
#2,1,3;

Wt = 0
Wt = SMO_Erlang(Tm, lambd, mu, n)
print(Wt)