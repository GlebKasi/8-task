import matplotlib.pyplot as mpl
import numpy as np

with open("/home/b01-103/Desktop/Scripts/kg/data.txt","r") as f:
    data_volt=f.read().split("\n")
with open("/home/b01-103/Desktop/Scripts/kg/settings.txt","r") as g:
    settings=g.read().split("\n")
volt_arr=np.array(data_volt, dtype=float)
u_max=max(volt_arr)
t_max=0
while volt_arr[t_max]!=u_max:
    t_max+=1
sett_arr=np.array(settings, dtype=float)
time_arr=np.linspace(0,(len(volt_arr)-1)*sett_arr[0],len(volt_arr))
volt_arr*=sett_arr[1]
t_1=t_max*sett_arr[0]
t_2=(len(volt_arr)-1)*sett_arr[0]-t_1

fig=mpl.figure(figsize=(16,10),dpi=400)
ax=fig.subplots()
ax.plot(time_arr,volt_arr,label='V(t)')
ax.legend()
ax.set_title('Зависимость напряжения на конденсаторе от времени')
ax.grid()
ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение на конденсаторе, мВ')
marks=20
time_scat_arr=np.linspace(0,len(volt_arr)*(marks-1)/marks*sett_arr[0],marks)
volt_scat_arr=np.zeros(marks)
for i in range(marks):
    volt_scat_arr[i]=volt_arr[int(i*(len(volt_arr)-1)/marks)]
ax.scatter(time_scat_arr,volt_scat_arr, c='red')
ax.text(40,2.5,'Время зарядки = '+str(round(t_1,2)))
ax.text(40,2.4,'Время разрядки = '+str(round(t_2,2)))
mpl.xlim([0,60])
mpl.ylim([0,3.3])
mpl.savefig("/home/b01-103/Desktop/Scripts/kg/graphs.svg")