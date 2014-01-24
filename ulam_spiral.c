#include <stdio.h>
void spiral();
static int x=0,a[100][100],start=1;
void main()
{
	int n;
	printf("Please enter the number for the Ulam Spiral:\n");
	scanf("%d",&n);
	spiral(n,start);
}
void spiral(int n,int start)
{	int i;
	for (i=x;i<n;i++)
	{
		a[x][i]=start++;
	}
	for (i=(x+1);i<n;i++)
	{
		a[i][n-1]=start++;
	}
	for (i=(n-2);i>=0;i--)
	{
		a[n-1][i]=start++;

	}	
	for (i=(n-2);i>=0;i--)
	{
		a[i][]
	}
}