import matplotlib.pyplot as plt
plt.style.use('./dark_mode.mplstyle')
import numpy as np
import math
class Plot():

    def __init__(self):
        self.colors = {
            'O(1)': '#3D3D3D',
            'O(log n)': '#3D3D3D',
            'O(n)': '#3D3D3D',
            'O(n log n)':'#3D3D3D',
            'O(n!)': '#3D3D3D',
            'O(n^2)': '#3D3D3D',
            'O(2ⁿ)': '#3D3D3D'
        }
        self.fig, self.ax = plt.subplots(facecolor='#1e1e1e')
        self.fig.set_figwidth(15)
        self.fig.set_figheight(10)
        self.fig.patch.set_facecolor('#1e1e1e')          
        self.ax.set_facecolor('#1e1e1e')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        # plt.tight_layout()

    def draw(self, value): 
        self.colors[value] = '#c084fc'
        self.ax.set_title(fr'${value}$', fontsize=40, color='white')
        n_fast = np.linspace(0.1, 5, 100)      
        n_fast2 = np.linspace(0.1, 7, 100)      
        n_mid = np.linspace(1, 25, 100)        
        n_slow = np.linspace(1, 90, 100)     

        self.ax.plot(n_slow, np.ones_like(n_slow), label='O(1)', color = self.colors['O(1)'],linewidth=4 )
        self.ax.plot(n_slow, np.log2(n_slow), label='O(log n)', color = self.colors['O(log n)'],linewidth=4)
        self.ax.plot(n_slow, n_slow, label='O(n)', color = self.colors['O(n)'],linewidth=4)
        self.ax.plot(n_mid, n_mid * np.log2(n_mid), label='O(n log n)', color = self.colors['O(n log n)'],linewidth=4)
        self.ax.plot(n_fast, [math.factorial(int(x)) if x >= 1 else 1 for x in n_fast], label='O(n!)', color = self.colors['O(n!)'],linewidth=4)
        self.ax.plot(n_fast2, 2**n_fast2, label='O(2ⁿ)', color = self.colors['O(2ⁿ)'],linewidth=4)
        self.ax.plot(n_mid[:42], n_mid[:42]*n_mid[:42], label='O(n^2)', color = self.colors['O(n^2)'],linewidth=4)


    def show_fig(self): 
        plt.show()
    def get_fig(self): 
        return self.fig