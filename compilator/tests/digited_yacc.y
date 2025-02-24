%{
#include <stdio.h>
#include <stdlib.h>

// Déclaration de prototypes pour les fonctions utilisées dans le fichier Yacc
void yyerror(const char *s);
int yylex();
%}

// Liste des tokens définis dans le fichier lex
%token LEFT RIGHT UP DOWN PRINT READ LOOP_START LOOP_END DEFINE CALL COMMENT_START COMMENT_END

%%
// Début de la grammaire
program:
    instructions
;

instructions:
    instruction
    | instructions instruction
;

instruction:
    LEFT            { printf("Déplacement gauche\n"); }
    | RIGHT         { printf("Déplacement droite\n"); }
    | UP            { printf("Incrémentation\n"); }
    | DOWN          { printf("Décrémentation\n"); }
    | PRINT         { printf("Affichage\n"); }
    | READ          { printf("Lecture\n"); }
    | LOOP_START    { printf("Début de boucle\n"); }
    | LOOP_END      { printf("Fin de boucle\n"); }
    | DEFINE        { printf("Définition de sous-programme\n"); }
    | CALL          { printf("Appel de sous-programme\n"); }
    | COMMENT_START { printf("Commentaire début\n"); }
    | COMMENT_END   { printf("Commentaire fin\n"); }
;

%%
// Fonction appelée en cas d'erreur
void yyerror(const char *s) {
    fprintf(stderr, "Erreur : %s\n", s);
}

// Fonction principale
int main() {
    return yyparse(); // Appelle l'analyseur syntaxique
}
