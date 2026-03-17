#!/usr/bin/env python3
"""
Python_Git_Updater - Bulk Git repository management tool
Updates all remote repos with ease across multiple repositories
"""

import argparse
import sys
from pathlib import Path

from git_updater.commands import repo_commands, git_commands


def create_parser():
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog='git-updater',
        description='Update all remote repos with ease',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python main.py update --path C:\\repos
  python main.py pull --path C:\\repos
  python main.py status --path C:\\repos
  python main.py commit --path C:\\repos --message "Automation"
  python main.py branches --path C:\\repos
        '''
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Update command (pull + push)
    update_parser = subparsers.add_parser('update', help='Pull and push all repos')
    update_parser.add_argument('--path', required=True, help='Directory containing repos')
    update_parser.add_argument('--branch', default='main', help='Branch to update (default: main)')
    update_parser.set_defaults(func=repo_commands.cmd_update_all)
    
    # Pull command
    pull_parser = subparsers.add_parser('pull', help='Pull all repos')
    pull_parser.add_argument('--path', required=True, help='Directory containing repos')
    pull_parser.add_argument('--branch', default='main', help='Branch to pull (default: main)')
    pull_parser.set_defaults(func=repo_commands.cmd_pull_all)
    
    # Push command
    push_parser = subparsers.add_parser('push', help='Push all repos')
    push_parser.add_argument('--path', required=True, help='Directory containing repos')
    push_parser.add_argument('--branch', default='main', help='Branch to push (default: main)')
    push_parser.set_defaults(func=repo_commands.cmd_push_all)
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Check status of all repos')
    status_parser.add_argument('--path', required=True, help='Directory containing repos')
    status_parser.set_defaults(func=repo_commands.cmd_status_all)
    
    # Commit command
    commit_parser = subparsers.add_parser('commit', help='Commit changes in all repos')
    commit_parser.add_argument('--path', required=True, help='Directory containing repos')
    commit_parser.add_argument('--message', required=True, help='Commit message')
    commit_parser.add_argument('--all', action='store_true', help='Stage all changes')
    commit_parser.set_defaults(func=repo_commands.cmd_commit_all)
    
    # Branches command
    branches_parser = subparsers.add_parser('branches', help='List branches in all repos')
    branches_parser.add_argument('--path', required=True, help='Directory containing repos')
    branches_parser.set_defaults(func=repo_commands.cmd_branches_all)
    
    # Clone command
    clone_parser = subparsers.add_parser('clone', help='Clone repos from config file')
    clone_parser.add_argument('--config', required=True, help='Config file with repo URLs')
    clone_parser.add_argument('--path', required=True, help='Directory to clone into')
    clone_parser.set_defaults(func=git_commands.cmd_clone_from_config)
    
    return parser


def main():
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(0)
    
    if hasattr(args, 'func'):
        try:
            args.func(args)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == '__main__':
    main()
