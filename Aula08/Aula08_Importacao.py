# Importação de arquivos de outro diretório
# Compare this snippet from Aula08/Exercicio.py:
# Importar imprimir_maior_numero de Aula03.ListaExercicio.Exercicio02

try:
    from Aula03.ListaExercicio.Exercicio02 import imprimir_maior_numero
except ModuleNotFoundError:
    print("Module not found. Please make sure the module and function exist and that the module is in the correct directory.")

imprimir_maior_numero()