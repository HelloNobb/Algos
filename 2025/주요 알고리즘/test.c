#include <stdio.h>

int main(void)
{
	int a = 10;

	printf("a: %d\n", a);
	printf("&a: %p\n", &a);
	
	int *p = &a;
	printf("*p: %d\n", *p);
	printf("p: %p\n", p);
	printf("&p: %p", &p);
}