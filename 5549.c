#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n, m, ncase, i, j, k;
    int O, J, I;
    char **planet;
    int **cases;

    scanf("%d", &n);
    scanf("%d", &m);
    scanf("%d", &ncase);

    //planet = (char**)calloc(n, sizeof(char*));
    cases = (int**)calloc(ncase, sizeof(int*));

    for (i =0 ; i < n ; i++)
    {
        //planet[i] = (char*)calloc(m, sizeof(char));
        scanf("%s", planet[i]);
        for (i = 0 ; i < m ; i++)
        {
            printf("%c ", planet[i][j]);
        }
    }
    for (i = 0 ; i < ncase ; i++)
    {
        cases[i] = (int*)calloc(4, sizeof(int));
        for (j = 0 ; j < 4 ; j++)
        {
            scanf("%d", &cases[i][j]);
        }
        I = 0;
        J = 0;
        O = 0;

        for (j = cases[i][0]-1 ; j < cases[i][2] ; j++)
        {
            for (k = cases[i][1]-1 ; k< cases[i][3] ; k++)
            {
                printf("%d:%d \n",j, k);
                if (planet[j][k] == 'O')
                {
                    O++;
                }
                else if (planet[k][k] == 'J')
                {
                    J++;
                }
                else
                {
                    I++;
                }
            }
        }
        printf ("%d %d %d\n", J, O, I);
    }
}
