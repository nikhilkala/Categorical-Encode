from distutils.core import setup
setup(
  name = 'categorical_encode',         
  packages = ['categorical_encode'],
  version = '0.1',     
  license='MIT',
  description = 'This Library converts categorical data of any kind {integer, float, strings} into discrete values{1,2,3... # Classes}.',
  author = 'Nikhil Kala',                   
  author_email = 'nikhilkala8@gmail.com',      
  url = 'https://github.com/nikhilkala/Categorical-Encode',  
  download_url = 'https://github.com/nikhilkala/Categorical-Encode/archive/v0.1.tar.gz',
  keywords = ['Machine Learning', 'Categorical Data', 'Encoding', 'Deep Learning','Pandas', 'DataFrame', 'Normalization'],  
  install_requires=[            
          'pandas',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)
