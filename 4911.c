#include <stdio.h>

/* return 1 if two matrix are identical
 * return 1 otherwise */
int checkidentical(int matrix[1000][1000], int dimension)
{
    int i, j, start, loop;
    int original[500][1000];
    int matring[500][1000];
    int ringnum = (dimension+1)/2;

    puts("function started\n");

    /*make ring from matrix*/
    for (i = 0 ; i < ringnum ; i++)
    {
        loop = dimension-i*2-1;
        if (loop ==0)
        {
            original[i][0] = dimension*dimension/2+1;
            matring[i][0] = matrix[dimension/2][dimension/2];
        }
        for (j=0 ; j<loop ; j++)
        {
            original[i][j] = i*(dimension+1) + j +1;
            original[i][j+loop] = dimension*(i+1) - i + dimension*j;
            original[i][j+loop*2] = dimension*dimension - i*(dimension+1) - j;
            original[i][j+loop*3] = dimension*dimension - dimension + 1 - (dimension-1)*i - (dimension)*j;

            matring[i][j] = matrix[i][i+j];
            matring[i][j+loop] = matrix[i+j][dimension-i-1];
            matring[i][j+loop*2] = matrix[dimension-i-1][dimension-i-j-1];
            matring[i][j+loop*3] = matrix[dimension-i-j-1][i];
        }
    }

    for (i = 0 ; i < ringnum ; i++)
    {
        loop = (dimension-i*2-1)*4;
        if (loop == 0)
        {
            loop = 1;
        }
        printf("original ring %d(loop: %d): \t", i, loop/4);
        for (j = 0 ; j < loop ; j++)
        {
            printf("%d ", original[i][j]);
        }
        printf("\ninput ring %d(loop: %d): \t\t", i, loop/4);
        for (j = 0 ; j < loop ; j++)
        {
            printf("%d ", matring[i][j]);
        }
        puts("");
    }


    for (i = 0 ; i < ringnum ; i++)
    {
        loop = (dimension-i*2-1)*4;
        if (loop == 0)
        {
            loop = 1;
        }

        for (j=0; j<loop ; j++)
        {
            if (matring[i][0] == original[i][j])
            {
                printf("found matching at %d!\n", j);
                start = j;
                break;
            }
        }

        //if there does not exist corresponding integer 
        if (j == loop)
        {
            puts("\n****NOT IDENTICAL!****");
            return 0;
        }

        for (j=0 ; j<loop ; j++)
        {
            //if two rings are not identical 
            if (matring[i][j] != original[i][(j+start)%loop])
            {
                puts("\n****NOT IDENTICAL!****");
                return 0;
            }
        }
    }

    puts("\n****IDENTICAL!****");
    return 1;
}

int main(void)
{
    int round = 1;
    int dimension, row, column, index=0;
    int matrix[1000][1000];

    while (round != 0)
    {
        scanf("%d", &dimension);
        if (dimension == 0)
        {
            break;
        }
        for (row = 0 ; row < dimension ; row++)
        {
            for (column = 0; column < dimension ; column++)
            {
                index++;
                scanf("%d", &matrix[row][column]);
            }
        }

        checkidentical(matrix, dimension);
    }
}
