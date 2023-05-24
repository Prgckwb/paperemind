from rich import print

from paperemind import SemanticScholar


def main():
    ss = SemanticScholar()
    outputs = ss.search("Diffusion models for image generation")
    for i, paper in enumerate(outputs.data):
        print(f"[{i}] {paper.title}")


if __name__ == '__main__':
    main()
