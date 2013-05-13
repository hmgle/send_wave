#include <string.h>
#include <stdlib.h>
#include "auth.h"

int main(void)
{
	uint8_t text[] = "hello, world";
	uint8_t *b64;
	uint8_t *unb64;
	size_t len;
	size_t len2;

	b64 = malloc(base64_encode_len(strlen((const char *)text)) + 1);
	base64_encode(text, strlen((const char *)text), b64, &len);
	printf("%s\n", b64);
	unb64 = malloc(base64_decode_len(b64, len) + 1);
	base64_decode(b64, len, unb64, &len2);
	printf("%s\n", unb64);
	free(unb64);
	free(b64);
	return 0;
}
