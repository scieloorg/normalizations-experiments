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
    - `Notebook <experiments_2018-04-19.ipynb>`_ /
      `XML pack <https://drive.google.com/open?id=1ek_18qnBaEEvOkUdateMHhA9FExOT4An>`_

  * - 2018-04-26
    - Creating a table with data from ``<aff>``-``<contrib>`` pairs
      (front matter) in 25 XML files using ``lxml``
    - `Notebook <experiments_2018-04-26.ipynb>`_ /
      `CSV <affs_table_25.csv>`_

  * - 2018-05-03
    - Loading/cleaning/analyzing a table of manually normalized data,
      including a DBSCAN clustering model for the institution name
    - `Notebook <experiments_2018-05-03.ipynb>`_ /
      `Raw manual CSV <https://drive.google.com/open?id=1Y_5jtWKOBhBUXQIQBZSb4qz13nyOwdWO>`_ /
      `Manual CSV <https://drive.google.com/open?id=1-RImt4SMK1a2t_t4GfMWT5ciDNIDQvoQ>`_

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
      `File list <https://drive.google.com/open?id=1bYP5DRzSS4BmDeEUA3mQrhH117LfPk5q>`_ /
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
    - `Notebook <2018-08-09_affiliations_report_summary.ipynb>`_ /
      `Summary <https://drive.google.com/open?id=1TPlf5FmZeZuUVZI4QiEJFyyPS7f32v7g>`_

  * - 2018-08-23 to 2018-11-14
    - Latent Semantic Analysis (LSA) on the CSV data
      for predicting the country code,
      using k-Means, k-NN and random forest
    - `Notebook <experiments_2018-08_words_lsa.ipynb>`_

  * - 2018-11-22 to 2019-03-08
    - Experiments with word2vec
      to find the country code from a single string
      having the merged information of an affiliation-contributor pair
    - `Notebook <experiments_2018-11_word2vec.ipynb>`_ /
      `Example <2019-03-08_rf_w2v_example.ipynb>`_ /
      `Dump Dictionary <https://drive.google.com/open?id=1z4vAm2m3ANp48b2XnRtSlNDM2Gp4vrMX>`_ /
      `Dump W2V 200 <https://drive.google.com/open?id=1EEI-sY-nprjzQ1yyS11F_fhocAKzRpIt>`_ /
      `Dump W2V 1000 <https://drive.google.com/open?id=1_HeYOyjPlM6s1taoXSpG48XjIWd6A921>`_

  * - 2018-12-06 to 2018-12-13
    - Looking for articles' PIDs from USP/UNESP/UNICAMP (SciELO Brazil)
      by analyzing the distinct values
      that appear as the institution name
    - `Notebook <experiments_2018-12_sao_paulo.ipynb>`_ /
      `XLSX <https://drive.google.com/file/d/1KwpXe-E-WET9CiPp8YZqRjor1JcJeuP6/view>`_

  * - 2019-01-10 to 2019-02-21
    - Looking for articles from EMBRAPA
      and public state universities in SP (USP/UNESP/Unicamp)
      in the entire SciELO Network
      by analyzing the institution name, country, state and city,
      as well as the graph of authors and institutions
    - `Notebook <experiments_2019-02_usp_unicamp_unesp_embrapa.ipynb>`_ /
      `XLSX <https://drive.google.com/file/d/1d3WIFoftk15uzGrPkSDzqaPqnSNeOfqq/view>`_

  * - 2019-05-13 to 2019-06-05
    - Analysis of the trained "W2V 200" model using other XML files
    - `Notebook <experiments_2019-05_w2v_evaluation.ipynb>`_ /
      `List of training files <https://drive.google.com/open?id=1bYP5DRzSS4BmDeEUA3mQrhH117LfPk5q>`_ /
      `Script requirements <requirements.w2v_country.txt>`_ /
      `Script <w2v_country.py>`_ /
      `W2V 200 results CSV <https://drive.google.com/open?id=1JTjUfYfYnspH1DL_mNVcGvIYJqIp-fta>`_

  * - 2019-08-15
    - Number of days until the first access burst
    - `Notebook <2019-08-15_first_access_burst.ipynb>`_

  * - 2019-08-21
    - Analyzing accesses of a single journal
      with Ratchet and ArticleMeta
    - `Notebook <2019-08-21_ratchet_example.ipynb>`_

  * - 2019-11-14 onwards
    - Applying FastText directly on ISIS ISO data
    - `Notebook <2019-08-21_ratchet_example.ipynb>`_ /
      `ISO files <https://drive.google.com/open?id=101-oKPeKF2LM0L2uO_dYL9fp0eKOCE_->`_

