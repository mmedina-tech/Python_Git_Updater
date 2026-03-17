# Python_Git_Updater

A powerful cross-platform CLI tool for managing and updating multiple Git repositories simultaneously. Perfect for developers who work with multiple projects and need to keep them synchronized with minimal effort.

**Repository:** https://github.com/mmedina-tech/Python_Git_Updater

## Features

✨ **Bulk Operations**
- Update multiple Git repositories in one command
- Pull from all repositories simultaneously
- Push to all repositories at once
- Batch commit changes across multiple repos
- Check status of all repositories

🔧 **Repository Management**
- Clone repositories from a configuration file
- List branches across all repositories
- Cross-platform support (Windows, Linux, macOS)
- Detailed progress reporting
- Error handling and logging

## Requirements

- **Python 3.7+** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- Git must be available in your system PATH

## Installation

### Clone the Repository

```bash
git clone https://github.com/mmedina-tech/Python_Git_Updater.git
cd Python_Git_Updater
```

### Run Directly

No additional dependencies needed! Just use Python directly:

```bash
python main.py --help
```

### (Optional) Create a Shortcut

**Windows:**
```powershell
# Create a batch file (Windows)
echo @echo off >> git-updater.bat
echo cd /d %~dp0 >> git-updater.bat
echo python main.py %* >> git-updater.bat
```

**Linux/macOS:**
```bash
# Create an alias
echo "alias git-updater='python /path/to/Python_Git_Updater/main.py'" >> ~/.bashrc
source ~/.bashrc
```

## Commands

### `python main.py update`
Pull and push all repositories in a directory.

```bash
python main.py update --path C:\repos
python main.py update --path /home/user/projects --branch develop
```

**Options:**
- `--path` (required) - Directory containing git repositories
- `--branch` (optional) - Branch to update (default: main)

---

### `python main.py pull`
Pull latest changes from all repositories.

```bash
python main.py pull --path C:\repos
python main.py pull --path /home/user/projects --branch main
```

**Options:**
- `--path` (required) - Directory containing git repositories
- `--branch` (optional) - Branch to pull from (default: main)

---

### `python main.py push`
Push changes to all repositories.

```bash
python main.py push --path C:\repos
python main.py push --path /home/user/projects --branch develop
```

**Options:**
- `--path` (required) - Directory containing git repositories
- `--branch` (optional) - Branch to push to (default: main)

---

### `python main.py status`
Check the status of all repositories.

```bash
python main.py status --path C:\repos
python main.py status --path /home/user/projects
```

Shows:
- Current branch for each repository
- Number of uncommitted changes
- File-level changes (first 3 shown)

**Options:**
- `--path` (required) - Directory containing git repositories

---

### `python main.py commit`
Commit changes in all repositories.

```bash
python main.py commit --path C:\repos --message "Update dependencies"
python main.py commit --path /home/user/projects --message "Fix bugs" --all
```

**Options:**
- `--path` (required) - Directory containing git repositories
- `--message` (required) - Commit message
- `--all` (optional) - Stage all changes with `git add -A` before committing

---

### `python main.py branches`
List all branches in all repositories.

```bash
python main.py branches --path C:\repos
python main.py branches --path /home/user/projects
```

Shows:
- All branches (local and remote)
- Current branch marked with `●`

**Options:**
- `--path` (required) - Directory containing git repositories

---

### `python main.py clone`
Clone multiple repositories from a configuration file.

```bash
python main.py clone --config repos.json --path C:\repos
python main.py clone --config repos.json --path /home/user/projects
```

**Options:**
- `--config` (required) - Path to configuration file (JSON)
- `--path` (required) - Directory to clone repositories into

---

## Configuration File

For the `clone` command, create a `repos.json` file with your repository URLs:

```json
{
  "repositories": [
    "https://github.com/username/repo1.git",
    "https://github.com/username/repo2.git",
    "https://github.com/username/repo3.git",
    "git@github.com:username/private-repo.git"
  ]
}
```

### Example Usage

```bash
python main.py clone --config repos.json --path ./my-projects
```

## Usage Examples

### Daily Maintenance

```bash
# Pull all changes from main branch
python main.py pull --path C:\dev\projects

# Check status of all repos
python main.py status --path C:\dev\projects
```

### Bulk Updates

```bash
# Update all repositories (pull and push)
python main.py update --path C:\dev\projects

# Update a specific branch
python main.py update --path C:\dev\projects --branch develop
```

### Bulk Commits

```bash
# Commit with a message in all repos that have changes
python main.py commit --path C:\dev\projects --message "Automated update"

# Stage all changes first, then commit
python main.py commit --path C:\dev\projects --message "Major update" --all
```

### Setup New Development Environment

```bash
# 1. Create repos.json with your repositories
# 2. Clone all at once
python main.py clone --config repos.json --path C:\my-projects

# 3. Check status of everything
python main.py status --path C:\my-projects
```

## Troubleshooting

### "Git command not found"
**Solution:** Git is not installed or not in your PATH.
- Install Git from [git-scm.com](https://git-scm.com/downloads)
- Restart your terminal/IDE after installation

### "No Git repositories found"
**Solution:** Directory doesn't contain any `.git` folders
- Verify the path you provided
- Ensure repositories are directly in that folder (nested one level deep is supported)

### "Authentication failed" on push/pull
**Solution:** Git credentials not configured
- For HTTPS: Configure git credentials
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your@email.com"
  ```
- For SSH: Set up SSH keys with GitHub
  ```bash
  ssh-keygen -t ed25519 -C "your@email.com"
  ```

### Command syntax errors
**Solution:** Run with `--help` to see the correct syntax
```bash
python main.py <command> --help
python main.py update --help
```

## Project Structure

```
Python_Git_Updater/
├── main.py                          # Entry point
├── README.md                        # This file
├── .gitignore                       # Git ignore rules
└── git_updater/
    ├── __init__.py
    ├── commands/
    │   ├── __init__.py
    │   ├── repo_commands.py        # Repository operations
    │   └── git_commands.py         # Git utilities (clone, etc)
    └── utils/
        ├── __init__.py
        └── git_helper.py           # Git helper functions
```

## Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Test your changes
5. Commit with clear messages
6. Push to your fork
7. Open a Pull Request

### Ideas for Contributions

- [ ] Add dry-run mode
- [ ] Add logging to file
- [ ] Support for different git providers (GitLab, Bitbucket, etc)
- [ ] Configuration file support for default paths
- [ ] Progress bar for long operations
- [ ] Tag management across repos
- [ ] Stash management

## Performance Tips

- **Large number of repos?** The tool processes repos sequentially. Consider:
  - Organizing repos into subdirectories
  - Using the branch filter to speed up operations
  - Running the tool during off-peak hours for remote operations

- **Slow network?** Use `pull` instead of `update` to skip unnecessary pushes

- **Large repos?** Shallow clones aren't supported yet, but you can edit `git_helper.py` to add `--depth 1` flag

## Roadmap

- [ ] Parallel processing for faster bulk operations
- [ ] Configuration file support (default paths, branches)
- [ ] Web UI dashboard
- [ ] Task scheduling integration
- [ ] Advanced filtering and search
- [ ] Git merge automation

## License

MIT License - See LICENSE file for details

## Support

- **Issues?** Open an issue on [GitHub Issues](https://github.com/mmedina-tech/Python_Git_Updater/issues)
- **Questions?** Check existing issues or documentation
- **Feature requests?** Create an issue with the `enhancement` label

## Author

Created by [mmedina-tech](https://github.com/mmedina-tech)

---

**Made with ❤️ for developers who love automation**
