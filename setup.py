import setuptools

setuptools.setup(
    name="pptx2md",
    version="0.0.1",
    author="sigilpunk",
    author_email="jskresl@gmail.com",
    packages=["pptx2md"],
    description="Suite of tools to convert PowerPoint Presentstions (.pptx) to other formats (.json, .md, .pptxt)",
    url="https://github.com/sigilpunk/pptx2md",
    license='MIT',
    python_requires='>=3.8',
    install_requires=['pathlib', 'python-pptx', 'tqdm']
)