# Towards More Inclusive Facial Detection

## Abstract
WebGazer uses computer webcams to track eye-gaze locations of users in real time. This eye-tracking library is solely implemented in JavaScript and can be easily integrated within a web browser. WebGazer uses a model implemented by another JavaScript library, clmtrackr to fit facial models on faces tracked through video. This library allows WebGazer to train models that map eye features and their relative position on the screen.

Currently, WebGazer fails to accurately track people with beards, people wearing glasses, or people with dark skin. With the training image set for one of the face detection modules integrated within WebGazer being one of the most diverse available, it is crucial to understand why it still continues to fail. In order for WebGazer to be as accurate as possible, it is crucial for this face detection module, clmtrackr to be as inclusive as possible and work for a wide variety of faces.

Learning extensively how the external face detection tracker module clmtrackr, included by default in WebGazer, works is the best way to improve how facial features are tracked while the script runs and help determine external factors that inhibit WebGazer from achieving its full potential.

## Datasets
The datasets used in this work are [MUCT](http://www.milbo.org/muct/) and Pilot Parliaments Benchmark (PPB). You can request access to the Pilot Parliaments Benchmark Dataset (for non-commercial use only) from the [Algorithmic Justice League](https://www.ajlunited.org/connect/request-dataset-for-research).

## Project Presentation
The project presentation can be found [here](https://docs.google.com/presentation/d/e/2PACX-1vQYkkshsEJSTDI2gJ0n2nbzFXtnoE_PbInYXVWYsq4oXIYgbrI8vxgUHqg53ANup9-KveUmWr1w8g5t/pub?start=false&loop=false&delayms=3000&slide=id.p).

