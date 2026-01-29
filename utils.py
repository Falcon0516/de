"""
Utility Functions

Helper functions for the task manager.
"""

from datetime import datetime
from typing import List


def get_current_time() -> str:
    """
    Get current time as formatted string.
    
    Returns:
        str: Current time in YYYY-MM-DD HH:MM:SS format
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def validate_priority(priority: str) -> bool:
    """
    Check if priority level is valid.
    
    Args:
        priority: Priority string to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    valid_priorities = ['low', 'medium', 'high']
    return priority.lower() in valid_priorities


def format_task_list(tasks: List) -> str:
    """
    Format a list of tasks for display.
    
    Args:
        tasks: List of Task objects
        
    Returns:
        str: Formatted string of all tasks
    """
    if not tasks:
        return "No tasks found."
    
    output = "\n" + "="*50 + "\n"
    output += "YOUR TASKS\n"
    output += "="*50 + "\n\n"
    
    for task in tasks:
        output += str(task) + "\n"
    
    output += "\n" + "="*50 + "\n"
    output += f"Total: {len(tasks)} task(s)\n"
    output += "="*50 + "\n"
    
    return output


def get_user_input(prompt: str, default: str = None) -> str:
    """
    Get input from user with optional default value.
    
    Args:
        prompt: Message to show user
        default: Default value if user presses Enter
        
    Returns:
        str: User's input or default value
    """
    if default:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "
    
    user_input = input(prompt).strip()
    
    if not user_input and default:
        return default
    
    return user_input


def confirm_action(message: str) -> bool:
    """
    Ask user to confirm an action.
    
    Args:
        message: Confirmation message
        
    Returns:
        bool: True if user confirms, False otherwise
    """
    response = input(f"{message} (y/n): ").lower().strip()
    return response in ['y', 'yes']