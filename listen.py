from PyQt5.QtCore import QThread, pyqtSignal
import sounddevice as sd
import numpy as np
from time import sleep

class Listen(QThread):
    sig = pyqtSignal([float, float, float])

    def __init__(self, freq=440.0):
        super().__init__()
        self.freq = freq
        self.data = np.zeros(8192, dtype=np.float32) # a large enough buffer
        self.current = 0 # an integer modulo 4
        self.previousPhase1 = 0.0
        self.previousPhase2 = 0.0
        self.previousPhase3 = 0.0
        self.sampleRate = 44100.0
        self.hannWindowM = 0.5 * (1 - np.cos(2 * np.pi*np.arange(2048) / (2048-1)))
        self.hannWindowL = 0.5 * (1 - np.cos(2 * np.pi * np.arange(4096) / (4096-1)))

    def run(self):
        with sd.InputStream(samplerate=44100, channels=1, blocksize=512, \
                       device=0, callback=self.callback):
            while True:
                sleep(1)

    def callback(self, indata, frames, time, status):
        # copy the incoming data and calculate the fft
        self.data[frames * self.current : frames * (self.current + 1)] = indata[:, 0]
        self.data[frames * (self.current + 8) : frames * (self.current + 9)] = indata[:, 0]
        self.current = (self.current + 1) % 8
        if self.freq > 200.0:
            fft = np.fft.rfft(self.data[frames * self.current : frames * (self.current + 4)] * self.hannWindowM, n=2048)

            # measurement for fundamental
            bin = int(self.freq * 4 * frames / self.sampleRate + 0.5) # closest bin to monitored frequency
            binFreq = bin * self.sampleRate / (4 * frames) # the frequency associated to that bin
            currentPhase = np.angle(fft[bin])
            expectedDeviation = 2 * np.pi * (self.freq - binFreq)*512 / self.sampleRate + (bin % 4) * np.pi/2
            x1 = (currentPhase - self.previousPhase1 - expectedDeviation + np.pi/2) % (np.pi) - np.pi / 2
            # modulo pi ou modulo 2pi ???
            x1 *= 10 / self.freq
            self.previousPhase1 = currentPhase

            # measurement for second harmonic
            bin = int(self.freq * 8 * frames / self.sampleRate+0.5)
            binFreq = bin * self.sampleRate / (4 * frames)
            currentPhase = np.angle(fft[bin])
            expectedDeviation = 2 * np.pi * (2*self.freq-binFreq) *512/self.sampleRate + (bin%4)*np.pi/2
            x2 = (currentPhase - self.previousPhase2 - expectedDeviation + np.pi/2) % (np.pi) - np.pi / 2
            x2 *= 10 / (2 * self.freq)
            self.previousPhase2 = currentPhase

            # measurement for third harmonic
            bin = int(self.freq * 12 * frames / self.sampleRate+0.5)
            binFreq = bin * self.sampleRate / (4 * frames)
            currentPhase = np.angle(fft[bin])
            expectedDeviation = 2 * np.pi * (3 * self.freq - binFreq) * 512 / self.sampleRate + (bin%4)*np.pi/2
            x3 = (currentPhase - self.previousPhase3 - expectedDeviation + np.pi/2) % (np.pi) - np.pi / 2
            x3 *= 10 / (3 * self.freq)
            self.previousPhase3 = currentPhase
            self.sig.emit(x1, x2, x3)

        elif self.current % 2 == 1:
            fft = np.fft.rfft(self.data[frames * (self.current - 1) : frames * (self.current + 7)] * self.hannWindowL, n=4096)

            # measurement for fundamental
            bin = int(self.freq * 8 * frames / self.sampleRate + 0.5)
            binFreq = bin * self.sampleRate / (8*frames)
            currentPhase = np.angle(fft[bin])
            expectedDeviation = 2 * np.pi * (self.freq - binFreq) * 1024 / self.sampleRate + (bin % 4) * np.pi / 2
            x1 = (currentPhase - self.previousPhase1 - expectedDeviation + np.pi/2) % (np.pi) - np.pi / 2
            x1 *= 10 / self.freq
            self.previousPhase1 = currentPhase

            # measurement for second harmonic
            bin = int(self.freq * 16 * frames / self.sampleRate + 0.5)
            binFreq = bin * self.sampleRate / (8 * frames)
            currentPhase = np.angle(fft[bin])
            expectedDeviation = 2 * np.pi * (2 * self.freq - binFreq) * 1024 / self.sampleRate + (bin % 4) * np.pi / 2
            x2 = (currentPhase - self.previousPhase2 - expectedDeviation + np.pi/2) % (np.pi) - np.pi / 2
            x2 *= 10 / (2 * self.freq)
            self.previousPhase2 = currentPhase

            # measurement for third harmonic
            bin = int(self.freq * 24 * frames / self.sampleRate + 0.5)
            binFreq = bin * self.sampleRate / (8 * frames)
            currentPhase = np.angle(fft[bin])
            expectedDeviation = 2 * np.pi * (3 * self.freq - binFreq) * 1024 / self.sampleRate + (bin % 4) * np.pi / 2
            x3 = (currentPhase - self.previousPhase3 - expectedDeviation + np.pi/2) % (np.pi) - np.pi / 2
            x3 *= 10 / (3 * self.freq)
            self.previousPhase3 = currentPhase
            self.sig.emit(x1, x2, x3)


    def stop(self):
        sd.CallbackStop()