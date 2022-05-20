#include<stdio.h>
int n,m,b[60]={0};
char a[30][30];
void input();
void check();
void max();
void input()
{

scanf("%d %d",&n,&m);
 for(int i=0;i<n;i++)
 {
for(int j=0;j<m;j++)
{
scanf("%c",&a[i][j]);
 }
 }
 }  
 void check()
 {
int c;
 for(int i=0;i<n;i++)
 {  c=1;
 	for(int j=0;j<m;j++)
 	{
 		if(a[i][j]=='#'&&a[i][j+1]=='#')
 		c++;
 	}
 	b[i]=c;	
 }
}
void reset()
{
	for(int i=0;i<60;i++)
	b[i]=0;
}
void max()
{
	for(int i=0;i<n;i++)
	    {    
	        for(int j=0;j<n;j++)
	        {
	    	if(b[j]<b[j+1])
	    	{
	    	int temp;
	    	temp=b[j];
	    	b[j]=b[j+1];
	    	b[j+1]=temp;
			}
		}
		}

	printf("%d",b[0]);
	printf("\n");
}
int main()
{   int t;
    scanf("%d",&t);
    for (int ts=1;ts<=t;ts++)
    {
    input();
	check();
	max();
	reset();
  } 
}
