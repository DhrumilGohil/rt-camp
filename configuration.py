import os
import sys
import subprocess

def check_dependencies():
    # Check if Docker is installed
    if not os.path.exists('/usr/bin/docker'):
        print("Docker is not installed. Installing Docker...")
        subprocess.call(['apt-get', 'install', '-y', 'docker'])
    
    # Check if Docker Compose is installed
    if not os.path.exists('/usr/bin/docker-compose'):
        print("Docker Compose is not installed. Installing Docker Compose...")
        subprocess.call(['apt-get', 'install', '-y', 'docker-compose'])

def create_wordpress_site(site_name):
    # Create a directory for the WordPress site
    os.makedirs(site_name, exist_ok=True)
    os.chdir(site_name)

    # Create a docker-compose.yml file
    with open('docker-compose.yml', 'w') as f:
        f.write("""
version: '3'
services:
  wordpress:
    image: wordpress:latest
    ports:
      - "80:80"
    environment:
      - WORDPRESS_DB_HOST=db
      - WORDPRESS_DB_NAME=wordpress
      - WORDPRESS_DB_USER=root
      - WORDPRESS_DB_PASSWORD=password
    volumes:
      - ./wordpress:/var/www/html
  db:
    image: mariadb
    environment:
      - MYSQL_ROOT_PASSWORD=password
      - MYSQL_DATABASE=wordpress
    volumes:
      - ./db:/var/lib/mysql
""")

    # Create a Docker network
    subprocess.call(['docker', 'network', 'create', site_name])

    # Start the containers
    subprocess.call(['docker-compose', 'up', '-d'])

    # Add entry to /etc/hosts
    with open('/etc/hosts', 'a') as f:
        f.write(f"127.0.0.1 {site_name}\n")

def enable_disable_site(enable, site_name):
    if enable:
        subprocess.call(['docker-compose', '-f', f'{site_name}/docker-compose.yml', 'up', '-d'])
        print(f"The site '{site_name}' has been enabled.")
    else:
        subprocess.call(['docker-compose', '-f', f'{site_name}/docker-compose.yml', 'down'])
        print(f"The site '{site_name}' has been disabled.")

def delete_site(site_name):
    subprocess.call(['docker-compose', '-f', f'{site_name}/docker-compose.yml', 'down', '-v'])
    subprocess.call(['rm', '-rf', site_name])
    print(f"The site '{site_name}' has been deleted.")

def open_in_browser(site_name):
    print(f"Please open http://{site_name} in your browser.")

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <command> <site_name>")
        return
    
    command = sys.argv[1]
    site_name = sys.argv[2]

    if command == 'create':
        check_dependencies()
        create_wordpress_site(site_name)
        open_in_browser(site_name)
    elif command == 'enable':
        enable_disable_site(True, site_name)
    elif command == 'disable':
        enable_disable_site(False, site_name)
    elif command == 'delete':
        delete_site(site_name)
    else:
        print("Invalid command.")

if __name__ == '__main__':
    main()