List of files that aren't stored in this repository:

* Dataset of manually normalized data:
  `aff_norm_update.csv (raw) <https://drive.google.com/open?id=1Y_5jtWKOBhBUXQIQBZSb4qz13nyOwdWO>`_,
  `aff_n15.csv (fixed) <https://drive.google.com/open?id=1-RImt4SMK1a2t_t4GfMWT5ciDNIDQvoQ>`_

* `Clea <https://github.com/scieloorg/clea>`_'s 2018-06-04 CSV
  and the XML pack from which it was created:
  `selecao_xml_br.tgz <https://drive.google.com/open?id=1ek_18qnBaEEvOkUdateMHhA9FExOT4An>`_,
  `inner_join_2018-06-04.csv <https://drive.google.com/open?id=1XmBh6YlfPkB5WfYSolAMP1EA5e02jHQO>`_,
  `inner_join_2018-06-04_filenames.txt <https://drive.google.com/open?id=1bYP5DRzSS4BmDeEUA3mQrhH117LfPk5q>`_

* ISIS ISO dump:
  `2019-11-13_iso200.zip <https://drive.google.com/open?id=101-oKPeKF2LM0L2uO_dYL9fp0eKOCE_->`_

* Random forest models based on Word2Vec:
  `dictionary_w2v_both.dump <https://drive.google.com/open?id=1z4vAm2m3ANp48b2XnRtSlNDM2Gp4vrMX>`_,
  `rf_w2v_200.dump <https://drive.google.com/open?id=1EEI-sY-nprjzQ1yyS11F_fhocAKzRpIt>`_,
  `rf_w2v_1000.dump <https://drive.google.com/open?id=1_HeYOyjPlM6s1taoXSpG48XjIWd6A921>`_

* Results of applying the ``rf_w2v_200.dump`` model:
  `2019-05_w2v_country.csv <https://drive.google.com/open?id=1JTjUfYfYnspH1DL_mNVcGvIYJqIp-fta>`_

* Country summary CSV based on the reports
  from `SciELO Analytics <https://analytics.scielo.org/>`_
  (2018-06-10):
  `documents_affiliations_country_summary.csv <https://drive.google.com/open?id=1TPlf5FmZeZuUVZI4QiEJFyyPS7f32v7g>`_

* XLSX with articles' PIDs based on the reports
  from `SciELO Analytics <https://analytics.scielo.org/>`_
  (2018-12-10):
  `pids_network_2018-12-10_usp_unesp_unicamp_embrapa.xlsx <https://drive.google.com/file/d/1d3WIFoftk15uzGrPkSDzqaPqnSNeOfqq/view>`_,
  `pids_2018-12-10_usp_unesp_unicamp.xlsx <https://drive.google.com/file/d/1KwpXe-E-WET9CiPp8YZqRjor1JcJeuP6/view>`_

Packages with old `reports <https://analytics.scielo.org/w/reports>`_
from SciELO Analytics on which some experiment was based:

* `2018-06-10 (All) <https://drive.google.com/open?id=1-FMfu8e83uAjkAQUK8xhtm2L5hn10m51>`_
* `2018-11-10 (Brazil) <https://drive.google.com/open?id=1WItJXlNzrYkm9rUicsvenH5QgmU4n2MR>`_
* `2018-12-10 (Brazil and Network) <https://drive.google.com/open?id=1yxvrvFAy-L0ZV9Mm_NKXTV7ztA_nLAEh>`_
