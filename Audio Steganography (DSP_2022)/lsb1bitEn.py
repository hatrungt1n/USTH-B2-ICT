import wave
import os
import time

def encode_lsb_1_bit(wavfile, textfile, save_path, file_name):
    start = time.time()
    # read wave audio file
    song = wave.open(wavfile, mode='rb')
    # Convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Text message
    f = open(textfile, "r")
    string = f.read()
    f.close()

    # Padding preprocess
    string = string + int((len(frame_bytes) - (len(string) * 8 * 8)) / 8) * "#"

    # Convert text to bit array
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))

    # Replace LSB of each byte of the audio data by one bit from the text bit array
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
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