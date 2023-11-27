#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>
/**
 * struct listint_s - struct to list next n
 * @n: number
 * @next: next in line
*/
struct listint_s
{
	int n;
	struct listint_s *next;
};

typedef struct listint_s listint_t;
#endif
