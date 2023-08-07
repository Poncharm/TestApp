import mne

def process_eeg(eeg_file):
    raw_data = mne.io.read_raw_edf(eeg_file, preload=True) # encoding='latin1'
    processed_eeg = raw_data.get_data()*(10**6)
    sfreq = raw_data.info['sfreq']
    time_range = raw_data.times

    return processed_eeg, time_range, sfreq
