# Datasette

Datasette is an open source tool for exploring and publishing structured data. It turns SQLite databases into an interactive website and a JSON API, making data easy to browse, query, and share.

Website: https://datasette.io

## What is Datasette?

Datasette takes structured data and makes it usable.

Given a SQLite database, Datasette automatically provides:
- A clean web interface for humans
- A JSON API for machines
- SQL-powered querying without backend code
- A deployable, shareable data app

It is designed to work out of the box with minimal configuration.

## Why Datasette?

Most data lives in files or databases that are hard to explore and harder to share.

Datasette solves this by:
- Eliminating custom backend work
- Making data immediately interactive
- Exposing APIs automatically
- Scaling from small datasets to large public collections

It is commonly used for data journalism, research, civic data, internal tools, and open data publishing.

## How it works

```
User
 |
 v
Browser / API Client
 |
 v
Datasette Server
 - Web UI
 - JSON API
 - Query Engine
 |
 v
SQLite Databases
```

Datasette runs directly against SQLite databases and translates queries into fast, read-only responses.

## Core features

- Interactive table browsing
- Filtering, sorting, and faceting
- JSON API for every table and query
- SQL query support
- Plugin system for extensibility
- Simple local and cloud deployment

## Getting started

Install Datasette:

```
pip install datasette
```

Run it against a database:

```
datasette mydata.db
```

Open your browser at:

```
http://localhost:8001
```

## Deployment

Datasette can run:
- Locally
- In Docker
- On cloud platforms using built-in publish commands

No managed backend or database service required.

## Plugins

Datasette supports plugins that can:
- Add authentication and permissions
- Customize the UI
- Add visualizations
- Extend API behavior

Plugins allow Datasette to adapt to many use cases without changing the core.

## Typical project structure

```
.
├── data
│   └── dataset.db
├── plugins
├── docs
└── README.md
```

## Contributing

Datasette is open source.

To contribute:
- Fork the repository
- Create a branch
- Add tests and documentation
- Submit a pull request

## License

Datasette is open source software. See the repository for license details.

## About

Datasette was built to make structured data easy to explore, publish, and share. It focuses on simplicity, transparency, and flexibility, allowing teams and individuals to turn data into something people can actually use.
