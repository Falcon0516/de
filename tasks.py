"""
Task Management Module

This module defines the Task class and functions to manage tasks.
"""

import json
from datetime import datetime
from typing import List, Optional


class Task:
    """
    Represents a single task.
    
    Attributes:
        id (int): Unique identifier for the task
        title (str): Task description
        completed (bool): Whether task is done
        created_at (str): When task was created
        priority (str): Priority level (low, medium, high)
    """
    
    def __init__(self, task_id: int, title: str, priority: str = "medium"):
        """
        Initialize a new task.
        
        Args:
            task_id: Unique ID for this task
            title: Description of the task
            priority: Priority level (default: medium)
        """
        self.id = task_id
        self.title = title
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.priority = priority
    
    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True
    
    def mark_incomplete(self):
        """Mark this task as not completed."""
        self.completed = False
    
    def to_dict(self):
        """
        Convert task to dictionary for JSON storage.
        
        Returns:
            dict: Task data as dictionary
        """
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'created_at': self.created_at,
            'priority': self.priority
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a Task object from a dictionary.
        
        Args:
            data: Dictionary containing task data
            
        Returns:
            Task: New Task object
        """
        task = cls(data['id'], data['title'], data.get('priority', 'medium'))
        task.completed = data['completed']
        task.created_at = data['created_at']
        return task
    
    def __str__(self):
        """String representation of task."""
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title} (Priority: {self.priority})"


# Global task list
tasks: List[Task] = []
next_id = 1


def add_task(title: str, priority: str = "medium") -> Task:
    """
    Add a new task to the list.
    
    Args:
        title: Task description
        priority: Priority level
        
    Returns:
        Task: The newly created task
    """
    global next_id
    task = Task(next_id, title, priority)
    tasks.append(task)
    next_id += 1
    return task


def get_all_tasks() -> List[Task]:
    """
    Get all tasks.
    
    Returns:
        List[Task]: All tasks
    """
    return tasks


def get_task_by_id(task_id: int) -> Optional[Task]:
    """
    Find a task by its ID.
    
    Args:
        task_id: ID to search for
        
    Returns:
        Task or None: The task if found, None otherwise
    """
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def delete_task(task_id: int) -> bool:
    """
    Delete a task by ID.
    
    Args:
        task_id: ID of task to delete
        
    Returns:
        bool: True if deleted, False if not found
    """
    task = get_task_by_id(task_id)
    if task:
        tasks.remove(task)
        return True
    return False