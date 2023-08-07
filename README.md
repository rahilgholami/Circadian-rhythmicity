# Code Description

The [main.ipynb](https://github.com/rahilgholami/Circadian-rhythmicity/blob/main/main.ipynb) consists of two major parts, first is the data preprocessing (Removing drift from data (stationarity) and data smoothing) and the second part is computing the wavelet power spectrum of the actual data and establishing a background power spectrum at significance level 5% to compare the actual spectrum against.

## 1. Data preprocessing

### 1.1 Stationarity
A signal is said to be stationary if its statistical properties such as mean, variance, frequency, and etc are not changing over time.
The mean of the time-series is increasing over the time. This trend can be removed using a polynomial regression.


### 1.2. Data smoothing 
Moving average is commonly used with time series data to smooth out fluctuations and  stand out important patterns.


## 2. Wavelet transform
The wavelet transform is a powerful mathematical tool used for analyzing time series data, especially when dealing with features such as frequency which vary over time. In contrast to the Fourier transform, the wavelet transform offers superior resolution in both time and frequency domains, enabling the extraction of time-frequency information. By applying the wavelet transform, we can detect the frequencies present in the signal and identify when these frequencies occur. This capability makes the wavelet transform an invaluable tool for understanding complex and dynamic time series data.

### 2.1 Wavelet power spectrum
The wavelet power spectrum can be derived from the wavelet transform. As outlined in reference [1], assessing the significance of the wavelet spectrum involves comparing it to a background spectrum.  The actual spectrumis evaluated against the background spectrum.
An appropriate background spectrum is either white noise or red noise. 

A simple model for red noise is the univariate lag-1 autoregressive process:

![equation](https://latex.codecogs.com/svg.image?x_{n}&space;=&space;\alpha&space;x_{n-1}&space;&plus;&space;z_{n})

where ![equation](https://latex.codecogs.com/svg.image?\alpha) is the the assumed lag-1 autocorrelation.

The power spectrum of red nosie is

![equation](https://latex.codecogs.com/svg.image?P_{k}&space;=&space;\frac{1-&space;\alpha^{2}}{1&plus;\alpha^{2}-2\alpha&space;\cos(2&space;\pi&space;k/N)})

where ![equation](https://latex.codecogs.com/svg.image?N) is the number of datapoints and ![equation](https://latex.codecogs.com/svg.image?k) is the frequancy index.
The mean background spectrum significant at ![equation](https://latex.codecogs.com/svg.image?5%) is

![equation](https://latex.codecogs.com/svg.image?\frac{1}{2}P_{k}\chi_{2}^{2})

where ![equation](https://latex.codecogs.com/svg.image?\chi_{2}^{2}) is a chi-square distribution with 2 degrees of freedom.









## References

[1] C. Torrence, G.P. Compo, A practical guide to wavelet analysis, Bulletin of the American Meteorological Society 79 (1998) 605–618.
