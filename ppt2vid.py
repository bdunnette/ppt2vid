#  Copyright (C) 2014 Regents of the University of Minnesota
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#Pseudocode:
#unzip myfile.pptx
#get list of slides from [Content Types].xml [sic]
#for slide in list:\
#  render slide to image (using e.g. openoffice impress?)
#  get relationships from ppt/slides/_rels/slideXXX.xml.rels
#  find relationship of type http://schemas.openxmlformats.org/officeDocument/2006/relationships/audio and get its target
#  get length of audio file, e.g. using process below
#  display rendered slide for length of audio, adding this to output video file
# 
#Convert pptx to jpegs (via pdf) - from https://stackoverflow.com/questions/21523267/how-to-convert-pptx-files-to-jpg-or-png-for-each-slide-on-linux
#libreoffice --headless --convert-to pdf filename.pptx
#convert my_filename.pdf my_filename%d.jpg
#
#Get length of wav file - from https://stackoverflow.com/questions/7833807/get-wav-file-length-or-duration
#import wave
#import contextlib
#fname = '/tmp/test.wav'
#with contextlib.closing(wave.open(fname,'r')) as f:
#    frames = f.getnframes()
#    rate = f.getframerate()
#    duration = frames / float(rate)
#    print(duration)
