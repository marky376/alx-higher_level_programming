#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *baby = list, *adult = list;

    while (baby && adult && adult->next)
    {
        baby = baby->next;
        adult = adult->next->next;

        if (baby == adult)
        {
            return (1);
        }
    }

    return (0);
}
