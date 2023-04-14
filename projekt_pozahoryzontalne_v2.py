import numpy as np
import matplotlib.pyplot as plt

class model:

    def __init__(self, tx_height, rx_height, distance, frequency, Er):
        self.tx_height = tx_height
        self.rx_height = rx_height
        self.frequency = frequency
        self.distance = distance
        self.Er = Er
        self.loss = 0
        
        N = (np.sqrt(self.Er)-1)*10**6
        K = abs((1-0.04665*np.exp(np.float128(0.005577*N)))**(-1))
        self.d_hor = np.float128(3.571*np.sqrt(K)*(np.sqrt(self.tx_height)*np.sqrt(self.rx_height)))
        
    def compute(self, disnatnce = None):
        if disnatnce is None:
            disnatnce = self.distance
            self.loss = 20*np.log10(self.tx_height*self.rx_height/(distance*1000)**2)+10*np.log10((1+(distance/(6*self.d_hor))**7)/(1+(distance/self.d_hor)**3))+(-distance/(13+77*(self.d_hor/distance)))+(22+self.frequency/2000)*np.log10(100/self.frequency)    
        else:
            part_distance = disnatnce
            loss = 20*np.log10(self.tx_height*self.rx_height/(part_distance*1000)**2)+10*np.log10((1+(part_distance/(6*self.d_hor))**7)/(1+(part_distance/self.d_hor)**3))+(-part_distance/(13+77*(self.d_hor/part_distance)))+(22+self.frequency/2000)*np.log10(100/self.frequency)
            return loss 

    def plot(self):
        x_points = []
        y_points = []

        x_points = np.arange(0.1, self.distance, 0.1)
        for i in x_points:
            y_points.append(self.compute(i))

        plt.plot(x_points, y_points)
        #plt.xscale('log')
        plt.grid()
        plt.xlabel("Dystans [km]")
        plt.ylabel("Tłumienie [dB]")
        plt.title("Tłumienie na podanej trasie")
        plt.show()

tx_height = input("Podaj wysokość antenty nadawczej w metrach: ")
rx_height = input("Podaj wysokość antenty odbiorczej w metrach: ")
distance = input("Podaj dystans w kilometrach: ")
frequency = input("Podaj częstotliwość w MHz: ")
Er = input("Podaj wartość współczynnika przenikalności elektrycznej: ")

tx_height, rx_height, distance, frequency, Er = float(tx_height), float(rx_height), float(distance), float(frequency), float(Er)

model = model(tx_height, rx_height, distance, frequency, Er)
model.compute()
print("Dystans [km]: %.3f" %model.distance)
print("Tłumienie na całej trasie [dB]: %.3f" %model.loss)
model.plot()        