#include<stdio.h>
int num,i;
int main()
{
	while(i!=100000)
	{
	  scanf("%d",&num);
	  if(num==42)
	  break;
	  else
	  printf("%d\n",num);
	  i++;
	}
}
