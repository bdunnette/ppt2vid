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
#Get length of wav file - from https://stackoverflow.com/questions/7833807/get-wav-file-length-or-duration
#import wave
#import contextlib
#fname = '/tmp/test.wav'
#with contextlib.closing(wave.open(fname,'r')) as f:
#    frames = f.getnframes()
#    rate = f.getframerate()
#    duration = frames / float(rate)
#    print(duration)
