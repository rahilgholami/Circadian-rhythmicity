# clock

## 1. Stationarity
A signal is said to be stationary if its statistical properties such as mean, variance, frequency, and etc are not changing with respect to time.
The mean of the time-series is increasing over the time. This trend can be removed using a polynomial regression.


## 2. Data smoothing 
Moving average is commonly used with time series data to smooth out fluctuations and  stand out important patterns.


## 3. Wavelet transform
Wavelet transform is mathematical tool to analyze time series data where features such as frequency varies over time.
Unlike Fourier transform, The wavelet transform has a high resolution in both time and frequency domains to obtain time-frequency
information. With the wavelet transform, it can be realized which frequencies are present in the signal and at which time these frequencies occur.

### 3.1 Wavelet power spectrum
Wavelet power spectrum can be computed from the wavelet transform. Following [1], to determine significance levels for the wavelet spectrum, a background spectrum is needed to compare the actual spectrum against. An appropriate background spectrum
is either white noise or red noise. 

A simple model for red noise is the univariate lag-1 autoregressive process:

![equation](https://latex.codecogs.com/svg.image?x_{n}&space;=&space;\alpha&space;x_{n-1}&space;&plus;&space;z_{n})

where ![equation](https://latex.codecogs.com/svg.image?\alpha) is the the assumed lag-1 autocorrelation.

The power spectrum of red nosie is

![equation](https://latex.codecogs.com/svg.image?P_{k}&space;=&space;\frac{1-&space;\alpha^{2}}{1&plus;\alpha^{2}-2\alpha&space;\cos(2&space;\pi&space;k/N)})

where ![equation](https://latex.codecogs.com/svg.image?N) is the number of datapoints and ![equation](https://latex.codecogs.com/svg.image?k&space;=0,&space;...,&space;N/2) is the frequancy index.
The mean background spectrum significant at ![equation](https://latex.codecogs.com/svg.image?5%) is

![equation](https://latex.codecogs.com/svg.image?\frac{1}{2}P_{k}\chi_{2}^{2})












[1] C. Torrence, G.P. Compo, A practical guide to wavelet analysis, Bulletin of the American Meteorological Society 79 (1998) 605–618.
