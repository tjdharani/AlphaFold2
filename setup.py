from setuptools import setup, find_packages

setup(
    name = 'alphafold2-pytorch',
    packages = find_packages(),
    version = '0.4.32',
    license='MIT',
    description = 'AlphaFold2 - Pytorch',
    long_description_context_type = 'text/markdown',
    author = 'credit : Phil Wang', 
    author_email = 'a@mail.com',
    url = 'https://github.com/tjdharani/AlphaFold2',
    Keywords = [
        'artificial intelligence',
        'attention mechanism',
        'protein folding'
    ],
    install_requires=[
        'einops>=0.3',
        'En-transformer>=0.2.3',
        'invariant-point-attention',
        'mdtraj>=1.8',
        'numpy',
        'proDy',
        'pytorch3d',
        'requests',
        'sidechainnet',
        'torch>=1.6',
        'transformers',
        'tqdm',
        'biopython',
        'mp-nerf>=0.1.5'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)