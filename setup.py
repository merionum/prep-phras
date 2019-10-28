from setuptools import setup
setup(
  name = 'pphrase',
  packages = ['pphrase'],
  version = '0.4',
  license='MIT', 
  description = 'Prepositional phrases extraction and semantics',
  author = 'Vadim Gudkov',
  author_email = 'vadim0006@gmail.com',
  url = 'https://github.com/merionum/pphrase',
  download_url = 'https://github.com/merionum/pphrase/archive/v_04.tar.gz',
  keywords = ['prepositional phrases', 'предложные конструкции', 'nlp'],
  install_requires=[
          'nltk',
          'spacy',
          'spacy_udpipe',
          'pymorphy2',
          'numpy',
      ],
  include_package_data=True,
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Topic :: Software Development :: Build Tools',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Programming Language :: Python :: Implementation :: CPython',
  ],
)
