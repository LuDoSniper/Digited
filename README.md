# Digited

## Fonctionnement

Digited est un langage de programmation très similaire au Brainfuck. Cependant, comme son nom l'indique, les seuls caractères interprétés sont des chiffres (à l'exception des parenthèses) Le Digited se déplace de case en case dans ce qui est appelé le `buffer`. La position actuelle dans le `buffer` se nomme le `cursor`.

Actions dans le buffer :
| Caractère | Action |
| :-: | :- |
| 8 | Augmenter la valeur courrante de 1 |
| 2 | Diminuer la valeur courrante de 1 |
| 6 | Ajouter 1 au `cursor` |
| 6 | Enlever 1 au `cursor` (attention, il est impossible d'aller à la position '-1' du buffer. Une exception sera levé si tel est le cas) |
| 7 | Début d'une boucle (va directement à `1` si la valeur courrante est égale à 0) |
| 1 | Fin de la boucle (retourne à `7` si la valeur courrante n'est pas égale à 0) |
| 9 | Affiche le caractère ascii égale à la valeur courrante |
| 3 | Lit un caractère et stock sa valeur dans la 'case mémoire' courrante |
| 5 | Délimite le début et la fin d'une fonction (la fonction est identifié en fonction de la valeur courante) |
| 0 | Appel la fonction correspondant à la valeur courrante |
| ( | Délimite le début d'un commentaire |
| ) | Délimite la fin d'un commentaire |

Tout autre caractère rencontré dans lors de l'execution du programme sera ignoré. Attention à utiliser les parenthèses pour ne pas interpréter certains chiffres.

> **Attention !**
> Les boucles imbriqué et les commentaires imbriqués ne fonctionnent pas pour le moment. Sachez également que '3' n'est pas pris en charge pour le moment par le compilateur.

Contact : lucien.donnarieix@hesias.fr
