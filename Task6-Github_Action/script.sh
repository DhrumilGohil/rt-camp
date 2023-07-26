#! bin/sh

echo "$REMOTE_USER@$REMOTE_HOST"

# Replace the placeholders with your actual remote server credentials and paths
mkdir -p ~/.ssh
touch  ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa
echo "$SSH_PRIVATE_KEY" > ~/.ssh/id_rsa
ssh-keyscan "$REMOTE_HOST" >> ~/.ssh/known_hosts
# echo `ls -ar`
# echo `ls github -a`
# Rsync command to copy files to the remote server

rsync -avz --delete --exclude=".git/" --exclude=".github/" --exclude="script.sh" github/ "$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH"

rsync -avz --delete "$REMOTE_USER@$REMOTE_HOST:~/github-test" .

