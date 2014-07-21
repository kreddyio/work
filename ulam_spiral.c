/*
This is a fun program to fill a square of given size with numbers starting from 1 in a spiral format.
Logic: This particular code uses recursion and looping for filling a 2D array with the numbers in spiral form.
AUTHOR:Kethu Harikishan Reddy
Email: kishanreddy.kethu@gmail.com
Version=1.0
*/
#include <stdio.h>
void spiral(int p);
static int x=0,a[100][100],start=1;
void main()
{
	int n;
	printf("Please enter any number less than 100 for the Ulam Spiral:\n");
	scanf("%d",&n);
	spiral(n);
	int i,j;
	for (i=0;i<n;i++)
	{	for (j=0;j<n;j++)
				printf("%3d  ",a[i][j]);//printing each array element
		printf("\n");
	}
}
void spiral(int p)
{	
	if (p<=0)
		return;
	else if (p==1)
	{
		a[x][x]=start;
		return;
	}

	int i;
	for (i=x;i<x+p;i++) //Top Left to Top Right.
	{
		a[x][i]=start++;
	}
	for (i=(x+1);i<x+p;i++) //Top Right to Bottom Right.
	{
		a[i][x+p-1]=start++;
	}
	for (i=(x+p-2);i>=x;i--) //Bottom Right to Bottom Left.
	{
		a[x+p-1][i]=start++;

	}	
	for (i=(x+p-2);i>x;i--) //Bottom Left to Top Left.
	{
		a[i][x]=start++;
	}
	x++;
	spiral(p-2); //Recursive call to itself with decrease in square size.
}