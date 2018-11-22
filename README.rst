Data normalization/cleaning experiments
=======================================

This repository contains analyses and experiments
performed with the goal of normalizing/cleaning the SciELO data,
intended to find and fix unclean/inconsistent values
in their raw format,
as well as other similar issues,
mainly towards the fields that regards to the affiliations.

Contents of this repository ordered by creation date:

.. list-table::

  * - **Date**
    - **Description**
    - **Link**

  * - 2018-04-05
    - Grabbing article ``<aff>`` and ``<country>`` data
      with BeautifulSoup 4
    - `Notebook <experiments_2018-04-05.ipynb>`_

  * - 2018-04-19
    - Article XML parsing with ``ElementTree``/``libxml2``/``lxml``,
      using XPath/XSLT
    - `Notebook <experiments_2018-04-19.ipynb>`_

  * - 2018-04-26
    - Creating a table with data from ``<aff>``-``<contrib>`` pairs
      (front matter) in 25 XML files using ``lxml``
    - `Notebook <experiments_2018-04-26.ipynb>`_ /
      `CSV <affs_table_25.csv>`_

  * - 2018-05-03
    - Loading/cleaning/analyzing a table of manually normalized data,
      including a DBSCAN clustering model for the institution name
    - `Notebook <experiments_2018-05-03.ipynb>`_

  * - 2018-05-10
    - Looking for alternatives to the CSS/XPath/XSLT based XML parsing:
      ``xmltodict`` on article XML and fuzzy regex on custom paths
    - `Notebook <experiments_2018-05-10.ipynb>`_

  * - 2018-05-17
    - Getting tags that looks like
      ``<article-id>``, ``<aff>`` and ``<contrib>``
      using fuzzy regex / Levenshtein distance
    - `Notebook <experiments_2018-05-17.ipynb>`_

  * - 2018-06-04
    - CSV generation with `Clea <https://github.com/scieloorg/clea>`_
    - `Notebook <experiments_2018-06-04.ipynb>`_ /
      `CSV <https://drive.google.com/file/d/1XmBh6YlfPkB5WfYSolAMP1EA5e02jHQO/view?usp=sharing>`_

  * - 2018-06-07
    - Analysis of the ``contrib_type`` field from Clea's CSV output
    - `Notebook <experiments_2018-06-07.ipynb>`_

  * - 2018-06-14 to 2018-07-05
    - Country analysis of Clea's CSV output using graphs (NetworkX),
      including a substantial analysis of alternative libraries
      for country normalization/cleaning in Python/R/Ruby,
      resulting in a taxonomy/classification of techniques
      (exact match, regex, fuzzy, graphs)
    - `Notebook <experiments_2018-06_country.ipynb>`_

  * - 2018-07-05
    - Analysis of the country in the manual normalization CSV data
      using graphs
    - `Notebook <experiments_2018-07-05.ipynb>`_

  * - 2018-07-12
    - Creation of a CrossRef fetching script
      for all articles in a ``article_doi`` CSV column
      due to the presence of several DOI / PID empty fields
    - `Notebook <experiments_2018-07-12.ipynb>`_ /
      `Script <fetch_crossref.py>`_

  * - 2018-07-23
    - Matching and normalizing PID/DOI using Crossref data,
      besides a first experiment based on the SciELO's "XML debug" API
      to get the current article PID from its older PID
    - `Notebook <experiments_2018-07-23.ipynb>`_ /
      `Script <headers_listener_tornado.py>`_

  * - 2018-07-26
    - Crunching/crawling data from SciELO's search engine
      and the XML debug API, looking for a specific DOI / PID
    - `Notebook <experiments_2018-07-26.ipynb>`_

  * - 2018-08-02 to 2018-08-16
    - Normalizing the USP institutions ``orgname`` (faculty name)
      and ``orgdiv1`` (department name) fields
      filled in Brazilian Portuguese
    - `Notebook <experiments_2018-08_usp.ipynb>`_

  * - 2018-08-09
    - Summarization of the affiliations report from SciELO Analytics
    - `Notebook <2018-08-09_affiliations_report_summary.ipynb>`_

  * - 2018-08-23 to 2018-11-14
    - Latent Semantic Analysis (LSA) on the CSV data
      for predicting the country code,
      using k-Means, k-NN and random forest
    - `Notebook <experiments_2018-08_words_lsa.ipynb>`_