import wave
import os
import time

def encode_lsb_2_bit(wavfile, textfile, save_path, file_name):
    start = time.time()
    # read wave audio file
    song = wave.open(wavfile, mode='rb')

    # Convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    f = open(textfile, "r")
    string = f.read()
    f.close()

    # Padding preprocess
    string = string + int((2 * len(frame_bytes) - (len(string) * 8 * 8)) / 8) * '#'

    # Convert text to bit array
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))

    # Replace 2 LSB instead of one
    j = 0
    for i in range(0, len(frame_bytes), 2):
        frame_bytes[j] = (frame_bytes[j] - (frame_bytes[j] % 4))
        if bits[i] == 0 and bits[i + 1] == 0:
            frame_bytes[j] += 0
        elif bits[i] == 0 and bits[i + 1] == 1:
            frame_bytes[j] += 1
        elif bits[i] == 1 and bits[i + 1] == 0:
            frame_bytes[j] += 2
        else:
            frame_bytes[j] += 3
        j = j + 1
    frame_modified = bytes(frame_bytes)

    complete_name = os.path.join(save_path, file_name)
    print(complete_name)

    # Write bytes to a new wave audio file
    with wave.open(complete_name + ".wav", 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()

    decodeTime = "Decode time: " + str(round(time.time() - start, 2)) + "seconds"
    print(decodeTime)

    return decodeTime


# encode_lsb_2_bit('sample.wav', 'text.txt')