# coding: utf-8
import wave
import struct
import numpy as np
from pylab import *

def createSineWave (A, f0, fs, length):
    """�U��A�A��{���g��f0�A�T���v�����O���g�� fs�A
    ����length�b�̐����g���쐬���ĕԂ�"""
    data = []
    # [-1.0, 1.0]�̏����l���������g���쐬
    for n in arange(length * fs):  # n�̓T���v���C���f�b�N�X
        s = A * np.sin(2 * np.pi * f0 * n / fs)
        # �U�����傫�����̓N���b�s���O
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)
    # [-32768, 32767]�̐����l�ɕϊ�
    data = [int(x * 32767.0) for x in data]
#    plot(data[0:100]); show()
    # �o�C�i���ɕϊ�
    data = struct.pack("h" * len(data), *data)  # list��*������ƈ����W�J�����
    return data

def play (data, fs, bit):
    import pyaudio
    # �X�g���[�����J��
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=int(fs),
                    output= True)
    # �`�����N�P�ʂŃX�g���[���ɏo�͂��������Đ�
    chunk = 1024
    sp = 0  # �Đ��ʒu�|�C���^
    buffer = data[sp:sp+chunk]
    while buffer != '':
        stream.write(buffer)
        sp = sp + chunk
        buffer = data[sp:sp+chunk]
    stream.close()
    p.terminate()

if __name__ == "__main__" :
    freqList = [262, 294, 330, 349, 392, 440, 494, 523]  # �h���~�t�@�\���V�h
    for f in freqList:
        data = createSineWave(1.0, f, 8000.0, 1.0)
        play(data, 8000, 16)
