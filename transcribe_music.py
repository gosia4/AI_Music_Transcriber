# transcribe_music.py

import librosa
import numpy as np
import pretty_midi

def extract_notes(audio_path, output_midi_path):
    y, sr = librosa.load(audio_path, sr=None)

    # Frequency extraction (FFT)
    fft = np.fft.fft(y)
    frequencies = np.fft.fftfreq(len(fft), 1/sr)

    # Example of note detection (simplified)
    notes = []
    for freq in frequencies:
        if freq > 0: 
            note_name = librosa.hz_to_note(freq)
            notes.append(note_name)

    # Creating MIDI files
    midi_data = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument(program=0)  # Piano

    # Add notes to MIDI file
    for i, note_name in enumerate(notes[:10]):  # Limit to 10 notes for example
        note_number = librosa.note_to_midi(note_name)
        note = pretty_midi.Note(
            velocity=100,  # Volume
            pitch=note_number,  # Note pitch
            start=i * 0.5,  # Start time
            end=(i + 1) * 0.5  # End time
        )
        instrument.notes.append(note)

    midi_data.instruments.append(instrument)
    midi_data.write(output_midi_path)
    print(f"Plik MIDI został zapisany jako {output_midi_path}")

if __name__ == "__main__":
    audio_path = "data/example.wav"
    output_midi_path = "data/example.mid"
    extract_notes(audio_path, output_midi_path)
