#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the pointer of the head of the linked list.
 * @number: The number to be inserted.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

    /* Fill in the data for the new node */
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

    /* Traverse the list to find the correct position for the new node */
	current = *head;
	prev = NULL;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

    /* Insert the new node into the list */
	prev->next = new_node;
	new_node->next = current;

	return (new_node);
}

/**
 * print_list - Prints the elements of a linked list.
 * @head: Pointer to the head of the linked list.
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

/**
 * free_list - Frees the memory used by a linked list.
 * @head: Pointer to the head of the linked list.
 */
void free_list(listint_t *head)
{
	listint_t *temp;

	while (head != NULL)
	{
		temp = head;
		head = head->next;
		free(temp);
		}
}
