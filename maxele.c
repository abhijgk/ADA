#include<stdio.h>

int main()
{
	int i, n,a[10],max;
	
	printf("enter the no of elements");
	scanf("%d",&n);
	printf("\nenter the array elements");
	
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
		
	}
	max=a[0];
	for(i=1;i<n;i++)
	{
		if(a[i]>max)
			max=a[i];
			//printf("%d",max);
	}
	printf("the max ele is  %d",max);
}