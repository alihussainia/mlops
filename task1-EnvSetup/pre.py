from subprocess import call
call("wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh", shell=True)
call("bash Anaconda3-2022.05-Linux-x86_64.sh", shell=True)
call("sudo apt update", shell=True)
call("sudo apt install docker.io", shell=True)
call("mkdir ~/soft", shell=True)
# call("cd /home/ubuntu/soft/", shell=True)
call("wget https://github.com/docker/compose/releases/download/v2.5.1/docker-compose-linux-x86_64 -O ~/soft/docker-compose", shell=True)
call("chmod +x ~/soft/docker-compose", shell=True)
# cd ..
# call("cd ..", shell=True)
# adding path to soft
# nano .bashrc
# append export PATH="${HOME}/soft:${PATH}"
call("""echo 'export PATH="${HOME}/soft:${PATH}"' >> ~/.bashrc""", shell=True)
# re-run .bashrc to apply changes
call(". ~/.bashrc", shell=True)
# which docker-compose # should see path to soft
call("which docker-compose", shell=True)
# add user to docker group
call("sudo groupadd docker", shell=True)
call("sudo usermod -aG docker $USER", shell=True)
# activate the changes
call("newgrp docker", shell=True)
# Log out and log back in so that your group membership is re-evaluated.
call("exit", shell=True)
