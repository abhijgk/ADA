#include<stdio.h>
int i,j,temp,max;
int fun(int a[],int k,int n)
{	
	for(i=0;i<=k-1;i++)
	{
		max=i;
		for(j=i+1;j<=n-1;j++)
		{
			if(a[max]<a[j])
			{
				max=j;
			}
		}
		temp=a[i];
		a[i]=a[max];
		a[max]=temp;
		printf("%d\n",a[i]);
	}
	
}
int main()
{
	int A[10],n,k,res;
	printf("\nenter the size & elements of the array\n");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&A[i]);
	}
	printf("\nenter the value of K\n");
	
	scanf("%d",&k);
	fun(A,k,n);
	
}