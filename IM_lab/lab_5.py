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
            flag = 0
            for j in range(len(Queue)):
                if flag == 0:
                    MassDevice.sort()
                    if Queue[0] < MassDevice[0] < Tm:
                        WT = WT + (MassDevice[0] - Queue[0])
                        t = -(1 / mu) * m.log(1 - np.random.rand(1)[0])
                        MassDevice[0] = MassDevice[0] + t
                        t = 0
                        Queue.pop(0)
                    else:
                        flag = 1
                else:
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
                    if Queue[0] > MassDevice[0]:
                        MassDevice[0] = Queue[0]
                        t = -(1 / mu) * m.log(1 - np.random.rand(1)[0])
                        MassDevice[0] = MassDevice[0] + t
                        t = 0
                        Queue.pop(0)
                else:
                    if Queue[0] < MassDevice[0] < Queue[len(Queue)-1]:
                        WT = WT + (MassDevice[0] - Queue[0])
                        t = -(1 / mu) * m.log(1 - np.random.rand(1)[0])
                        MassDevice[0] = MassDevice[0] + t
                        t = 0
                        Queue.pop(0)
                    else:
                        flag = 1
            else:
                break
    M_WT = (1/EventCount)*WT
    return M_WT

Tm = int(input())
lambd = float(input())
mu = float(input())
n = int(input())
#2,1,3;

Mass_Wt = []
Wt = 0
N = 1000
Sum_Wt = 0

for i in range(N+1):
    Wt = SMO_Erlang(Tm, lambd, mu, n)
    Mass_Wt.append(Wt)
    Sum_Wt = Sum_Wt + Wt

EstemetM_Wt = (1/N)*Sum_Wt
print(Mass_Wt)
print("Оценка среднего времени простоя заявки в очереди: ", EstemetM_Wt)