from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

reqs = ['absl-py==0.13.0', 'aiohttp==3.7.4', 'alabaster==0.7.12', 'anyio==2.2.0', 'appdirs==1.4.4', 'argcomplete==1.12.3', 'argh==0.26.2', 'argon2-cffi==20.1.0', 'arrow==0.13.1', 'astor==0.8.1', 'astroid==2.6.6', 'astropy==4.3.1', 'async-generator==1.10', 'async-timeout==3.0.1', 'atomicwrites==1.4.0', 'attrs==21.2.0', 'autopep8==1.5.6', 'Babel==2.9.1', 'backcall==0.2.0', 'binaryornot==0.4.4', 'black==19.10b0', 'bleach==4.0.0', 'blinker==1.4', 'bokeh==2.3.3', 'Bottleneck==1.3.2', 'branca==0.4.2', 'brotlipy==0.7.0', 'cached-property==1.5.2', 'cachetools==4.2.2', 'cerebralcortex-kernel==3.3.16', 'certifi==2021.5.30', 'cffi==1.14.0', 'chardet==3.0.4', 'charset-normalizer==2.0.4', 'click==8.0.1', 'cloudpickle==1.1.1', 'colorlover==0.3.0', 'cookiecutter==1.7.2', 'coverage==5.5', 'coveralls==3.2.0', 'cryptography==3.4.7', 'cufflinks==0.17.3', 'cycler==0.10.0', 'Cython==0.29.24', 'datascience==0.17.0', 'debugpy==1.4.1', 'decorator==5.0.9', 'defusedxml==0.7.1', 'diff-match-patch==20200713', 'docopt==0.6.2', 'docutils==0.17.1', 'entrypoints==0.3', 'flake8==3.9.0', 'folium==0.12.1', 'fonttools==4.25.0', 'future==0.18.2', 'gast==0.2.2', 'gatspy==0.3', 'geographiclib==1.52', 'geopy==2.2.0', 'google-auth==1.33.0', 'google-auth-oauthlib==0.4.4', 'google-pasta==0.2.0', 'graphviz==0.16', 'grpcio==1.36.1', 'h5py==3.2.1', 'hdfs3==0.3.1', 'idna==3.2', 'imagesize==1.2.0', 'importlib-metadata==3.10.0', 'inflection==0.5.1', 'influxdb==5.3.1', 'iniconfig==1.1.1', 'intervaltree==3.1.0', 'ipykernel==6.2.0', 'ipython==7.26.0', 'ipython-genutils==0.2.0', 'ipywidgets==7.6.4', 'isort==5.9.3', 'jedi==0.17.2', 'jeepney==0.7.1', 'Jinja2==2.11.3', 'jinja2-time==0.2.0', 'joblib==1.0.1', 'json5==0.9.6', 'jsonschema==3.2.0', 'jupyter-client==7.0.1', 'jupyter-core==4.7.1', 'jupyter-server==1.4.1', 'jupyterlab==3.1.7', 'jupyterlab-pygments==0.1.2', 'jupyterlab-server==2.7.2', 'jupyterlab-widgets==1.0.1', 'Keras-Applications==1.0.8', 'Keras-Preprocessing==1.1.2', 'keyring==23.0.1', 'kiwisolver==1.3.1', 'lazy-object-proxy==1.6.0', 'Markdown==3.3.4', 'MarkupSafe==1.1.1', 'matplotlib==3.4.2', 'matplotlib-inline==0.1.2', 'mccabe==0.6.1', 'mistune==0.8.4', 'msgpack==1.0.2', 'multidict==5.1.0', 'munkres==1.1.4', 'mypy-extensions==0.4.3', 'nbclassic==0.2.6', 'nbclient==0.5.3', 'nbconvert==6.1.0', 'nbformat==5.1.3', 'nbsphinx==0.8.7', 'nest-asyncio==1.5.1', 'networkx==2.6.2', 'neurokit2==0.1.0', 'notebook==6.4.3', 'numexpr==2.7.3', 'numpy==1.19.2', 'numpydoc==1.1.0', 'oauthlib==3.1.1', 'olefile==0.46', 'opt-einsum==3.3.0', 'packaging==21.0', 'pandas==1.1.5', 'pandocfilters==1.4.3', 'parso==0.7.0', 'pathspec==0.7.0', 'pennprov==2.2.9', 'pexpect==4.8.0', 'pickleshare==0.7.5', 'Pillow==8.3.1', 'pip==21.2.2', 'plotly==5.1.0', 'pluggy==0.13.1', 'poyo==0.5.0', 'prometheus-client==0.11.0', 'prompt-toolkit==3.0.17', 'protobuf==3.11.2', 'psutil==5.8.0', 'ptyprocess==0.7.0', 'py==1.10.0', 'py-ecg-detectors==1.0.2', 'py4j==0.10.9', 'pyarrow==4.0.1', 'pyasn1==0.4.8', 'pyasn1-modules==0.2.8', 'pycodestyle==2.6.0', 'pycparser==2.20', 'pydocstyle==6.1.1', 'pydot==1.4.1', 'pyerfa==1.7.3', 'pyflakes==2.2.0', 'Pygments==2.10.0', 'PyJWT==2.1.0', 'pylint==2.9.6', 'pyls-black==0.4.6', 'pyls-spyder==0.3.2', 'pyOpenSSL==20.0.1', 'pyparsing==2.4.7', 'pyrsistent==0.17.3', 'PySocks==1.7.1', 'pyspark==3.1.2', 'pytest==6.2.5', 'python-dateutil==2.8.2', 'python-jsonrpc-server==0.4.0', 'python-language-server==0.36.2', 'python-slugify==5.0.2', 'pytz==2021.1', 'PyWavelets==1.1.1', 'pyxdg==0.27', 'PyYAML==5.4.1', 'pyzmq==22.2.1', 'QDarkStyle==3.0.2', 'qstylizer==0.1.10', 'QtAwesome==1.0.2', 'qtconsole==5.1.0', 'QtPy==1.10.0', 'regex==2021.8.3', 'requests==2.26.0', 'requests-oauthlib==1.3.0', 'rope==0.19.0', 'rsa==4.7.2', 'Rtree==0.9.7', 'scikit-learn==0.22.2.post1', 'scipy==1.7.1', 'seaborn==0.11.2', 'SecretStorage==3.3.1', 'Send2Trash==1.5.0', 'setuptools==52.0.0.post20210125', 'Shapely==1.7.1', 'six==1.16.0', 'sniffio==1.2.0', 'snowballstemmer==2.1.0', 'sortedcontainers==2.4.0', 'Sphinx==4.0.2', 'sphinxcontrib-applehelp==1.0.2', 'sphinxcontrib-devhelp==1.0.2', 'sphinxcontrib-htmlhelp==2.0.0', 'sphinxcontrib-jsmath==1.0.1', 'sphinxcontrib-qthelp==1.0.3', 'sphinxcontrib-serializinghtml==1.1.5', 'spyder==5.0.5', 'spyder-kernels==2.0.5', 'SQLAlchemy==1.3.24', 'SQLAlchemy-Utils==0.37.8', 'tenacity==8.0.1', 'tensorboard==2.4.0', 'tensorboard-plugin-wit==1.6.0', 'tensorflow==2.1.0', 'tensorflow-addons==0.14.0', 'tensorflow-estimator==2.1.0', 'tensorflow-probability==0.8.0rc0', 'termcolor==1.1.0', 'terminado==0.9.4', 'testpath==0.5.0', 'text-unidecode==1.3', 'textdistance==4.2.1', 'threadpoolctl==2.2.0', 'three-merge==0.1.1', 'tinycss==0.4', 'toml==0.10.2', 'tornado==6.1', 'traitlets==5.0.5', 'typed-ast==1.4.3', 'typeguard==2.12.1', 'typing-extensions==3.10.0.0', 'ujson==4.0.2', 'Unidecode==1.2.0', 'urllib3==1.26.6', 'watchdog==2.1.3', 'wcwidth==0.2.5', 'webencodings==0.5.1', 'Werkzeug==1.0.1', 'wheel==0.37.0', 'whichcraft==0.6.1', 'widgetsnbextension==3.5.1', 'wrapt==1.12.1', 'wurlitzer==2.1.1', 'yapf==0.31.0', 'yarl==1.6.3', 'zipp==3.5.0']

