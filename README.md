# Python_Git_Updater

A cross-platform CLI tool that updates all remote repos with ease.

## Features

- Bulk update multiple Git repositories
- Batch pull, push, and commit operations
- Cross-platform support (Windows, Linux, macOS)
- Progress tracking and logging
- Configuration file support

## Installation

```bash
git clone <repo-url>
cd Python_Git_Updater
python main.py --help
```

## Usage

```bash
# Update all repos in a directory
python main.py update --path /path/to/repos

# Pull all repos
python main.py pull --path /path/to/repos

# Check status of all repos
python main.py status --path /path/to/repos
```

## Requirements

- Python 3.7+
- Git installed and in PATH

## License

MIT
