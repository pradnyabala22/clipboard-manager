import sys
import clipboard
import json
import os
import argparse

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    try:
        with open(filepath, "w") as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data(filepath):
    if not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}

def save_clipboard(data, key):
    data[key] = clipboard.paste()
    save_data(SAVED_DATA, data)
    print("Data saved!")

def load_clipboard(data, key):
    if key in data:
        clipboard.copy(data[key])
        print("Data copied to clipboard.")
    else:
        print("Key does not exist.")

def list_data(data):
    if data:
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("No data saved.")

def delete_data(data, key):
    if key in data:
        del data[key]
        save_data(SAVED_DATA, data)
        print(f"Deleted data for key: {key}")
    else:
        print("Key does not exist.")

def clear_data():
    save_data(SAVED_DATA, {})
    print("All data cleared.")

def main():
    parser = argparse.ArgumentParser(description="Clipboard manager")
    parser.add_argument("command", choices=["save", "load", "list", "delete", "clear"], help="Command to execute")
    parser.add_argument("--key", help="Key for the save or load command")
    
    args = parser.parse_args()
    command = args.command
    key = args.key
    
    data = load_data(SAVED_DATA)
    
    if command == "save":
        if key is None:
            key = input("Enter a key: ")
        save_clipboard(data, key)
    elif command == "load":
        if key is None:
            key = input("Enter a key: ")
        load_clipboard(data, key)
    elif command == "list":
        list_data(data)
    elif command == "delete":
        if key is None:
            key = input("Enter a key: ")
        delete_data(data, key)
    elif command == "clear":
        confirm = input("Are you sure you want to clear all data? (y/n): ")
        if confirm.lower() == 'y':
            clear_data()

if __name__ == "__main__":
    main()





