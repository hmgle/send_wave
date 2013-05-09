#include <string.h>
#include <stdlib.h>
#include "auth.h"

int main(void)
{
	uint8_t a[] = "hello, world";
	uint8_t *b;
	size_t len;

	b = malloc(base64_encode_len(strlen((const char *)a)) + 1);
	base64_encode(a, strlen((const char *)a), b, &len);
	printf("%s\n", b);
	free(b);
	return 0;
}
