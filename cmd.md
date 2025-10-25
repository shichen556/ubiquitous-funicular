# Eliminar historial pwsh: 
$validos = Get-History | Where-Object { -not $_.Exception }
Clear-History
$validos | ForEach-Object { Add-History -InputObject $_ }

git/GitHub
0. Instalar git si no lo está
	git --version
	0.1. Iniciar sesión si no está
		git config --global user.name <usuario>
		git config --global user.email <email>
		git config --global --list
1. Inicializar
	git init
2. Commit
	git status
	git add .
	git commit -m "Version base"
	git log
3. Deshacer últimos cambios (cargar el ultimo commit que se hizo)
	git stash

Ejemplos: 
Conventional commits https://www.conventionalcommits.org/en/v1.0.0/
git commit -m "[tipo](alcance): [asunto][descripcion]"
Ej.
git commit -m "refactor(button.js): Cambiar color del botón-Cambiar color de fondo del componente a naranja en vez de azul por medio de clases de TailWindCSS"

.gitignore
	Archivo para decir a git que archivos subir y que otros no
4. Push
	(Comandos en GitHub una vez creado el repositorio)
		
	git remote add origin https://github.com/shichen556/ubiquitous-funicular.git
	git branch -M main
	git push -u origin main

Optional: 
	Configurar nombre de la rama principal por defecto:
		git config --global init.defaultBranch <name>

	Cambiar nombre de la rama:
		git branch -m <name>



Modules Installed () from 'C:\\Users\\YIXI\\Desktop\\3D models for Blender Test\\blender_mmd_tools-main.zip' into 'C:\\Users\\YIXI\\AppData\\Roaming\\Blender Foundation\\Blender\\3.3\\scripts\\addons'
