import os
import subprocess
import datetime
import tempfile

def backup_postgresql_db(host, user, password, database_name):
    # Create a temporary file with a .sql suffix
    with tempfile.NamedTemporaryFile(suffix='.sql', delete=False) as temp_file:
        backup_file = temp_file.name

    # Prepare the environment variables for pg_dump
    env = os.environ.copy()
    env['PGPASSWORD'] = password  # Set the password in the environment

    # Run the pg_dump command to create the backup
    try:
        subprocess.run(
            [
                "pg_dump",
                "-h", host,
                "-U", user,
                "-d", database_name,
                "-F", "c",  # Custom format for better compression
                "-f", backup_file  # Output file
            ],
            check=True,
            env=env
        )
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e}")
        return None

    # Display file information
    file_size = os.path.getsize(backup_file)  # Size in bytes
    file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(backup_file))  # Last modified time

    print(f"Backup created at: {backup_file}")
    print(f"File size: {file_size / 1024:.2f} KB")  # Size in kilobytes
    print(f"Last modified: {file_mtime}")

    return backup_file

# Example usage
#if __name__ == "__main__":
#    host = "localhost"
#    user = "your_username"
#    password = "your_password"
#    database_name = "your_database_name"
#
#    backup_path = backup_postgresql_db(host, user, password, database_name)
#    if backup_path:
#        print(f"Backup successful. File saved at: {backup_path}")
#    else:
#        print("Backup failed.")
#