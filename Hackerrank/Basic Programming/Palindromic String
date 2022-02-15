/*You have been given a String S. You need to find and print whether this string is a palindrome or not. If yes, print "YES" (without quotes), else print "NO" (without quotes).

Input Format
The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.

Output Format
Print the required answer on a single line.*/
#include<stdio.h>
#include<string.h>
int main()
{
	char temp,s[103],orgs[103];
	scanf("%s",&s);
	int a=strlen(s);
    strcpy(orgs,s);
	
     for (int i=0;i<a/2;i++)
		{
			temp=s[i];
			s[i]=s[a-(i+1)];
			s[a-(i+1)]=temp;
		}

	if(strcmp(orgs,s)==0)
	printf("YES");
	else
	printf("NO");
    
}
