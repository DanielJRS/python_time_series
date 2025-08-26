# Em python, o que é um cabeçalho dentro de um arquivo python e para que serve? O que é um docstring e para que serve? Qual a diferença do cabeçalho arquivo para o docstring?

# O cabeçalho são as primeiras linhas de um arquivo Python, geralmente contendo: Comentários com informações sobre o arquivo (autor, data, descrição geral); Imports necessários; Configurações especiais (como encoding) 
# e serve para documentar o projeto como um todo, adicionar informações relevantes para que auxiliem o desenvolvedor na hora de resolver as problemáticas do código.

# O docstring é uma string especial (entre """) que documenta funções, classes ou módulos específicos. Serve para explicar o que uma função/classe faz e como usar.

# Principal diferença: Cabeçalho: documenta o arquivo inteiro (comentários normais #); Docstring: documenta partes específicas do código (strings """) e pode ser acessada programaticamente com help()
#O docstring é mais "vivo" - Python consegue lê-lo e exibi-lo quando você pede ajuda sobre uma função.


# exercício 1: formate o cabeçalho deste arquivo


# exercícios de 2 a 4, implementar os métodos abaixo:

def maximo(nums):
    """Retorna o maior elemento de uma lista não vazia, sem usar max()."""
    # TODO: percorra a lista guardando o maior atual
    ...

def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    # TODO: retorne se n é par
    ...

def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    # TODO: implemente de forma iterativa (sem recursão)
    ...
