<h1 align="right">
    <img alt="UnmaskedDocumentsUpdate" title="#UnmaskedDocumentsUpdate" src="https://www.brain.agr.br/images/logo.png" width="200px" />
</h1>

# unmasked-documents-update Documentation

## Status

![](https://img.shields.io/badge/Production-%234ea94b.svg?&style=for-the-badge)

## Introduction

unmasked-documents-update is a crawler designed download and update our public database related to Culture UnmaskedDocuments information.

## Table of Contents

- [unmasked-documents-update Documentation](#unmasked-documents-update-documentation)
  - [Status](#status)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [What is the crawler](#what-is-the-crawler)
  - [Technologies](#technologies)
  - [How To Use](#how-to-use)
    - [Local Dependency Setup](#local-dependency-setup)
    - [Installation](#installation)
    - [Environment Variables](#environment-variables)
    - [Requirements dataset](#requirements-dataset)
    - [Usage](#usage)
    - [Exceptions](#exceptions)
  - [New Features and Improvements](#new-features-and-improvements)
  - [About](#about)

## What is the crawler

The crawler is an automated web scraping program. It is given a set of URLs, and from there it will follow a specific set of instructions to crawl the website and extract data from its pages and/or endpoints.


## Technologies

This project was developed with the following technologies:

- [bg-update](https://github.com/brain-ag/brainag-update)
- [Python-dotenv](https://pypi.org/project/python-dotenv)
- [requests](https://docs.python-requests.org)
- [boto3](https://boto3.readthedocs.io)
- [peewee](http://docs.peewee-orm.com)
- [psycopg2-binary](https://www.psycopg.org)
- [pytz](https://pypi.org/project/pytz)
- [tqdm](https://github.com/tqdm/tqdm)

## How To Use

### Local Dependency Setup

To clone and run this application, you'll need the following dependencies installed on your computer.

- Required:
  - [Git](https://git-scm.com)
  - [Python](https://www.python.org)
  - [Pip](https://pypi.org/project/pip)

### Installation

From your command line:

```bash
# Clone this repository
$ git clone git@github.com:brain-ag/unmasked-documents-update.git

# Go into the repository
$ cd unmasked-documents-update 

# Create virtual environment folder
$ mkdir venv

# Create virtual environment files
$ virtualenv venv

# Activate virtual env
$ source venv/bin/activate

# Install packages
$ python -m pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
```

### Environment Variables

You will also need to create a .env file on the root of your project, and create variables as shown bellow:

```env
DB_DATABASE=<database name>
DB_USER=<user>
DB_PASSWORD=<password>
DB_HOST=<host>
DB_PORT=<port>

S3_BUCKET=<s3 bucket>

```
### Requirements dataset
Alert: Don't perform this step if you are using brain_public database.
* ibge_cities
  * required fields: estado_cod, municipio_ibge_cod

### Usage
1. Download culture file from site https://sidra.ibge.gov.br/tabela/1612

2. Upload file to S3 using:

```
# Upload
$ python update.py upload ./app/data/exemplo-tabela1612.csv
```

3. ON SERVER : Download file to S3 using:
```
# Download
$ python update.py download unmasked-documents/trigo-tabela1612.csv
```

3. ON SERVER : run script passing the path and the desired culture name:
```
# Update database
$ python update.py ./app/data/20220628-092701-trigo-tabela1612.csv wheat
```

## New Features and Improvements

**_Please_, feel free to make any contributions you feel will make unmasked-documents-Update Documentation better.**

For adding new features or improvements, please follow instructions below:

- **Create a branch with your feature: `git checkout -b my-feature`**
- **Commit changes: `git commit -m 'feat: My new feature'`**
- **Make a push to your branch: `git push origin my-feature`**
- **Submit all pull requests to the develop(dev) branch**

## About

Ibama-Update is guided and supported by the Brain [Developer Team](mailto:guilherme.costa@br.experian.com).<br/>
It is maintained by Brain, Inc. The names and logos are trademarks of Brain, Inc.
