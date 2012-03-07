#instalação do modulo financeiro
#nao deve ser chamado utilizando sudo

sudo apt-get install python-dev libxml2
sudo apt-get install python-setuptools
easy_install pip

pip install django==1.3.1
pip install django-piston piston-mini-client 
