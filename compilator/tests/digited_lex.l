%{
#include "y.tab.h"    
%}

%%

4          { return LEFT; }
6          { return RIGHT; }
8          { return UP; }
2          { return DOWN; }
9          { return PRINT; }
3          { return READ; }
7          { return LOOP_START; }
1          { return LOOP_END; }
5          { return DEFINE; }
0          { return CALL; }
\(         { return COMMENT_START; }
\)         { return COMMENT_END; }
[ \t\n]    { /* Ignorer les espaces, tabulations et retours à la ligne */ }
.          { /* Ignorer tout autre caractère */ }

%%
