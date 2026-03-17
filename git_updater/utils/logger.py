"""Logging configuration for the tool."""

import logging
import logging.handlers
from pathlib import Path
from datetime import datetime


def setup_logging(log_file=None, verbose=False):
    """Configure logging to both file and console.
    
    Args:
        log_file (str, optional): Path to log file. If None, logs go to console only.
        verbose (bool): Enable verbose output (DEBUG level).
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger('git_updater')
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # Set log level
    log_level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(log_level)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.DEBUG)  # Always log everything to file
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def get_default_log_path():
    """Get the default log path in a logs directory."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"logs/git_updater_{timestamp}.log"
