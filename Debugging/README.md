##Debugging assignment
##duclimer:
from pyo import *
s = Server().boot()
s.start()
snd = SndTable("/Users/rrome/Documents/GitHub/lmsc261sp21/110Debugging/dulcimer.aiff")
env = HannTable()
pos = Phasor(freq=snd.getRate()*.25, mul=snd.getSize())
dur = Noise(mul=.001, add=.1)
g = Granulator(snd, env, [1, 1.001], pos, dur, 32, mul=.1).out()

##melodies
from pyo import *
s = Server().boot()
s.start()
wav = SquareTable()
env = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
met = Metro(.125, 12).play()
amp = TrigEnv(met, table=env, dur=1, mul=.1)
pit = TrigXnoiseMidi(met, dist='loopseg', x1=20, scale=1, mrange=(48,84))
out = Osc(table=wav, freq=pit, mul=amp).out()

The most big issue I met is I couldn't run pyo, I followed the instruction but it still shows me warning and says can't find the documents.So I'll just write what the issue might be down below.

First, the directory should change to myself's:
"/Users/zhouqianying/Documents/GitHub/MyLMSC261/Debugging/dulcimer.aiff"

I'm not sure is the line "wav = SquareTable()" stands for wav file. If it is, it should change to aiff or something relates.So does the line
"out = Osc(table=wav, freq=pit, mul=amp).out()"

These are the things that might be the issue I currently found. Thank you.
