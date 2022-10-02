import librosa, librosa.display, glob
import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew
import pandas as pd

kurtosis_music = []
skew_music = []
mean_music = []
sd_music = []
zero_crossing = []
zero_crossing_mean = []
zero_crossing_sd = []
spectral_centroids_mean = []
spectral_centroids_sd = []
spectral_rolloff_mean = []
spectral_rolloff_sd = []
mfccs1_mean = []
mfccs1_sd = []
mfccs2_mean = []
mfccs2_sd = []
mfccs3_mean = []
mfccs3_sd = []
mfccs4_mean = []
mfccs4_sd = []
mfccs5_mean = []
mfccs5_sd = []
mfccs6_mean = []
mfccs6_sd = []
mfccs7_mean = []
mfccs7_sd = []
mfccs8_mean = []
mfccs8_sd = []
mfccs9_mean = []
mfccs9_sd = []
mfccs10_mean = []
mfccs10_sd = []
mfccs11_mean = []
mfccs11_sd = []
mfccs12_mean = []
mfccs12_sd = []
mfccs13_mean = []
mfccs13_sd = []
mfccs14_mean = []
mfccs14_sd = []
mfccs15_mean = []
mfccs15_sd = []
mfccs16_mean = []
mfccs16_sd = []
mfccs17_mean = []
mfccs17_sd = []
mfccs18_mean = []
mfccs18_sd = []
mfccs19_mean = []
mfccs19_sd = []
mfccs20_mean = []
mfccs20_sd = []
chroma_stft1_mean = []
chroma_stft1_sd = []
chroma_stft2_mean = []
chroma_stft2_sd = []
chroma_stft3_mean = []
chroma_stft3_sd = []
chroma_stft4_mean = []
chroma_stft4_sd = []
chroma_stft5_mean = []
chroma_stft5_sd = []
chroma_stft6_mean = []
chroma_stft6_sd = []
chroma_stft7_mean = []
chroma_stft7_sd = []
chroma_stft8_mean = []
chroma_stft8_sd = []
chroma_stft9_mean = []
chroma_stft9_sd = []
chroma_stft10_mean = []
chroma_stft10_sd = []
chroma_stft11_mean = []
chroma_stft11_sd = []
chroma_stft12_mean = []
chroma_stft12_sd = []
spectral_bandwidth_2_mean = []
spectral_bandwidth_3_mean = []
spectral_bandwidth_4_mean = []
spectral_bandwidth_2_sd = []
spectral_bandwidth_3_sd = []
spectral_bandwidth_4_sd = []


