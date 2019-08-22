#include<stdio.h>
int i,j,temp,min;
int fun(int a[],int k,int n)
{	
	for(i=0;i<=k-1;i++)
	{
		min=i;
		for(j=i+1;j<=n-1;j++)
		{
			if(a[min]>a[j])
			{
				min=j;
			}
		}
		temp=a[i];
		a[i]=a[min];
		a[min]=temp;
	}
	return a[i-1];
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
	res=fun(A,k,n);
	printf("The value is %d\n",res);
}

