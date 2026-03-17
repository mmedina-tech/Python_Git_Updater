"""Git helper functions for repository operations."""

import subprocess
import logging
from pathlib import Path


logger = logging.getLogger(__name__)


class GitError(Exception):
    """Custom exception for git operations."""
    pass


# Global dry-run flag
_DRY_RUN = False


def set_dry_run(enabled):
    """Set dry-run mode globally."""
    global _DRY_RUN
    _DRY_RUN = enabled


def is_dry_run():
    """Check if dry-run mode is enabled."""
    return _DRY_RUN


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
    """Pull changes from remote.
    
    Args:
        repo_path: Path to repository
        branch: Branch to pull
    
    Returns:
        True if successful, False if dry-run
    
    Raises:
        GitError: If pull fails
    """
    if _DRY_RUN:
        logger.info(f"[DRY-RUN] Would pull from origin/{branch} in {repo_path}")
        return False
    
    try:
        subprocess.run(
            ['git', '-C', str(repo_path), 'pull', 'origin', branch],
            capture_output=True,
            text=True,
            check=True
        )
        logger.info(f"Pulled from origin/{branch}: {repo_path}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Pull failed in {repo_path}: {e.stderr}")
        raise GitError(f"Pull failed: {e.stderr}")


def push_repo(repo_path, branch='main'):
    """Push changes to remote.
    
    Args:
        repo_path: Path to repository
        branch: Branch to push
    
    Returns:
        True if successful, False if dry-run
    
    Raises:
        GitError: If push fails
    """
    if _DRY_RUN:
        logger.info(f"[DRY-RUN] Would push to origin/{branch} in {repo_path}")
        return False
    
    try:
        subprocess.run(
            ['git', '-C', str(repo_path), 'push', 'origin', branch],
            capture_output=True,
            text=True,
            check=True
        )
        logger.info(f"Pushed to origin/{branch}: {repo_path}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Push failed in {repo_path}: {e.stderr}")
        raise GitError(f"Push failed: {e.stderr}")


def commit_changes(repo_path, message, stage_all=False):
    """Commit changes in repository.
    
    Args:
        repo_path: Path to repository
        message: Commit message
        stage_all: Whether to stage all changes
    
    Returns:
        True if committed, False if no changes or dry-run
    
    Raises:
        GitError: If commit fails
    """
    if _DRY_RUN:
        logger.info(f"[DRY-RUN] Would commit in {repo_path} with message: {message}")
        return False
    
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
        logger.info(f"Committed in {repo_path}: {message}")
        return True
    except subprocess.CalledProcessError as e:
        if 'nothing to commit' in e.stderr:
            logger.debug(f"Nothing to commit in {repo_path}")
            return False  # Nothing to commit
        logger.error(f"Commit failed in {repo_path}: {e.stderr}")
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
    """Clone a repository.
    
    Args:
        url: Git repository URL
        path: Path where to clone
    
    Returns:
        True if successful, False if dry-run
    
    Raises:
        GitError: If clone fails
    """
    if _DRY_RUN:
        logger.info(f"[DRY-RUN] Would clone {url} to {path}")
        return False
    
    try:
        subprocess.run(
            ['git', 'clone', url, str(path)],
            capture_output=True,
            text=True,
            check=True
        )
        logger.info(f"Cloned {url} to {path}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Clone failed: {e.stderr}")
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