for filename in glob.glob("./processed_music/*.wav"):
    #x: time series
    #sr: sampling rate
    x, sr = librosa.load(filename)
    kurtosis_music.append(kurtosis(x))
    skew_music.append(skew(x))
    mean_music.append(np.mean(x))
    sd_music.append(np.std(x))

    zero_cros = librosa.zero_crossings(x, pad=False)
    zero_crossing.append(sum(zero_cros))
    zero_crossing_mean.append(np.mean(zero_cros))
    zero_crossing_sd.append(np.std(zero_cros))

    spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)
    spectral_centroids_mean.append(np.mean(spectral_centroids))
    spectral_centroids_sd.append(np.std(spectral_centroids))

    spectral_rolloff = librosa.feature.spectral_rolloff(x, sr=sr)
    spectral_rolloff_mean.append(np.mean(spectral_rolloff))
    spectral_rolloff_sd.append(np.std(spectral_rolloff))

    mfccs = librosa.feature.mfcc(x, sr=sr)
    mfccs1_mean.append(np.mean(mfccs[0,:]))
    mfccs1_sd.append(np.std(mfccs[0,:]))
    mfccs2_mean.append(np.mean(mfccs[1,:]))
    mfccs2_sd.append(np.std(mfccs[1,:]))
    mfccs3_mean.append(np.mean(mfccs[2,:]))
    mfccs3_sd.append(np.std(mfccs[2,:]))
    mfccs4_mean.append(np.mean(mfccs[3,:]))
    mfccs4_sd.append(np.std(mfccs[3,:]))
    mfccs5_mean.append(np.mean(mfccs[4,:]))
    mfccs5_sd.append(np.std(mfccs[4,:]))
    mfccs6_mean.append(np.mean(mfccs[5,:]))
    mfccs6_sd.append(np.std(mfccs[5,:]))
    mfccs7_mean.append(np.mean(mfccs[6,:]))
    mfccs7_sd.append(np.std(mfccs[6,:]))
    mfccs8_mean.append(np.mean(mfccs[7,:]))
    mfccs8_sd.append(np.std(mfccs[7,:]))
    mfccs9_mean.append(np.mean(mfccs[8,:]))
    mfccs9_sd.append(np.std(mfccs[8,:]))
    mfccs10_mean.append(np.mean(mfccs[9,:]))
    mfccs10_sd.append(np.std(mfccs[9,:]))
    mfccs11_mean.append(np.mean(mfccs[10,:]))
    mfccs11_sd.append(np.std(mfccs[10,:]))
    mfccs12_mean.append(np.mean(mfccs[11,:]))
    mfccs12_sd.append(np.std(mfccs[11,:]))
    mfccs13_mean.append(np.mean(mfccs[12,:]))
    mfccs13_sd.append(np.std(mfccs[12,:]))
    mfccs14_mean.append(np.mean(mfccs[13,:]))
    mfccs14_sd.append(np.std(mfccs[13,:]))
    mfccs15_mean.append(np.mean(mfccs[14,:]))
    mfccs15_sd.append(np.std(mfccs[14,:]))
    mfccs16_mean.append(np.mean(mfccs[15,:]))
    mfccs16_sd.append(np.std(mfccs[15,:]))
    mfccs17_mean.append(np.mean(mfccs[16,:]))
    mfccs17_sd.append(np.std(mfccs[16,:]))
    mfccs18_mean.append(np.mean(mfccs[17,:]))
    mfccs18_sd.append(np.std(mfccs[17,:]))
    mfccs19_mean.append(np.mean(mfccs[18,:]))
    mfccs19_sd.append(np.std(mfccs[18,:]))
    mfccs20_mean.append(np.mean(mfccs[19,:]))
    mfccs20_sd.append(np.std(mfccs[19,:]))

    chroma_stft = librosa.feature.chroma_stft(x, sr)
    chroma_stft1_mean.append(np.mean(chroma_stft[0,:]))
    chroma_stft1_sd.append(np.std(chroma_stft[0,:]))
    chroma_stft2_mean.append(np.mean(chroma_stft[1,:]))
    chroma_stft2_sd.append(np.std(chroma_stft[1,:]))
    chroma_stft3_mean.append(np.mean(chroma_stft[2,:]))
    chroma_stft3_sd.append(np.std(chroma_stft[2,:]))
    chroma_stft4_mean.append(np.mean(chroma_stft[3,:]))
    chroma_stft4_sd.append(np.std(chroma_stft[3,:]))
    chroma_stft5_mean.append(np.mean(chroma_stft[4,:]))
    chroma_stft5_sd.append(np.std(chroma_stft[4,:]))
    chroma_stft6_mean.append(np.mean(chroma_stft[5,:]))
    chroma_stft6_sd.append(np.std(chroma_stft[5,:]))
    chroma_stft7_mean.append(np.mean(chroma_stft[6,:]))
    chroma_stft7_sd.append(np.std(chroma_stft[6,:]))
    chroma_stft8_mean.append(np.mean(chroma_stft[7,:]))
    chroma_stft8_sd.append(np.std(chroma_stft[7,:]))
    chroma_stft9_mean.append(np.mean(chroma_stft[8,:]))
    chroma_stft9_sd.append(np.std(chroma_stft[8,:]))
    chroma_stft10_mean.append(np.mean(chroma_stft[9,:]))
    chroma_stft10_sd.append(np.std(chroma_stft[9,:]))
    chroma_stft11_mean.append(np.mean(chroma_stft[10,:]))
    chroma_stft11_sd.append(np.std(chroma_stft[10,:]))
    chroma_stft12_mean.append(np.mean(chroma_stft[11,:]))
    chroma_stft12_sd.append(np.std(chroma_stft[11,:]))

    spectral_bandwidth_2 = librosa.feature.spectral_bandwidth(x+0.01, sr=sr)[0]
    spectral_bandwidth_3 = librosa.feature.spectral_bandwidth(x+0.01, sr=sr, p=3)[0]
    spectral_bandwidth_4 = librosa.feature.spectral_bandwidth(x+0.01, sr=sr, p=4)[0]
    spectral_bandwidth_2_mean.append(np.mean(spectral_bandwidth_2))
    spectral_bandwidth_3_mean.append(np.mean(spectral_bandwidth_3))
    spectral_bandwidth_4_mean.append(np.mean(spectral_bandwidth_4))
    spectral_bandwidth_2_sd.append(np.std(spectral_bandwidth_2))
    spectral_bandwidth_3_sd.append(np.std(spectral_bandwidth_3))
    spectral_bandwidth_4_sd.append(np.std(spectral_bandwidth_4))

    #chroma = librosa.feature.chroma_cens(y=x, sr=sr)
    #tempo, beat_frames = librosa.beat.beat_track(y=x, sr=sr)
    #contrast = librosa.feature.spectral_contrast(y=x, sr=sr)

