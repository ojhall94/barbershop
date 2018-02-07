import barbershop
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import ClosePlots as cp
import pandas as pd

# x = np.linspace(0,10,1000)
# y = np.linspace(0,10,1000)
# z = np.linspace(0,10,1000)

x = np.arange(10)
y = np.arange(10)
z = np.arange(10)
n = np.arange(10)
df = pd.DataFrame({'x':x, 'y':y, 'z':z, 'n':n})


barber = barbershop.open(df, 'x', 'y')
barber.histograms_on(x=True,y=True)

barber.add_client('z', lower=1., upper=5.)
# barber.add_client(z, 'n')
barber.add_client('a')
# barber.add_client(z, 'b')
# barber.add_client(z, 'c')

barber.show_mirror()

# del barber

'''
check_seating
barbiside [reset cuts]?
'''
