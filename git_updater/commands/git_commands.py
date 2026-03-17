"""Git-level commands like cloning."""

import json
from pathlib import Path
from git_updater.utils.git_helper import clone_repo


def cmd_clone_from_config(args):
    """Clone multiple repositories from a config file."""
    config_file = Path(args.config)
    target_path = Path(args.path)
    
    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_file}")
    
    target_path.mkdir(parents=True, exist_ok=True)
    
    # Load config
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON in config file")
    
    repos = config.get('repositories', [])
    
    print(f"\n{'Cloning Repositories':^60}")
    print("=" * 60)
    print(f"Found {len(repos)} repository(ies) in config\n")
    
    success = 0
    failed = 0
    
    for repo_url in repos:
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        repo_path = target_path / repo_name
        
        print(f"→ {repo_name:<40}", end=" ")
        
        if repo_path.exists():
            print("✗ Already exists")
            continue
        
        try:
            clone_repo(repo_url, repo_path)
            print("✓ Cloned")
            success += 1
        except Exception as e:
            print(f"✗ Failed")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {success} cloned, {failed} failed")
    print("=" * 60 + "\n")
