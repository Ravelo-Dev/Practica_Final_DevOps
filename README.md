Proyecto DevOps: 

Implementación de Servidor Apache con Ansible y Vagrant

Descripción del Proyecto:

Este proyecto tiene como objetivo la configuración y despliegue automatizado de un servidor web Apache utilizando Vagrant y Ansible. Adicionalmente, el proyecto incluye la integración de pruebas unitarias que se ejecutan automáticamente mediante GitHub Actions cada vez que se actualiza el repositorio.


Prerrequisitos:

Vagrant: Herramienta para la creación y gestión de entornos virtualizados.
VirtualBox: Proveedor de Vagrant para la creación de máquinas virtuales.
Ansible: Herramienta de automatización para la gestión de la configuración.
GitHub Actions: Servicio de CI/CD para la automatización de flujos de trabajo.

Integración Continua (CI) con GitHub Actions

Cada vez que se realiza un cambio en el repositorio, GitHub Actions ejecutará automáticamente las pruebas unitarias definidas en el archivo ci.yml. Esta automatización asegura que todos los cambios en el código son validados antes de ser integrados en la rama principal.

Archivos Clave:

Vagrantfile: Configura la máquina virtual Ubuntu Jammy 64-bit con una IP privada.
playbook.yml: Automáticamente instala Apache, copia los archivos del sitio web y arranca el servicio de Apache.
inventario.ini: Define los parámetros de conexión SSH necesarios para que Ansible gestione la máquina virtual.
test_page.py: Contiene las pruebas unitarias para verificar el correcto funcionamiento de la página web.
ci.yml: Configura GitHub Actions para ejecutar las pruebas unitarias automáticamente.
