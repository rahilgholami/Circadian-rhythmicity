import pywt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def wavelet(ax, time, signal, scales, waveletname = 'cmor', 
                 cmap = plt.cm.get_cmap('Dark2'), title = '', ylabel = '', xlabel = ''):
    
    dt = time[1] - time[0]
    [coefficients, frequencies] = pywt.cwt(signal, scales, waveletname, dt)
    power = (abs(coefficients)) ** 2
    period = 1./frequencies
    
    num_lev = 128
    contourlevels = np.log2(np.linspace(224, 5000, num_lev + 1)) 
    im = ax.contourf(time, np.log2(period), np.log2(power), contourlevels, extend='both', cmap='plasma')
    plt.rc('xtick', labelsize=19)
    plt.rc('ytick', labelsize=19)
    ax.set_title(title, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
    ax.set_xlabel(xlabel, fontsize=20)
    yticks = 2**np.arange(np.ceil(np.log2(period.min())), np.ceil(np.log2(period.max())))
    ax.set_yticks(np.log2(yticks))
    ax.set_yticklabels(yticks)

    cbar_ax = fig.add_axes([0.95, 0.5, 0.03, 0.25])
    fig.colorbar(im, cax=cbar_ax, orientation="vertical")
    
    return time, period, power

if __name__ == '__main__':
  t_n = 10
  N = 100000
  T = t_n / N
  f_s = 1/T

  xa = np.linspace(0, t_n, num=N)
  xb = np.linspace(0, t_n, num=N//2)

  frequency = 0.5
  ya, yb = np.sin(2*np.pi*frequency*xa), np.sin(2*np.pi*frequency*xb)

  plt.figure(figsize=(10,5))
  plt.subplot(1,2,1)
  plt.plot(xa, ya)
  plt.title(f'length of signal:{len(xa)}, period=2')
  plt.subplot(1,2,2)
  plt.plot(xb, yb)
  plt.title(f'length of signal:{len(xb)}, period=2')
  plt.show()

  title = 'Wavelet Transform (Power Spectrum) of signal with length 50K'
  ylabel = 'Period'
  xlabel = 'Time'
  fig, ax = plt.subplots(figsize=(25, 10))

  N = len(yb)
  time = xb 
  scales = np.arange(1000, 20000, 1000)

  time, period, power = wavelet(ax, time, yb, scales, xlabel=xlabel, ylabel=ylabel, title=title)

normalization_factor = np.var(ya)

mean_spectrum = []
window_size = 1500
power_array = np.array(power)

for i in range(power_array.shape[0]):
    df = pd.DataFrame(data=power_array[i,:]).rolling(window=window_size)
    mean_spectrum.extend((df.mean().dropna()).mean())

  fig, ax = plt.subplots(figsize=(10, 5))
  plt.plot(period, mean_spectrum/normalization_factor, '.-')
  ax.invert_xaxis()
  plt.xlabel("Period(h)", fontsize=18)
  plt.ylabel("Normalized Power Spectrum", fontsize=18)
  plt.show()
  plt.show()