# Get the long description from the README file
long_description= ("A hierarchical generative model for cardiological signals"
                    "(PPG,ECG etc.) that keeps the physiological"
                    " characteristics intact.")

if __name__ == '__main__':
    setup(
        name="CardioGen",

        version='1.0.0',

        package_data={'': ['default.yml']},

        description=("A hierarchical generative model for cardiological signals"
                    "(PPG,ECG etc.) that keeps the physiological"
                    " characteristics intact."),
        long_description_content_type='text/markdown',
        long_description=long_description,

        author='https://sense-lab-osu.github.io/',
        author_email='agarwal.270@buckeyemail.osu.edu',

        license='BSD3',
        url = 'https://github.com/SENSE-Lab-OSU/cardio_gen_model/blob/master/LICENSE',


        classifiers=[

            'Development Status :: 5 - Production/Stable',

            'Intended Audience :: Healthcare Industry',
            'Intended Audience :: Science/Research',

            'License :: OSI Approved :: BSD License',

            'Natural Language :: English',

            'Programming Language :: Python :: 3',

            'Topic :: Scientific/Engineering :: Information Analysis',
            'Topic :: System :: Distributed Computing'
        ],

        keywords='mResearch machine-learning deep-learning GAN generative-model',

        # You can just specify the packages manually here if your project is
        # simple. Or you can use find_packages().
        packages=find_packages(exclude=['contrib', 'docs', 'tests','Examples']),

        # List run-time dependencies here.  These will be installed by pip when
        # your project is installed. For an analysis of "install_requires" vs pip's
        # requirements files see:
        # https://packaging.python.org/en/latest/requirements.html
        install_requires=reqs,

    )