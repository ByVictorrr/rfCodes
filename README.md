# rfCodes - research on radio frequency [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ByVictorrr/rfCodes/blob/master/LICENSE.md)

My research I have done for rolling codes and rf and reverse engineering those.

## What does rf stand for?

rf stands for radio frequency.

## What actually is radio frequency.

radio frequency is a subset of the electromagnetic spectrum, with wavelength ranging from as high as 300 gigahertz (GHz) to as low as 30 hertz.

## How to produce a radio wave?

A radio wave is an electromagnetic wave, which consists of a changing magnetic and electric wave moving through space changing with time.

To produce a wave that is considered a radio wave, we can accelerate particles trhough wires.

### Maxwell's Equations

![GaussElectric](https://latex.codecogs.com/gif.latex?%5Coint%20%5Cvec%7BE%7D%20%5Ccdot%20%5Cvec%7BdA%7D%20%3D%20%5Cfrac%7Bq_i_n%7D%7B%5Cepsilon_0%7D)

![GaussMagnetic](https://latex.codecogs.com/gif.latex?%5Coint%5Cvec%7BB%7D%5Ccdot%20d%5Cvec%7BA%7D%3D0)

![FaradaysGen](https://latex.codecogs.com/gif.latex?%5Coint%20%5Cvec%7BE%7D%5Ccdot%20%5Cvec%7Bdl%7D%3D%20-%20%5Cfrac%7B%5Cmathrm%7Bd%20%5CPhi_B%7D%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%20%3D%20-%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%5Cint%20%5Cvec%7BB%7D%5Ccdot%20%5Cvec%7BdA%7D)

![ampere-maxwell](https://latex.codecogs.com/gif.latex?%5Coint%5Cvec%7BB%7D%5Ccdot%20d%5Cvec%7Bl%7D%3D%5Cmu_0%20i_%7Bthru%7D%20&plus;%5Cmu_0%5Cepsilon_0%5Cfrac%7Bd%5CPhi_E%7D%7Bdt%7D%3D%5Cmu_0%28I_%7Bthru%7D&plus;i_d%29)

![pic gauss E](https://www.tutorialspoint.com/images/physics/electric_charges_and_fields/gauss_theorem.jpg)

![pic guass B](http://scientificsentence.net/Equations/Electrostatics/Magnetic-Dipole.jpg)

![faraday](http://www.physics.louisville.edu/cldavis/phys299/notes/mag_faraday_fig2.jpg)

![pic Amp-max](http://www.rakeshkapoor.us/ClassNotes/HTMLFiles/Electromagnetic_Waves_9.gif)

where:

![displacement current](https://latex.codecogs.com/gif.latex?i_d%3D%5Cepsilon_0%5Cfrac%7Bd%5CPhi_E%7D%7Bdt%7D)

![constant 1](https://latex.codecogs.com/gif.latex?%5Cmu_0%3D4%5Cpi%20%5Ccdot%2010%5E%7B-7%7D%5Cfrac%7BT%5Ccdot%20m%7D%7BA%7D)

![constant 2](https://latex.codecogs.com/gif.latex?%5Cepsilon_0%3D8.854%5Ctimes%2010%5E%7B-12%7D%5Cfrac%7BC%5E2%7D%7BN%5Ccdot%20m%5E2%7D)


## Derivation of Maxwells Equations to get the Wave Equation

![WaveEQN](http://www.pstcc.edu/departments/natural_behavioral_sciences/Web%20Physics/D03408.gif)

![wave gif](https://upload.wikimedia.org/wikipedia/commons/9/99/EM-Wave.gif)



## How to solve the Wave Equation

https://www.youtube.com/watch?v=f0FeWyloHrs

## Characteristics of wave

* Amplitude

* Frequency

* Phase

## How is information Encoded into a wave?

First off there are two inputs in order to produce a modulated wave. You need a modulating signal which is the information and then the carrier signal which is a sine wave. 

Modulation is the process of varrying frequency, amplitude or phase of any carrier wave.

![block diagram modulation](http://www.equestionanswers.com/notes/images/modulation-block-diagram.png)

The modulating signal can be an analog signal like music, image or a digital signal like computer data.

### Types of modulation

1.) Analog

    Amplitude modulation
    
    Frequency modulation
    
    Phase modulation

2.)Digital

    Pulse amplitude modulation(PAM)
    
    Pulse width modulation(PWM)
    
    Pulse code modulation(PCM)
    
#### Analog Modulation

Frequency modulation: 


Amplitude modulation: is the process of changing the amplitude of the carrier signal w/ respect to the instaneous value of the modulating signal.

![Modulation](https://camo.githubusercontent.com/cbc1986cfdd285b8dfe5db106b6d9fb36188a1f0/687474703a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f612f61342f416d666d332d656e2d64652e676966)


![visual of Modulation](https://www.taitradioacademy.com/wp-content/uploads/2014/10/Image-8.png)


## Resouces

[modulation techniques](https://www.youtube.com/watch?v=beFoCZ7oMyY)

[fixed codes](https://andrewmohawk.com/2015/08/31/hacking-fixed-key-remotes-with-only-rfcat/)

[rfcat helper](https://github.com/ComThings/RfCatHelpers)

[rfcat bruteforce](https://github.com/ComThings/github-rfpwnon)

[general bruteforce](http://samy.pl/opensesame/)

[rolling code](https://crypto.stackexchange.com/questions/18311/how-does-a-rolling-code-work)

[radio frequency](https://en.wikipedia.org/wiki/Radio_frequency)

[radio waves](https://en.wikipedia.org/wiki/Radio_wave)

[maxwell eqn](http://www.pstcc.edu/departments/natural_behavioral_sciences/Web%20Physics/Chapter%20034.htm)

[arduino rf](https://www.youtube.com/watch?v=b5C9SPVlU4U)
