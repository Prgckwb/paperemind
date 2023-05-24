# paperemind
PythonSDK for retrieving article information from Semantic Scholar

## Installation
WIP

## Usage
The code below is under development and subject to destructive change.
```python
from rich import print

from paperemind import SemanticScholar


def main():
    ss = SemanticScholar()
    outputs = ss.search("Diffusion models for image generation")
    for i, paper in enumerate(outputs.data):
        print(f"[{i}] {paper.title}")


if __name__ == '__main__':
    main()
```

The result of executing the code is as follows:
```text
[0] Multilevel Diffusion: Infinite Dimensional Score-Based Diffusion Models for Image Generation
[1] DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation
[2] GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models
[3] Cascaded Diffusion Models for High Fidelity Image Generation
[4] Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation
[5] Swinv2-Imagen: Hierarchical Vision Transformer Diffusion Models for Text-to-Image Generation
[6] Implementing and Experimenting with Diffusion Models for Text-to-Image Generation
[7] Denoising diffusion probabilistic models for 3D medical image generation
[8] Exploring Discrete Diffusion Models for Image Captioning
[9] Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding
```
