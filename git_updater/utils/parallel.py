"""Progress tracking utilities."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock


class ProgressTracker:
    """Track progress of operations across multiple items."""
    
    def __init__(self, total):
        """Initialize progress tracker.
        
        Args:
            total (int): Total number of items.
        """
        self.total = total
        self.current = 0
        self.success = 0
        self.failed = 0
        self.lock = Lock()
    
    def increment(self, status='success'):
        """Increment progress counter.
        
        Args:
            status (str): 'success' or 'failed'.
        """
        with self.lock:
            self.current += 1
            if status == 'success':
                self.success += 1
            elif status == 'failed':
                self.failed += 1
    
    def get_progress(self):
        """Get current progress.
        
        Returns:
            tuple: (current, total, success, failed).
        """
        with self.lock:
            return self.current, self.total, self.success, self.failed
    
    def print_progress(self):
        """Print progress bar."""
        current, total, success, failed = self.get_progress()
        percent = (current / total * 100) if total > 0 else 0
        bar_length = 40
        filled = int(percent / 100 * bar_length)
        bar = '█' * filled + '░' * (bar_length - filled)
        print(f"\r[{bar}] {percent:.1f}% ({current}/{total}) ✓{success} ✗{failed}", end='', flush=True)


def run_parallel(items, operation, max_workers=4, on_complete=None):
    """Run operations in parallel on multiple items.
    
    Args:
        items (list): Items to process.
        operation (callable): Function to call for each item. Should accept item as argument.
        max_workers (int): Maximum number of concurrent workers.
        on_complete (callable): Callback when an item completes. Receives (item, success, error).
    
    Returns:
        dict: Results keyed by item with values of (success, result/error).
    """
    results = {}
    tracker = ProgressTracker(len(items))
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_item = {
            executor.submit(operation, item): item 
            for item in items
        }
        
        # Process completed tasks
        for future in as_completed(future_to_item):
            item = future_to_item[future]
            
            try:
                result = future.result()
                tracker.increment('success')
                results[item] = (True, result)
                
                if on_complete:
                    on_complete(item, True, None)
                    
            except Exception as e:
                tracker.increment('failed')
                results[item] = (False, str(e))
                
                if on_complete:
                    on_complete(item, False, e)
            
            tracker.print_progress()
    
    print()  # New line after progress bar
    return results
