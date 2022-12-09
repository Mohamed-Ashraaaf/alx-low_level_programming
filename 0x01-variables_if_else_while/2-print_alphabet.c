#include <stdio.h>
#include <stdlib.h>

/**
 *  * main - prints the alphabet in lowercase.
 *
 *   * Return: 0 on success
 */

int main(void)
{
	int ch = 'a';
	
	while (ch <= 'z')
	{
		putchar(ch);
		ch++;
											}
	putchar('\n');
	return (0);
}
