# SynthID
SynthID-style encoder/decoder for robust video watermarking: extract frames, embed mid-freq DCT noise patterns, and rebuild the video. Decoder performs frequency analysis, noise correlation, heatmap visualization, and bit recovery. Marker survives cropping, compression, filters, resizing, screenshots, and screen recordings. 

# SynthID-Style Watermarking

This repository demonstrates a robust, frequency-based watermarking method for images and videos using a SynthID-inspired encoder/decoder pipeline. Google Developer working on that. 

## Overview

* **Encoder:** Embeds an invisible watermark into mid-frequency DCT bands using a structured noise pattern.
* **Decoder:** Recovers the embedded signal through frequency analysis and noise correlation.
* **Dual-Embed:** Ensures the watermark survives cropping, compression, resizing, filtering, screenshots, and screen recordings.

## Pipeline

**Input → Encoded → Visualized Marker**

| Original                | Invisible Marked                       | Visible Marker                                          |
| ----------------------- | -------------------------------------- | ------------------------------------------------------- |
| ![input.png](input.png) | ![input\_marked.png](input_marked.png) | ![input\_marked\_visible.png](input_marked_visible.png) |

## Features

* Robust mid-frequency watermark embedding
* Invisible to the human eye
* Decoder heatmap revealing marker structure
* Supports video (frame-wise) and images
* Metadata storage optional

## File Structure (Bild is Pic in German)

```
encoder_bild.py
decoder_bild.py
  input.png
  input_marked.png
  input_marked_visible.png
wartermarking.md
```

## License

MIT License — free for personal and commercial use.

## Contact

Contact: Leon Sateraa, IG@staatsberater
