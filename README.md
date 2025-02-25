# AI Music Transcriber

Final project for the Elements of AI course

## Summary
This project aims to create an AI tool that converts audio recordings of music into sheet music. The goal is to help musicians, students, and composers transcribe music more efficiently.

## Background
Transcribing music by ear is a time-consuming and challenging task, especially for complex pieces. This project solves the problem by automating the process using AI. My personal motivation is my passion for music and technology, and I believe this tool can make music more accessible to everyone.

## How is it used?
Users upload an audio file (e.g., MP3 or WAV) to the system. The AI analyzes the audio and generates a sheet music file (e.g., in MIDI or PDF format). The solution is ideal for musicians who want to learn new songs or composers who need to transcribe their ideas quickly.

## Data sources and AI methods
- **Data**: MusicNet Dataset (contains audio recordings paired with corresponding sheet music).
- **AI techniques**: 
  - Signal processing (e.g., Fourier transform to extract frequencies).
  - Deep learning (e.g., convolutional neural networks for pitch detection, recurrent neural networks for sequence modeling).

## Challenges
- The system may struggle with polyphonic music (multiple instruments or voices).
- Background noise in recordings can affect accuracy.
- Real-time transcription is computationally intensive.

## What next?
- Improve accuracy for complex music (e.g., orchestral pieces).
- Add support for real-time transcription (e.g., live performances).
- Integrate with music notation software (e.g., MuseScore, Sibelius).

## Acknowledgments
- MusicNet Dataset for providing labeled audio and sheet music data.
- Inspiration from similar projects like Google's Magenta.
