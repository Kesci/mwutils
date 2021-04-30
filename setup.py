import setuptools

setuptools.setup(
    name="mwutils",
    version="0.4.7-post1",
    author="heywhale.com",
    description="use in mw",
    url="https://github.com/kesci/mwutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["PyJWT", "requests", "pynvml", "psutil"],
    python_requires='>=3.6',
)
