#include <stdio.h>
#include <stdlib.h>

int cal(void)
{
    int i, j, M, N, k;
    int store[2][50];
    char array[50][50];
    char temp;
    int flag = 1;

    scanf("%d", &N);
    scanf("%d", &M);


    for (i = 0 ; i < N ; i++)
    {
        scanf("%s", array[i]);
        store[1][i] = N;
        store[0][i] = N;
    }


    while(flag)
    {
        flag = 0;
        for (i = 0 ; i < M ; i++)
        {
            store[1][i] = N;
            store[0][i] = N;
        }
        for (j = 0 ; j < M ; j++)
        {
            for (i = 0 ; i < N ; i++)
            {
                if (array[i][j] == 'o')
                {
                    store[0][j] = i;
                    flag = 1;
                }
                else if (array[i][j] != '.')
                {
                    if (store[0][j] < N)
                    {
                        store[1][j] = i;
                        break;
                    }
                }
            }

            if (store[0][j] != N)
            {
                for (i = store[0][j] ; i < store[1][j]-1 ; i++)
                {
                    array[i][j] = '.';
                }
                array[store[1][j]-1][j] = 'O';
            }
        }
    }

    for (i = 0 ; i < N ; i++)
    {
        for (j = 0 ; j < M ; j++)
        {
            if (array[i][j] == 'O')
            {
                printf("o");
            }
            else
            {
                printf("%c", array[i][j]);
            }
        }
        puts("");
    }
}

int main(void)
{
    cal();
}
