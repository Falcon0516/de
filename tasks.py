"""
Task Management Module

This module defines the Task class and functions to manage tasks.
"""
import json
import os
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
        self.id = task_id
        self.title = title
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.priority = priority
        self.tags = []  # Add this line instead
        self.category = "general"  # Add this line
    
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
#to do: implement save_tasks and load_tasks functionss
DATA_FILE = "data/tasks.json"


def save_tasks_to_file():
    """
    Save all tasks to JSON file.
    
    This function converts all Task objects to dictionaries
    and writes them to a JSON file for persistence.
    """
    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    # Convert all tasks to dictionaries
    task_dicts = [task.to_dict() for task in tasks]
    
    # Write to file
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump({
                'tasks': task_dicts,
                'next_id': next_id
            }, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False


def load_tasks_from_file():
    """
    Load tasks from JSON file.
    
    This function reads the JSON file and recreates
    Task objects from the saved data.
    """
    global tasks, next_id
    
    # Check if file exists
    if not os.path.exists(DATA_FILE):
        return False
    
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        
        # Clear current tasks
        tasks.clear()
        
        # Recreate Task objects
        for task_dict in data['tasks']:
            task = Task.from_dict(task_dict)
            tasks.append(task)
        
        # Restore next_id
        next_id = data['next_id']
        
        return True
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return False