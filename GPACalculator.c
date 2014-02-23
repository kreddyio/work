/*
DESCRIPTION: This is a program to calculate my GPA in my semester.
AUTHOR: Kethu Harikishan Reddy
EMAIL: kishanreddy.kethu@gmail.com
*/
#include <stdio.h>
typedef struct course
{
	char *name;
	int units,grade;
}course;
void main()
{	
	int i,a,n,units,grade,flag=1,score=0,sum=0,tot=0;
	float gpa;
	char name[5];
	printf("How many courses do you have this sem?\n");
	scanf("%d",&i);
	if(i>9)
	{
		printf("Error!You can only take 9 courses in a sem.\n");
	}
	else
	{
		course list[9];
		printf("You'll now be prompted to enter details about each course.\n");
		for(n=0;n<i;n++)
		{
			printf("Enter the name of course no. %d (3 characters should suffice).\n",n+1);
			scanf("%s",name);
			list[n].name = name;
			while(flag==1)
			{	
				printf("Enter the credits for the course %s\n",name);
				scanf("%d",&units);
				if(units>4)
				{	
					printf("Error! credits cannot be more than 4.");					
				}
				else if(units<=0)
					printf("Error!credits can't be zero or negative.");
				else
				{
					list[n].units = units;
					flag = 0;
				}
			}
			while(flag==0)
			{
				printf("Enter your grade (in numbers) for the course %s\n",name);
				scanf("%d",&grade);
				if(grade>10)
					printf("Error!grade cannot be more than 10.");
				else if(grade<0)
					printf("Error!grade cannot be negative.");
				else
				{
					list[n].grade = grade;
					flag=1;
				}				
			}
			tot=tot+units;
			score = grade*units;
			sum=sum+score;			
		}
		gpa = (float)sum/tot;
		printf("The final GPA of your semester is %f\n",gpa);		
	}
}
