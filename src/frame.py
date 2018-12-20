from src import constants
from src import utilities as util


class Frame:
    def __init__(self, total_content):
        frame_header = util.dec_to_bin(
            int.from_bytes(total_content[0:4], "big"))[::-1]
        self.marker = frame_header[0:11]
        self.mpeg_index = frame_header[11:13]
        self.layer_index = frame_header[13:15]
        self.protection = frame_header[15]
        self.bitrate_index = frame_header[16:20]
        self.bitrate = constants.BITRATES[self.bitrate_index]
        self.sample_rate_index = frame_header[20:22]
        self.sample_rate = constants.SAMPLERATES[self.sample_rate_index]
        self.padding = frame_header[22]
        self.private = frame_header[23]
        self.channel = frame_header[24:26]
        self.extension = frame_header[26:28]
        self.copyright = frame_header[28]
        self.original = frame_header[29]
        self.emphasis = frame_header[30:32]
        self.frame_size = int(
            (144 * self.bitrate * 1000) / self.sample_rate) + int(self.padding)
        self.frame = total_content[4:self.frame_size]
