#include "auth.h"

static const uint8_t encoding_table[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

size_t base64_encode_len(size_t src_len)
{
	return 4 * ((src_len + 2) / 3);
}

uint8_t *base64_encode(const uint8_t *src, size_t src_len, uint8_t *dst, size_t *dst_len)
{
	uint8_t in[3];
	uint8_t *po = dst;
	uint32_t triple;
	size_t i;

	*dst_len = 4 * ((src_len + 2) / 3);
	fprintf(stderr, "dst_len is %d\n", *dst_len);
	for (i = 0; i + 2 < src_len; i += 3) {
		in[0] = src[i];
		in[1] = src[i + 1];
		in[2] = src[i + 2];
		triple = (in[0] << 0x10) + (in[1] << 0x08) + in[2];
		*po++ = encoding_table[(triple >> 3 * 6) & 0x3f];
		*po++ = encoding_table[(triple >> 2 * 6) & 0x3f];
		*po++ = encoding_table[(triple >> 1 * 6) & 0x3f];
		*po++ = encoding_table[(triple >> 0 * 6) & 0x3f];
	}
	if (src_len % 3 == 1) {
		*po++ = encoding_table[src[i] >> 0x02];
		*po++ = encoding_table[(src[i] & 0x03) << 4];
		*po++ = '=';
		*po++ = '=';
	} else if (src_len % 3 == 2) {
		triple = (src[i] << 0x10) + (src[i + 1] << 0x08);
		*po++ = encoding_table[(triple >> 3 * 6) & 0x3f];
		*po++ = encoding_table[(triple >> 2 * 6) & 0x3f];
		*po++ = encoding_table[(triple >> 1 * 6) & 0x3f];
		*po++ = '=';
	}
	// *(dst + *dst_len) = '\0';
	*po = '\0';
	return dst;
}

uint8_t *base64_decode(const uint8_t *src, size_t src_len, uint8_t *dst, size_t *dst_len)
{
	return dst;
}

char *urlencode(const char *src, int len, char *dst)
{
	return dst;
}

char *urldecode(const char *src, int len, char *dst)
{
	return dst;
}
