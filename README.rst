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

**MARu** is a morphological analyzer for Russian, written in Python, powered by machine learning and neural networks.

Installation
------------

::

    $ pipenv install maru

or just use `pip` (though you should definitely take a look at `pipenv <https://pipenv.readthedocs.io/en/latest/>`_).


What's in the Box?
------------------

.. image:: https://sociorocketnewsen.files.wordpress.com/2013/10/maru-top.jpg?w=580&h=305&crop=1

- ✨ Morphological analysis with contextual disambiguation using `Universal Dependencies <http://universaldependencies.org/u/feat/index.html>`_ tags.
- 🌈 Trained via various machine learning methods: linear model, CRF, deep neural network.
- 🔮 Speed/accuracy trade-off between different methods.
- 🍰 Vocabulary-based lemmatization, built on top of `pymorphy2 <https://github.com/kmike/pymorphy2>`_.


Usage
-----

First, create a `maru.analyzer.Analyzer <https://github.com/chomechome/maru/blob/master/maru/analyzer.py#L13-L36>`_ object using the factory method:

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

Other available taggers that you can pass to ``maru.get_analyzer`` are ``'linear'``, ``'rnn'``, and ``'pymorphy'``.
Another available lemmatizer is ``'dummy'`` (no actual lemmatization, slightly improves inference speed).

You can refer to the following table when choosing an algorithm to use:

+-----------------------------------------------------------------------------------------------------+
|                    Full tag accuracy (per token, per sentence) and inference speed                  |
+----------+--------+--------+--------+--------+--------+--------+--------+--------+------------------+
| Tagger   |   News (Lenta)  |   Social (VK)   | Literature (JZ) |       All       | Inference speed  |
+==========+========+========+========+========+========+========+========+========+==================+
| Pymorphy | 77.24% | 12.85% | 72.71% | 18.84% | 73.16% | 10.91% | 74.43% | 14.85% | 49000 tokens/sec |
+----------+--------+--------+--------+--------+--------+--------+--------+--------+------------------+
| Linear   | 95.00% | 61.73% | 91.64% | 59.51% | 93.00% | 57.87% | 93.26% | 59.62% | 26500 tokens/sec |
+----------+--------+--------+--------+--------+--------+--------+--------+--------+------------------+
| CRF      | 95.55% | 64.53% | 91.82% | 61.27% | 93.59% | 63.96% | 93.70% | 62.95% |  5500 tokens/sec |
+----------+--------+--------+--------+--------+--------+--------+--------+--------+------------------+
| RNN      | 97.65% | 79.33% | 95.43% | 75.88% | 95.84% | 73.60% | 96.34% | 76.14% |  1000 tokens/sec |
+----------+--------+--------+--------+--------+--------+--------+--------+--------+------------------+

Accuracy was measured on the `MorphoRuEval-2017 <https://github.com/dialogue-evaluation/morphoRuEval-2017>`_ test set.
Inference speed was estimated on a system with 32 GB RAM, Intel i7 6700K as CPU and GeForce GTX 1060 as GPU.
RNN performance is given for single sentence inference. An addition of batch inference in the future can greatly improve it.
