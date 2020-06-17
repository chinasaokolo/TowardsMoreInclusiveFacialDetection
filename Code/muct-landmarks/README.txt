README.txt for MUCT landmarks
-----------------------------

This directory contains the following files, containing
the manual landmark data for the MUCT images in various formats:

    (i)    muct76.shape       shape file (www.milbo.users.sonic.net/stasm)
    (ii)   muct76.rda         R data file (www.r-project.org/
    (iii)  muct76.csv         comma separated values
    (iv)   muct76-opencv.csv  comma separated values in OpenCV coords (0,0 at top left).

For more details, please go to www.milbo.org/muct.

Note that the coordinate system in these files is the one used by
Stasm (i.e. the origin 0,0 is the center of the image, x increases as
you move right, y increases as you move up).  The exception is
muct76-opencv.csv, where the format is the "OpenCV format" (i.e. the
origin 0,0 is at the top left, x increases as you move left, y
increases as you move down).

Unavailable points are marked with coordinates 0,0 (regardless of the
coordinate system mentioned above).  "Unavailable points" are points
that are obscured by other facial features.  (This refers to landmarks
behind the nose or side of the face -- the position of such landmarks
cannot easily be estimated by human landmarkers -- in contrast, the
position of landmarks behind hair or glasses was estimated by the
landmarkers).  

So any points with the coordinates 0,0 should be ignored.  Unavailable
points appear only in camera views b and c.  Unless your software
knows how to deal with unavailable points, you should use only camera
views a, d, and e.

Note that subjects 247 and 248 are identical twins.

Please respect the privacy of the people who volunteered to have their
faces photographed and DO NOT REPRODUCE the MUCT images in any
publically available document (especially web pages).

However, the following subjects have agreed to allow their faces to be
reproduced in academic papers (but not on web pages):

   000, 001, 002, 200, 201, 400, 401, 402.


Stephen Milborrow
Petaluma, Sep 2010
