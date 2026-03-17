# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-16

### Added

- **Initial Release**
- `update` command - Pull and push all repositories
- `pull` command - Batch pull from all repositories
- `push` command - Batch push to all repositories
- `status` command - Check status of all repositories
- `commit` command - Batch commit changes across repositories
- `branches` command - List branches in all repositories
- `clone` command - Clone repositories from JSON configuration
- Cross-platform support (Windows, Linux, macOS)
- Comprehensive documentation and examples
- GitHub repository integration
- Error handling and logging

### Features

- Supports nested repository discovery (up to 1 level deep)
- Formatted output with visual indicators (✓, ✗, →)
- Detailed status reporting with file counts
- Configuration file support for bulk cloning
- Branch tracking across multiple repositories
- Progress feedback for each operation

## [Unreleased]

### Planned Features

- Parallel processing for faster bulk operations
- Dry-run mode to preview changes before execution
- Configuration file support for default paths and branches
- Logging to file
- Progress bars for long operations
- Web UI dashboard
- Support for different git providers (GitLab, Bitbucket)
- Tag management across repositories
- Stash management across repositories
- Task scheduling integration

### Known Issues

- Sequential processing (no parallel operations)
- Limited filesystem recursion depth
- No shallow clone support

---

## Version History

### [1.0.0]

**Release Date:** March 16, 2026

The inaugural release of Python_Git_Updater featuring all core functionality for bulk repository management.
