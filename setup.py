from setuptools import setup, find_packages
import os
import sys

version = '0.0.0'
setup(name='spiga',
      version=version,
      description='SPIGA: Shape Preserving Facial Landmarks with Graph Attention Networks.',
      author='Naveen Gupta',
      author_email='naveen.gupta@unscript.ai',
      license='Apache License 2.0',
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6'
      )


def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(src_path)
    sys.path.insert(0, src_path)


if __name__ == "__main__":
    print(find_packages())
    setup_package()