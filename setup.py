from setuptools import find_packages, setup

setup(
    name="upscaling",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "torch",
        "torchvision",
        "numpy",
        "opencv-python",
        "imageio"
    ],
)
