#include "lists.h"
/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the linked list.
 *
 * Return: Pointer to the head of the reversed linked list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half;
	listint_t *first_half;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = reverse_list(slow);


	first_half = *head;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			return (0);
		}

		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}
/**
 * print_list - Prints elements of a linked list.
 * @head: Pointer to the head of the linked list.
 *
 * Description: This function prints the elements of a linked list.
 */
void print_list(listint_t *head)
{
	while (head != NULL)
	{
		printf("%d ", head->n);
		head = head->next;
	}
	printf("\n");
}
