# EcoSecure
 A simple application that uses a Python deep learning model in order to recognise and identify faces. The model interfaces with a HTML/CSS web dashboard using the Flask API in order to reflect the findings of the model. For instance, if an authenticated user (specified by the owner of the app) is detected, then it notifies the web dashboard of this. Conceived during Hack The Valley 4 (2020).

# Table of Contents
* [Introduction](https://github.com/AbChatt/EcoSecure#introduction)
* [Technologies](https://github.com/AbChatt/EcoSecure#technologies)
* [Requirements](https://github.com/AbChatt/EcoSecure#requirements)
* [Examples](https://github.com/AbChatt/EcoSecure#examples)
* [Status](https://github.com/AbChatt/EcoSecure#status)
* [Acknowledgements](https://github.com/AbChatt/EcoSecure#acknowledgments)

## Introduction 
Home Security has always been an innovative segment of the market. From the earliest rudimentary alarm systems to the high resolution video cameras of today, providers have always been striving to constantly iterate on their product offerings. However, in recent years, there is a disturbing trend towards increasingly exorbitant pricing (systems cost anywhere from a few hundred to a few thousand dollars) and lock in from providers (due to the proprietary nature of the hardware and software used). EcoSecure was conceived as a response to these challenges as well as the ever present issue of e-waste. Since we all have older phones at home in generally good condition, why not repurpose that hardware to build a security system? At the very least, the cost advantages would be undeniable. The open source nature of our software, along with its modularity as a web application clearly address both challenges of current systems and one can extract many more years of usefulness from those older, obsolete phones, thus reducing e-waste.

## Technologies
This project consists of a Python backend, which implements a Convolutional Neural Network (CNN) that recognises and identifies faces. The ML model interfaces with the HTML/CSS front end using the Flask API

## Requirements
This project requires the following libraries and frameworks:

* Flask v1.1.1
* numpy v1.18.1
* Pillow v7.0.0
* opencv-contrib-python v4.2.0.32
* face_recognition v1.2.3
* flask_sqlalchemy v2.4.1
* requests v2.22.0

In addition to the above, you will need Python (v3.6.8), HTML5 and CSS3. This has also been tested on Python v3.7.4 but newer versions may create issues

## Examples
Some sample screenshots of functionality, the website would provide are shown below

## Status
As of February 2020 (last commit was the 16th), the project is active

## Acknowledgements
Parts of this project were adapted from [OpenCV Python Series](https://github.com/codingforentrepreneurs/OpenCV-Python-Series). Furthermore, we used the [facial recognition API](https://github.com/ageitgey/face_recognition) and took inspiration from [this](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py) example.
