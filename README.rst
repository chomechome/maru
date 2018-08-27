MARu: Morphological Analyzer for Russian
========================================


.. image:: https://img.shields.io/pypi/v/maru.svg
    :target: https://pypi.python.org/pypi/maru
    :alt: Package version

.. image:: https://img.shields.io/pypi/l/maru.svg
    :target: https://pypi.python.org/pypi/maru
    :alt: Package license

.. image:: https://img.shields.io/pypi/pyversions/maru.svg
    :target: https://pypi.python.org/pypi/maru
    :alt: Python versions

.. image:: https://travis-ci.org/chomechome/maru.svg?branch=master
    :target: https://travis-ci.org/chomechome/maru
    :alt: TravisCI status

.. image:: https://codecov.io/github/chomechome/maru/coverage.svg?branch=master
    :target: https://codecov.io/github/chomechome/maru
    :alt: Code coverage

---------------

**MARu** is a morphological analyzer for Russian, written in Python, backed by machine learning and neural networks.

Installation
------------

::

    $ pipenv install maru

or just use `pip` (though you should definitely take a look at `pipenv <https://pipenv.readthedocs.io/en/latest/>`_).


What's in the Box?
------------------

.. image:: https://sociorocketnewsen.files.wordpress.com/2013/10/maru-top.jpg?w=580&h=305&crop=1

- ✨✨✨ Morphological analysis with contextual disambiguation.
- 🌈🌈🌈 Trained via various machine learning methods: SVM, CRF, deep neural network.
- 🔮🔮🔮 Speed/accuracy trade-off between different methods.
- 💬💬💬 Vocabulary-based lemmatization, built on top of `pymorphy2 <https://github.com/kmike/pymorphy2>`_.


Usage
-------

First, create a `maru.analyzer.Analyzer` object using the factory method:

.. code-block:: python

    >> import maru
    >> analyzer = maru.get_analyzer(tagger='crf', lemmatizer='pymorphy')

Then, analyze some text:

.. code-block:: python

    >> analyzed = analyzer.analyze(['мама', 'мыла', 'раму'])  # note that this returns an iterator
    >> for morph in analyzed:
    ...     print(morph)
    ...
    Morph(word='мама', lemma='мама', tag=Tag(pos=NOUN,animacy=Anim,case=Nom,gender=Fem,number=Sing))
    Morph(word='мыла', lemma='мыть', tag=Tag(pos=VERB,aspect=Imp,gender=Fem,mood=Ind,number=Sing,tense=Past,verbform=Fin,voice=Act))
    Morph(word='раму', lemma='рама', tag=Tag(pos=NOUN,animacy=Inan,case=Acc,gender=Fem,number=Sing))

