# rt-camp

Save the script in a file named script.py, and you can run it using the following command:

python script.py <command> <site_name>

# WordPress Site Management Script

This command-line script allows you to easily manage WordPress sites using a LEMP stack running inside Docker containers.

## Installation

1. Ensure that Python 3 is installed on your system.
2. Clone this repository or download the `script.py` file.
3. Install the required dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
   
   
   python script.py <command> <site_name>
   
Replace <command> with one of the following commands: create, enable, disable, or delete. <site_name> should be the desired name for your WordPress site.

Commands
1. Create a WordPress site
This command creates a new WordPress site using the latest WordPress version.

``` python script.py create example.com ```

Replace example.com with the desired site name. This command will install Docker and Docker Compose if they are not already installed, create the necessary containers, set up the WordPress site, and add an entry to /etc/hosts to access the site.

2. Enable or disable a WordPress site
You can start or stop the containers for a WordPress site using the following commands:

To enable a site:

``` python script.py enable example.com ```

To disable a site:

``` python script.py disable example.com ```

Replace example.com with the name of the site you want to enable or disable. These commands will start or stop the containers for the specified site.

3. Delete a WordPress site
This command deletes a WordPress site and removes all associated containers and local files.

``` python script.py delete example.com ```

Replace example.com with the name of the site you want to delete. This command will stop and remove the containers, delete the site directory, and remove the entry from /etc/hosts.

Additional Notes

Ensure that you have appropriate permissions to install packages and modify system files (sudo access may be required).
Make sure that ports 80 and 443 are available on your system as they will be used by the Docker containers.
After creating a site or enabling it, open http://example.com (replace with your site name) in your browser to access the WordPress site.

