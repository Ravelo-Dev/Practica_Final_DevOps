Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/jammy64"
    config.vm.network "private_network", ip: "192.168.56.10"
    
    config.vm.hostname = "ravelo-dev-server"
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
    config.vm.provision "ansible_local" do |ansible|
        ansible.playbook = "ansible/playbook.yml"  
        ansible.compatibility_mode = "2.0"
    end    
  end