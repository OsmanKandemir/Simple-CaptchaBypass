#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from pytesseract import image_to_string 
import Image


print image_to_string(Image.open('cap1.png'))
print image_to_string(Image.open('cap1.jpg'))