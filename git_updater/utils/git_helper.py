"""Git helper functions for repository operations."""

import subprocess
from pathlib import Path


class GitError(Exception):
    """Custom exception for git operations."""
    pass


def is_git_repo(path):
    """Check if a directory is a git repository."""
    git_dir = Path(path) / '.git'
    return git_dir.exists()


def get_current_branch(repo_path):
    """Get the current branch name."""
    try:
        result = subprocess.run(
            ['git', '-C', str(repo_path), 'rev-parse', '--abbrev-ref', 'HEAD'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def get_status(repo_path):
    """Get git status of repository."""
    try:
        result = subprocess.run(
            ['git', '-C', str(repo_path), 'status', '--porcelain'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def pull_repo(repo_path, branch='main'):
    """Pull changes from remote."""
    try:
        subprocess.run(
            ['git', '-C', str(repo_path), 'pull', 'origin', branch],
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        raise GitError(f"Pull failed: {e.stderr}")


def push_repo(repo_path, branch='main'):
    """Push changes to remote."""
    try:
        subprocess.run(
            ['git', '-C', str(repo_path), 'push', 'origin', branch],
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        raise GitError(f"Push failed: {e.stderr}")


def commit_changes(repo_path, message, stage_all=False):
    """Commit changes in repository."""
    try:
        if stage_all:
            subprocess.run(
                ['git', '-C', str(repo_path), 'add', '-A'],
                capture_output=True,
                text=True,
                check=True
            )
        
        subprocess.run(
            ['git', '-C', str(repo_path), 'commit', '-m', message],
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        if 'nothing to commit' in e.stderr:
            return False  # Nothing to commit
        raise GitError(f"Commit failed: {e.stderr}")


def get_branches(repo_path):
    """Get list of branches."""
    try:
        result = subprocess.run(
            ['git', '-C', str(repo_path), 'branch', '-a'],
            capture_output=True,
            text=True,
            check=True
        )
        branches = [b.strip() for b in result.stdout.split('\n') if b.strip()]
        return branches
    except subprocess.CalledProcessError:
        return []


def clone_repo(url, path):
    """Clone a repository."""
    try:
        subprocess.run(
            ['git', 'clone', url, str(path)],
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        raise GitError(f"Clone failed: {e.stderr}")


def find_git_repos(root_path):
    """Find all git repositories in a directory."""
    root = Path(root_path)
    repos = []
    
    for item in root.iterdir():
        if item.is_dir() and is_git_repo(item):
            repos.append(item)
        elif item.is_dir() and not item.name.startswith('.'):
            # Recursively search subdirectories (one level deep)
            repos.extend(find_git_repos(item))
    
    return sorted(repos)
