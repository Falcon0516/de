"""
Task Manager CLI - Main Program

Command-line interface for managing tasks.
"""

import sys
from tasks import add_task, get_all_tasks, get_task_by_id, delete_task
from utils import format_task_list, validate_priority, confirm_action, get_user_input
from tasks import (add_task, get_all_tasks, get_task_by_id, 
                   delete_task, save_tasks_to_file, load_tasks_from_file)

def show_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("TASK MANAGER")
    print("="*50)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("="*50)


def handle_add_task():
    """Handle adding a new task."""
    print("\n--- Add New Task ---")
    
    # Get task title
    title = get_user_input("Enter task description")
    
    if not title:
        print("❌ Task description cannot be empty!")
        return
    
    # Get priority
    priority = get_user_input("Enter priority (low/medium/high)", "medium")
    
    # Validate priority
    if not validate_priority(priority):
        print("❌ Invalid priority! Using 'medium' instead.")
        priority = "medium"
    
    # Add task
    task = add_task(title, priority.lower())
    print(f"✅ Task added successfully! (ID: {task.id})")


def handle_view_tasks():
    """Handle viewing all tasks."""
    tasks = get_all_tasks()
    print(format_task_list(tasks))


def handle_complete_task():
    """Handle marking a task as complete."""
    print("\n--- Complete Task ---")
    
    # Show all tasks first
    handle_view_tasks()
    
    # Get task ID
    try:
        task_id = int(get_user_input("Enter task ID to complete"))
    except ValueError:
        print("❌ Invalid ID! Please enter a number.")
        return
    
    # Find and complete task
    task = get_task_by_id(task_id)
    
    if task:
        if task.completed:
            print("⚠️  Task is already completed!")
        else:
            task.mark_complete()
            print(f"✅ Task {task_id} marked as complete!")
    else:
        print(f"❌ Task with ID {task_id} not found!")


def handle_delete_task():
    """Handle deleting a task."""
    print("\n--- Delete Task ---")
    
    # Show all tasks first
    handle_view_tasks()
    
    # Get task ID
    try:
        task_id = int(get_user_input("Enter task ID to delete"))
    except ValueError:
        print("❌ Invalid ID! Please enter a number.")
        return
    
    # Confirm deletion
    task = get_task_by_id(task_id)
    if not task:
        print(f"❌ Task with ID {task_id} not found!")
        return
    
    if confirm_action(f"Delete task '{task.title}'?"):
        if delete_task(task_id):
            print(f"✅ Task {task_id} deleted successfully!")
        else:
            print(f"❌ Failed to delete task {task_id}.")
    else:
        print("❌ Deletion cancelled.")

def main():
    """Main program loop."""
    # Load existing tasks
    if load_tasks_from_file():
        print("✅ Loaded existing tasks from file.")
    else:
        print("📝 Starting with empty task list.")
    
    print("Welcome to Task Manager!")
    print("Manage your tasks efficiently from the command line.")
    
    while True:
        show_menu()
        
        choice = get_user_input("Enter your choice (1-5)")
        
        if choice == '1':
            handle_add_task()
            save_tasks_to_file()  # Auto-save after adding
        elif choice == '2':
            handle_view_tasks()
        elif choice == '3':
            handle_complete_task()
            save_tasks_to_file()  # Auto-save after completing
        elif choice == '4':
            handle_delete_task()
            save_tasks_to_file()  # Auto-save after deleting
        elif choice == '5':
            save_tasks_to_file()  # Save before exiting
            print("\n👋 Goodbye! Thanks for using Task Manager.")
            sys.exit(0)
        else: 
            print("")
#this is a change

if __name__ == "__main__":
    main()
