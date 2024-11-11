import numpy as np
import matplotlib.pyplot as plt
#set the variables
h=int(input("¿Desde que altura lo lanzas?"))
g=9.8 
t_max=np.sqrt(2*h/g)
#steps
time_steps=np.linspace(0,t_max,num=100)
#calculations
y_positions=h-(0.5*g*time_steps**2)
distances_fallen=np.diff(y_positions)
average_distance=np.mean(distances_fallen)
#print the data
print("Time to hit the ground:",t_max,"seconds")
print("Average distance fallen per time step:",average_distance,"meters")
#visual representation with plt.
plt.figure(figsize=(10,5))
plt.plot(time_steps,y_positions,label='Position of Ball')
plt.title('Free Fall Motion of a Ball')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.axhline(0,color='red',linestyle='--',label='Ground Level')
plt.legend()
plt.grid()
plt.show()

