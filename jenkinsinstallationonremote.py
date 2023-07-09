from fabric import Connection

def configure_servers():
    # Define the remote servers
    servers = [
        {'host': 'host ip', 'username': 'username', 'password': 'password'}
    ]

    # Iterate over each server
    for server in servers:
        # Connect to the server
        conn = Connection(host=server['host'], user=server['username'], connect_kwargs={'password': server['password']})

        try:
            # Run commands to provision and configure the server
            print(f"Configuring server: {server['host']}")
            commands = [
                'apt update',
                'apt install -y default-jdk',
                'curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc',
                'echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list',
                'apt update',
                'apt install jenkins -y',
                'systemctl start jenkins'
            ]

            for cmd in commands:
                conn.sudo(f'{cmd} > /dev/null')
            print(f"Server configuration completed: {server['host']}")

        finally:
            # Close the connection
            conn.close()

# Execute the configuration
configure_servers()
