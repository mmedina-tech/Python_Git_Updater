"""Repository-level commands that operate on multiple repos."""

from pathlib import Path
from git_updater.utils.git_helper import (
    find_git_repos, is_git_repo, pull_repo, push_repo, 
    commit_changes, get_branches, get_status, get_current_branch
)


def cmd_update_all(args):
    """Pull and push all repositories."""
    repos = find_git_repos(args.path)
    
    if not repos:
        print(f"No git repositories found in {args.path}")
        return
    
    print(f"\n{'Git Repository Updater':^60}")
    print("=" * 60)
    print(f"Found {len(repos)} repository(ies)\n")
    
    success = 0
    failed = 0
    
    for repo in repos:
        repo_name = repo.name
        branch = get_current_branch(repo)
        
        print(f"→ {repo_name:<40} [{branch}]", end=" ")
        
        try:
            pull_repo(repo, args.branch)
            push_repo(repo, args.branch)
            print("✓ Updated")
            success += 1
        except Exception as e:
            print(f"✗ Failed")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {success} success, {failed} failed")
    print("=" * 60 + "\n")


def cmd_pull_all(args):
    """Pull all repositories."""
    repos = find_git_repos(args.path)
    
    if not repos:
        print(f"No git repositories found in {args.path}")
        return
    
    print(f"\n{'Pulling Repositories':^60}")
    print("=" * 60)
    print(f"Found {len(repos)} repository(ies)\n")
    
    success = 0
    failed = 0
    
    for repo in repos:
        repo_name = repo.name
        print(f"→ {repo_name:<40}", end=" ")
        
        try:
            pull_repo(repo, args.branch)
            print("✓ Pulled")
            success += 1
        except Exception as e:
            print(f"✗ Failed: {str(e)[:30]}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {success} success, {failed} failed")
    print("=" * 60 + "\n")


def cmd_push_all(args):
    """Push all repositories."""
    repos = find_git_repos(args.path)
    
    if not repos:
        print(f"No git repositories found in {args.path}")
        return
    
    print(f"\n{'Pushing Repositories':^60}")
    print("=" * 60)
    print(f"Found {len(repos)} repository(ies)\n")
    
    success = 0
    failed = 0
    
    for repo in repos:
        repo_name = repo.name
        print(f"→ {repo_name:<40}", end=" ")
        
        try:
            push_repo(repo, args.branch)
            print("✓ Pushed")
            success += 1
        except Exception as e:
            print(f"✗ Failed: {str(e)[:30]}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {success} success, {failed} failed")
    print("=" * 60 + "\n")


def cmd_status_all(args):
    """Show status of all repositories."""
    repos = find_git_repos(args.path)
    
    if not repos:
        print(f"No git repositories found in {args.path}")
        return
    
    print(f"\n{'Repository Status':^60}")
    print("=" * 60)
    print(f"Found {len(repos)} repository(ies)\n")
    
    for repo in repos:
        repo_name = repo.name
        branch = get_current_branch(repo)
        status = get_status(repo)
        
        changes = len(status.split('\n')) if status else 0
        
        print(f"→ {repo_name:<35} [{branch}] {changes:>3} changes")
        
        if status:
            for line in status.split('\n')[:3]:  # Show first 3 changes
                if line:
                    print(f"    {line[:55]}")
            if len(status.split('\n')) > 3:
                print(f"    ... and {len(status.split(chr(10))) - 3} more")
    
    print("\n" + "=" * 60 + "\n")


def cmd_commit_all(args):
    """Commit changes in all repositories."""
    repos = find_git_repos(args.path)
    
    if not repos:
        print(f"No git repositories found in {args.path}")
        return
    
    print(f"\n{'Committing Changes':^60}")
    print("=" * 60)
    print(f"Found {len(repos)} repository(ies)")
    print(f"Message: {args.message}\n")
    
    success = 0
    failed = 0
    no_changes = 0
    
    for repo in repos:
        repo_name = repo.name
        print(f"→ {repo_name:<40}", end=" ")
        
        try:
            result = commit_changes(repo, args.message, args.all)
            if result:
                print("✓ Committed")
                success += 1
            else:
                print("- No changes")
                no_changes += 1
        except Exception as e:
            print(f"✗ Failed")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {success} committed, {no_changes} no changes, {failed} failed")
    print("=" * 60 + "\n")


def cmd_branches_all(args):
    """List branches in all repositories."""
    repos = find_git_repos(args.path)
    
    if not repos:
        print(f"No git repositories found in {args.path}")
        return
    
    print(f"\n{'Repository Branches':^60}")
    print("=" * 60)
    print(f"Found {len(repos)} repository(ies)\n")
    
    for repo in repos:
        repo_name = repo.name
        branches = get_branches(repo)
        current = get_current_branch(repo)
        
        print(f"→ {repo_name}")
        for branch in branches:
            marker = "●" if branch.strip('* ') == current else " "
            print(f"  {marker} {branch}")
        print()
    
    print("=" * 60 + "\n")
