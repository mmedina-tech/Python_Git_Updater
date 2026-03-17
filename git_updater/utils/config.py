"""Configuration management."""

import json
from pathlib import Path


class Config:
    """Handle configuration from JSON files."""
    
    def __init__(self, config_file=None):
        """Initialize configuration.
        
        Args:
            config_file (str, optional): Path to config file.
        """
        self.config = {}
        if config_file:
            self.load(config_file)
    
    def load(self, config_file):
        """Load configuration from JSON file.
        
        Args:
            config_file (str): Path to config file.
        
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is invalid JSON.
        """
        path = Path(config_file)
        
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {config_file}")
        
        with open(path, 'r') as f:
            self.config = json.load(f)
    
    def get(self, key, default=None):
        """Get a configuration value.
        
        Args:
            key (str): Configuration key (supports dot notation: 'section.key').
            default: Default value if key not found.
        
        Returns:
            Configuration value or default.
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        
        return value if value is not None else default
    
    def get_repositories(self):
        """Get list of repositories from config.
        
        Returns:
            list: Repository list or empty list if not found.
        """
        return self.get('repositories', [])
    
    def get_default_path(self):
        """Get default repository path.
        
        Returns:
            str: Default path or None.
        """
        return self.get('defaults.path')
    
    def get_default_branch(self):
        """Get default branch.
        
        Returns:
            str: Default branch or 'main'.
        """
        return self.get('defaults.branch', 'main')
    
    def is_dry_run_enabled(self):
        """Check if dry-run mode is enabled by default.
        
        Returns:
            bool: True if dry-run enabled.
        """
        return self.get('defaults.dry_run', False)