df = pd.DataFrame({'name': glob.glob("./processed_music/*.wav"),
                   'kurtosis_music': kurtosis_music,
                   'skew_music': skew_music,
                   'mean_music': mean_music,
                   'sd_music': sd_music,
                   'zero_crossing': zero_crossing,
                   'zero_crossing_mean': zero_crossing_mean,
                   'zero_crossing_sd': zero_crossing_sd,
                   'spectral_centroids_mean': spectral_centroids_mean,
                   'spectral_centroids_sd': spectral_centroids_sd,
                   'spectral_rolloff_mean': spectral_rolloff_mean,
                   'spectral_rolloff_sd': spectral_rolloff_sd,
                   'mfccs1_mean': mfccs1_mean,
                   'mfccs1_sd': mfccs1_sd,
                   'mfccs2_mean': mfccs2_mean,
                   'mfccs2_sd': mfccs2_sd,
                   'mfccs3_mean': mfccs3_mean,
                   'mfccs3_sd': mfccs3_sd,
                   'mfccs4_mean': mfccs4_mean,
                   'mfccs4_sd': mfccs4_sd,
                   'mfccs5_mean': mfccs5_mean,
                   'mfccs5_sd': mfccs5_sd,
                   'mfccs6_mean': mfccs6_mean,
                   'mfccs6_sd': mfccs6_sd,
                   'mfccs7_mean': mfccs7_mean,
                   'mfccs7_sd': mfccs7_sd,
                   'mfccs8_mean': mfccs8_mean,
                   'mfccs8_sd': mfccs8_sd,
                   'mfccs9_mean': mfccs9_mean,
                   'mfccs9_sd': mfccs9_sd,
                   'mfccs10_mean': mfccs10_mean,
                   'mfccs10_sd': mfccs10_sd,
                   'mfccs11_mean': mfccs11_mean,
                   'mfccs11_sd': mfccs11_sd,
                   'mfccs12_mean': mfccs12_mean,
                   'mfccs12_sd': mfccs12_sd,
                   'mfccs13_mean': mfccs13_mean,
                   'mfccs13_sd': mfccs13_sd,
                   'mfccs14_mean': mfccs14_mean,
                   'mfccs14_sd': mfccs14_sd,
                   'mfccs15_mean': mfccs15_mean,
                   'mfccs15_sd': mfccs15_sd,
                   'mfccs16_mean': mfccs16_mean,
                   'mfccs16_sd': mfccs16_sd,
                   'mfccs17_mean': mfccs17_mean,
                   'mfccs17_sd': mfccs17_sd,
                   'mfccs18_mean': mfccs18_mean,
                   'mfccs18_sd': mfccs18_sd,
                   'mfccs19_mean': mfccs19_mean,
                   'mfccs19_sd': mfccs19_sd,
                   'mfccs20_mean': mfccs20_mean,
                   'mfccs20_sd': mfccs20_sd,
                   'spectral_bandwidth_2_mean': spectral_bandwidth_2_mean,
                   'spectral_bandwidth_3_mean': spectral_bandwidth_3_mean,
                   'spectral_bandwidth_4_mean': spectral_bandwidth_4_mean,
                   'spectral_bandwidth_2_sd': spectral_bandwidth_2_sd,
                   'spectral_bandwidth_3_sd': spectral_bandwidth_3_sd,
                   'spectral_bandwidth_4_sd': spectral_bandwidth_4_sd,
                   'chroma_stft1_mean': chroma_stft1_mean,
                   'chroma_stft1_sd': chroma_stft1_sd,
                   'chroma_stft2_mean': chroma_stft2_mean,
                   'chroma_stft2_sd': chroma_stft2_sd,
                   'chroma_stft3_mean': chroma_stft3_mean,
                   'chroma_stft3_sd': chroma_stft3_sd,
                   'chroma_stft4_mean': chroma_stft4_mean,
                   'chroma_stft4_sd': chroma_stft4_sd,
                   'chroma_stft5_mean': chroma_stft5_mean,
                   'chroma_stft5_sd': chroma_stft5_sd,
                   'chroma_stft6_mean': chroma_stft6_mean,
                   'chroma_stft6_sd': chroma_stft6_sd,
                   'chroma_stft7_mean': chroma_stft7_mean,
                   'chroma_stft7_sd': chroma_stft7_sd,
                   'chroma_stft8_mean': chroma_stft8_mean,
                   'chroma_stft8_sd': chroma_stft8_sd,
                   'chroma_stft9_mean': chroma_stft9_mean,
                   'chroma_stft9_sd': chroma_stft9_sd,
                   'chroma_stft10_mean': chroma_stft10_mean,
                   'chroma_stft10_sd': chroma_stft10_sd,
                   'chroma_stft11_mean': chroma_stft11_mean,
                   'chroma_stft11_sd': chroma_stft11_sd,
                   'chroma_stft12_mean': chroma_stft12_mean,
                   'chroma_stft12_sd': chroma_stft12_sd})
compression_opts = dict(method='zip',
                        archive_name='out.csv')
df.to_csv('out.zip', index=False,
          compression=compression_opts)